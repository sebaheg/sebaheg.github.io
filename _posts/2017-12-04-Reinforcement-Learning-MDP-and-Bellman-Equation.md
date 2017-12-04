---
layout: post
title: "Reinforcement Learning: MDP and Bellman Equation"
tags: machine-learning
mathjax: true
live: true
---

## Introduction
Reinforcement learning is a goal oriented approach to solving problems where an agent has to take decisions in order to maximise some cumulative reward. There are two ways of learning a new skill top-down or bottom-up. The top-down approach is theoretical, you consider expert knowledge and read books about a topic in order to understand it better. Another way of doing it is the more practical bottom-up approach, where you try to learn by doing.

In a previous post, I gave an introduction to reinforcement learning. In the this post I will try to summaries the theory of reinforcement learning. We will look into how the problem can be framed mathematically and develop a criterion for when we have reached optimality. Since reinforcement learning is goal oriented, we do not know what is optimal behaviour beforehand. Therefore, this criterion for optimality provides indispensable guidance in helping the agent to learn.

## Markov decision problem
In order to formalise the reinforcement learning problem we need to put it into some mathematics. The [Markov
decision problem](https://en.wikipedia.org/wiki/Markov_decision_process) (MDP) framework can be used to achieve this. The MDP relies on the Markov property, which states that:

<p class="message">
"The future is independent of the past given the present."
</p>

A Markov chain is a (possibly stochastic) discrete time process determining the transition between different states \\( s \\). In order for it to be a Markov chain, it needs to satisfy the Markov property. Extending Markov chains with decisions and rewards gives a MDP. The different components in a MDP are:

* States: \\( s \in \mathbb{S} \\)
* Observations: \\( y \in \mathbb{Y} \\)
* Actions: \\( a \in \mathbb{A} \\)
* Reward: \\( R(s,a): \mathbb{S} \times \mathbb{A} \to \mathbb{R} \\)
* State transition: \\( T(s' \mid s,a): \mathbb{S} \times \mathbb{A} \to [0,1] \\)

Using this notation we can express a process with the Markov property as

\begin{equation}
\mathbb{P} (s_{t+1} \mid s_t, a_t, s_{t-1}, a_{t-1}, ...) = \mathbb{P} (s_{t+1} \mid s_t, a_t),
\end{equation}

meaning our state transition \\( T(s' \mid s,a) \\) only need to depend on the current state. In the case of a deterministic Markov process we can define the state transition function \\( f_T(s,a): \mathbb{S} \times \mathbb{A} \to \mathbb{S} \\) as

\begin{equation}
s_{t+1} = f_T(s_t,a_t,s_{t-1},a_{t-1},...) = f_T(s_t,a_t).
\end{equation}

In case we do have perfect state observation of the process then \\( y_t = s_t \\), otherwise \\( \mathbb{P} (y_t \mid s_t) \\) in the stochastic case. In the deterministic case we have \\( y_t = f_O(s_t) \\), where \\( f_O(s): \mathbb{S} \to \mathbb{Y} \\) is the observation function. Futhermore, the process can be said to be stationary if the probability \\( \mathbb{P} \\) (or the functions \\( f \\) in the deterministic case) does not change with time.

### State
The Markov state is a sufficient statistics of the future. A Markov state can always be found, since one can always include the complete history of the past in the current state. However, it is preferable to keep the state representation as compact as possible without losing the Markov property. Therefore, it is the up designer of the algorithm to choose appropriate information of the past to include in the state representation.

An example of an imperfect state representation (which is non-Markov) is to only include the position and not the velocity of a flying aircraft. In this case there is no way to tell the difference between an aircraft that is falling straight down or cruising at a safe speed from its state alone. In this case the correct state representation would be both position and velocity. This fact is mathematically justified in that both position and velocity is needed to integrate the governing equations of motion forward in time.

### Agent
The agent in reinforcement learning is an entity that is learning and making decision based on previous experience. It can be anything from a Go player to a physical robot playing football. The agent is not told how to achieve a task rather it is given an objective in the form of a reward signal. Then it is up to the agent to find a policy that enables it to make the correct actions given an observation for reaching the objective. The agent may not have perfect perception of the state. Observations might be noisy or provide only incomplete information. The most naive strategy to deal with partially observability is to simply ignore it.

### Environment
The agent is situated in an environment with some characteristics. Some examples of environments are the rules of Go, real world physics and Atari 2600 games. Usually, the characteristics of an environment are not known and can be both deterministic or stochastic. In stochastic environments, taking the same action in the same state twice may result in different next states and/or rewards. Furthermore, if the if the environment is non-stationary, the probabilities of making state transitions or receiving specific rewards may also change over time.

### The reward
One of the main assumptions in reinforcement learning is the *reward hypothesis*. This assumption states that all goals can be described as maximising the expected cumulative reward. Furthermore, a single scalar must be enough to specify the reward signal since the aim of a agent is to provide appropriate actions. To make actions you need to weight up different possible outcomes in the end anyway. This assumption might be the most disputable assumption in all of reinforcement learning.

In order for agents to learn optimal operating strategies in an environment, the designer has to define what the optimal is. This means specifying a objective function that the agent can use in the optimisation. The most commonly used objective (or target) function to maximise is the infinite-horizon discounted reward. This model takes long-run reward into account but future rewards are geometrically discounted using a discounting factor \\( \gamma \in [0,1] \\). The cumulative discounted reward is calculated as:

\begin{equation}
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + ... + \gamma^T R_{t+N+1} = \sum_{k=0}^{N} \gamma^k R_{t+k+1},
\end{equation}

where \\( R_t = R(s_t,a_t) \\). The task to be performed can either be divided into distinct episodes (Episodical) for which \\( N \in \mathbb{N} \\) or continuing for which \\( N \to \infty \\). Setting \\( \gamma = 0 \\) and \\( \gamma \\) = 1 result in a myopic and far-sighted estimate respectively. The use of a discounting factor \\( \gamma \\) can be justified in several ways:

* future reward is more uncertain and should therefore be discounted;
* future reward is less valuable (see for example [Time value of money](https://en.wikipedia.org/wiki/Time_value_of_money));
* as a mathematical trick to bound the infinite sum.

### Experience tuple
By putting the concept of state, action and reward together we represent a sample of experience as

\begin{equation}
\langle s, a, r, s' \rangle,
\end{equation}

where \\( s' \\) is the next state after taking action \\( a \\) in state \\( s \\). For an episode of length \\( N \\) we will accumulate a corresponding number of such experience tuples.

## Finding a policy
The policy is a set of implicit or explicit rules that signifies how the agent should behave in different circumstances. The policy \\( \pi(a|s): \mathbb{S} \times \mathbb{A} \to [0,1] \\) can be represented as the probability of taking an action \\( a \\) given the state \\( s \\) according to

\begin{equation}
\pi(a|s) = \mathbb{P} \big( A_t=a | S_t=s \big).
\end{equation}

If we knew the dynamics of the environment, meaning we have a perfect model of the state transition function \\( T(s' \mid s,a) \\) and the state-action space is not too large then we could apply techniques such as dynamic programming to find optimal policy. In very large state-action spaces, where it is infeasible to use exhaustive search algorithms, Monte Carlo tree search are preferred. However, in general we do not have a perfect model of the MDP environments and need to explore techniques for determining the optimal policy anyway. This might be a hard task, but there are some good news. It can be shown for the infinite-horizon discounted reward that there exists an optimal deterministic stationary policy \\( \pi^{\ast} \\) given that the environment also is stationary.

### Action-value function
A useful concept in developing policies is the concept of action-value function. The action-value function can be seen as the expected cumulative discounted reward (or the "quality") of starting in state \\( s \\) taking action \\( a \\) and then following policy \\( \pi \\). The action-value function is always conditional on some policy and can be defined as

\begin{equation}
Q^{\pi}(s,a) = \mathbb{E_{\pi}} \big[ G_t | S_t=s, A_t=a \big].
\end{equation}

Finding the optimal policy \\( \pi^{\ast} \\) is equivalent to finding the optimal state-action value function \\( Q^{\ast} \\) and solving the MDP. Because when the optimal state-action value function is found, we have the optimal policy by

$$
\begin{equation}
    \pi^{\ast}(a|s) =
\begin{cases}
    1, & \text{if } a = \mathop{\mathbin{\arg}{\max}}\limits_{a \in \mathcal{A}} Q^{\ast}(s,a) \\
    0, & \text{otherwise}.
\end{cases}
\end{equation}
$$

Conversely, the optimal value of a state is the infinite cumulative discounted rewards that the agent will gain if it starts in that state and executes the optimal policy. So the state-action value function and the policy are really to sides of the same coin. The meaning of an optimal state-action value (or policy) can be expressed mathematically as

\begin{equation}
\max_{a'} Q^{\ast}(s,a') \ge \max_{a'} Q^{\pi}(s,a') \ \forall s, \pi.
\end{equation}

### Bellman equation
A fundamental idea in solving reinforcement learning problems is the Bellman's principle of optimality. It states that:

<p class="message">
"An optimal policy has the property that whatever the initial state and initial decision are, the remaining decisions must constitute an optimal policy with regard to the state resulting from the first decision."
</p>

This principle can be derived by considering the definition of the state-action value function as

<p align="center">
$$
\begin{align}
Q^{\pi}(s,a) &= \mathbb{E_{\pi}} \big[ G_t | S_t=s, A_t=a \big] \\
             &= \mathbb{E_{\pi}} \big[ R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + ...| S_t=s, A_t=a \big] \\
             &= \mathbb{E_{\pi}} \big[ R_{t+1} + \gamma (R_{t+2} + \gamma R_{t+3} + ...)| S_t=s, A_t=a \big] \\
             &= \mathbb{E_{\pi}} \big[ R_{t+1} + \gamma G_{t+1}| S_t=s, A_t=a \big] \\
             &= \mathbb{E_{\pi}} \big[ R_{t+1} + \gamma Q^{\pi}(S_{t+1},A_{t+1})| S_t=s, A_t=a \big].
\end{align}
$$
</p>

So the state-action value function can be decomposed into the immediate reward \\( R_{t+1} \\) and the discounted reward of the successor states. Now, we can calculate the expectation by averaging the probability over all possible states and actions to arrive at the Bellman expectation equation given by

\begin{equation}
Q^{\pi}(s,a) = R(s,a) + \gamma \sum_{s' \in \mathcal{S}} T(s'|s,a) \sum_{a' \in \mathcal{S}} \pi(a'|s') Q^{\pi}(s',a').
\end{equation}

By substituting in the optimal policy we have found an equation for the optimal state-action value function as

\begin{equation}
Q^{\ast}(s,a) = R(s,a) + \gamma \sum_{s \in \mathcal{S}} T(s'|s,a) \max_{a'} Q^{\ast}(s',a').
\end{equation}

This equation is referred to as the Bellman optimality equation and recursively relates the optimal action-value function with itself. This means that if we got our state-action value function correct, then it must obey the Bellman optimality equation. This gives a sound mathematical ground to use this equation as guidance to find the optimal state-action value function. However, the value function resulting from the Bellman optimality equation might be nonlinear and there is no guaranteed that it has a closed form expression.

### References
* David Silver's [course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html) on reinforcement learning
* Leslie Pack, Kaelbing et al., Reinforcement Learning: A Survey
* Wikipedia, [Bellman equation](https://en.wikipedia.org/wiki/Bellman_equation)
* Wikipedia, [Markov decision process](https://en.wikipedia.org/wiki/Markov_decision_process)
