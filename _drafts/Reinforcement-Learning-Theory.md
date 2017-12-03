---
layout: post
title: "Reinforcement Learning: Theory"
tags: machine-learning
mathjax: true
live: true
---

### Introduction


The promise of RL: a way of programming agents by reward and punishment, without needing to specify **how** a task is to be achieved.

Reinforcement learning is goal oriented.
Goal is implicitly given by some external signal
Two different ways of learning. Practical and theoretical. Either you sit down and learn everything about a topic before you execute on it. Or you actually try to learn by playing.
d that many of its successes have come when a computer could practice relentlessly in simulations.
By experimenting, computers are figuring out how to do things that no programmer could teach them.
MIT Review






### Problem formulation
The reinforcement learning problem can be formulated


![RL](/images/RL.jpeg)

#### Agent
The agent in reinforcement learning is an entity that is learning and making decision based on previous experience. It can be anything from a Go player to a physical robot playing football. The agent is not told how to achieve a task rather it is given an objective. Then it is up to the agent how to reach this goal.

#### Environment
The agent is situated in an environment. The environment can be an Atari game, a market or a  (including real world physics)


In general the environment is non-deterministic but we will assume a deterministic environment,
We will also assume full observarability.
These are assumptions that simplifies the math. But the basic idea with reinforcement learning can still be conveyed.
We also assume that the environment is stationary. Probabilities do not change over time.
The environment in reinforcement learning is typically formulated as a Markov decision process.

A Markov decision process is a discrete time and stochastic control process. At every time step \( s_t \)

It is not sure the agent can observe the full environment,
Environment can be deterministic or stochastic. That is taken the same action in the same state twice may result in different next states and/or rewards. Furthermore, if the if the environment is non-stationary, the probabilities of making state transitions or reciving specific reinforcement signals do not change over time.



### The reward
Could be nice to have the robot picture here. 1M dollar or 1 dollar.
Money is worth more now than in the future.
We can invest the money and earn more money.

Reward hypothesis:
all goals can be descirbed by maximation of expected culmulative reward. Single scalar must be enough becasue in the end you want to make actions. And to make actions you need to weight up different possible outcomes. Therefore, a single scalar must be enough.  

The discount can be seen as an interest rate, or by the fact that the future is more uncertain. or simply just like a mathematical trick to bound the infinite sum.

In order to be able to construct optimal agents operating in an environent, we have to define what optimal is. The most commonly use objective (or target) function to maximise is the infinite-horizon discounted. This model takes long-run reward into account but future rewards are geometrically discounted using a discounting factor \\( \gamma \in [0,1) \\). The total reward is then calculated as:
One reason for discounting the reward is to represent the fact that we do not have a perfect model. We are uncertain about the future.
\\( R_t \in \mathbb{R} \\)


We can do undiscounted markov reward processes if all sequences are finite.
\begin{equation}
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + ... + \gamma^T R_{t+T+1} = \sum_{k=0}^{T} \gamma^k R_{t+k+1}
\end{equation}

\\( \gamma \\) = 1 far-sighted
\\( \gamma \\) = 0

\\( T \in \mathbb{N} \\) Episodical
\\( T \to \infty \\) Continuing



The discounting factor \\( \gamma \\) can be justified in several ways:

