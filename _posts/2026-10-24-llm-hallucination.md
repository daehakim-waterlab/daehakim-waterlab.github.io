---
layout: post
title: "Why LLMs make things up, and what you can do about it"
date: 2026-10-24 06:45:00 +0900
description: "A short guide to LLM hallucination (confabulation): what it is, why it happens, why reasoning-era models do it less, which models do it least as of October 2026, and practical habits that cut the errors you see."
tags: artificial-intelligence large-language-models hallucination research-practice
categories: notes
related_posts: false
---

Anyone who uses large language models (LLMs) for research has met the problem: a confident answer, a plausible citation, and then the discovery that the paper does not exist. This is usually called hallucination. Here is what we know about why it happens, how much it has improved, and what users can do about it.

## Hallucination, or confabulation

"Hallucination" is the popular term, but many researchers prefer **confabulation**, a word borrowed from neurology. A patient who confabulates fills gaps in memory with invented details and believes them, with no intent to deceive. That is close to what an LLM does: it produces fluent, specific and wrong content, with the same confidence as when it is right.

Farquhar et al. (2024) use confabulation for a narrower case: answers that are both wrong and arbitrary, so that asking the same question again gives a different answer. That distinction turns out to be useful, as we will see below.

## Why it happens

A 2025 analysis by Kalai and colleagues at OpenAI gives the clearest explanation so far (Kalai et al. 2025). It has two parts.

**Pretraining makes some errors unavoidable.** A model learns by predicting text. For facts that appear many times in the training data, such as the boiling point of water, it learns the pattern. For facts that appear only once or rarely, such as a particular researcher's birthday or the page numbers of a 2003 paper, there is no pattern to learn. The authors show that the error rate on such facts is tied to how many of them appear only once in training data. Bibliographic details, numbers, names and niche facts are exactly this kind of knowledge.

**Training and evaluation reward guessing.** Most benchmarks score an answer as right or wrong. "I don't know" scores zero, the same as a wrong answer, so a model that always guesses scores higher than one that admits uncertainty. The authors compare it to a multiple-choice exam with no penalty for wrong answers: the rational strategy is to never leave a blank. Models were, in effect, trained to be good test-takers.

## Why reasoning models do it less

Hallucination has dropped markedly over the past year, but not simply because models now "think" before answering. When OpenAI released its first strong reasoning model, o3, in 2025, it hallucinated more than its predecessor on an internal test of facts about people: 33% versus 16% for o1, because it made more claims overall (OpenAI 2025a). Reasoning gives a model more chances to be right and more chances to be wrong.

What changed is better explained by three things.

1. **Rewarding abstention.** After the diagnosis above, labs began training models to decline when unsure. OpenAI reported that in its GPT-5 thinking model, the share of factual claims containing errors was 65% lower than in o3 (OpenAI 2025b).
2. **Using reasoning to check.** Thinking time helps when a model uses it to test its own answer, not only to build a longer argument.
3. **Tools.** Models that can search the web or read a supplied document answer from evidence instead of memory. Much of the improvement in everyday use comes from this.

The result shows clearly on AA-Omniscience, a benchmark by Artificial Analysis that asks hard factual questions without web access and, unusually, does not penalize "I don't know" (Figure 1).

