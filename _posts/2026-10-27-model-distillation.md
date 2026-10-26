---
layout: post
title: "Model distillation: how AI models learn from each other, and what they lose"
date: 2026-10-27 01:05:00 +0900
description: "What distillation is, why it lets new models catch up with the frontier so quickly, why it has become a dispute between AI labs, whether it can be prevented, and the limits of models built this way."
tags: artificial-intelligence large-language-models distillation research-practice
categories: notes
related_posts: false
---

In July 2026, the White House science adviser accused the Chinese company Moonshot AI of building its Kimi K3 model by "distilling" Anthropic's Claude Fable. China's embassy in Washington called the allegation "entirely unfounded" (Business Today 2026), and several AI researchers doubted it, noting that K3 appeared only about two weeks after Fable became public and that distillation alone is unlikely to produce such a strong model so quickly (AI Weekly 2026). True or not, the episode shows how central one technique has become to the competition between AI labs. This post explains what distillation is, why it works, whether it can be stopped, and what models built this way tend to lack.

## What distillation is

Distillation means training a smaller or newer model, the "student," to imitate a stronger one, the "teacher." The idea was popularized by Hinton and colleagues in 2015 (Hinton et al. 2015). Their key observation was that a teacher's full output carries more information than its final answer. When a language model completes "The capital of Australia is …," it assigns a high probability to Canberra, but also a noticeable probability to Sydney and almost none to Perth (Figure 1a). Those small numbers encode how the teacher sees the world, which mistakes are plausible and which are not. Hinton called it "dark knowledge." A student trained to match the whole distribution learns faster and from fewer examples than one trained only on correct answers.

Inside a lab, distillation is routine and legitimate. The fast, cheap versions of frontier models are typically distilled from larger ones, and DeepSeek released a family of small open models distilled from its R1 reasoning model (DeepSeek-AI 2025).

The controversial version works from the outside. A competitor cannot see another lab's probabilities, but it can send millions of questions through the public interface, collect the answers, and train its own model on them. The student then sees much less than in the classic setup: one sampled answer instead of a full distribution, and often no reasoning at all (Figure 1b).

