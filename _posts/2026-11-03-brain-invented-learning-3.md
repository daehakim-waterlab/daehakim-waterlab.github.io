---
layout: post
title: "How the brain invented learning, part III: simulating in A Brief History of Intelligence"
date: 2026-11-03 09:10:00 +0900
description: "Notes on the third of Max Bennett's five breakthroughs: how early mammals learned to try things out in imagination, why the neocortex looks like a generative model, and how the same idea became model-based reinforcement learning, from Dyna to AlphaGo and MuZero."
tags: artificial-intelligence neuroscience reinforcement-learning book-notes
categories: notes
related_posts: false
---

In [part I]({% post_url 2026-10-25-brain-invented-learning %}), bilaterian worms learned to steer toward the good and away from the bad. In [part II]({% post_url 2026-10-26-brain-invented-learning-2 %}), early vertebrates learned by trial and error, with dopamine signaling whether things turned out better than expected. Both kinds of learning share a limitation: the animal has to actually do something to learn from it.

This post covers the third breakthrough in Max Bennett's _A Brief History of Intelligence_ (2023): simulating. In Bennett's account it arrived with the first mammals and their new brain structure, the neocortex, which let an animal try things out in imagination before trying them in the world. In AI, the same idea is called model-based reinforcement learning. As before, the summary is my own paraphrase of the book's argument, and some connections, notably to Dyna, AlphaGo and MuZero, come from the broader literature.

## 1. Breakthrough 3, Simulating: trying things out in the head

A fish that learns by trial and error stores, for each situation, how good each action has turned out to be. This works, but it has a cost: every lesson requires a real attempt, and some attempts are fatal. It is also inflexible. If the world changes, for example if food moves to a new place, the fish must relearn by trial and error, because it has no idea why its old habits worked.

An animal with a model of its world can do better. It can ask "what would happen if I went left?" and answer the question without moving.

### Rats that think before they turn

In 1948, Edward Tolman reported that rats allowed to explore a maze without any reward later learned to run it much faster than rats that had never seen it, and that they could take shortcuts they had never been trained on (Tolman 1948). He concluded that rats build a "cognitive map" of their surroundings, not just a list of rewarded turns.

Tolman and his contemporaries also noticed that rats at a choice point often pause and look back and forth between the options, a behavior called vicarious trial and error. Almost sixty years later, recordings from the rat hippocampus showed what happens during those pauses. Place cells, which fire when a rat is at a particular location, fired in sequences that swept ahead of the animal, first down one path and then down the other, as if the rat were mentally walking each route before choosing (Johnson and Redish 2007).

## 2. The neocortex as a generative model

The neocortex is the structure that most distinguishes the mammalian brain. Bennett's central claim about it is that it works as a generative model: it learns how the world is structured well enough to produce plausible sensory experience on its own.

This idea is older than modern AI. In the nineteenth century, Hermann von Helmholtz argued that perception is a kind of unconscious inference: we do not simply receive images, we infer the most likely world that would have produced them. That is why we fill in the blind spot and see shapes in ambiguous pictures. If the brain can generate what it expects to see, the same machinery can be run without input, and that is imagination.

Evidence that memory and imagination share this machinery comes from patients with damage to the hippocampus. Such patients not only struggle to remember the past; they also struggle to imagine new experiences, producing fragmented scenes when asked to picture, for example, lying on a beach (Hassabis et al. 2007).

**The AI connection.** Neural network researchers arrived at similar ideas. The "wake-sleep" algorithm of the 1990s trained a network to recognize inputs while a second, generative pathway learned to produce them, alternating between a waking phase driven by data and a "sleeping" phase driven by the network's own fantasies (Hinton et al. 1995). Predictive coding models of the visual cortex proposed that higher brain areas send predictions downward and only the errors travel upward (Rao and Ballard 1999). Today's generative AI, which produces text, images and video from learned models, is the most visible descendant of this line of thought.

## 3. What simulation buys

### Planning

A model lets an animal compare futures before committing to one, as the hippocampal sweeps suggest rats do. This is planning, and it is most useful when mistakes are costly and the situation is new.

### Learning from imagined experience

A model also lets an animal learn from experiences it never had. During sleep and rest, the rat hippocampus replays sequences of place-cell activity from the day's runs (Wilson and McNaughton 1994), a candidate mechanism for consolidating and extending what was learned.

