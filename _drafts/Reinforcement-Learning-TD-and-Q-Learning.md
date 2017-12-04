---
layout: post
title: "Reinforcement Learning: TD and Q-Learning"
tags: machine-learning
mathjax: true
live: true
---

### Q-Learning

This is the same as taking the best

\begin{equation}
V(s) <-- V(s) + \alpha (r + \gamma V(s') - V(s))
\end{equation}

Whenever a state s is visited, its estimated value is updated to be closer to r+\gammaV(s') since r is the instantaneous reward recived in V(s') is the estimated value of the actually occurring next state. The key ida is that r+\gamma V(s) is a sample of the value of V(s), and it is more likely to be correct because it incoporates the real r. As time goes on, we know more about the final state. This is the intuition behind the Bellman Equation. If the learning rate \alpha is adjusted proporly (it must decrease slowly) and the policy is held fix, this algorithm is guaranteed to converge to the optimal value function.  \\( V^ast(s) = \max_a Q(s,a) \\)

The main idea of Q-learning is that we can iteratively approximate the Q value using the Bellman equation.
It has been shown that
The idea with Q-learning is to iteratively approximate the Q-function using the Bellman equation and update it as soon as we learn something about our environment.

The way to think about Q is the best possible score at the end of the game after performing action a in state s. It is callled Q-function because it represents the "quality" of a certain action in a given state.  

Q-learning is the most popular and seems to be the most effective model-free algorithm for learning model-free from delayed reinforcement.
The following equation is used:
Q-learning can be seen as an incremental update in the direction of the newest error or as a picard iteration.

Guesses are getting progressively better and this backs up so that you get the correct value function.

Q-learning is a kind of [temporal difference algorithm](https://en.wikipedia.org/wiki/Temporal_difference_learning)
The reason these algorithms converge is that the next state you have stepped one step forward in time which brings you closer to the real truth.

Bootstrapping = "feeds of itself."

<p align="center">
$$
\begin{align}
Q(s,a) &= Q(s,a) + \alpha \Big(r + \gamma \max_{a'} Q(s',a') - Q(s,a) \Big) \\
       &= (1-\alpha) Q(s,a) + \alpha \Big(r + \gamma \max_{a'} Q(s',a') \Big)
\end{align}
$$
</p>

if each action is executed in each state an infinite number of times, on an infinite run and \alpha is decayed appropriately, the Q-values will converge with probability 1 to Q^\ast. If alpha is not decreased then we might over shoot and oscillate around the optimal Q.

If you act too greedy the algorithm might not converge to the optimal value, but actually get stuck. Since you might not see enough of the state-action space to find a optimal policy.

can be seen as fixed point iteration of the Bellman equation.


Alpha should be decreased slowly.

In here, we represent the world as a graph of states connected by transitions (or actions). It means that to predict your future state, you will only need to consider your current state and the action that you choose to perform. The key here is that you don’t need to consider your previous states. This is what people call a Markov Model. Although your past does have influences on your future, this model works because you can always encode information about the past in your current state.

Q-Learning is a method of finding these optimal policies. You can read more about it on this page. Essentially, through trials-and-errors, you find a Q-value for each state-action pair. This Q-value represents the desirability of an action given the current state. Over time, if the world is static (i.e. the physics or the cause-and-effects don’t change), the Q-values would converge and the optimal policy of a given state would be the action with the largest Q-value.

**Temporal credit assignment problem**, action might have far reaching effects.
**Exploration vs exploitation dilemma**
### Exploration vs exploitation dilemma.
sequential data is correlated.
credit assignment problem.
learning changes

Exploration depends on how long the agent is expected to play. longer plays more exploration is needed. Might be that you get a bad meal at a good restaurant. So ther emay also be a component of uncertainty. There are some ad-hoc strategies that have been developed to account for this. The do not provide optimal algorithms for this type of problem. They should rather be seen as reasonable and computational tractable heuristics.
Unlucky sampling in the beginning might indicate that the best action's reward is less than the reward obtained from a suboptimal action. Then the suboptimal action will be chosen and the Leaving the true optimal  action starved of data and its superiority never discovered.

* Greedy
Unlucky sampling might result in that the agent narrows in on a suboptimal policy, not discovering that there are better policiies. Since the agent greedly feeds of the best discovered action, it will never explore and discover other potentially better actions.
* epsilon-greedy
Here we choose a random action with a probability p, that could slowly decrease as the agent feeds of the optimal action in the end.
* Softmax exploration
Boltzmann exploration tries to remedy the fact that a non-greedy action it is no more likely to try a promising alternative than a clearly hopeless alternative. The temperature should be decreased with time otherwise the algorithm might be unnecessarly slow to converge.
\\( P(a) = \frac{\exp{\hat R(a)/T}}{\sum_{a' \in A} \exp{\hat R(a')/T}} \\)  

Generally it can be said that exploration should converge to some regime where exploratory action is taken rarely or never. However, when the environment is non-stationary, exploration must continue in order to notice changes to the environment.  

In cases where we have a stationary environment, the exploration should eventually go to zero, otherwise exploration must continue to take place to notice changes in the environent. For cartpole this should be zero in the end.

To choose the best restaurant is similar to the [multi-armed bandit problem](https://en.wikipedia.org/wiki/Multi-armed_bandit).

The longer the game is to be played the more value is there in exploration. Might be that I get a bad meal in a good restataurant, but need to test several time to find out.


Reinforcement learning is a type of problem

### Function approximators
Generalization over actions,
Generalization over states

Tables are noisy. There is usually a generalization that can be found. The value of a state very close to another state is probably similar. This can not be captured with table Q-learning since all states must be visited.

Tables are noisy and take long time to learn. Neural network can generalize from seen states to unseen states.

Insert picture with different architecutre possibiliies.
Using the network to find the optimal action in the continous case can be challanging.


### Conclusion
In order to solve highly complex problems, we must give up tabula rasa learning techniques and being to incorporate bias that will give leverage to the learning process. Alpha Go zero is a step towards tabula rasa learning. Link the video with David Silver.

"With appropriate biases  supplied by human programmers or teachers  complex reinforcement  learning problems will eventually b e solvable  There is still much work to b e done and many interesting questions remaining for learning techniques and esp ecially regarding metho ds for approximating  decomp osing  and incorp orating bias into problems
"
### References
* David Silver's [course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html) on reinforcement learning
* Leslie Pack, Kaelbing et al., Reinforcement Learning: A Survey