![Correct, wrong and declined answers on AA-Omniscience for current and earlier LLMs](/assets/img/blog/2026-10-24-hallucination-answers.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 1.** Out of 100 hard factual questions answered without web search, how many each model got right, got wrong, or declined (or answered only partly), for current models and two models released in November 2025. Wrong answers are computed as accuracy minus the AA-Omniscience Index. Gemini 4 Argon was not yet public when these results were recorded. Figure by Daeha Kim, drawn from AA-Omniscience results (Artificial Analysis) as compiled on 4 October 2026._

## Which model hallucinates least?

As of October 2026, the answer depends on what you want.

- **Fewest wrong answers among frontier models:** Gemini 4 Argon. It gets about half the questions right, declines most of the rest, and gives a wrong answer to only 8 in 100.
- **Best balance of knowing and admitting:** Claude Opus 5.5 leads the AA-Omniscience Index (correct minus wrong), with GPT-6 Astra close behind. These models know more, so they answer more questions correctly, but they still guess on about 20 in 100.
- **Large differences remain:** some capable models still answer almost every question and get about half of them wrong.

A year earlier, the leading models gave wrong answers to 33–40 questions in 100. The improvement is real. Two caveats apply. Rankings change every few months, and they differ between tasks: on summarizing a supplied document faithfully, a different leaderboard (Vectara's) ranks models in another order. And no model is at zero.

## What you can do

Even with the best model, the habits of the user matter more than the choice of model. These are the ones I find most effective, most of them also recommended by the model developers themselves (Anthropic 2026).

1. **Give it the source.** Paste the paper, report or data, and ask it to answer only from that material. Asking for exact quotes first, and building the answer on them, works especially well for long documents.
2. **Give permission not to know.** Say explicitly: "If you are not sure, say so." This simple sentence counters the guessing habit described above.
3. **Turn on search for facts, and open the links.** A cited source is only useful if it exists and says what the model claims. Check DOIs and page numbers yourself; this is where fabrication is most common.
4. **Ask twice.** Ask the same factual question in a new conversation, or rephrase it. If the answers disagree, treat both as unverified. This is the practical version of Farquhar's method, which detects confabulations from inconsistency across repeated answers.
5. **Ask for a separate check.** After a draft, ask the model to list each factual claim and verify it, ideally in a fresh session. Splitting generation and verification reduces errors (Dhuliawala et al. 2023).
6. **Don't lead the witness.** "Isn't it true that…?" invites agreement. Ask neutral questions, and be suspicious when the model simply confirms what you hoped.
7. **Know the danger zones.** References, numbers, names, dates, recent events and very specialized facts are where models fail most. Reasoning, coding and explaining well-documented concepts are much safer.

## Bottom line

Hallucination is not a mysterious bug. It follows from how models learn rare facts and from training that rewarded guessing. The newest models hallucinate much less, mainly because they have learned to say "I don't know" and to check with tools, not just because they reason longer. The best defense is still on the user's side: give the model the evidence, allow it to be uncertain, and verify anything that matters, especially citations and numbers.

**Questions to think about**

1. Would you prefer a model that answers 66 of 100 questions correctly and 20 wrongly, or one that answers 50 correctly and 8 wrongly? Does your answer depend on the task?
2. Kalai and colleagues argue that benchmarks should penalize wrong answers more than abstentions. How would that change how we grade students?
3. Which of the seven habits above could you build into your group's standard workflow for literature reviews?

---

**한 줄 요약 (Korean summary).** LLM이 그럴듯하지만 틀린 내용을 자신 있게 만들어내는 현상을 흔히 환각(hallucination)이라고 부르지만, 기억의 빈틈을 지어낸 내용으로 메우는 신경학 용어를 빌려 작화(confabulation)라고도 한다. Kalai 등(2025)에 따르면 원인은 두 가지다. 학습 데이터에 드물게 등장하는 사실(서지 정보, 수치, 인명 등)은 패턴으로 학습할 수 없고, 대부분의 평가가 "모른다"를 오답과 똑같이 0점 처리해 추측을 보상해 왔다. 추론 모델이라고 저절로 나아진 것은 아니어서, 2025년 o3는 이전 모델보다 오히려 더 많이 틀렸다. 최근의 큰 개선은 모를 때 답을 거절하도록 한 학습, 추론을 자기 검증에 쓰는 것, 검색 같은 도구 사용 덕분이다. 2026년 10월 기준 웹 검색 없이 어려운 사실 질문 100개를 풀게 하면, 틀린 답이 가장 적은 최상위 모델은 Gemini 4 Argon(약 8개)이고, 정답과 오답의 차이가 가장 큰 모델은 Claude Opus 5.5와 GPT-6 Astra(정답 63–66개, 오답 약 20개)이다. 1년 전 주요 모델은 오답이 33–40개였다. 사용자가 할 수 있는 일로는 원문 자료를 주고 그 안에서만 답하게 하기, "모르면 모른다고 하라"고 명시하기, 검색을 켜고 인용 링크와 DOI를 직접 확인하기, 같은 질문을 새 대화에서 다시 해 보기, 별도의 검증 단계를 두기, 유도 질문 피하기, 그리고 참고문헌·수치·인명·최신 정보처럼 오류가 잦은 영역을 특히 조심하기가 있다.

---

**References**

Anthropic (2026). Reduce hallucinations. _Claude Platform Documentation_. [https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)

Artificial Analysis (2026). AA-Omniscience: knowledge and hallucination benchmark. [https://artificialanalysis.ai/evaluations/omniscience](https://artificialanalysis.ai/evaluations/omniscience)

Dhuliawala, S., Komeili, M., Xu, J., Raileanu, R., Li, X., Celikyilmaz, A., & Weston, J. (2023). Chain-of-verification reduces hallucination in large language models. _arXiv_, 2309.11495. [https://doi.org/10.48550/arXiv.2309.11495](https://doi.org/10.48550/arXiv.2309.11495)

Farquhar, S., Kossen, J., Kuhn, L., & Gal, Y. (2024). Detecting hallucinations in large language models using semantic entropy. _Nature_, 630, 625–630. [https://doi.org/10.1038/s41586-024-07421-0](https://doi.org/10.1038/s41586-024-07421-0)

Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. (2025). Why language models hallucinate. _arXiv_, 2509.04664. [https://doi.org/10.48550/arXiv.2509.04664](https://doi.org/10.48550/arXiv.2509.04664)

OpenAI (2025a). OpenAI o3 and o4-mini system card. [https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf)

OpenAI (2025b). GPT-5 system card. _arXiv_, 2601.03267. [https://doi.org/10.48550/arXiv.2601.03267](https://doi.org/10.48550/arXiv.2601.03267)

_The figure is original. The Python script that produces it is available on [GitHub](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-24-hallucination-answers.py)._
