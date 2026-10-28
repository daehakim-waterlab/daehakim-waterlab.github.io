---
layout: post
title: "More compute, better AI: how much better?"
date: 2026-10-29 07:20:00 +0900
description: "What neural scaling laws actually predict when hardware and compute grow, where the extra compute comes from, how much thinking longer adds, and the limits of power, data and money, checked against the primary sources as of October 2026."
tags: artificial-intelligence large-language-models scaling-laws computing
categories: notes
related_posts: false
---

"Scaling laws" are the reason AI companies are building gigawatt data centers. The idea is that a language model improves predictably as it gets more computing power, more parameters and more data. But how much better? If we had ten or a hundred times more computing power than today, what would we get? This post works through the answer using the original papers and the latest data, as of October 2026.

## The scaling law in one sentence

In 2020, Kaplan and colleagues at OpenAI showed that a language model's loss, a measure of how badly it predicts the next word, falls as a power law of training compute, over eight orders of magnitude (Kaplan et al. 2020). In 2022, DeepMind's "Chinchilla" study refined the recipe: for a given compute budget, parameters and training data should grow together, roughly 20 tokens of text per parameter (Hoffmann et al. 2022). A later replication by Epoch AI corrected the fitted constants but confirmed the 20-to-1 rule (Besiroglu et al. 2024).

The corrected fit makes the returns concrete. Loss has an irreducible floor, set by the inherent unpredictability of text, and only the gap above that floor can be closed. **Each 10× increase in compute closes about a third of the remaining gap; 100× closes about half** (Figure 1a, my calculation from the fit). In other words, every halving of what is left to gain costs about a hundredfold more compute.

