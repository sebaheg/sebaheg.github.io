---
layout: post
title: "Reinforcement Learning: Q-Learning"
tags: machine-learning
description: Q-learning is because of its simplicity and applicability the most popular algorithm in reinforcement learning. In this blog post, temporal difference learning, which is the basis of Q-learning is discussed together with the exploration-exploitation dilemma and how function approximation can help to remedy the curse of dimensionality. 
mathjax: true
comments: true
live: true
---

## Introduction
Reinforcement learning is computational approach to understand and automate goal-directed learning and decision making. It is a kind of artificial intelligence which is based on simpler and fewer general principles compared to systems based on vast amounts of domain knowledge. The main idea of reinforcement learning is to learn from interaction, without having to rely on exemplary supervision or complete models of the environment.

In previous blog posts, I have layed the foundation for the theory behind reinforcement learning. In this post we will see how this theory can be used to construct actual algorithms that learn by iteratively update themselves with data from experience.

## Temporal difference learning
Undoubtedly the most novel idea of reinforcement learning is that of temporal differencing (TD). TD learning is a combination of Monte Carlo methods and dynamic programming (DP). Just like Monte Carlo, TD methods can learn directly from raw experience without a model describing the dynamics of environment. And just like DP, TD methods update estimates based in part on other learned estimates, without waiting for a final outcome. The capabilities of TD methods have not yet been fully explored. Sutton and Barto describe their potential as:

<p class="message">
"They are general methods for learning to make long-term predictions about dynamical systems. For example, TD methods may be relevant to predicting financial data, life spans, election outcomes, weather patterns, animal behavior, demands on power stations, or customer purchases. It was only when TD methods were analyzed as pure prediction methods, independent of their use in reinforcement learning, that their theoretical properties first came to be well understood. Even so, these other potential applications of TD learning methods have not yet been extensively explored."
</p>

The core idea of TD methods is that one adjusts estimates to match other, more accurate, estimates. The reason this works is because the target estimates are produced further into the future, when more information is available. TD methods learn from incomplete episodes (so that continuing tasks also can be dealt with) by substituting the remainder of the return with an estimate. This is known as bootstrapping and allows for learning online after each time step. Bootstrapping allows to learn faster by exploiting the Markov property, which is ignored by Monte Carlo methods.

TD methods are similar to Monte Carlo in that learning takes place by sampling the environment according to some policy. But Monte Carlo methods require to complete a whole episode before learning happens. Monte Carlo methods only take information from the ground truth and are therefore unbiased. However, because they update the whole episode after the which contain much uncertainty, they are high variance. On the other hand, TD methods are biased since they do not use the ground truth for learning (they use estimates instead), but have lower variance because they update over a shorter time span. This trade-off is know as the [Bias–variance tradeoff
](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff).

## Exploration-exploitation dilemma
How many restaurants in a new city should you explore before starting to exploit your favourite ones? This is exactly what the Exploration-exploitation dilemma is about, and in reinforcement learning it is called [multi-armed bandit problem](https://en.wikipedia.org/wiki/Multi-armed_bandit). Even if you find that one restaurant does not serve any tasty food. How can you know for sure that it was not because you picked the wrong dish or the chef had a bad day. Furthermore, if you are staying in the city for a long while, you might want to keep looking longer for that

When using a greedy policy that, unlucky sampling in the beginning might indicate that best expected reward of the best action is less than the expected reward from a suboptimal action. The suboptimal action will continue to get chosen, leaving the true optimal action starved of data and its superiority never discovered.

Several ad-hoc strategies have been developed as remedies for the Exploration-exploitation dilemma. One naive way that have proven to be efficient in practice is the \\( \epsilon \\)-greedy policy. An \\( \epsilon \\)-greedy policy takes a random action with the probability \\( \epsilon \in [0,1] \\). It is clear that in stationary environments the optimal policy does not include an element of randomness, thus \\( \epsilon \\) should slowly be decreased. Another, maybe more sensible way is Boltzmann exploration. Boltzmann exploration tries to remedy the fact that a non-greedy action is no more likely to try a promising alternative than a clearly hopeless alternative. This is done by choosing actions based on their softmax probability according to their state-action value as

\begin{equation}
\pi(a|s) = \frac{\exp{ \big[ Q(a,s)/T \big] }}{\sum_{a' \in A} \exp{ \big[ Q(s,a)/T \big] }}.
\end{equation}

The parameter \\( T \\) is the temperature, which should be decreased over time to promote more promising actions and by doing so speed up convergence.

## Q-Learning
The most popular method method in reinforcement learning is Q-learning. This method is built on TD learning and provides a framework for learning model-free from delayed reinforcement. The main idea of Q-learning is to iteratively approximate the \\( Q_{\ast}(s,a) \\) using the Bellman optimality equation. The method is online since it updates the best estimate of the Q-value as soon new experience is collected and work independently of the policy being followed. The iterative updating scheme for the Q-value is

<p align="center">
$$
\begin{align}
Q(s,a) &= Q(s,a) + \alpha \Big(r + \gamma \max_{a'} Q(s',a') - Q(s,a) \Big) \\
       &= (1-\alpha) Q(s,a) + \alpha \Big(r + \gamma \max_{a'} Q(s',a') \Big)
\end{align}
$$
</p>

where \\( \alpha \in [0,1] \\) is a learning parameter that signifies how fast learning should be. Choosing \\( \alpha \\) too big however, will lead to divergence. If the state-action space is discrete (or can be discretized) then the state-action value function can be represented by a look-up table. The equation above represents to different ways of looking at the update. In the first equality, the Q-value is updated in the direction of the error in the RHS of the Bellman optimality equation. In the second equality, the Q-value is updated by using applying fixed-point iteration.

In a stationary environment and a small enough \\(( \alpha \\)), the Q-learning update is guaranteed to converge \\( Q(s,a) \rightarrow Q_{\ast}(s,a) \\) if all state-action pairs continue to be updated. In order to make sure that all state are explored, an \\( \epsilon \\)-greedy behaviour policy is usually applied. However, our target policy is the optimal policy, which is a greedy policy. For this reason, Q-learning is an off-policy learning algorithm.

## Function approximation
As mentioned, the state-action value function \\( Q(s,a) \\) can be represented by a look-up table. However, tables are noisy and take long time to learn for large state-action spaces. In fact, because of the [curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality) learning with look-up table is impractical for most real applications. Furthermore, state-action pairs that are close to each other are usually similar. For reason, it is close at hand to think that function approximizers could find these generalizations. One type of such function approximizers that have proven capable are [neural networks](). When replacing the look-up table with a neural network, the update is done by minimizing the loss function

\begin{equation}
L(\boldsymbol{w}) = \big( r + \gamma \max_{a'} Q(s',a',\boldsymbol{w}) - Q(s,a,\boldsymbol{w}) \big)^2
\end{equation}

by updating the weights \\( \boldsymbol{w} \\) of the neural network.

## References
* David Silver's [course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html) on reinforcement learning
* Leslie Pack, Kaelbing et al., Reinforcement Learning: A Survey
* Richard S. Sutton and Andrew G. Barto, [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/bookdraft2017nov5.pdf)
* Wikipedia, [Q-learning](https://en.wikipedia.org/wiki/Q-learning)
* Wikipedia, [Temporal difference learning](https://en.wikipedia.org/wiki/Temporal_difference_learning)
