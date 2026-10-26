---
layout: post
title: "How the brain invented learning, part I: steering and reinforcing in A Brief History of Intelligence"
date: 2026-10-25 21:00:00 +0900
description: "Notes on the first two of Max Bennett's five breakthroughs: how bilaterian worms learned to steer by good and bad, how early vertebrates learned by trial and error, and why dopamine turned out to be the TD error of reinforcement learning."
tags: artificial-intelligence neuroscience reinforcement-learning book-notes
categories: notes
related_posts: false
---

The problems a worm solved 600 million years ago, and a fish solved 500 million years ago, look remarkably like the problems AI researchers ran into in the late twentieth century. Max Bennett's _A Brief History of Intelligence_ (2023) is built around that overlap.

Bennett is not a neuroscientist; he is an AI entrepreneur. That gives the book an unusual angle. He asks: at the points where we get stuck trying to build intelligence into machines, how, and in what order, did evolution get past them? His answer is organized into five "breakthroughs": steering, reinforcing, simulating, mentalizing, and speaking.

This post covers only the first two. Steering is the story of how bilaterian animals got the first brains. Reinforcing is the story of how early vertebrates acquired trial-and-error learning. The main characters in both are neurons, synapses, and dopamine, and each maps with surprising precision onto the weights of artificial neural networks and the reward signal of reinforcement learning.

The summary below is my own paraphrase of the book's argument. A few connections, notably the three-factor learning rule, come from the broader neuroscience literature rather than from the book itself.

## 1. The birth of the neuron: speed was the price of eating

Neurons came before brains. And they evolved not for thinking, but because of how animals eat.

Plants and fungi live by absorbing sunlight or the nutrients around them. They have no reason to hurry. Animals took a different path: they eat other living things. Food moves, and you might be food yourself. That strategy demands a body that can respond quickly and as a whole. Chemicals diffusing slowly from cell to cell were not enough.

Neurons solve this. They carry electrical signals (action potentials) from one end of the body to the other almost instantly, then pass the signal to the next cell across a synapse using chemical messengers (neurotransmitters). The contrast is telling: sponges, which feed by filtering water, have no neurons, while cnidarians such as jellyfish have a diffuse nerve net spread across the body.

But a jellyfish's nerve net mostly runs reflexes. A stimulus arrives, and a fixed response goes out. A central processor that pools many signals into a single decision, a brain, comes only in the next step.

**The AI connection.** The artificial neuron that McCulloch and Pitts proposed in 1943 is a radical simplification of the biological one: multiply the inputs by weights, sum them, and fire if the sum crosses a threshold. Synaptic strength became the weight, and whether a neuron fires became the activation function. Every layer of modern deep learning still rests on this abstraction.

## 2. Breakthrough 1, Steering: toward the good, away from the bad

The first brains appeared about 600 million years ago in bilaterians, animals with a head and a tail, a left and a right. Once a body has a front end, sense organs and neurons cluster there, and the animal becomes something that must decide which way to go.

The nematode _C. elegans_ offers a living glimpse of what these early animals were like. With only 302 neurons, this tiny worm turns toward a strengthening food odor and away from a strengthening danger signal. It has no map and no representation of a goal. It moves on a single question: is this direction getting better or worse?

Bennett calls this the first breakthrough, steering. Its core is the ability to sort the world into good and bad, what neuroscientists call valence. Food odor is good; toxins are bad. This simple binary is where intelligence begins.

### The original jobs of dopamine and serotonin

Remarkably, dopamine, the molecule we know as the "reward chemical," is already present in this worm, but in a different role. In nematodes, dopamine roughly signals "something good is nearby." When the worm is near food, dopamine is released, and the worm slows down to search the area thoroughly. Serotonin, by contrast, signals "I have eaten; I am full," and makes the worm stop searching and rest.

At this stage, then, neuromodulators are less like messages carrying specific information and more like broadcasts that shift the state of the whole body. Bennett locates the origin of emotion here. Combinations of valence and arousal form primitive affective states, and these states make behavior persist. They are what keep the worm searching even when the food scent briefly fades.

### The AI connection: Roomba

Bennett's analogy is the Roomba robot vacuum. Rodney Brooks's behavior-based robotics does not model the world in detail. Instead, it stacks simple reaction rules on top of sensor input to produce sensible-looking behavior. Bump into a wall, turn; find a dirty patch, scrub it longer. It is the same principle as the nematode's steering.

The lesson is clear: useful, intelligent-looking behavior is possible without a model of the world. But a Roomba cannot learn from experience. The nematode went one step further, and the difference lies in the synapse.

