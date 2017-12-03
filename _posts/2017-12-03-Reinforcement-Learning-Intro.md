---
layout: post
title: "Reinforcement Learning: Intro"
tags: machine-learning
mathjax: true
live: true
---

## Introduction
The field of [Machine learning](https://en.wikipedia.org/wiki/Machine_learning) can roughly be divided into three broad subfields: [supervised learning](https://en.wikipedia.org/wiki/Supervised_learning), [unsupervised learning](https://en.wikipedia.org/wiki/Unsupervised_learning) and [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning). Reinforcement learning is concerned with having an agent that learns to maximise some notion of cumulative reward. This is different from both supervised learning (where input/output pairs are presented to the algorithm) and unsupervised learning (where the goal of the algorithm is to find hidden structure in unlabelled data). Indeed, unlike the two other two subfields, reinforcement learning is not a set of methods but a family of problems.

Reinforcement learning is based on a simple but powerful principle from nature called [behaviourism phycology](https://en.wikipedia.org/wiki/Behaviorism). This principle was pioneered more than 100 years ago by psychologist Edward Thorndike. He placed cats inside boxes from which they could only escape from by pressing a lever. After while pacing around and meowing, they would eventually step on the lever by chance. They then learned to associate the behaviour with the desired outcome and escaped future trials with increasing speed. Later, Ivan Pavlov further developed this with his work on [classical conditioning](https://en.wikipedia.org/wiki/Classical_conditioning). His dogs learned to produce the same response (salivation), to a conditioned stimulus (such as a bell) after pairing with a unconditioned stimulus (such as food). Pavlov's dogs learned to relate ringing bells or even that his assistant stepped into the room with that food was probably on the way.

Using this principle of reward and punishment, several algorithms where developed. Already in 1992, Gerald Tesauro at IBM developed a reinforcement learning approach to play backgammon. His program [TD-Gammon](https://en.wikipedia.org/wiki/TD-Gammon) was able to rival top human backgammon players at the time. TD-Gammon came up with new strategies humans had previously not considered or ruled out erroneously. These strategies impacted the backgammon community and the view on optimal game play. However, not much success was seen, despite many efforts to scale the algorithms to more complex and real world problems.

The breakthrough came in March 2016 when DeepMind's AlphaGo program won against one of the best Go players of all time, Lee Sedol. This victory is a milestone in artificial intelligence that was not thought by experts to be achieved in the coming decade. The reason is that the game of Go consists of so much larger number of state configurations (\\( \sim 10^{170} \\) compared to \\( \sim 10^{20} \\) for backgammon). For this reason it is impossible to only rely on brute force and search algorithms with the computational power available in the foreseeable future.

In October 2017, DeepMind published a new paper in Nature explaining how they developed a updated version of the AlphaGo called AlphaGo Zero that beat the previous strongest version with 100-0 in games. The main difference between AlphaGo Zero and previous version is that previous version all used data from expert human Go players to learn how to play. Instead AlphaGo Zero played against itself over and over again, starting from completely random game play. Over the course of days, AlphaGo Zero had accumulated the human knowledge about Go developed over thousands of years. Just like TD-Gammon, AlphaGo has developed unconventional strategies that outsmart the current human knowledge about how the game should be played.

## Applications
The reinforcement learning problem, due to its generality, is studies in several other disciplines except for board games. Some of these disciplines are: robotics, game theory, control theory and operations research. The actual end task changes from case to case when reinforcement learning applied to problems. Some examples applications of reinforcement learning is:
https://deepmind.com/blog/alphago-zero-learning-scratch/
* Play the ancient game of Go
* [Reduce energy consumption in data centre](https://deepmind.com/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-40/)
* [Make a humanoid learn how to walk](https://www.youtube.com/watch?v=gn4nRCC9TwQ)
* Mange a financial portfolio
* [Play Atari games](https://www.nature.com/articles/nature14236)

Me personally, I am most interested in how reinforcement learning can be used in control and game theory to improve the operation of energy systems.  

## Reinforcement learning problem
The ultimate goal of a learning algorithm solving a reinforcement learning problem is to find a sequence of actions from some state, that leads to the highest possible cumulative reward. The learning algorithm is usually referred to as an agent (depicted as a brain in the figure below). The agent receive information about the environment it is operating in through its perception. By taking different action, the state the agent is currently in might be altered as well as the environment itself.

<p align="center">
  <img width="400" height="400" src="/images/RL.jpeg">
</p>

Just as Pavlov's dogs, the algorithm need to deal with the temporal credit assignment problem. This is the problem of crediting the right state and/or action to the reward (or positive stimulus). The problem can be illustrated by considering a rat that can either be rewarded with a cheese or electrocuted. Given the two previous sequences in the figure below, what would be the outcome of the third sequence? There is no right answer. The three previous symbols agree with electrocution but by counting the different elements in both sequences one could argue that the cheese would be the outcome.

<p align="center">
  <img width="500" height="350" src="/images/temporal-credit.jpeg">
</p>

The temporal assignment problem can in many cases be even more complex and hard to detect. The promise of reinforcement learning algorithms is to provide a framework that can solve the temporal credit problem.  

## Conclusion
One of the most fundamental questions that phycologists have been struggling with is: "how do we learn a new skill?". With an understanding of this, we could unlock more potential in human beings but also train machines to do complex tasks. The promise of reinforcement learning is to automatically program machines to do tasks that are impractical to program by hand.

Until recently, reinforcement learning algorithms have required biases supplied by human programmers or teachers to perform complex tasks. However, in many real-world situations, human knowledge may be too expensive, too unreliable or there may not be enough examples to learn from. For this reason, a long-standing ambition of AI research is to remove human knowledge completely from the algorithms and still achieving super-human performance. This is referred to as tabula rasa learning and requires algorithms to create knowledge form first principles. The advances of AlphaGo Zero brings confidence that AI will work as a multiplier for human ingenuity. This could help us to solve some of the most challenging and impactful problems humanity is facing. David Silver argues that the kind of learning algorithms might help us on this mission in a [mind-blowing video](https://www.youtube.com/watch?v=WXHFqTvfFSw).

There is little doubt that the algorithms behind AlphaGo Zero are powerful. However, the fact that it requires to play millions of games in order to achieve the same performance as expert humans indicates that it uses a fundamental different way of learning. Even more impressive would be if it would only play roughly as many games as a Go expert plays in their career before becoming a champion. Indeed, the next step of the reinforcement learning research is to find solutions to problems even when there is not large amount of training data to learn from.

## References
* DeepMind, [Deep Reinforcement Learning](https://deepmind.com/blog/deep-reinforcement-learning/)
* DeepMind, [AlphaGo Zero](https://deepmind.com/blog/alphago-zero-learning-scratch/)
* David Silver et al., [Mastering the game of Go with deep neural networks and tree search](https://www.nature.com/articles/nature16961.epdf?shared_access_token=eKK0163L_QWhJOnSS4Wet9RgN0jAjWel9jnR3ZoTv0OivKk3lXs6SxMz535byYwHqIVouJ6qKrtxfOrBqgMI8z2GAxKloOrZJt2uhpOg7ZJrYyYlxydsd7C2FJN6_Oeui0xLpQ4rv5dW4j8qo7PZCEpVRl6vsFBUeBY00_dlKUE%3D)
* David Silver et al., [Mastering the game of Go without human knowledge](https://www.nature.com/articles/nature24270)
* MIT Technology Review, [Reinforcement Learning](https://www.technologyreview.com/s/603501/10-breakthrough-technologies-2017-reinforcement-learning/)
Volodymyr Mnih et al., [Human-level control through deep reinforcement learning](https://www.nature.com/articles/nature14236)
* Gerald Tesauro, [TD-Gammon](https://courses.cs.washington.edu/courses/cse590hk/01sp/Readings/tesauro95cacm.pdf)
* Wikipedia, [Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning)
