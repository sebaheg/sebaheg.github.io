---
layout: post
title: "Reinforcement Learning: Bellman Equation"
tags: machine-learning
description: The Bellman equation is indispensable for the development of reinforcement learning algorithms. In this blog post, we will drive both the expectation and optimality version of this equation.
mathjax: true
comments: true
live: true
---

## Introduction
Now that we have formalized the reinforcement learning problem using the MDP, we can start looking into how actually take decisions. In this post, I will explain the concept of value function and criterion for when we have reached optimal solution. Since reinforcement learning is goal oriented, we do not know what is optimal behaviour beforehand. Therefore, this criterion for optimality provides indispensable guidance in helping the agent to learn.

## Finding a policy
The policy is a set of implicit or explicit rules that signifies how the agent should behave in different circumstances. The policy \\( \pi(a|s): \mathcal{S} \times \mathcal{A} \to [0,1] \\) can be represented as the probability of taking an action \\( a \\) given the state \\( s \\) according to

\begin{equation}
\pi(a|s) = \mathbb{P}_{\pi} \big( A_t=a | S_t=s \big).
\end{equation}

It can be shown for the infinite-horizon discounted reward that there exists an optimal deterministic stationary policy \\( \pi_{\ast} \\) given that the environment also is stationary. If we know the dynamics of the environment, meaning we have a perfect model of the state transition \\( p(s',r \mid s,a) \\) and the state-action space is not too large, then we could apply techniques such as dynamic programming or linear programming to find the optimal policy. In very large state-action spaces, where it is infeasible to use exhaustive search algorithms, Monte Carlo tree searches are preferred instead. However, in general we do not have a perfect model of the MDP environments and need to explore techniques for determining the optimal policy anyway. This might seem like an insurmountable task, but there are some good news.

Reinforcement learning algorithms can overcome this problem by interactive with the environment and combining ideas from dynamic programming and Monte Carlo search. These algorithms access the state transition probabilities through a simulator that is typically restarted many times to update the algorithms knowledge about state transition dynamics.

### Action-value function
Undoubtedly, the most crucial idea of reinforcement learning is that of value functions. Whereas the reward signal indicates what is good in an immediate sense, a value function specifies what is good in the long run. The state-action value function can be seen as the expected cumulative discounted reward (or the "quality") of starting in state \\( s \\), taking action \\( a \\) and then following policy \\( \pi \\). The action-value function is always conditional on some policy and can be defined as

\begin{equation}
Q_{\pi}(s,a) = \mathbb{E_{\pi}} \big[ G_t | S_t=s, A_t=a \big].
\end{equation}

It is values which we are most concerned with when making and evaluating decisions. We seek to take actions that bring states of highest value, not highest reward, because those are the action that bring the greatest amount of reward in the long run. In fact, finding the optimal policy \\( \pi_{\ast} \\) is equivalent to finding the optimal state-action value function \\( Q_{\ast} \\) and by that solve the MDP. Because when the optimal state-action value function is found, we have the optimal policy by

$$
\begin{equation}
    \pi^{\ast}(a|s) =
\begin{cases}
    1, & \text{if } a = \mathop{\operatorname{argmax}}\limits_{a'} Q_{\ast}(s,a') \\
    0, & \text{otherwise}.
\end{cases}
\end{equation}
$$

Or in word, any policy that is greedy with respect to the optimal value functions must be an optimal policy. Conversely, the optimal value of a state is the infinite cumulative discounted rewards that the agent will gain if it starts in that state and executes the optimal policy. So the state-action value function and the policy are really to sides of the same coin. It is the state-action value function that allows us to develop methods for solving a MDP without having access to a model of the environment. For this reason, methods using state-action value functions are called model-free methods.

In order to know what we are looking for, we must specific what an optimal state-action value function (or policy) is. Mathematically, the optimal state-action value function can be expressed as

\begin{equation}
\max_{a'} Q^{\ast}(s,a') \ge \max_{a'} Q^{\pi}(s,a') \ \forall s, \pi.
\end{equation}

There is always at least one policy that is better than or equal to all other policies. Although, there may be more than one. On the other side, the state-action value function is unique and shared by all optimal policies.

### Bellman equation
A fundamental idea in solving reinforcement learning problems is the Bellman's principle of optimality. It states that:

<p class="message">
"An optimal policy has the property that whatever the initial state and initial decision are, the remaining decisions must constitute an optimal policy with regard to the state resulting from the first decision."
</p>

This means that in order to achieve a global optimal trajectory, it is sufficient to maximize every subtrajectory locally as illustrated in the figure below (by the way, it is [Bellman]() to the right).

<p align="center">
  <img width="600" height="300" src="/images/bellman.png">
</p>

We can derive this principle by considering the definition of the state-action value function as

<p align="center">
$$
\begin{align}
Q_{\pi}(s,a) &= \mathbb{E_{\pi}} \big[ G_t \mid S_t=s, A_t=a \big] \\
             &= \mathbb{E_{\pi}} \big[ r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + ...| S_t=s, A_t=a \big] \\
             &= \mathbb{E_{\pi}} \big[ r_{t+1} + \gamma (r_{t+2} + \gamma r_{t+3} + ...)| S_t=s, A_t=a \big] \\
             &= \mathbb{E_{\pi}} \big[ r_{t+1} + \gamma G_{t+1}| S_t=s, A_t=a \big] \\
             &= \mathbb{E_{\pi}} \big[ r_{t+1} + \gamma
             \mathbb{E_{\pi}} \big( G_{t+1} \mid S_{t+1}, A_{t+1} \big) \mid S_t=s, A_t=a \big] \\
             &= \mathbb{E_{\pi}} \big[ r_{t+1} + \gamma Q_{\pi}(S_{t+1},A_{t+1}) \mid S_t=s, A_t=a \big].
\end{align}
$$
</p>

We see that the state-action value function can be decomposed into the immediate reward \\( r_{t+1} \\) and the discounted reward of the successor states. The expectation of the cumulative discounted reward can be calculated by weighting with the probability, then summing over all possible states, rewards and actions according to

\begin{equation}
Q_{\pi}(s,a) = \sum_{s' \in \mathcal{S}} \sum_{r \in \mathcal{R}} p(s',r \mid s,a) \bigg[ r + \gamma \sum_{a' \in \mathcal{A}} \pi(a'|s') Q_{\pi}(s',a') \bigg].
\end{equation}

In the deterministic case, it reduces to

\begin{equation}
Q_{\pi}(s,a) = r + \gamma Q_{\pi}(s',\pi(s')),
\end{equation}

where \\( \pi(s): \mathcal{S} \to \mathcal{A} \\). This equation is referred to as the Bellman expectation equation and is the consistency condition on the state-action value function. Given Bellman's principle of optimality, the optimal policy is to act greedy with respect to the optimal state-action value function. Therefore, by substituting in the optimal policy we have found an equation for the optimal state-action value function as

<p align="center">
$$
\begin{align}
Q_{\ast}(s,a) &= \sum_{s' \in \mathcal{S}} \sum_{r \in \mathcal{R}} p(s',r \mid s,a) \bigg[ r + \gamma Q_{\ast}(s',\mathop{\operatorname{argmax}}\limits_{a'} Q_{\ast}(s',a')) \bigg] \\
&= \sum_{s' \in \mathcal{S}} \sum_{r \in \mathcal{R}} p(s',r \mid s,a) \bigg[ r + \gamma \mathop{\max}\limits_{a'} Q_{\ast}(s',a') \bigg]
\end{align}
$$
</p>

In the deterministic case, it reduces to

\begin{equation}
Q_{\ast}(s,a) = r + \mathop{\max}\limits_{a'} \gamma Q_{\ast}(s',a'),
\end{equation}

This equation is referred to as the Bellman optimality equation and recursively relates the optimal action-value function with itself. Intuitively, the Bellman optimality equation expresses the fact that the state-action value function under an optimal policy is equal to the immediate return from taking an action plus the discounted expected future return following the optimal policy from the successor state and onwards. If we got our state-action value function correct, then it must obey the Bellman optimality equation. This provides a sound mathematical ground to use as guidance to find the optimal state-action value function. However, the value function resulting from the Bellman optimality equation might be nonlinear and there is no guaranteed that it has a closed form expression.

### References
* David Silver's [course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html) on reinforcement learning
* Leslie Pack, Kaelbing et al., Reinforcement Learning: A Survey
* Richard S. Sutton and Andrew G. Barto, [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/bookdraft2017nov5.pdf)
* Wikipedia, [Bellman equation](https://en.wikipedia.org/wiki/Bellman_equation)
