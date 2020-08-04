---
layout: post
title: "Reinforcement Learning: Markov Decision Process"
tags: machine-learning
description: In this post, the reinforcement learning problem is formalized using the Markov decision process.  
mathjax: true
comments: true
live: true
---

## Introduction
In a previous post, I gave an introduction to reinforcement learning. In the this post I will try to lay the foundation of the reinforcement learning theory. We will look into how the problem can be framed mathematically.

## Markov decision process
In order to reason about reinforcement learning problem we need to put it into some mathematics. The [Markov
decision process](https://en.wikipedia.org/wiki/Markov_decision_process) (MDP) framework is a classical formalization of sequential decision making, which we can use to achieve this. The MDP relies on the Markov property, which states that:

<p class="message">
"The future is independent of the past given the present."
</p>

A Markov chain is a (possibly stochastic) discrete time process determining the transition between different states \\( s \\). In order for it to be a Markov chain, it needs to satisfy the Markov property. Extending Markov chains with decisions and rewards gives the MDP. An illustration of the MDP is given in the figure below.

<p align="center">
  <img width="400" height="400" src="/images/RL.jpeg">
</p>

The different components in a MDP are:

* States: \\( s \in \mathcal{S} \\)
* Observations: \\( y \in \mathcal{Y} \\)
* Actions: \\( a \in \mathcal{A} \\)
* Reward: \\( r \in \mathcal{R} \\)
* State transition: \\( p(s',r \mid s,a): \mathcal{S} \times \mathcal{R} \times \mathcal{S} \times \mathcal{A} \to [0,1] \\)

Using this notation we can express a process with the Markov property as

\begin{equation}
\mathbb{P} (s_{t+1} \mid s_t, a_t, s_{t-1}, a_{t-1}, ...) = \mathbb{P} (s_{t+1} \mid s_t, a_t),
\end{equation}

meaning our state transition \\( p(s',r \mid s,a) \\) only need to depend on the current state. In the case of a deterministic Markov process we can define the state transition function \\( f(s,a): \mathcal{S} \times \mathcal{A} \to \mathcal{S} \times \mathcal{R} \\) as

\begin{equation}
(s_{t+1},r_{t+1}) = f(s_t,a_t,s_{t-1},a_{t-1},...) = f(s_t,a_t).
\end{equation}

The mapping between states and observations is \\( y_t = s_t \\), in the case we do have perfect state observation of the process. If the observation is noisy or incomplete, we have \\( \mathbb{P} (y_t \mid s_t) \\) in the stochastic case and \\( y_t = g(s_t) \\) in the deterministic case (where \\( g(s): \mathcal{S} \to \mathcal{Y} \\) is the  observation function). Furthermore, the process can be said to be stationary if the probability \\( \mathbb{P} \\) (or the functions \\( f \\) and \\( g \\) in the deterministic case) does not change with time.

### State
According to the Markov property, the Markov state is a sufficient statistics of the future. A Markov state can always be found, since one can always include the complete history of the past in the current state. However, it is preferable to keep the state representation as compact as possible without losing the Markov property. Therefore, it is the up designer of the algorithm to choose appropriate information of the past to include in the state representation.

An example of an imperfect state representation (which is non-markovian) is to only include the position and not the velocity of a flying aircraft. In this case there is no way to tell the difference between an aircraft that is falling straight down or cruising at a safe speed from its state alone. In this case the correct state representation would be both position and velocity. This fact is mathematically justified in that both initial position and velocity is needed to integrate the governing equations of motion (Newton's second law) forward in time.

### Agent
The agent in reinforcement learning is an entity that is learning and making decision based on previous experience. It can be anything from a Go player to a physical robot playing football. The agent is not told how to achieve a task rather it is given an objective in the form of a reward signal. By using the information in the reward signal, it is up to the agent to find a policy that enables it to make the correct action given an observation for reaching the long-term objective. The agent may not have perfect perception of the state. Observations might be noisy or provide only incomplete information.

### Environment
The agent is situated in an environment with some characteristics. Some examples of environments are the rules of Go, Atari 2600 games and real world physics. In the MDP, the state transitions are given by the state transition function \\( p(s',r \mid s,a) \\). Usually, the characteristics of an environment are not known and can be both deterministic or stochastic. In stochastic environments, taking the same action in the same state twice may result in different next states and/or rewards. Furthermore, if the environment is non-stationary, the probabilities of making state transitions or receiving specific rewards may also change over time.

### The reward
One of the main assumptions in reinforcement learning is the reward hypothesis, which states:

<p class="message">
"That all of what we mean by goals and purposes can be well thought of as the maximisation of the expected value of the cumulative sum of a received scalar signal (called reward)."
</p>

It argued that a single scalar must be enough to specify the reward signal since the aim of a agent is to provide appropriate actions. To make actions you need to weight up different possible outcomes in the end anyway. This assumption is probably the most disputable assumption in all of reinforcement learning.

The reward signal is external to the agent (and should be beyond its ability to change arbitrarily) since it part of the task definition. Therefore, it is up to the designer of the algorithm to express the the reward signal mathematically. If we want a reinforcement learning agent to do something for us, we must proved rewards to it in such a way that by maximizing them, the agent will also achieve our goal. In other words, if the reward is designed to maximize some artificial subgoal, then the agent might find a way to solve the subgoal without solving the actual goal.

The MDP might involve delayed rewards and the need to trade-off immediate and delayed rewards. For this reason it is not sufficient to only account for the immediate when learning optimal operating strategies. The most commonly used objective (or target) function to maximise is the infinite-horizon discounted reward. This objective function takes long-run reward into account but future rewards are geometrically discounted using a discounting factor \\( \gamma \in [0,1] \\). The cumulative discounted reward is calculated as:

\begin{equation}
G_t = r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + ... + \gamma^{T-1} r_{t+T} = \sum_{k=1}^{T} \gamma^{k-1} r_{t+k},
\end{equation}

where the probability of receiving reward \\( r_{t+1} \\) is given by

\begin{equation}
R(r_{t+1} \mid s_t,a_t) =  \sum_{s_{t+1} \in \mathcal{S}} p(s_{t+1},r_{t+1} \mid s_t,a_t).
\end{equation}

The task to be performed can either be divided into distinct episodes (for episodical tasks) for which \\( T \in \mathbb{N} \\) or be continuing for which \\( T \to \infty \\). Setting \\( \gamma = 0 \\) and \\( \gamma \\) = 1 result in a myopic and far-sighted estimate respectively. The use of a discounting factor \\( \gamma \\) can be justified in several ways:

* future reward is more uncertain and should therefore be discounted;
* future reward is less valuable (see for example [Time value of money](https://en.wikipedia.org/wiki/Time_value_of_money));
* as a mathematical trick to bound the infinite sum.

In order to assure that the sum is bounded for continuing tasks, the reward sequence \\( \{ r_k \} \\) must be bounded as well as \\( \gamma \neq 1 \\). We can see episodical tasks to be a special case of continuing tasks by considering an "absorbing" terminal state which maps back to itself with probability 1 and repeatedly gives zero reward. Therefore, \\( G_T = 0 \\) for episodical tasks.

### Experience tuple
By putting the concept of state, action and reward together we can represent a sample of experience as

\begin{equation}
\langle s, a, r, s' \rangle,
\end{equation}

where \\( s' \\) is the next state after taking action \\( a \\) in state \\( s \\) and receiving reward \\( r \\). For an episode of length \\( T \\) we will accumulate a corresponding number of such experience tuples.

### References
* David Silver's [course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html) on reinforcement learning
* Leslie Pack, Kaelbing et al., Reinforcement Learning: A Survey
* Richard S. Sutton and Andrew G. Barto, [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/bookdraft2017nov5.pdf)
* Wikipedia, [Markov decision process](https://en.wikipedia.org/wiki/Markov_decision_process)
