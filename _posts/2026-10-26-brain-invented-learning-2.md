---
layout: post
title: "How the brain invented learning, part II: reinforcing in A Brief History of Intelligence"
date: 2026-10-26 09:30:00 +0900
description: "Notes on the second of Max Bennett's five breakthroughs: how early vertebrates learned by trial and error, how reinforcement learning ran into the same problem, and why dopamine turned out to be the TD error."
tags: artificial-intelligence neuroscience reinforcement-learning book-notes
categories: notes
related_posts: false
---

In [part I]({% post_url 2026-10-25-brain-invented-learning %}), we followed the first of the five breakthroughs in Max Bennett's _A Brief History of Intelligence_ (2023): steering. Bilaterian worms learned to move toward the good and away from the bad, and to store experience in the strength of their synapses. Their dopamine meant only "something good is nearby."

This post covers the second breakthrough, reinforcing: how early vertebrates acquired trial-and-error learning, how AI researchers ran into the same problem, and how the same molecule, dopamine, was turned into a learning signal. As before, the summary is my own paraphrase of the book's argument.

## 1. Breakthrough 2, Reinforcing: try it, then learn from the result

The stage for the second breakthrough is the early vertebrates that emerged about 500 million years ago, after the Cambrian explosion. The brains of these fish-like ancestors already had the basic blueprint that persists all the way to the human brain: a precursor of the cortex (the pallium), the basal ganglia, thalamus, hypothalamus, midbrain, and hindbrain.

What this blueprint made possible was trial-and-error learning. The nematode's associative learning was about learning that "good things follow this stimulus." Vertebrates learn that "good things follow when I do this." They learn the consequences not of stimuli but of their own actions.

### From Thorndike to Minsky

In 1898, Edward Thorndike placed cats in puzzle boxes and watched. At first they poked at everything until they happened to release the latch, but with repetition their escape times fell. Actions followed by satisfying outcomes are repeated; actions followed by unpleasant ones fade. This is the law of effect, and fish learn the same way.

The trouble surfaced when people tried to put this principle into machines. In the early 1950s Marvin Minsky built SNARC, a neural-network machine that learned by reinforcement, and he later named the critical obstacle: the temporal credit assignment problem. When you win a game of chess, which of the dozens of earlier moves contributed to the win? The later the reward arrives, the harder it is to know which action to reinforce.

### Sutton's answer: learn from changes in prediction, not from the reward itself

Temporal difference (TD) learning, formalized by Richard Sutton in the 1980s, sidesteps the problem elegantly. Instead of waiting for the final reward, the learner keeps a running prediction of how good things are going to be, and learns from the difference between successive predictions. If the position suddenly looks better, the action just taken was probably a good one.

$$
\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)
$$

Here $$V(s)$$ is the predicted value of state $$s$$, $$r$$ is the immediate reward, and $$\gamma$$ is the discount factor. $$\delta$$, the TD error, measures how much better things turned out than expected. The architecture is often split in two: a critic that evaluates states, and an actor that adjusts its policy using the critic's error.

In 1992, Gerald Tesauro at IBM used this method to build TD-Gammon, a neural network that plays backgammon. Learning by playing against itself, it reached a level close to the best human players. It was the first striking evidence that reinforcement learning really works.

## 2. Dopamine is the TD error

The most dramatic moment in the book is the discovery that an algorithm AI researchers had devised on paper was already running inside the brain.

In the 1980s and 1990s, Wolfram Schultz recorded the activity of dopamine neurons in the monkey midbrain. The setup was simple: a light (the cue) comes on, and a few seconds later juice (the reward) arrives. But the dopamine neurons' behavior could not be explained as a response to reward.

- **Before learning:** when juice arrives unexpectedly, dopamine neurons fire strongly.
- **After learning:** they fire when the light comes on, and do not respond when the juice itself arrives.
- **When the light is not followed by juice:** firing drops below baseline at the moment the juice should have come.

In all three cases, dopamine tracks not the reward received but the difference between the reward received and the reward expected.

These three patterns are exactly how the TD error $$\delta$$ behaves. An unexpected reward is a positive error, a predicted reward is zero error, and the absence of an expected reward is a negative error. And the moment a prediction of "something good is coming" first appears, when the light comes on, is precisely when the outlook improves. When Schultz, Peter Dayan, and Read Montague published this correspondence in _Science_ in 1997, the view took hold that dopamine is not a "pleasure chemical" but a reward prediction error signal.

### Dopamine changed its meaning

Seen through Bennett's evolutionary lens, the finding becomes even more interesting. In the nematode, dopamine was a state signal: "something good is nearby." In vertebrates, the same molecule is repurposed as a learning signal: "things just got better than expected." Evolution did not invent a new molecule. It changed the meaning of an existing broadcast channel.