## 3. Synaptic plasticity: the first learning

Bilaterians do more than run reflexes. Nematodes and the sea slug _Aplysia_ both show associative learning. If food has always followed a particular odor, the odor alone becomes enough to draw them in. It is the same principle as Pavlov's dog salivating at the sound of a bell.

The physical basis of this learning is synaptic plasticity: when two neurons are active together, the synapse between them strengthens. Donald Hebb proposed this rule in 1949, and it is often summarized as "neurons that fire together, wire together." Eric Kandel used the simple circuits of _Aplysia_ to show that learning is indeed stored as changes in synaptic strength, work that earned him the 2000 Nobel Prize.

### Two problems that primitive learning already faced

Bennett makes a striking point here. Even the simplest associative learning already confronted two problems that AI still struggles with today.

First, the credit assignment problem. If several stimuli were present just before food was found, which one deserves the credit? Animals handle this with a handful of tricks:

- **Eligibility traces:** only synapses that were active within a short window before the outcome are candidates for change.
- **Overshadowing:** among several stimuli, the stronger or more salient one takes the association.
- **Latent inhibition:** a stimulus that has often been experienced with no consequence is slow to acquire a new association.
- **Blocking:** if one stimulus already predicts the outcome well, a newly added stimulus is not learned.

Second, the continual learning problem. How do you learn something new without losing what you already know? Artificial neural networks suffer from catastrophic forgetting: training on new data overwrites old knowledge. In animals, an extinguished association is not erased but suppressed. The evidence is spontaneous recovery, where the old response returns on its own after some time, and the fact that relearning is much faster than the original learning.

### The AI connection: weights and the three-factor rule

Synaptic strength as a weight, and plasticity as a weight update, is a natural mapping. Stepping slightly beyond the book, there is a more precise one.

A pure Hebbian rule looks at only two factors: were the two neurons active together? In the real brain, a neuromodulator such as dopamine enters as a third factor. Co-activation leaves a trace at the synapse, and if dopamine is broadcast shortly afterward, that trace is consolidated into a lasting change. This structure, known in neuroscience as the three-factor learning rule, closely resembles how a single scalar in reinforcement learning ("that outcome was good") modulates the direction of updates across the whole network.

In the nematode, dopamine still meant "something good is nearby." The heart of the second breakthrough is that this signal became a more refined learning signal: "that was better than expected."

## 4. Breakthrough 2, Reinforcing: try it, then learn from the result

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

## 5. Dopamine is the TD error

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

## 6. The correspondence at a glance

The tables below pair each biological mechanism with its AI counterpart, grouped by breakthrough. The last column is my own judgment of how close the match is.

**Groundwork**

| Biological mechanism | AI counterpart | How close |
| --- | --- | --- |
| Neuron (action potential, fire or not) | Artificial neuron (McCulloch–Pitts, activation function) | Extreme simplification |
| Synaptic strength | Weight | Conceptually direct |

**Steering**

| Biological mechanism | AI counterpart | How close |
| --- | --- | --- |
| Approach and avoidance by valence | Reactive robots (Roomba, behavior-based robotics) | Same principle |
| Global neuromodulator broadcast (dopamine, serotonin) | Global scalar signal (reward, learning-rate modulation) | Same principle |
| Synaptic plasticity (Hebbian rule) | Weight update | Different rules (local in the brain, backpropagation in deep learning) |
| Eligibility traces | Eligibility traces (TD(λ)) | Same term, same role |
| Spontaneous recovery after extinction | Catastrophic forgetting | Contrast: the brain suppresses, networks overwrite |

**Reinforcing**

| Biological mechanism | AI counterpart | How close |
| --- | --- | --- |
| Law of effect (trial and error) | Policy reinforcement | Direct |
| Dopamine as reward prediction error | TD error δ | Quantitative match (Schultz et al., 1997) |
| Action selection in the basal ganglia | Actor (actor-critic) | Rough match; details debated |
| Dopamine response to novelty | Intrinsic motivation, exploration bonus | Functional match |

## 7. Closing: similar, but not the same

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
2. Animals suppress old associations rather than erase them. What would an artificial network need in order to do the same?
3. TD learning learns from changes in prediction rather than from the final outcome. Where in your own field could a model learn from forecast updates rather than from observed outcomes alone?

---

