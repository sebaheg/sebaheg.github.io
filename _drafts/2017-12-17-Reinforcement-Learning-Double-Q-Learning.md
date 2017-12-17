---
layout: post
title: "Reinforcement Learning: Double Q-Learning"
tags: machine-learning
mathjax: true
live: true
---

Read maximation bias chapter one more time 6.7) in the book before I continue on this chapter. 

## Temporal_difference_learning

But are TD methods sound? Certainly it is convenient to learn one guess from the next, without waiting for an actual outcome, but can we still guarantee convergence to the correct answer? Happily, the answer is yes. For any fixed policy ⇡, TD(0) has been proved to converge to v⇡, in the mean for a constant step-size parameter if it is sufficiently small, and with probability 1 if the step-size parameter decreases according to the usual stochastic approximation conditions

TD methods update their estimates based in part on other estimates. They learn a guess from a guess— they bootstrap. I

Shown to the right is the backup diagram for tabular TD(0). The value estimate for the state node at the top of the backup diagram is updated on the basis of the one sample transition from it to the immediately following state. We refer to TD and Monte Carlo updates as sample updates because they involve looking ahead to a sample successor state (or state–action pair), using the value of the successor and the reward along the way to compute a backed-up value, and then updating the value of the original state (or state– action pair) accordingly. Sample updates di↵er from the expected updates of DP methods in that they are based on a single sample successor rather than on a complete distribution of all possible successors.COPY

Thus, TD methods combine the sampling of Monte Carlo with the bootstrapping of DP.

 As we discussed above, there will be a positive maximization bias if we use the maximum of the estimates as an estimate of the maximum of the true values. COPYOne way to view the problem is that it is due to using the same samples (plays) both to determine the maximizing action and to estimate its value.

 Suppose we divided the plays in two sets and used them to learn two independent estimates, call them Q1(a) and Q2(a), each an estimate of the true value q(a), for all a 2 A. We could then use one estimate, say Q1, to determine the maximizing action A⇤ = argmaxa Q1(a), and the other, Q2, to provide the estimate of its value, Q2(A⇤) = Q2(argmaxa Q1(a)). This estimate will then be unbiased in the sense that E[Q2(A⇤)] = q(A⇤).

All the control algorithms that we have discussed so far involve maximization in the construction of their target policies. For example, in Q-learning the target policy is the greedy policy given the current action values, which is defined with a max, COPY In these algorithms, a maximum over estimated values is used implicitly as an estimate of the maximum value, which can lead to a significant positive bias.

## Double Q-learning

The idea of double learning extends naturally to algorithms for full MDPs. For example, the double learning algorithm analogous to Q-learning, called Double Q-learning, divides the time steps in two, perhaps by flipping a coin on each step. If the coin comes up heads, the update is

\begin{equation}
Q_1(s,a) = Q_1(s,a) + \alpha \Big(r + \gamma Q_2(s', \mathop{\operatorname{argmax}}\limits_{a' \in \mathcal{A}}) Q_1(s,a) - Q_1(s,a) \Big)
\end{equation}
or
\begin{equation}
Q_2(s,a) = Q_2(s,a) + \alpha \Big(r + \gamma Q_1(s', \mathop{\operatorname{argmax}}\limits_{a' \in \mathcal{A}}) Q_2(s,a) - Q_2(s,a) \Big)
\end{equation}

If the coin comes up tails, then the same update is done with Q1 and Q2 switched, so that Q2 is updated.

The two approximate value functions are treated completely symmetrically. The behavior policy can use both action-value estimates. For example, an "-greedy policy for Double Q-learning could be based on the average (or sum) of the two action-value estimates.COPY

##

## References
* David Silver's [course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html) on reinforcement learning
* Leslie Pack, Kaelbing et al., Reinforcement Learning: A Survey
* Richard S. Sutton and Andrew G. Barto, [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/bookdraft2017nov5.pdf)
* Wikipedia, [Q-learning](https://en.wikipedia.org/wiki/Q-learning)
* Wikipedia, [Temporal difference learning](https://en.wikipedia.org/wiki/Temporal_difference_learning)
