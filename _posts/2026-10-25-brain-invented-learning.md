---
layout: post
title: "How the brain invented learning, part I: steering in A Brief History of Intelligence"
date: 2026-10-25 21:00:00 +0900
description: "Notes on the first of Max Bennett's five breakthroughs: how the first neurons and brains appeared, how bilaterian worms learned to steer by good and bad, and how even their simple learning already faced problems that AI still struggles with."
tags: artificial-intelligence neuroscience neural-networks book-notes
categories: notes
related_posts: false
---

The problems a worm solved 600 million years ago, and a fish solved 500 million years ago, look remarkably like the problems AI researchers ran into in the late twentieth century. Max Bennett's _A Brief History of Intelligence_ (2023) is built around that overlap.

Bennett is not a neuroscientist; he is an AI entrepreneur. That gives the book an unusual angle. He asks: at the points where we get stuck trying to build intelligence into machines, how, and in what order, did evolution get past them? His answer is organized into five "breakthroughs": steering, reinforcing, simulating, mentalizing, and speaking.

This post covers the first, steering: the story of how bilaterian animals got the first brains. The second, reinforcing, the story of how early vertebrates acquired trial-and-error learning, follows in [part II]({% post_url 2026-10-26-brain-invented-learning-2 %}). The main characters in both are neurons, synapses, and dopamine, and each maps with surprising precision onto the weights of artificial neural networks and the reward signal of reinforcement learning.

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

## 4. The correspondence so far

The tables below pair each biological mechanism with its AI counterpart. The last column is my own judgment of how close the match is.

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

## 5. Closing: a sense of good and bad, and a memory

Steering and synaptic plasticity gave the first brains two things: a way to sort the world into good and bad, and a way to store experience in the strength of synapses. Each maps neatly onto something in AI, from reactive robots to weight updates. But the nematode's learning was about stimuli, not about its own actions, and its dopamine still meant only "something good is nearby." How that signal became a learning signal, and why it turned out to match an algorithm AI researchers had already written down, is the subject of [part II]({% post_url 2026-10-26-brain-invented-learning-2 %}).

**Questions to think about**

1. A Roomba behaves sensibly without learning anything. Which tasks in your own field could be handled by simple steering rules, and which need learning?
2. Animals suppress old associations rather than erase them. What would an artificial network need in order to do the same?
3. Eligibility traces, overshadowing, latent inhibition and blocking are the animal's tricks for credit assignment. Which of them have counterparts in how scientists attribute an observed change to one of several possible causes?

---

**한 줄 요약 (Korean summary).** AI 기업가 Max Bennett는 『A Brief History of Intelligence』에서 지능의 진화를 다섯 번의 돌파 과정(steering, reinforcing, simulating, mentalizing, speaking)으로 정리하며, AI 연구자들이 막혔던 문제를 진화가 어떤 순서로 풀었는지를 다룬다. 이 글은 첫 단계인 조향(steering)을 다룬다. 약 6억 년 전 좌우대칭동물은 좋고 나쁨(valence)에 따라 다가가거나 피하기 시작했고, 함께 활동한 신경세포 사이의 연결이 강해지는 방식으로 경험에서 배우게 되었다. 그런데 이 단순한 학습도 오늘날 AI가 겪는 두 가지 어려움을 이미 안고 있었다. 하나는 먹이를 찾기 직전에 냄새, 빛, 온도 같은 여러 자극이 함께 있었다면 그중 어느 것을 기억해야 하는지 가려내는 일(신용 할당)이고, 다른 하나는 새로운 것을 배울 때 예전에 배운 것이 지워지지 않게 하는 일(지속 학습)이다.

---

**Reference**

Bennett, M. (2023). _A Brief History of Intelligence: Evolution, AI, and the Five Breakthroughs That Made Our Brains_. Mariner Books.