**한 줄 요약 (Korean summary).** AI 기업가 Max Bennett는 『A Brief History of Intelligence』에서 지능의 진화를 다섯 번의 돌파 과정(steering, reinforcing, simulating, mentalizing, speaking)으로 정리하며, AI 연구자들이 막혔던 문제를 진화가 어떤 순서로 풀었는지를 다룬다. 약 6억 년 전 좌우대칭동물은 좋고 나쁨(valence)에 따라 다가가거나 피하는 조향(steering)을 시작했다. 이 단계의 선충에서 도파민은 무엇을 배우게 하는 신호가 아니라, “근처에 먹이가 있다”고 몸 전체에 알려 천천히 주변을 뒤지게 만드는 상태 신호였다. 선충은 경험으로 배울 수도 있었다. 함께 활동한 신경세포 사이의 연결(시냅스)이 강해지면서, 먹이 직전에 맡은 냄새만으로도 그쪽으로 다가가게 된다. 그런데 이 단순한 학습조차 오늘날 AI가 씨름하는 두 가지 문제에 이미 부딪혔다. 하나는 먹이를 찾기 직전에 여러 자극이 있었다면 그중 어느 것 덕분이었는지 가려내는 문제(신용 할당)이고, 다른 하나는 새로운 것을 배우면서도 예전에 배운 것을 잊지 않는 문제(지속 학습)이다. 약 5억 년 전 초기 척추동물은 한 걸음 더 나아갔다. “어떤 자극 뒤에 좋은 일이 오는가”가 아니라 “내가 어떤 행동을 했을 때 좋은 결과가 오는가”를 배우는 시행착오 학습(reinforcing)이다. 이 학습을 이끄는 신호를 보여준 것이 Schultz 등(1997)의 원숭이 실험이다. 불빛이 켜지고 몇 초 뒤 주스가 나오는 실험에서, 도파민 뉴런은 예상하지 못한 주스에는 강하게 반응했지만, 불빛으로 주스를 예상하게 된 뒤에는 주스가 아니라 불빛에 반응했고, 예상한 주스가 나오지 않으면 오히려 활동이 줄었다. 즉 도파민은 보상의 크기가 아니라 “예상보다 얼마나 좋았는가”를 알린다. 이는 AI 연구자 Richard Sutton이 기계가 늦게 오는 보상으로부터 배우도록 고안한 시간차(TD) 학습의 오차 신호와 똑같은 방식으로 움직인다. 정리하면, 진화는 학습을 위해 새로운 물질을 만든 것이 아니라, 선충 때부터 있던 도파민 신호의 뜻을 “좋은 것이 근처에 있다”에서 “예상보다 좋았다”로 바꾸어 다시 쓴 셈이다. 그렇다고 뇌가 곧 강화학습 알고리즘이라고 말하기는 이르다. 차이도 분명하기 때문이다. 뇌의 시냅스는 바로 이웃한 신경세포의 정보만으로 바뀌지만, 인공신경망은 출력의 오차를 모든 층에 정밀하게 되돌려 보내 학습한다. 물고기는 몇 번의 시도만으로 배우지만, 백개먼을 익힌 TD-Gammon은 수십만 번의 대국이 필요했다. 동물은 새로 배워도 옛 기억을 지우지 않고 눌러 두었다가 다시 꺼내 쓰지만, 인공신경망은 새 학습이 옛 지식을 덮어쓰기 쉽다. 또 도파민은 보상 예측 말고도 움직임, 의욕, 새로움에 대한 반응에도 관여한다. 그럼에도 이 대응은 의미가 있다. AI 연구자들은 뇌를 흉내 내서 이 해법을 찾은 것이 아니라 같은 문제를 풀려다 찾았다. 진화와 공학이 서로 모른 채 같은 답에 도달했다는 것은, 그 답이 우연이 아니라 풀어야 할 문제의 성격 자체에서 나온다는 것을 보여준다.

---

**References**

Bennett, M. (2023). _A Brief History of Intelligence: Evolution, AI, and the Five Breakthroughs That Made Our Brains_. Mariner Books.

Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. _Science_, 275, 1593–1599. [https://doi.org/10.1126/science.275.5306.1593](https://doi.org/10.1126/science.275.5306.1593)

Sutton, R. S. (1988). Learning to predict by the methods of temporal differences. _Machine Learning_, 3, 9–44. [https://doi.org/10.1007/BF00115009](https://doi.org/10.1007/BF00115009)

Tesauro, G. (1995). Temporal difference learning and TD-Gammon. _Communications of the ACM_, 38, 58–68. [https://doi.org/10.1145/203330.203343](https://doi.org/10.1145/203330.203343)

Sutton, R. S., & Barto, A. G. (2018). _Reinforcement Learning: An Introduction_ (2nd ed.). MIT Press.