![Predicted loss and training data needed versus training compute](/assets/img/blog/2026-10-29-scaling-loss.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 1.** (a) Pretraining loss predicted by the Chinchilla scaling law (with Epoch AI's corrected constants) when compute is allocated optimally between model size and data, with the approximate training compute of some well-known models and of the largest run Epoch AI judges feasible by 2030. (b) The number of training tokens the same law calls for, compared with the estimated stock of public human-written text. The fit describes one family of models; it shows the shape of the curve, not the exact loss of any frontier model. Figure by Daeha Kim, calculated from Besiroglu et al. (2024), with compute estimates from Brown et al. (2020) and Epoch AI, and the data stock from Villalobos et al. (2024)._

## Does lower loss mean a smarter model?

Loss falls smoothly, but people experience abilities, and abilities sometimes seem to appear suddenly with scale. A 2023 study showed that most of these apparent jumps are artifacts of all-or-nothing scoring: more than 92% of the claimed "emergent abilities" came from just two metrics that give credit only for a perfectly right answer (Schaeffer et al. 2023). Measured with continuous scores, the same abilities improve gradually.

Real-world capability has nonetheless improved fast. METR measures the length of software tasks, in human working time, that AI agents can complete half the time. That "time horizon" doubled about every seven months between 2019 and 2025 (Kwa et al. 2025), and on METR's updated task suite the doubling time shortened to about 130 days since 2023 and 89 days since 2024 (METR 2026). By mid-2026 the best models were near the ceiling of what the suite can measure. METR stopped updating its measurements in September, so there is no reliable figure for the months since.

## Faster chips are only part of the story

The obvious way to get more compute is better hardware, but chips alone improve slowly. Epoch AI decomposed the growth of frontier training compute, about 4.2× per year since 2018 (Epoch AI 2025; Figure 2):

- more chips per training run: 1.7× per year;
- longer training runs: 1.5× per year;
- faster chips: 1.4× per year.

In log terms, faster chips supply only about a quarter of the growth. At 1.4× per year, a tenfold improvement from chips alone takes about seven years. The frontier gets ten times more compute about every year and a half mainly by spending more: the cost of the largest training runs has grown about 2.4× per year (Cottier et al. 2024), and the largest single data centers now draw about a gigawatt.

Better algorithms add a further multiplier. The compute needed to reach a given level of language-model performance has halved about every eight months, equivalent to about 2.8× more "effective" compute every year (Ho et al. 2024). Combining both, effective compute has grown roughly tenfold or more per year, my calculation.

![Growth factors of frontier training compute and its components](/assets/img/blog/2026-10-29-scaling-sources.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 2.** Median yearly growth of training compute for frontier models since 2018 and its three components, and the yearly gain from better algorithms expressed as equivalent compute. Figure by Daeha Kim, drawn from numbers reported by Epoch AI (2025) and Ho et al. (2024)._

## A second axis: thinking longer

Since 2024, a second kind of scaling has mattered as much as the first. Reasoning models such as OpenAI's o1 improve when they are allowed to spend more compute on each question. On the AIME 2024 math competition, o1 solved 74% of problems with one attempt, 83% with a majority vote over 64 attempts, and 93% when a learned scorer picked the best of 1,000 (OpenAI 2024). On the ARC-AGI puzzle benchmark, o3 rose from 75.7% to 87.5% when given about 172 times more compute per task (ARC Prize 2024).

The pattern is the same as in pretraining: gains are roughly linear in the logarithm of compute, so each additional step costs ten to a hundred times more (Figure 3). Reinforcement learning, the training method behind these reasoning models, shows a similar shape but levels off at a ceiling set by the training recipe (Khatri et al. 2025).

![Accuracy versus number of samples per problem for o1 and o3](/assets/img/blog/2026-10-29-scaling-inference.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 3.** Accuracy of OpenAI's o1 on AIME 2024 and of o3 (preview) on ARC-AGI-1 as more samples are used per problem. The o1 points use different ways of combining samples (a single attempt, a majority vote and re-ranking by a learned scorer). Figure by Daeha Kim, drawn from numbers reported by OpenAI (2024) and ARC Prize (2024)._

## The limits ahead: power, data and money

Epoch AI estimates that a training run of about 2×10²⁹ FLOP, roughly 400 times the largest known run of 2025, is likely feasible by 2030, but power is the first constraint to bind: such a run would need about 6 gigawatts, while today's largest single sites draw about one (Sevilla et al. 2024).

Data may bind even earlier. The stock of public human-written text is estimated at about 300 trillion tokens (Villalobos et al. 2024). A compute-optimal run of 10²⁸ FLOP would already need about 150 trillion tokens, half of it (Figure 1b). Repeating data helps for a while, since up to about four passes over the same text is nearly as good as new data (Muennighoff et al. 2023), and synthetic data and reinforcement learning on checkable tasks are partly a response to this limit.

## Have the returns diminished?

In late 2024 and 2025, reports suggested that simply making pretraining bigger was paying off less than expected, and OpenAI's GPT-4.5 was widely seen as a modest step. In November 2025, Ilya Sutskever described the period from 2020 to 2025 as an "age of scaling" now giving way to an "age of research." Yet over the same period, measured capability accelerated: an Epoch AI analysis found that several capability indices, including METR's time horizon, sped up around 2024, driven largely by reasoning models and concentrated in code and mathematics (Epoch AI 2026).

Both observations fit the scaling law. Returns to pretraining compute were always diminishing in the sense shown in Figure 1, so a few times more compute buys a modest step. What changed is that labs found a second, cheaper axis, reinforcement learning and inference-time compute, and better algorithms on top.

## So how much does more hardware buy?

- **On paper:** each 10× in training compute closes about a third of the remaining gap in loss. Large, steady gains require exponential increases in compute.
- **In practice:** that 10× arrives about every 18 months, but mostly from more chips and more money; faster chips alone would take about seven years to deliver it.
- **Beyond pretraining:** letting models think longer adds similar log-linear gains per question, at a cost paid every time the model is used.
- **Limits:** power and data, not chip speed, are the constraints most likely to bind before 2030.

Scaling laws do not promise that more hardware makes AI arbitrarily capable. They promise steady improvement for exponentially rising cost, and so far that bargain, combined with better algorithms, has been good enough to keep progress fast.

**Questions to think about**

1. If each halving of the remaining loss costs a hundredfold more compute, what would make it worth paying?
2. Inference-time compute is paid every time a model is used. How does that change the economics compared with training compute, which is paid once?
3. Many scientific models also improve with resolution and data following power laws. Where in your own field have you seen diminishing returns of this kind?

---

**한 줄 요약 (Korean summary).** 스케일링 법칙에 따르면 언어 모델의 손실은 학습 연산량의 거듭제곱 법칙으로 줄어들지만, 줄일 수 있는 부분에는 바닥이 있어 연산량을 10배 늘릴 때마다 남은 격차의 약 3분의 1, 100배 늘리면 약 절반이 줄어든다. 최첨단 모델의 학습 연산량은 해마다 약 4배씩 늘었지만 칩 성능 향상(연 1.4배)의 기여는 4분의 1 정도이고, 나머지는 더 많은 칩, 더 긴 학습, 더 큰 투자에서 나왔으며, 알고리즘 개선이 해마다 약 2.8배의 연산 효과를 더했다. 2024년 이후에는 답하기 전에 더 오래 생각하게 하는 추론 연산이 두 번째 축이 되었지만, 이 역시 연산량의 로그에 비례해 좋아져 한 단계 나아갈 때마다 10–100배의 비용이 든다. 앞으로는 칩 속도보다 전력(2030년 규모의 학습에 약 6 GW)과 데이터(공개 텍스트 약 300조 토큰)가 먼저 한계가 될 가능성이 크다.

---

**References**

ARC Prize (2024). OpenAI o3 breakthrough high score on ARC-AGI-Pub. 20 December 2024 (costs revised in 2025). [https://arcprize.org/blog/oai-o3-pub-breakthrough](https://arcprize.org/blog/oai-o3-pub-breakthrough)

Besiroglu, T., Erdil, E., Barnett, M., & You, J. (2024). Chinchilla scaling: a replication attempt. _arXiv_, 2404.10102. [https://doi.org/10.48550/arXiv.2404.10102](https://doi.org/10.48550/arXiv.2404.10102)

Cottier, B., Rahman, R., Fattorini, L., Maslej, N., Besiroglu, T., & Owen, D. (2024). The rising costs of training frontier AI models. _arXiv_, 2405.21015. [https://doi.org/10.48550/arXiv.2405.21015](https://doi.org/10.48550/arXiv.2405.21015)

Epoch AI (2025). Training compute growth is driven by larger clusters and longer training runs. 8 January 2025. [https://epoch.ai/data-insights/training-compute-decomposition](https://epoch.ai/data-insights/training-compute-decomposition)

Epoch AI (2026). Have AI capabilities accelerated? 16 April 2026. [https://epoch.ai/publications/have-ai-capabilities-accelerated](https://epoch.ai/publications/have-ai-capabilities-accelerated)

Ho, A., Besiroglu, T., Erdil, E., Owen, D., Rahman, R., Guo, Z. C., Atkinson, D., Thompson, N., & Sevilla, J. (2024). Algorithmic progress in language models. _arXiv_, 2403.05812. [https://doi.org/10.48550/arXiv.2403.05812](https://doi.org/10.48550/arXiv.2403.05812)

Hoffmann, J., Borgeaud, S., Mensch, A., Buchatskaya, E., Cai, T., Rutherford, E., et al. (2022). Training compute-optimal large language models. _arXiv_, 2203.15556. [https://doi.org/10.48550/arXiv.2203.15556](https://doi.org/10.48550/arXiv.2203.15556)

Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., et al. (2020). Scaling laws for neural language models. _arXiv_, 2001.08361. [https://doi.org/10.48550/arXiv.2001.08361](https://doi.org/10.48550/arXiv.2001.08361)

Khatri, D., et al. (2025). The art of scaling reinforcement learning compute for LLMs. _arXiv_, 2510.13786. [https://doi.org/10.48550/arXiv.2510.13786](https://doi.org/10.48550/arXiv.2510.13786)

Kwa, T., West, B., Becker, J., et al. (2025). Measuring AI ability to complete long tasks. _arXiv_, 2503.14499. [https://doi.org/10.48550/arXiv.2503.14499](https://doi.org/10.48550/arXiv.2503.14499)

METR (2026). Time Horizon 1.1. 29 January 2026. [https://metr.org/blog/2026-01-29-time-horizon-1-1/](https://metr.org/blog/2026-01-29-time-horizon-1-1/)

Muennighoff, N., Rush, A. M., Barak, B., Le Scao, T., Piktus, A., Tazi, N., Pyysalo, S., Wolf, T., & Raffel, C. (2023). Scaling data-constrained language models. _arXiv_, 2305.16264. [https://doi.org/10.48550/arXiv.2305.16264](https://doi.org/10.48550/arXiv.2305.16264)

OpenAI (2024). Learning to reason with LLMs. 12 September 2024. [https://openai.com/index/learning-to-reason-with-llms/](https://openai.com/index/learning-to-reason-with-llms/)

Schaeffer, R., Miranda, B., & Koyejo, S. (2023). Are emergent abilities of large language models a mirage? _Advances in Neural Information Processing Systems_, 36. [https://doi.org/10.48550/arXiv.2304.15004](https://doi.org/10.48550/arXiv.2304.15004)

Sevilla, J., et al. (2024). Can AI scaling continue through 2030? Epoch AI, 20 August 2024. [https://epoch.ai/blog/can-ai-scaling-continue-through-2030](https://epoch.ai/blog/can-ai-scaling-continue-through-2030)

Villalobos, P., Ho, A., Sevilla, J., Besiroglu, T., Heim, L., & Hobbhahn, M. (2024). Will we run out of data? Limits of LLM scaling based on human-generated data. _arXiv_, 2211.04325. [https://doi.org/10.48550/arXiv.2211.04325](https://doi.org/10.48550/arXiv.2211.04325)

_All three figures are original. The Python scripts that produce them are available on GitHub: [Figure 1](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-29-scaling-loss.py), [Figure 2](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-29-scaling-sources.py), [Figure 3](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-29-scaling-inference.py)._