![Teacher probability distribution and what a student model can see](/assets/img/blog/2026-10-27-distill-signal.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 1.** (a) An illustrative next-word distribution from a teacher model: besides the right answer, it shows which wrong answers are close. (b) What a student model can learn from, from a lab distilling its own model to a competitor working through a chat interface. The probabilities and bar lengths are illustrative. Figure by Daeha Kim, a schematic based on Hinton et al. (2015)._

## Why it has become a dispute

The attraction is obvious: answers from a frontier model are far cheaper to collect than the compute, data and expertise needed to develop the same abilities independently. In February 2026, Anthropic reported that three Chinese labs, DeepSeek, Moonshot AI and MiniMax, had generated more than 16 million exchanges with Claude through about 24,000 fraudulent accounts, targeting its strongest abilities: agentic reasoning, tool use and coding (Anthropic 2026; Figure 2). These are Anthropic's attributions; the labs have not confirmed them. The July accusation about Kimi K3 went further, but its evidence has not been made public.

![Exchanges with Claude attributed to distillation campaigns by three labs](/assets/img/blog/2026-10-27-distill-campaigns.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 2.** Exchanges with Claude that Anthropic attributed to distillation campaigns by three AI labs, as reported in February 2026. According to Anthropic, the campaigns targeted agentic coding and tool use (MiniMax); agentic reasoning, tool use, coding, computer use and vision (Moonshot AI); and reasoning and the grading of answers for reinforcement learning (DeepSeek). Figure by Daeha Kim, drawn from numbers reported in Anthropic (2026)._

The dispute has an uncomfortable side for the accusers, too. Frontier models were themselves trained on vast amounts of text written by others, and the line between learning from public outputs and copying is contested. What makes the current cases different, in the labs' view, is the use of fake accounts and the violation of terms of service to extract a competitor's specific capabilities at scale.

## Can it be prevented?

Not completely. Anything a model shows its users, it also shows a potential student. What labs can do is make distillation slower, costlier and less useful:

- **Detection.** Classifiers that recognize distillation patterns, such as huge numbers of similar prompts or systematic attempts to extract reasoning, and that link many accounts to one operator (Anthropic 2026).
- **Access control.** Stronger identity checks for the account types most often abused, and sharing of indicators between labs and cloud providers.
- **Hiding the reasoning.** Since 2024, several labs show only a summary of their models' step-by-step reasoning. OpenAI cited competitive advantage, alongside safety monitoring, when it decided not to show the raw reasoning of its o1 models (OpenAI 2024).
- **Poisoned outputs.** Researchers have proposed "antidistillation sampling," which subtly changes how a model picks its words so that the answers remain useful to people but are much less useful as training data for a student (Savani et al. 2025).

Each defense has a cost for legitimate users, who also want to see the reasoning and use the model at scale. The realistic goal is to keep distillation from being a shortcut, not to make it impossible.

## What distilled models lack

Distillation lets a model catch up quickly. But copying has limits.

**Style transfers more easily than substance.** In a careful 2023 study, researchers fine-tuned open models on ChatGPT outputs. Human raters judged the imitations close to ChatGPT, because they had learned its confident, well-structured style, yet on targeted tests of factual knowledge, coding and problem solving they improved little or not at all (Gudibande et al. 2024). The authors concluded that closing the gap requires a stronger base model, not more imitation. A distilled model can therefore look better than it is, which also makes some benchmark scores and first impressions misleading.

**The student learns only what it is asked.** A campaign aimed at coding and agents transfers coding and agents. Rare facts, niche fields, other languages and unusual situations are covered thinly, and the student sees only sampled answers without the teacher's uncertainty. As discussed in an [earlier post on hallucination]({% post_url 2026-10-24-llm-hallucination %}), rare facts are exactly where models make things up.

**It inherits mistakes, and copies of copies degrade.** A student copies its teacher's errors and biases along with its strengths. When models are trained repeatedly on the output of other models, the rare parts of the original data, the tails of the distribution, gradually disappear, a process known as model collapse (Shumailov et al. 2024).

**It stays one step behind.** A student rarely surpasses its teacher in what it copies, and it can only copy what already exists. Distillation is a way to follow the frontier, not to move it.

**Safety behavior may not come along.** Anthropic argues that illicitly distilled models are unlikely to keep the safeguards built into the original, such as refusals to help with weapons or cyberattacks (Anthropic 2026).

**Provenance becomes a risk.** For companies, universities and public agencies, a model built in violation of another provider's terms carries legal and reputational risk, and possibly sanctions. That matters when choosing a model for sensitive work.

## Bottom line

Distillation is an old and useful idea: a small model learns faster from a teacher's full judgments than from right answers alone. Done from the outside, through millions of questions, it lets new models catch up with the frontier at a fraction of the cost, which is why it has become a source of accusations between labs and governments. It cannot be fully prevented, only made harder. And it has clear limits: distilled models copy style more easily than substance, cover what they were asked and little else, inherit their teachers' errors and stay one step behind. For users, the lesson is to test such models on their own tasks, especially rare and specialized ones, before trusting their benchmark scores.

**Questions to think about**

1. If a model's benchmark scores come partly from imitating a stronger model, how would you design a test that reveals the difference?
2. Where should the line be drawn between learning from public outputs, which all models do, and illicit distillation?
3. Would you use a model of uncertain provenance for research with sensitive data? What would you need to know first?

---

**한 줄 요약 (Korean summary).** 증류(distillation)는 작거나 새로운 모델(학생)이 더 강한 모델(교사)의 출력을 따라 하며 배우는 방법으로, 교사가 정답뿐 아니라 어떤 오답이 그럴듯한지까지 담은 확률 분포를 학생에게 전해 준다. 연구소 안에서 작고 빠른 모델을 만드는 데는 흔히 쓰이지만, 경쟁사가 수백만 개의 질문을 보내 답만 모아 학습하는 외부 증류는 최근 큰 분쟁이 되었다. Anthropic은 2026년 2월 중국의 세 연구소가 약 2만 4천 개의 가짜 계정으로 Claude와 1,600만 회 이상 대화했다고 밝혔고, 7월에는 미국 정부가 Kimi K3가 Claude Fable을 증류해 만들어졌다고 주장했지만 근거는 공개되지 않았다. 증류는 탐지, 계정 확인, 추론 과정 숨기기 등으로 어렵게 만들 수는 있어도 완전히 막을 수는 없다. 이렇게 만든 모델은 빠르게 따라잡을 수 있다는 장점이 있지만, 내용보다 말투를 더 쉽게 배우고, 질문받은 분야 밖의 드문 지식에 약하며, 교사의 오류를 물려받고, 늘 한발 뒤처진다는 한계가 있다.

---

**References**

AI Weekly (2026). Researchers doubt Kimi K3 was distilled from Anthropic's Fable. 24 July 2026 (after TechCrunch). [https://aiweekly.co/alerts/researchers-doubt-kimi-k3-was-distilled-from-anthropics-fable](https://aiweekly.co/alerts/researchers-doubt-kimi-k3-was-distilled-from-anthropics-fable)

Anthropic (2026). Detecting and preventing distillation attacks. 23 February 2026. [https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks](https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks)

Business Today (2026). US claims China's Moonshot AI used Anthropic's Fable 5 to build Kimi K3 AI model. 23 July 2026. [https://www.businesstoday.in/technology/artificial-intelligence/story/us-claims-chinas-moonshot-ai-used-anthropics-fable-5-to-build-kimi-k3-ai-model-544664-2026-07-23](https://www.businesstoday.in/technology/artificial-intelligence/story/us-claims-chinas-moonshot-ai-used-anthropics-fable-5-to-build-kimi-k3-ai-model-544664-2026-07-23)

DeepSeek-AI (2025). DeepSeek-R1: incentivizing reasoning capability in LLMs via reinforcement learning. _arXiv_, 2501.12948. [https://doi.org/10.48550/arXiv.2501.12948](https://doi.org/10.48550/arXiv.2501.12948)

Gudibande, A., Wallace, E., Snell, C., Geng, X., Liu, H., Abbeel, P., Levine, S., & Song, D. (2024). The false promise of imitating proprietary LLMs. _International Conference on Learning Representations (ICLR 2024)_. [https://doi.org/10.48550/arXiv.2305.15717](https://doi.org/10.48550/arXiv.2305.15717)

Hinton, G., Vinyals, O., & Dean, J. (2015). Distilling the knowledge in a neural network. _arXiv_, 1503.02531. [https://doi.org/10.48550/arXiv.1503.02531](https://doi.org/10.48550/arXiv.1503.02531)

OpenAI (2024). Learning to reason with LLMs. 12 September 2024. [https://openai.com/index/learning-to-reason-with-llms/](https://openai.com/index/learning-to-reason-with-llms/)

Savani, Y., Trockman, A., Feng, Z., Xu, Y. E., Schwarzschild, A., Robey, A., Finzi, M., & Kolter, J. Z. (2025). Antidistillation sampling. _arXiv_, 2504.13146. [https://doi.org/10.48550/arXiv.2504.13146](https://doi.org/10.48550/arXiv.2504.13146)

Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. (2024). AI models collapse when trained on recursively generated data. _Nature_, 631, 755–759. [https://doi.org/10.1038/s41586-024-07566-y](https://doi.org/10.1038/s41586-024-07566-y)

_Both figures are original. The Python scripts that produce them are available on GitHub: [Figure 1](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-27-distill-signal.py), [Figure 2](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-27-distill-campaigns.py)._
