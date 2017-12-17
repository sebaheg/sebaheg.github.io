---
layout: post
title: Q-Learning for CartPole Problem
tags: machine-learning python
mathjax: true
live: true
---
<!-- Eligibility Traces

Frequent heuristics
Recency heuristics-->

<!-- On-policy vs Off-policy
Describe this and what is the difference. In off-policy we can learn from other's policies. Meaning we can learn from human behaviour and so on.

One reason for doing off-policy learning is so that we can explore at the same time as we improve our policy which should not explore.
* Off-policy is important in order to learn from humans
* re-use old experience generated from previous policies. (Do online updating)
* learn about optimal policy while following exploratory policy
Q-learning is specific to TD(0)-->

Reinforcement learning is a goal oriented framework where agents are developed that have to take decisions in order to maximise some cumulative reward. There are two ways of learning a new skill top-down or bottom-up. The top-down approach is theoretical, you consider expert knowledge and might read books about a topic in order to understand it better. Another way of doing it is the more practical bottom-up approach, where you try to learn by doing.

sequential data is correlated.

sequential data is correlated.
learning changes

http://kengz.me/openai_lab/#openai-lab

We can do undiscounted markov reward processes if all sequences are finite.


We do not need to discount in this case?
sum is not infinite,
value is the same all the time


Read this:
http://kvfrans.com/simple-algoritms-for-solving-cartpole/
https://github.com/vmayoral/basic_reinforcement_learning/blob/master/tutorial4/README.md
https://keon.io/deep-q-learning/

Deep Q-learning
https://pythonprogramming.net/openai-cartpole-neural-network-example-machine-learning-tutorial/
https://www.pinchofintelligence.com/getting-started-openai-gym/
https://www.analyticsvidhya.com/blog/2017/01/introduction-to-reinforcement-learning-implementation/
Here we talk more about Q-learning and the cartpole problem.

Reinforcement learning is a type of problem

OpenAI provides several different such problems (or environments) that can be accessed through a user-friendly API. in order to help people develop their RL algorithms.

https://gym.openai.com/

Idea: make a OpenAI gym for reinforcement learning for energy.
RL is a problem not a solution. It is a markov

Cartpole is a classical Reinforcement learning problem.
start with random actions and then learn how to master the game without being told how the game even works.
deep-q learning is a model-free approach as apposed to control theory/automatic control

In machine learning terms, CartPole is basically a binary classification problem. There are four features as inputs, which include the cart position, its velocity, the pole’s angle to the cart and its derivative (i.e. how fast the pole is “falling”).

The core of Q-Learning is to estimate a value for every possible pare of a state (s) and an action (a) by getting rewarded.

Basically, a (S, A)-tuple’s new q-value depends on its old q-value, the immediate reward received for the action and the maximum q-value achievable in the following state.

 By repeatedly walking through all nodes and transistions, the agent can update any (S, A)-pairs q-value, while the results of good and bad actions are slowly “backpropagated” from terminal nodes to early nodes. The agent ends up with a (usually multidimensional) table mapping states and actions to q-values, so that given any state, the best action can be picked by choosing the highest respective q-value.