* future reward is more uncertain and should therefore be discounted;
* future reward is less valuable (see for example [Time value of money](https://en.wikipedia.org/wiki/Time_value_of_money));
* as a mathematical trick to bound the infinite sum.

### Markov decision problem
In order to put the reinforcement learning problem into some mathematics, the [Markov decision problem](https://en.wikipedia.org/wiki/Markov_decision_process) (MDP) framework can be used. The MDP relies on the Markov property, which states that:

<p class="message">
"The future is independent of the past given the present."
</p>

A Markov chain is a (possibly stochastic) process determining the transition between different states \\( s \\). In order for it to be a Markov chain, it needs to satisfy the Markov property. Extending Markov chains with decisions and rewards gives a MDP. Mathematically, a MDP satisfies

To summaries,

* States: \\( s \in \mathbb{S} \\)
* Actions: \\( a \in \mathbb{A} \\)
* Reward function: \\( R: \mathbb{S} \times \mathbb{A} \to \mathbb{R} \\)
* State transition function: \\( T: \mathbb{S} \times \mathbb{A} \to \mathbb{S} \\)


\begin{equation}
s_{t+1} = f(s_t,a_t,s_{t-1},a_{t-1},...) = f(s_t,a_t)
\end{equation}

A Markov state can always be found since one can always include the complete history of the past in the current state.  it is possible to render a problem to become Markovian.

For example, problem could be the steering of an aircraft. In order to determine the future position of an aircraft given and the pilot's steering action, we need both its current position and velocity. If only the position is known, there is no way to tell the difference between an aircraft that is falling straight down or cruising a at a safe speed from its state. This fact is mathematically justified in that both position and velocity is needed to integrate the governing equations of motion forward in time.



One episode forms a finite sequence of states, actions and rewards.


experience tuple (s,a,r,s')

The markov state is a sufficient statistics of the future. If you took an imperfect state representation, which is non-Markov, only the position and not the velocity for example. If we included the whole past in the state, then it would be markovian. Therefore, there is always a markov state.

The aim of the programmer/designer is to find useful representations of the past to use in the state. What we would believe would happend next depends on our representation of state.

### Temporal credit assignment problems
Talk about the picture by silver with the rat.
Exploration vs exploitation
sequential data is correlated.
credit assignment problem.
learning changes



## Partially observable environments.
The agent might not have a perfect perception of the state of the environment. Unforetunatly, complete observarability is necessary for learning methods based on MDP. Observations might be noisy or provide incomplete information. Most naive strategy for dealing with partially observability is to ignore it.

## Finding a policy
If we knew the dynamics of the environment, meaning we have a perfect model of the state transition function. Then we could apply techniques such as dynamic programming. But since we do not have a perfect model of the MDP environments, we need to explore technieques for determining the optimal policy given a correct model.

We can rely on the result that, for the infinite horizon discounted model, there exists an optimal deterministic stationary policy.

is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions. The next time the same subproblem occurs, instead of recomputing its solution, one simply looks up the previously computed solution, thereby saving computation time at the expense of a (hopefully) modest expenditure in storage space. COPY

**Temporal credit assignment problem**, action might have far reaching effects.
**Exploration vs exploitation dilemma**

\begin{equation}
\pi(s|a) = \mathbb{P} \big[ A_t=a | S_t=s \big]
\end{equation}

For now we only consider stationary policies.

### Action-value function
The action-value function can be seen as the expected reward of starting in state \\( s \\) taking action \\( a \\) and then following policy \\( \pi \\).

\begin{equation}
Q_{\pi}(s,a) = \mathbb{E_{\pi}} \big[ G_t | S_t=s, A_t=a \big]
\end{equation}



## Bellman equation
It can be shown theoretically that there exist a deterministic optimal policy \\( \pi^{\ast} \\) for any MDP. To find this policy we first need to consider the action-value function

The optimal action-value function must have:

\begin{equation}
\max_{a'} Q^{\ast}(s,a') \ge \max_{a'} Q^{\ast}(s,a') \ \forall s, \pi
\end{equation}

When we have Q* we are done. We have solved the MDP.

The optimal policy is then given direcly as

$$
\begin{equation}
    \pi^{\ast}(a|s) =
\begin{cases}
    1, & \text{if } a = \mathop{\mathbin{\arg}{\max}}\limits_{a \in \mathcal{A}} Q^{\ast}(s,a) \\
    0, & \text{otherwise}
\end{cases}
\end{equation}
$$

All possible policies can be ordered by considering the partial ordering as

\begin{equation}
\pi \ge \pi' \ if \ \max_{a'} q_{\pi}(s,a') \ge \max_{a'} q_{\pi'}(s,a') \ \forall s
\end{equation}

The optimal policy \\( \pi^* \\) is better or equal to all other policies according to this partial ordering. Furthermore, \\( \max_{a'} Q^{\ast}(s,a) \\) is

It can be shown that there is an deterministic optimal policy. This optimal policy achieve the optimal value and action value function.



<p align="center">
$$
\begin{align}
Q_{\pi}(s,a) &= \mathbb{E_{\pi}} \big[ G_t | S_t=s, A_t=a \big] \\
             &= \mathbb{E_{\pi}} \big[ R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + ...| S_t=s, A_t=a \big] \\
             &= \mathbb{E_{\pi}} \big[ R_{t+1} + \gamma (R_{t+2} + \gamma R_{t+3} + ...)| S_t=s, A_t=a \big] \\
             &= \mathbb{E_{\pi}} \big[ R_{t+1} + \gamma G_{t+1}| S_t=s, A_t=a \big] \\
             &= \mathbb{E_{\pi}} \big[ R_{t+1} + \gamma Q_{\pi}(S_{t+1},A_{t+1})| S_t=s, A_t=a \big] \\

\end{align}
$$
</p>


Bellman expection equation

\begin{equation}
Q_{\pi}(s,a) = R_s^a + \gamma \sum_{s' \in \mathcal{S}} T(s'|s,a) \sum_{a' \in \mathcal{S}} \pi(a'|s') Q_{\pi}(s',a')
\end{equation}


Bellman optimality equation
The optimal action-value function is recursively related by the Bellman optimality equation.
- is non-linear
- no closed form solution (in general)
\begin{equation}
Q^{\ast}(s,a) = R_s^a + \gamma \sum_{s \in \mathcal{S}} T(s'|s,a) \max_{a'} Q^{\ast}(s',a')
\end{equation}



 If we have q* then we immediately have the optimal policy.

The Bellman equations is important in the derivation

The value function can be decomposed into two parts:
* Immediate reward R_{t+1}
* discounted value of successor states

If we got our value function correct, then it must obey the Bellman equation.

There is a non closed form solution to the Bellman optimality equation and it is non-linear.


\begin{equation}
V_{\pi}(s)
\end{equation}

Derive the bellman equation
Then we can just choose the policy so that

The optimal value of a state is the infinite discounted sum of the rewards that the agent will gain if it starts in that state and executes the optimal policy. This is written as follows,

In this section I need to have a discussion on different trajectories. Use these to explain the Bellman optimality.

Read note an see if I can write this chapter, with what I got already.

It can be shown that the Bellman equation provide the optimal policy.

\begin{equation}
V^*(s) = \max_\pi \sum_{t=0}^{\infty} \gamma^t r_t
\end{equation}

This is the same as taking the best

\begin{equation}
V(s) <-- V(s) + \alpha (r + \gamma V(s') - V(s))
\end{equation}

Whenever a state s is visited, its estimated value is updated to be closer to r+\gammaV(s') since r is the instantaneous reward recived in V(s') is the estimated value of the actually occurring next state. The key ida is that r+\gamma V(s) is a sample of the value of V(s), and it is more likely to be correct because it incoporates the real r. As time goes on, we know more about the final state. This is the intuition behind the Bellman Equation. If the learning rate \alpha is adjusted proporly (it must decrease slowly) and the policy is held fix, this algorithm is guaranteed to converge to the optimal value function.  \\( V^*(s) = \max_a Q(s,a) \\)

### Q-Learning


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

if each action is executed in each state an infinite number of times, on an infinite run and \alpha is decayed appropriately, the Q-values will converge with probability 1 to Q^*. If alpha is not decreased then we might over shoot and oscillate around the optimal Q.

If you act too greedy the algorithm might not converge to the optimal value, but actually get stuck. Since you might not see enough of the state-action space to find a optimal policy.

can be seen as fixed point iteration of the Bellman equation.


Alpha should be decreased slowly.

In here, we represent the world as a graph of states connected by transitions (or actions). It means that to predict your future state, you will only need to consider your current state and the action that you choose to perform. The key here is that you don’t need to consider your previous states. This is what people call a Markov Model. Although your past does have influences on your future, this model works because you can always encode information about the past in your current state.

Q-Learning is a method of finding these optimal policies. You can read more about it on this page. Essentially, through trials-and-errors, you find a Q-value for each state-action pair. This Q-value represents the desirability of an action given the current state. Over time, if the world is static (i.e. the physics or the cause-and-effects don’t change), the Q-values would converge and the optimal policy of a given state would be the action with the largest Q-value.


### Exploration vs exploitation dilemma.
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