**The AI connection.** In 1990, Richard Sutton proposed Dyna, an architecture in which an agent learns a model of its environment from real experience and then also learns from simulated experience generated by that model (Sutton 1990). The effect is dramatic even in a tiny maze. Figure 1 shows a simulation I ran of the maze used in Sutton and Barto's textbook: an agent that learns only from real steps needs about 28 trips to find a near-shortest path, while one that adds 50 imagined steps for each real step needs about 3. Replaying stored experience later became a key ingredient of deep reinforcement learning, including DQN, which learned to play 49 Atari games directly from the screen pixels (Mnih et al. 2015).

![Steps per episode in a maze for agents with and without imagined experience](/assets/img/blog/2026-11-03-dyna-maze.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 1.** Steps needed to reach the goal in a small maze, for an agent that learns only from real experience and for agents that also learn from 5 or 50 imagined steps per real step, generated from a model learned along the way (Dyna-Q). Averages over 30 runs; the first episode is omitted. Figure by Daeha Kim, a simulation of the Dyna maze described in Sutton and Barto (2018)._

### Learning from what did not happen

A model makes it possible to ask "what if I had chosen otherwise?" Rats seem to do this too. In a task where they chose between restaurants offering food after different delays, rats that skipped a good deal and then met a worse one looked back toward the option they had passed, and neurons in their orbitofrontal cortex represented the missed option, a pattern the authors interpreted as regret (Steiner and Redish 2014). Learning from counterfactuals extracts more from each experience than learning from outcomes alone.

### Habits and plans side by side

Mammals did not replace the old system with the new one. They kept both. Fast, cached habits handle familiar situations; slow, model-based planning handles new or changing ones. An influential computational account proposes that the brain arbitrates between the two according to which is more reliable at the moment, with planning favored early in learning and habits once a task is well practiced (Daw et al. 2005).

## 4. The AI connection: planning with a model

The most famous AI systems of the last decade are, at their core, simulators. AlphaGo combined neural networks, which learned to evaluate positions and suggest moves, with tree search, which simulated possible continuations of the game before each move (Silver et al. 2016). It played Go using a perfect model of the rules.

MuZero went a step further: it learned its own model of the environment and planned inside that learned model, reaching superhuman play in Go, chess and shogi and strong play in Atari games without being told the rules (Schrittwieser et al. 2020). DreamerV3 learns a world model and trains its behavior largely in imagined trajectories, and with one fixed configuration it learned to collect diamonds in Minecraft from scratch (Hafner et al. 2025). These are the engineering versions of a rat pausing at a fork in the maze.

## 5. The correspondence at a glance

The table below pairs each biological mechanism with its AI counterpart. The last column is my own judgment of how close the match is.

| Biological mechanism | AI counterpart | How close |
| --- | --- | --- |
| Cognitive map (Tolman) | Learned model of the environment | Same idea |
| Neocortex as a generative model | Generative models (wake-sleep, modern generative AI) | Same principle, very different mechanisms |
| Perception as inference, predictive coding | Predictive coding networks | Influential hypothesis on both sides |
| Vicarious trial and error, hippocampal sweeps | Planning by simulation (tree search) | Functional match |
| Replay during sleep and rest | Dyna, experience replay | Functional match |
| Regret, counterfactual learning | Counterfactual updates in planning | Partial match |
| Arbitration between habits and planning | Hybrid model-free and model-based agents | Active research on both sides |

## 6. Closing: imagination has a price

Simulation made mammals flexible learners. They could plan around danger, learn from experiences they never had, and regret choices without repeating them. But simulation is slow and costly, which is why habits remain, and a simulation is only as good as the model behind it. A wrong model produces confident plans that fail, a problem that model-based AI shares.

Bennett's next breakthrough, mentalizing, turns the simulator inward and toward others: primates began to model not just the world but minds, including their own. That is the subject of part IV.

**Questions to think about**

1. A model-free learner needs many real trials; a model-based learner needs a good model. In which of your own problems is it easier to collect experience, and in which is it easier to build a model?
2. Hydrologists run rainfall–runoff models to compare flood-control options before choosing one. In what ways is that like a rat pausing at a fork in the maze, and in what ways is it different?
3. If imagination and memory share the same machinery, what might that mean for how reliable our memories are?

---

**한 줄 요약 (Korean summary).** 『A Brief History of Intelligence』의 세 번째 돌파는 초기 포유류가 신피질을 통해 얻은 시뮬레이션(simulating) 능력이다. 시행착오 학습은 실제로 해 봐야만 배울 수 있지만, 세계의 모형을 가진 동물은 머릿속에서 먼저 시도해 보고 고를 수 있다. 실제로 쥐는 갈림길에서 멈춰 두 길을 번갈아 살피며, 이때 해마의 위치세포가 앞으로 갈 경로를 차례로 미리 훑는다. 이 생각은 AI에서 모형 기반 강화학습이 되었고, 상상한 경험으로도 학습하는 Dyna에서 바둑의 AlphaGo, 스스로 규칙을 배워 계획하는 MuZero로 이어졌다.

---

**References**

Bennett, M. (2023). _A Brief History of Intelligence: Evolution, AI, and the Five Breakthroughs That Made Our Brains_. Mariner Books.

Daw, N. D., Niv, Y., & Dayan, P. (2005). Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control. _Nature Neuroscience_, 8, 1704–1711. [https://doi.org/10.1038/nn1560](https://doi.org/10.1038/nn1560)

Hafner, D., Pasukonis, J., Ba, J., & Lillicrap, T. (2025). Mastering diverse control tasks through world models. _Nature_, 640, 647–653. [https://doi.org/10.1038/s41586-025-08744-2](https://doi.org/10.1038/s41586-025-08744-2)

Hassabis, D., Kumaran, D., Vann, S. D., & Maguire, E. A. (2007). Patients with hippocampal amnesia cannot imagine new experiences. _Proceedings of the National Academy of Sciences_, 104, 1726–1731. [https://doi.org/10.1073/pnas.0610561104](https://doi.org/10.1073/pnas.0610561104)

Hinton, G. E., Dayan, P., Frey, B. J., & Neal, R. M. (1995). The "wake-sleep" algorithm for unsupervised neural networks. _Science_, 268, 1158–1161. [https://doi.org/10.1126/science.7761831](https://doi.org/10.1126/science.7761831)

Johnson, A., & Redish, A. D. (2007). Neural ensembles in CA3 transiently encode paths forward of the animal at a decision point. _Journal of Neuroscience_, 27, 12176–12189. [https://doi.org/10.1523/JNEUROSCI.3761-07.2007](https://doi.org/10.1523/JNEUROSCI.3761-07.2007)

Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Veness, J., Bellemare, M. G., et al. (2015). Human-level control through deep reinforcement learning. _Nature_, 518, 529–533. [https://doi.org/10.1038/nature14236](https://doi.org/10.1038/nature14236)

Rao, R. P. N., & Ballard, D. H. (1999). Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects. _Nature Neuroscience_, 2, 79–87. [https://doi.org/10.1038/4580](https://doi.org/10.1038/4580)

Schrittwieser, J., Antonoglou, I., Hubert, T., Simonyan, K., Sifre, L., Schmitt, S., et al. (2020). Mastering Atari, Go, chess and shogi by planning with a learned model. _Nature_, 588, 604–609. [https://doi.org/10.1038/s41586-020-03051-4](https://doi.org/10.1038/s41586-020-03051-4)

Silver, D., Huang, A., Maddison, C. J., Guez, A., Sifre, L., van den Driessche, G., et al. (2016). Mastering the game of Go with deep neural networks and tree search. _Nature_, 529, 484–489. [https://doi.org/10.1038/nature16961](https://doi.org/10.1038/nature16961)

Steiner, A. P., & Redish, A. D. (2014). Behavioral and neurophysiological correlates of regret in rat decision-making on a neuroeconomic task. _Nature Neuroscience_, 17, 995–1002. [https://doi.org/10.1038/nn.3740](https://doi.org/10.1038/nn.3740)

Sutton, R. S. (1990). Integrated architectures for learning, planning, and reacting based on approximating dynamic programming. In _Machine Learning Proceedings 1990_ (pp. 216–224). Morgan Kaufmann. [https://doi.org/10.1016/B978-1-55860-141-3.50030-4](https://doi.org/10.1016/B978-1-55860-141-3.50030-4)

Sutton, R. S., & Barto, A. G. (2018). _Reinforcement Learning: An Introduction_ (2nd ed.). MIT Press.

Tolman, E. C. (1948). Cognitive maps in rats and men. _Psychological Review_, 55, 189–208. [https://doi.org/10.1037/h0061626](https://doi.org/10.1037/h0061626)

Wilson, M. A., & McNaughton, B. L. (1994). Reactivation of hippocampal ensemble memories during sleep. _Science_, 265, 676–679. [https://doi.org/10.1126/science.8036517](https://doi.org/10.1126/science.8036517)

_The figure is original. The Python script that produces it is available on [GitHub](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-11-03-dyna-maze.py)._