### OpenAI Gym
[OpenAI](https://en.wikipedia.org/wiki/OpenAI#Universe)

Can use OpenAI universe to make your own environments in the end.

### Cartpole problem
A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track. The pendulum starts upright, and the goal is to prevent it from falling over by increasing and reducing the cart's velocity.




The documentation for the problem can be found [here](https://github.com/openai/gym/wiki/CartPole-v0)
For CartPole-v0 one of the actions applies force to the left, and one of them applies force to the right. (Can you figure out which is which?) So we affect force not speed directly!!

This is essentially the classic inverted pendulum problem which you could find in a typical undergraduate control course. However, instead of applying control theories, the goal here is to solve it using controlled trial-and-error, also known as reinforcement learning. COPY

The Cart-Pole world consists of a cart that moves along the horizontal axis and a pole that is anchored on the cart. At every time step, you can observe its position (x), velocity (x_dot), angle (theta), and angular velocity (theta_dot). These are the observable states of this world. At any state, the cart only has two possible actions: move to the left or move to the right.
In other words, the state-space of the Cart-Pole has four dimensions of continuous values and the action-space has one dimension of two discrete values.


<table>
  <thead>
    <tr>
      <th>State variable</th>
      <th>Lower bound</th>
      <th>Upper bound</th>
    </tr>
  </thead>
  <tr>
    <th align="center">\( x \)</th>
    <th align="center">-4.8</th>
    <th align="center">4.8</th>
  </tr>
  <tr>
    <th align="center">\( \dot x \)</th>
    <th align="center">\( -\infty \)</th>
    <th align="center">\( \infty \)</th>
  </tr>
  <tr>
    <tr>
      <th align="center">\( \theta \)</th>
      <th align="center">-0.48</th>
      <th align="center">0.48</th>
    </tr>
  </tr>
  <tbody>
    <tr>
      <th align="center">\(\dot \theta \)</th>
      <th align="center">\( -\infty \)</th>
      <th align="center">\( \infty \)</th>
    </tr>
  </tbody>
</table>

Num	Action
0	Push cart to the left
1	Push cart to the right

Note: The amount the velocity is reduced or increased is not fixed as it depends on the angle the pole is pointing. This is because the center of gravity of the pole increases the amount of energy needed to move the cart underneath it

Starting state:
All observations are assigned a uniform random value between ±0.05

Episode Termination

Pole Angle is more than ±20.9°
Cart Position is more than ±2.4 (center of the cart reaches the edge of the display)
Episode length is greater than 200
Solved Requirements

Considered solved when the average reward is greater than or equal to 195.0 over 100 consecutive trials.



### Random actions

<p align="center">
  <video controls="controls">
    <source type="video/mp4" src="/videos/im.mp4"></source>
    <p>Your browser does not support the video element.</p>
  </video>
</p>



### Q-Learning
In here, we represent the world as a graph of states connected by transitions (or actions). It means that to predict your future state, you will only need to consider your current state and the action that you choose to perform. The key here is that you don’t need to consider your previous states. This is what people call a Markov Model. Although your past does have influences on your future, this model works because you can always encode information about the past in your current state.

Q-Learning is a method of finding these optimal policies. You can read more about it on this page. Essentially, through trials-and-errors, you find a Q-value for each state-action pair. This Q-value represents the desirability of an action given the current state. Over time, if the world is static (i.e. the physics or the cause-and-effects don’t change), the Q-values would converge and the optimal policy of a given state would be the action with the largest Q-value.

Let’s define a function Q(s, a) such that for given state s and action a it returns an estimate of a total reward we would achieve starting at this state, taking the action and then following some policy.



### Discretizing the feature space
One major limitation of my classical Q-Learning approach was that the number of possible states had to be reduced from basically infinity (due to the observations’ continuous nature) to, in my case

Good reference to get started:
http://mnemstudio.org/path-finding-q-learning-tutorial.htm

Accordingly, with DQN we don’t need discrete buckets anymore, but are able to directly use the raw observations.

Having fewer optimal polices to find means faster training. However, discretizing the state-space too coarsely might prevent convergence as important information might be discretized away.

The input is a state-vector (or a batch of such) - consisting of four features in this case (which corresponds to four input neurons)The output is a vector of Q-values, one for each possible action - two in our case (corresponding to two output neurons).

### Exploration vs exploitation
* epsilon-greedy policy


### Training
experience tuples (old_state, performed_action, received_reward, new_state).
experience replay, go throught the game several times
At fixed intervals (e.g. after each training episode, but NOT after each step), batches are sampled from memory and used as training data for the network. Consequently, the network (hopefully) improves every episode and predicts more precise Q-values for state-action pairs.

- try to increase the number of hidden units in the second hidden layer.
- Make mini-batch training instead of online training
- larger replay memory memory size to 100,000.
- Does it make sense to set gamma = 1?
- different weight decays
- tune the hyperparameters alpha, and so on.
logarithmic decay

The purpose of the training is to enhance the 'brain' of our agent, represented by matrix Q.  More training results in a more optimized matrix Q

\begin{equation}
\varepsilon() = \max(0.01, \min(\varepsilon, 1-\log(t+1) \cdot decay))
\end{equation}

$$ \max p $$
$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$



Actually the main challenge was to convert the continuous, 4-dimensional input space to a discrete space with a finite and preferably small, yet expressive, number of discrete states. The less states we have, the smaller the Q-table will be, the less steps the agent will need to properly learn its values. However, too few states might not hold enough information to properly represent the environment.


### Hyperparameters
alpha: regularization to make updates less radical, which, in the first place, prevents from errors caused by noise
epsilon: exploitation and exploration. This should prevent the algorithm from getting stuck in local minima. pick a random action with probability epsilon

















OpenAI provides several different such problems (or environments) that can be accessed through a user-friendly API. in order to help people develop their RL algorithms.

https://gym.openai.com/
RL is a problem not a solution. It is a markov

Cartpole is a classical Reinforcement learning problem.
start with random actions and then learn how to master the game without being told how the game even works.
deep-q learning is a model-free approach as apposed to control theory/automatic control

In machine learning terms, CartPole is basically a binary classification problem. There are four features as inputs, which include the cart position, its velocity, the pole’s angle to the cart and its derivative (i.e. how fast the pole is “falling”).

The core of Q-Learning is to estimate a value for every possible pare of a state (s) and an action (a) by getting rewarded.

Basically, a (S, A)-tuple’s new q-value depends on its old q-value, the immediate reward received for the action and the maximum q-value achievable in the following state.

 By repeatedly walking through all nodes and transistions, the agent can update any (S, A)-pairs q-value, while the results of good and bad actions are slowly “backpropagated” from terminal nodes to early nodes. The agent ends up with a (usually multidimensional) table mapping states and actions to q-values, so that given any state, the best action can be picked by choosing the highest respective q-value.

### Cartpole problem
For CartPole-v0 one of the actions applies force to the left, and one of them applies force to the right. (Can you figure out which is which?) So we affect force not speed directly!!

This is essentially the classic inverted pendulum problem which you could find in a typical undergraduate control course. However, instead of applying control theories, the goal here is to solve it using controlled trial-and-error, also known as reinforcement learning. COPY

The Cart-Pole world consists of a cart that moves along the horizontal axis and a pole that is anchored on the cart. At every time step, you can observe its position (x), velocity (x_dot), angle (theta), and angular velocity (theta_dot). These are the observable states of this world. At any state, the cart only has two possible actions: move to the left or move to the right.
In other words, the state-space of the Cart-Pole has four dimensions of continuous values and the action-space has one dimension of two discrete values.


<table>
  <thead>
    <tr>
      <th>State variable</th>
      <th>Lower bound</th>
      <th>Upper bound</th>
    </tr>
  </thead>
  <tr>
    <tr>
      <th align="center">\( \theta \)</th>
      <td>21</td>
      <td>23</td>
    </tr>
  </tr>
  <tbody>
    <tr>
      <th align="center">\(\dot \theta \)</th>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th align="center">\( x \)</th>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th align="center">\( \dot x \)</th>
      <th align="center">10</th>
      <th align="center">100</th>
    </tr>
  </tbody>
</table>

### Random actions

<p align="center">
  <video controls="controls">
    <source type="video/mp4" src="/videos/im.mp4"></source>
    <p>Your browser does not support the video element.</p>
  </video>
</p>







### Discretizing the feature space
One major limitation of my classical Q-Learning approach was that the number of possible states had to be reduced from basically infinity (due to the observations’ continuous nature) to, in my case

Good reference to get started:
http://mnemstudio.org/path-finding-q-learning-tutorial.htm

Accordingly, with DQN we don’t need discrete buckets anymore, but are able to directly use the raw observations.

Having fewer optimal polices to find means faster training. However, discretizing the state-space too coarsely might prevent convergence as important information might be discretized away.

The input is a state-vector (or a batch of such) - consisting of four features in this case (which corresponds to four input neurons)The output is a vector of Q-values, one for each possible action - two in our case (corresponding to two output neurons).



### Training
experience tuples (old_state, performed_action, received_reward, new_state).
experience replay, go throught the game several times
At fixed intervals (e.g. after each training episode, but NOT after each step), batches are sampled from memory and used as training data for the network. Consequently, the network (hopefully) improves every episode and predicts more precise Q-values for state-action pairs.

- try to increase the number of hidden units in the second hidden layer.
- Make mini-batch training instead of online training
- larger replay memory memory size to 100,000.
- Does it make sense to set gamma = 1?
- different weight decays
- tune the hyperparameters alpha, and so on.
logarithmic decay

The purpose of the training is to enhance the 'brain' of our agent, represented by matrix Q.  More training results in a more optimized matrix Q

\begin{equation}
\varepsilon() = \max(0.01, \min(\varepsilon, 1-\log(t+1) \cdot decay))
\end{equation}

$$ \max p $$
$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$



Actually the main challenge was to convert the continuous, 4-dimensional input space to a discrete space with a finite and preferably small, yet expressive, number of discrete states. The less states we have, the smaller the Q-table will be, the less steps the agent will need to properly learn its values. However, too few states might not hold enough information to properly represent the environment.


### Hyperparameters
alpha: regularization to make updates less radical, which, in the first place, prevents from errors caused by noise
epsilon: exploitation and exploration. This should prevent the algorithm from getting stuck in local minima. pick a random action with probability epsilon

### References
OpenAI Gym, [gym.openai.com/docs/](https://gym.openai.com/docs/)
https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff
https://medium.com/@tuzzer/cart-pole-balancing-with-q-learning-b54c6068d947

### References
OpenAI Gym, [gym.openai.com/docs/](https://gym.openai.com/docs/)
https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff
https://medium.com/@tuzzer/cart-pole-balancing-with-q-learning-b54c6068d947
Blog posts:
* [Gaetan Juvin](https://medium.com/@gtnjuvin/my-journey-into-deep-q-learning-with-keras-and-gym-3e779cc12762)
http://koaning.io/hello-deepq.html
http://koaning.io/hello-deepq.html
http://kvfrans.com/simple-algoritms-for-solving-cartpole/
https://medium.com/@gtnjuvin/my-journey-into-deep-q-learning-with-keras-and-gym-3e779cc12762
https://towardsdatascience.com/reinforcement-learning-w-keras-openai-actor-critic-models-f084612cfd69