The structure that receives this signal and adjusts behavior is the basal ganglia. The basal ganglia select one action from the available options and reinforce choices followed by a positive dopamine signal, so that those choices become easier to repeat. In reinforcement-learning terms, the basal ganglia play the actor, and the dopamine signal is the critic's error.

### Curiosity: surviving in a world of sparse rewards

Bennett argues that vertebrates also became curious at this stage. Fish explore novel things, and dopamine neurons respond not only to reward but also to novel stimuli. Novelty itself works as a kind of reward.

AI ran into the same problem. In environments where reward is very rare, such as the Atari game _Montezuma's Revenge_, random exploration never reaches the first reward, so learning never gets started. Researchers' fix was intrinsic motivation: a bonus for visiting states not seen before, in effect artificial curiosity. It is the same answer evolution reached 500 million years earlier.

## 3. The correspondence at a glance

The table below pairs each biological mechanism with its AI counterpart. The last column is my own judgment of how close the match is.

| Biological mechanism | AI counterpart | How close |
| --- | --- | --- |
| Law of effect (trial and error) | Policy reinforcement | Direct |
| Dopamine as reward prediction error | TD error δ | Quantitative match (Schultz et al., 1997) |
| Action selection in the basal ganglia | Actor (actor-critic) | Rough match; details debated |
| Dopamine response to novelty | Intrinsic motivation, exploration bonus | Functional match |

## 4. Closing: similar, but not the same

Following the two breakthroughs reveals a single thread. Neurons arose for fast response, the bilaterian brain for steering by good and bad, synaptic plasticity for storing experience, and dopamine's reinterpretation for learning from delayed reward. Each step reuses the parts of the one before rather than discarding them.

Still, it is too early to say that "the brain is a reinforcement learning algorithm." A few differences are clear.

- **Learning rule:** synapses change using only local information. Whether the brain has anything like backpropagation, which sends the output error precisely back through the layers, remains an open question.
- **Data efficiency:** TD-Gammon needed hundreds of thousands of self-play games. A fish learns in a handful of trials.
- **Forgetting:** animals keep old memories in suppressed form while learning new ones. Artificial networks are still weak here.
- **Dopamine's other faces:** dopamine does more than signal reward prediction error. It is involved in movement, motivation, and novelty, and how to interpret the signal is still an active research question.

Even so, the correspondence is illuminating. AI researchers did not reach these answers by copying the brain; they reached them by trying to solve the same problems. That evolution and engineering converged independently on the same solutions suggests that those solutions may come from the structure of the problems themselves.

Bennett's next breakthrough, simulating, concerns the mammalian neocortex and its ability to simulate the future in the mind: trying things out in imagination rather than in reality. That is the story of model-based reinforcement learning, and I plan to take it up in the next post.

**Questions to think about**

1. Dopamine changed from a state signal in worms to a learning signal in vertebrates. What other cases do you know where evolution, or engineering, repurposed an existing channel for a new job?
2. A fish learns in a handful of trials, while TD-Gammon needed hundreds of thousands of games. What might explain the difference?
3. TD learning learns from changes in prediction rather than from the final outcome. Where in your own field could a model learn from forecast updates rather than from observed outcomes alone?

---

**한 줄 요약 (Korean summary).** 약 5억 년 전 초기 척추동물은 자신의 행동 결과로부터 배우는 시행착오 학습(reinforcing)을 얻었다. Schultz 등(1997)은 원숭이의 도파민 뉴런이 보상 자체가 아니라 “예상보다 얼마나 좋았는가”에 반응한다는 것을 보였고, 이는 Sutton이 고안한 시간차(TD) 학습의 오차 신호와 같다. 진화는 새로운 물질을 만들지 않고, 선충 때부터 있던 도파민 신호의 뜻을 “근처에 좋은 것이 있다”에서 “예상보다 좋았다”로 바꾸었다. 뇌와 강화학습 사이에는 차이도 많지만, 둘이 서로 모른 채 같은 해법에 이르렀다는 것은 그 해법이 문제 자체의 성격에서 나온다는 것을 시사한다.

---

**References**

Bennett, M. (2023). _A Brief History of Intelligence: Evolution, AI, and the Five Breakthroughs That Made Our Brains_. Mariner Books.

Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. _Science_, 275, 1593–1599. [https://doi.org/10.1126/science.275.5306.1593](https://doi.org/10.1126/science.275.5306.1593)

Sutton, R. S. (1988). Learning to predict by the methods of temporal differences. _Machine Learning_, 3, 9–44. [https://doi.org/10.1007/BF00115009](https://doi.org/10.1007/BF00115009)

Tesauro, G. (1995). Temporal difference learning and TD-Gammon. _Communications of the ACM_, 38, 58–68. [https://doi.org/10.1145/203330.203343](https://doi.org/10.1145/203330.203343)

Sutton, R. S., & Barto, A. G. (2018). _Reinforcement Learning: An Introduction_ (2nd ed.). MIT Press.
