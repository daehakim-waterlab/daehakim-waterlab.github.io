---
layout: post
title: "Writing and coding with LLMs: what we gain, what we lose, and how to catch the errors"
date: 2026-10-21 00:10:00 +0900
description: "What the evidence says about using large language models to write and to code: where they help, where human-only work is still better, why our own sense of how well it went is unreliable, and practical ways to detect the errors."
tags: llm writing coding research-integrity education
categories: notes
related_posts: false
---

Large language models (LLMs) are now part of how many researchers write papers and code analyses. One large study estimates that by late 2024 up to 22% of the text in computer science papers showed signs of LLM modification (Liang et al. 2025), and more than 40% of the code submitted in one introductory programming course in 2024 was flagged as LLM-generated, up from almost none in 2022 (Baek et al. 2026). The question for a research group is no longer whether to use these tools, but how to use them without losing what makes the work ours, and how to catch the mistakes they make. In [an earlier post]({% post_url 2026-10-18-from-chatbot-to-coworker %}) I looked at what LLM agents can already do in hydrologic modeling; this one is about the person using them.

This post collects what I consider the most useful evidence, from controlled experiments rather than opinion pieces. It is longer than usual, because the topic deserves care. I have tried to report every number as the original authors did, and to say when a study is small, preliminary or not yet peer-reviewed. One caveat applies throughout: most of these experiments used models from 2023 and 2024, and the tools have improved much faster than the evidence about them. I come back to this near the end.

## What LLMs do well

The gains are real, and they are largest for well-defined tasks.

- **Speed and polish on routine writing.** In a preregistered experiment with 453 professionals, access to ChatGPT cut the time needed for occupation-specific writing tasks by 40% and raised the rated quality by 18% (Noy & Zhang 2023). The least skilled writers gained the most, so the gap between workers narrowed.
- **Speed on self-contained coding tasks.** In a controlled experiment with 95 developers, those using GitHub Copilot finished a small web-server task 55.8% faster (Peng et al. 2023). This was a short, clearly specified task, and the study was run by researchers at GitHub and Microsoft.
- **Better results inside the "frontier."** In an experiment with 758 consultants at Boston Consulting Group, GPT-4 users completed 12.2% more tasks, 25.1% faster and with more than 40% higher quality on tasks that the model handles well. Below-average performers improved most (Dell'Acqua et al. 2023).
- **More ideas.** Writers who received ideas from an LLM produced short stories rated more novel and more useful, especially writers who were less creative to begin with (Doshi & Hauser 2024).
- **Useful critique.** When GPT-4 commented on thousands of published papers, the overlap between its points and those of human reviewers was similar to the overlap between two human reviewers (Liang et al. 2024).
- **Structure.** Asking a model to plan before it writes (outline, characters, key events, then revision of the plan) produces stories that human raters preferred in 68.5% of comparisons, although that evaluation had only 35 responses (Lewenberg et al. 2025).

## What is lost compared with writing it ourselves

The costs are less visible, and that is what makes them dangerous.

**The meaning shifts, not only the style.** The most striking recent study is a preprint by Abdulhai and colleagues (2026). In a randomized study, 100 people wrote an essay on "Does money lead to happiness?", some with an LLM available. People who let the model write most of the text were far more likely to end up with no clear position at all: 67% of their essays were neutral, compared with 40% of essays written without an LLM. People who used the model only for advice or as a search tool wrote essays that looked like the human-only ones.

![Stance of essays written with and without an LLM](/assets/img/blog/2026-10-21-llm-stance.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 1.** Stance of essays on "Does money lead to happiness?" in a randomized study with 100 participants, by how much the writer relied on an LLM. Heavy reliance pushed essays toward neutrality; using the model only for advice or search did not. Figure by Daeha Kim, drawn from numbers reported in Abdulhai et al. (2026)._

The same authors then asked three current LLMs to revise 86 student essays written in 2021, before ChatGPT existed, giving the models the same expert feedback the students had received. Even when told to fix only grammar, the models changed the content: they replaced far more words than the students did when revising their own drafts, cut pronouns by 40–60%, removed personal examples, made the tone more emotional and pushed every essay in the same semantic direction. In one example, a student's cautious "perhaps America is not ready for self-driving cars" became a firmer statement. The heavy LLM users in the user study also said their essays were less creative and less in their own voice, yet they were just as satisfied with the result. In science the same effect is already visible: in peer reviews for a major machine learning conference, reviews generated by LLMs gave scores about 10% higher and judged papers by different criteria, mentioning clarity and relevance less and reproducibility and scalability more.

**Everyone starts to sound the same.** Stories written with LLM ideas were individually better but more similar to one another (Doshi & Hauser 2024). An explainable detector of machine text found that human news articles cover a wider variety of themes and vocabulary, while newer models produce text concentrated in a narrow part of the space that human writing occupies (Liebe et al. 2026). Even teams of LLM agents become more alike when they read each other's drafts. Interestingly, one remedy works for machines as it does for people: in "blind peer review," each agent receives feedback but revises its own draft without seeing the others', which preserves diversity (Li et al. 2026). The parallel with brainstorming research, where people who work alone first produce more original ideas than groups, is hard to miss.

**Learning suffers when the model does the thinking.** In a field experiment with nearly 1,000 high school students, unrestricted access to a GPT-4 tutor raised practice scores by 48%, but on the later exam without AI those students scored 17% worse than students who never had it. A version designed to give hints rather than answers avoided the harm (Bastani et al. 2025). In a survey of 319 knowledge workers, higher confidence in AI went with less critical thinking, and the work shifted from producing to checking (Lee et al. 2025). A small EEG study reported that most essay writers who used ChatGPT could not quote a sentence from the essay they had just written (Kosmyna et al. 2025); it is a preprint with 54 participants and its methods have been criticized, so I treat it as a warning sign rather than a result.

**Outside the frontier, AI makes us worse.** In the consultant experiment, on a task that looked similar but lay outside what GPT-4 could do well, AI users were 19 percentage points less likely to reach the correct answer than those working alone (Dell'Acqua et al. 2023). The difficulty is that the boundary is invisible: the model sounds equally confident on both sides of it.

## Our sense of how well it went is unreliable

This, to me, is the most important finding in the whole literature. In a randomized trial with 16 experienced open-source developers working on their own large projects, allowing AI tools made them 19% _slower_. Before the study they expected to be 24% faster, and afterwards they still believed they had been 20% faster (Becker et al. 2025). Outside experts predicted even larger gains.

![Expected versus measured effect of AI tools on developer speed](/assets/img/blog/2026-10-21-perception-gap.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 2.** Predicted and measured change in the time experienced developers needed to complete tasks in their own projects when AI tools were allowed. Negative values mean faster. Figure by Daeha Kim, drawn from numbers reported in Becker et al. (2025)._

The direction is not always the same. A 2026 follow-up by the same group, with 57 developers and late-2025 tools, pointed toward a speedup rather than a slowdown, but its confidence intervals include zero and the authors themselves call the data unreliable (Becker et al. 2026). The main reason is telling: many developers declined to take part, or held back some of their tasks, because they did not want to work without AI, and the authors think this hides a larger speedup than they could measure. And in the Copilot experiment, users underestimated their gain. The lesson is not that AI always slows us down; it is that our feelings about it are not measurements. The same gap appears in security: people with an AI assistant wrote less secure code and were more likely to believe it was secure (Perry et al. 2023), and the heavy LLM users in the essay study were satisfied with essays that no longer said what they thought.

## How often LLM output is wrong

Error rates depend on the task and the model, and they fall as models improve. But in every study I found, they are well above zero.

![Error rates measured in LLM output in published studies](/assets/img/blog/2026-10-21-llm-error-rates.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 3.** Error rates of LLM output reported in published studies. Each bar comes from a different study, model, task and year (2021–2024), so the bars should not be compared with one another; newer models generally do better. The point is that none is negligible. Figure by Daeha Kim, drawn from numbers reported in Walters & Wilder (2023), Kabir et al. (2024), Bastani et al. (2025), Pearce et al. (2022) and Spracklen et al. (2025)._

Some of these errors are easy to miss. More than half of ChatGPT's answers to Stack Overflow questions contained incorrect information, yet in a small user study people overlooked the misinformation 39% of the time (Kabir et al. 2024). Code models invent package names that do not exist: among 576,000 code samples, at least 5.2% from commercial models and 21.7% from open-source models referred to a non-existent package (Spracklen et al. 2025). Attackers can register those names and wait for someone to install them. In writing, the classic failure is the invented citation: in 2023, 55% of the references produced by GPT-3.5 and 18% of those produced by GPT-4 did not exist, and 24% of GPT-4's real references contained substantive errors (Walters & Wilder 2023). Industry surveys point the same way at a larger scale: the DORA 2024 survey of about 39,000 software professionals found that higher AI adoption was associated with slightly better code quality and documentation, but lower delivery stability (Google Cloud DORA 2024).

One gap in the evidence should be stated plainly. I found no rigorous trial comparing the factual error rate or peer-review outcome of scientific manuscripts written with and without LLM help. We are all, in effect, running that experiment on ourselves.

## The evidence is older than the tools

Almost every experiment above used GPT-3.5, GPT-4 or early versions of Copilot, and most were run in 2023 or 2024. The models have moved much faster than the experimental literature, so the specific numbers in this post probably understate what current models can do. The drop in invented references from GPT-3.5 to GPT-4 in a single year (55% to 18%) is a small example of how quickly such figures go out of date.

Two benchmarks give a sense of the pace. METR measures the length of task, in hours of skilled human work, that a model can complete on its own half of the time. This "time horizon" doubled about every seven months from 2019 to early 2025 (Kwa et al. 2025), and METR's revised estimate puts the doubling time since 2023 at about four months (METR 2026). On GDPval, in which experienced professionals blindly compare model and expert deliverables for tasks that take an expert about seven hours, the best model in the original paper matched or beat the expert in 47.6% of comparisons (Patwardhan et al. 2025); a model released a few months later was reported at 70.9% (OpenAI 2025). The failed follow-up in the previous section points the same way: when experienced developers refuse to work without a tool, the tool is probably doing something for them.

These numbers deserve the same scrutiny as any other. The METR tasks are self-contained software tasks, and METR itself notes that few of its tasks remain beyond the latest models and that the trend is somewhat sensitive to which tasks are included. GDPval was built by a model developer, and the 70.9% figure comes from that developer's product announcement rather than a peer-reviewed paper. And on GDPval tasks whose deliverable was plain text, closest to the writing this post is about, models did worst: the experts rated the model's deliverable better than their own in only 14% of comparisons for Claude Opus 4.1 and 23% for GPT-5 (Patwardhan et al. 2025).

More importantly, benchmarks measure the model working alone. They do not test what the earlier sections are about: whether our arguments keep their strength, whether our writing stays our own, whether students still learn, and whether we notice when the model has crossed its frontier. A more capable model may even make some of these problems worse, because it is more tempting to hand it the thinking, and its errors become rarer and therefore harder to spot.

I use these tools every day, and my own impression is that they have become far more useful in the past year than the studies above suggest. I think that impression is probably right. But it is also exactly the kind of evidence Figure 2 warns against, so the practical advice that follows does not change: measure, test and check.

## Detecting the errors

None of the following is new to anyone trained in science. LLMs simply make it more necessary.

**For code**

- **Write the test before you ask for the code.** Decide what the correct output is, ideally with a case you can solve by hand, and run it. In hydrology that means checking that a water balance closes, that a model reproduces an analytical solution, or that it gives the published result for a benchmark catchment.
- **Run everything, and read every line you keep.** If you cannot explain a line, you do not yet own it.
- **Check that every imported package actually exists** and is the one you intended, before installing it.
- **Work in small steps.** Ask for one function at a time and inspect the change, rather than accepting a whole script.
- **Pay extra attention to security, file handling and anything that deletes or overwrites data**, where the studies above found the most problems.

**For writing**

- **Open every reference.** Look up each DOI and confirm that the paper exists and says what the sentence claims. Never cite a paper you have not opened.
- **Trace every number** back to its source table or figure.
- **Compare meaning, not only grammar.** After an LLM edits a paragraph, compare it with your original sentence by sentence and ask whether each claim is still the one you intended, at the strength you intended.
- **Ask for critique, not a rewrite.** "What is unclear or unsupported here?" keeps your text and your argument intact. "Improve this" invites the model to replace them.

**Signals in the model's own words.** In a study of 30,300 classroom utterances labeled by several LLMs, wrong labels came with explanations that were five times more likely to hedge ("might," "could") and twice as likely to narrate the model's own thinking ("I think," "I realize"), and they were usually longer. Correct ones linked evidence to conclusions with words like "because" and "therefore" (Ahtisham et al. 2026). That study is about classifying text, not about code, but the rule of thumb transfers: a long, hedging, self-narrating explanation is a reason to check more carefully.

**Ask more than once.** If you ask the same factual question several times and get different answers, the model is probably guessing. This idea underlies "semantic entropy," which detects many confabulations from the disagreement among repeated answers (Farquhar et al. 2024). A related technique, chain-of-verification, has the model draft an answer, write its own fact-checking questions, answer them independently and then revise; in benchmark tests it cut the number of hallucinated items in list-style answers by more than three quarters (Dhuliawala et al. 2024). Both catch inconsistency, not errors the model makes consistently, so they complement rather than replace checking against sources.

**Detecting AI-written text is a different problem, and a risky one.** Detectors of machine-written text are improving, but they wrongly flag human writing. One recent detector labeled 25% of randomly collected human news articles as machine-written (Liebe et al. 2026). A detector of LLM-generated code that was more than 99% accurate still flagged one of five reference solutions written by the course instructor (Baek et al. 2026). People are not reliable judges either: most cannot tell AI-written from human-written self-descriptions (Jakesch et al. 2023), although people who use LLMs often for writing are much better at it (Russell et al. 2025). Baek and colleagues draw a sensible conclusion for teaching: when code looks generated, ask the student a few conceptual questions about it rather than imposing a penalty.

## A working attitude

Putting the evidence together, this is the approach I suggest to students in my group.

- **Think first, then prompt.** Decide what you want to say, or what the code must do, before you open the chat window. The essay study shows that using an LLM for advice preserves your voice and your conclusions; letting it draft does not.
- **Use the model as a critic, a tutor or a student, not as a ghostwriter.** In a small preliminary study, students who taught rhetorical strategies to an LLM playing a novice student used more of those strategies in their own essays and made fewer errors on a delayed test than after a video lecture (Miller & Bosch, in press). Explaining to the model is good for you; letting the model explain to the reader is not.
- **Stay inside the frontier, or verify harder outside it.** LLMs are most reliable on common tasks with checkable answers. The further you are from that, the more you must check. The frontier moves outward with every model generation, so test it again for your own tasks rather than relying on what was true last year.
- **Match the checking to the stakes.** A plotting script and a figure for a paper do not need the same scrutiny as a flood frequency analysis that will inform a design.
- **Keep some work unaided.** Skills that are never exercised fade. Write some first drafts, derivations and functions yourself, especially while you are still learning them.
- **Keep the responsibility.** The model is not an author. Whatever goes out under your name, you must be able to explain and defend line by line, and you should disclose how you used AI.

## Bottom line

- LLMs make routine writing and coding faster and often better, especially for less experienced people, on tasks within their competence.
- They also change what we say, make our writing more alike, can weaken learning, and make us worse on tasks just beyond their competence.
- Our own impression of how much they helped is unreliable; only measurement and checking tell us.
- Error rates in LLM output are well above zero. Tests for code and source checks for writing are not optional.
- The tools are improving faster than the evidence. Current models are probably more capable than the studies here suggest, but benchmarks measure the model, not what happens to us when we use it.
- Use LLMs to think better, not to think less.

**Questions to think about**

1. Pick a recent piece of your own writing that an LLM edited. Compare the two versions sentence by sentence. Did any claim change in strength or meaning?
2. For the hydrological model you use most, what simple test (a water balance, an analytical case, a benchmark catchment) would tell you that AI-generated code is wrong?
3. The developers in Figure 2 felt faster but were slower. How could you measure, honestly, whether an AI tool is helping your own research?
4. Benchmarks say the models have improved dramatically since these studies. What evidence would convince you that your own use of them has improved as well?

---

**한 줄 요약 (Korean summary).** LLM은 정해진 글쓰기와 코딩 작업을 빠르고 매끄럽게 해 주며, 특히 경험이 적은 사람에게 도움이 크다(전문직 글쓰기 시간 40% 단축·품질 18% 향상, 간단한 코딩 과제 55.8% 단축). 그러나 사람이 직접 쓴 글과 비교하면 잃는 것도 분명하다. 무작위 실험에서 LLM이 글 대부분을 쓰게 한 사람들의 에세이는 67%가 입장 없는 중립으로 끝났고(직접 쓴 경우 40%), 문법만 고치라고 해도 LLM은 단어와 주장, 어조를 바꾸었다. LLM과 함께 쓴 글은 서로 비슷해지고, 답을 그대로 주는 AI를 쓴 학생들은 AI 없이 치른 시험에서 17% 낮은 점수를 받았으며, 모델이 잘하지 못하는 과제에서는 오히려 정답률이 19%p 떨어졌다. 더 중요한 것은 체감과 실제가 다르다는 점이다. 숙련 개발자들은 AI 덕분에 20% 빨라졌다고 믿었지만 실제로는 19% 느려졌다. 연구마다 차이는 있지만 LLM 출력의 오류율(가짜 인용, 틀린 답, 보안 취약점, 존재하지 않는 패키지)은 결코 0이 아니다. 다만 이 실험들은 대부분 2023–2024년 모델을 썼고, 모델의 능력은 그보다 훨씬 빠르게 늘고 있다. 모델이 혼자 끝낼 수 있는 과제의 길이는 최근 약 4개월마다 두 배가 되었고, 전문가 수준 업무 평가(GDPval)에서 최신 모델은 전문가와 같거나 나은 결과를 70% 이상 냈다는 보고도 있다. 그래서 지금의 LLM은 이 글의 수치보다 유능할 가능성이 크다. 그러나 벤치마크는 모델 혼자의 능력을 잴 뿐, 우리가 쓸 때 주장과 목소리, 배움이 지켜지는지는 재지 않으며, 순수 텍스트 과제에서는 여전히 성적이 가장 낮았다. 따라서 코드는 먼저 검증 기준(물수지, 해석해, 벤치마크)을 정하고 테스트하며, 글은 모든 인용과 수치를 원문에서 확인하고 수정 전후의 의미를 비교해야 한다. 같은 질문을 여러 번 해 답이 달라지거나 설명이 길고 얼버무리는 표현이 많으면 더 의심해야 한다. LLM은 대필자가 아니라 비평가·튜터·학생으로 쓰고, 먼저 스스로 생각한 뒤에 사용하며, 결과에 대한 책임은 끝까지 자신이 져야 한다.

---

**References**

Abdulhai, M., White, I., Wan, Y., Qureshi, I., Leibo, J. Z., Kleiman-Weiner, M., & Jaques, N. (2026). How LLMs distort our written language. arXiv:2603.18161. [https://doi.org/10.48550/arXiv.2603.18161](https://doi.org/10.48550/arXiv.2603.18161)

Ahtisham, B., Vanacore, K., Zhou, Z., Lee, J., & Kizilcec, R. F. (2026). LLM reasoning predicts when models are right: Evidence from coding classroom discourse. arXiv:2602.09832. [https://doi.org/10.48550/arXiv.2602.09832](https://doi.org/10.48550/arXiv.2602.09832)

Baek, J., Yamazaki, T., Morihata, A., Mori, J., Yamakata, Y., Taura, K., & Chiba, S. (2026). LLM-based explainable detection of LLM-generated code in Python programming courses. In _Proceedings of the 57th ACM Technical Symposium on Computer Science Education V.1_, 80–86. [https://doi.org/10.1145/3770762.3772605](https://doi.org/10.1145/3770762.3772605)

Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. _Proceedings of the National Academy of Sciences_, 122(26), e2422633122. [https://doi.org/10.1073/pnas.2422633122](https://doi.org/10.1073/pnas.2422633122)

Becker, J., Rush, N., Barnes, E., & Rein, D. (2025). Measuring the impact of early-2025 AI on experienced open-source developer productivity. arXiv:2507.09089. [https://doi.org/10.48550/arXiv.2507.09089](https://doi.org/10.48550/arXiv.2507.09089)

Becker, J., Rush, N., Cunningham, T., Rein, D., & Mahamud, K. (2026). We are changing our developer productivity experiment design. METR blog, 24 February 2026. Not peer-reviewed. [https://metr.org/blog/2026-02-24-uplift-update/](https://metr.org/blog/2026-02-24-uplift-update/)

Dell'Acqua, F., McFowland III, E., Mollick, E. R., et al. (2023). Navigating the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge worker productivity and quality. Harvard Business School Working Paper 24-013. [https://doi.org/10.2139/ssrn.4573321](https://doi.org/10.2139/ssrn.4573321)

Dhuliawala, S., Komeili, M., Xu, J., Raileanu, R., Li, X., Celikyilmaz, A., & Weston, J. (2024). Chain-of-verification reduces hallucination in large language models. In _Findings of the Association for Computational Linguistics: ACL 2024_, 3563–3578. [https://doi.org/10.18653/v1/2024.findings-acl.212](https://doi.org/10.18653/v1/2024.findings-acl.212)

Doshi, A. R., & Hauser, O. P. (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. _Science Advances_, 10(28), eadn5290. [https://doi.org/10.1126/sciadv.adn5290](https://doi.org/10.1126/sciadv.adn5290)

Farquhar, S., Kossen, J., Kuhn, L., & Gal, Y. (2024). Detecting hallucinations in large language models using semantic entropy. _Nature_, 630, 625–630. [https://doi.org/10.1038/s41586-024-07421-0](https://doi.org/10.1038/s41586-024-07421-0)

Google Cloud DORA (2024). _Accelerate State of DevOps Report 2024_. Industry survey report. [https://dora.dev/research/2024/dora-report/](https://dora.dev/research/2024/dora-report/)

Jakesch, M., Hancock, J. T., & Naaman, M. (2023). Human heuristics for AI-generated language are flawed. _Proceedings of the National Academy of Sciences_, 120(11), e2208839120. [https://doi.org/10.1073/pnas.2208839120](https://doi.org/10.1073/pnas.2208839120)

Kabir, S., Udo-Imeh, D. N., Kou, B., & Zhang, T. (2024). Is Stack Overflow obsolete? An empirical study of the characteristics of ChatGPT answers to Stack Overflow questions. In _Proceedings of the CHI Conference on Human Factors in Computing Systems_, 1–17. [https://doi.org/10.1145/3613904.3642596](https://doi.org/10.1145/3613904.3642596)

Kosmyna, N., Hauptmann, E., Yuan, Y. T., et al. (2025). Your brain on ChatGPT: Accumulation of cognitive debt when using an AI assistant for essay writing task. arXiv:2506.08872. [https://doi.org/10.48550/arXiv.2506.08872](https://doi.org/10.48550/arXiv.2506.08872)

Kwa, T., West, B., Becker, J., Deng, A., Garcia, K., Hasin, M., Jawhar, S., Kinniment, M., Rush, N., Von Arx, S., et al. (2025). Measuring AI ability to complete long software tasks. arXiv:2503.14499. [https://doi.org/10.48550/arXiv.2503.14499](https://doi.org/10.48550/arXiv.2503.14499)

Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The impact of generative AI on critical thinking: Self-reported reductions in cognitive effort and confidence effects from a survey of knowledge workers. In _Proceedings of the CHI Conference on Human Factors in Computing Systems_, 1–22. [https://doi.org/10.1145/3706598.3713778](https://doi.org/10.1145/3706598.3713778)

Lewenberg, Y., Sheftel, H., & Karov, Y. (2025). Plan before you write: Improve LLM writing by planning. _Advances in Neural Information Processing Systems 38 (NeurIPS 2025), Creative AI Track_.

Li, W., Song, M., Shen, Z., Zhao, D., Long, Y., Li, Y., Li, Y., Yang, R., & Wang, M. (2026). LLM Review: Enhancing creative writing via blind peer review feedback. arXiv:2601.08003. [https://doi.org/10.48550/arXiv.2601.08003](https://doi.org/10.48550/arXiv.2601.08003)

Liang, W., Zhang, Y., Cao, H., et al. (2024). Can large language models provide useful feedback on research papers? A large-scale empirical analysis. _NEJM AI_, 1(8). [https://doi.org/10.1056/AIoa2400196](https://doi.org/10.1056/AIoa2400196)

Liang, W., Zhang, Y., Wu, Z., et al. (2025). Quantifying large language model usage in scientific papers. _Nature Human Behaviour_, 9, 2599–2609. [https://doi.org/10.1038/s41562-025-02273-8](https://doi.org/10.1038/s41562-025-02273-8)

Liebe, L., Baum, J., Barz-Cech, T., Scheibel, W., & Döllner, J. (2026). Detecting and comparing LLM capabilities to human writers through linguistic analysis. _SN Computer Science_, 7, 621. [https://doi.org/10.1007/s42979-026-05131-0](https://doi.org/10.1007/s42979-026-05131-0)

METR (2026). Time Horizon 1.1. METR blog, 29 January 2026. Not peer-reviewed. [https://metr.org/blog/2026-1-29-time-horizon-1-1/](https://metr.org/blog/2026-1-29-time-horizon-1-1/)

Miller, S., & Bosch, N. (in press). Learning by teaching an LLM: A new approach to writing instruction.

Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. _Science_, 381(6654), 187–192. [https://doi.org/10.1126/science.adh2586](https://doi.org/10.1126/science.adh2586)

OpenAI (2025). Introducing GPT-5.2. Product announcement, December 2025. Not peer-reviewed. [https://openai.com/index/introducing-gpt-5-2/](https://openai.com/index/introducing-gpt-5-2/)

Patwardhan, T., Dias, R., Proehl, E., Kim, G., Wang, M., Watkins, O., Posada Fishman, S., Aljubeh, M., Thacker, P., Fauconnet, L., Kim, N. S., Chao, P., Miserendino, S., Chabot, G., Li, D., Sharman, M., Barr, A., Glaese, A., & Tworek, J. (2025). GDPval: Evaluating AI model performance on real-world economically valuable tasks. arXiv:2510.04374. [https://doi.org/10.48550/arXiv.2510.04374](https://doi.org/10.48550/arXiv.2510.04374)

Pearce, H., Ahmad, B., Tan, B., Dolan-Gavitt, B., & Karri, R. (2022). Asleep at the keyboard? Assessing the security of GitHub Copilot's code contributions. In _2022 IEEE Symposium on Security and Privacy_, 754–768. [https://doi.org/10.1109/SP46214.2022.9833571](https://doi.org/10.1109/SP46214.2022.9833571)

Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). The impact of AI on developer productivity: Evidence from GitHub Copilot. arXiv:2302.06590. [https://doi.org/10.48550/arXiv.2302.06590](https://doi.org/10.48550/arXiv.2302.06590)

Perry, N., Srivastava, M., Kumar, D., & Boneh, D. (2023). Do users write more insecure code with AI assistants? In _Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security_, 2785–2799. [https://doi.org/10.1145/3576915.3623157](https://doi.org/10.1145/3576915.3623157)

Russell, J., Karpinska, M., & Iyyer, M. (2025). People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text. In _Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics_. arXiv:2501.15654. [https://doi.org/10.48550/arXiv.2501.15654](https://doi.org/10.48550/arXiv.2501.15654)

Spracklen, J., Wijewickrama, R., Sakib, A. H. M. N., Maiti, A., Viswanath, B., & Jadliwala, M. (2025). We have a package for you! A comprehensive analysis of package hallucinations by code generating LLMs. In _34th USENIX Security Symposium_, 3687–3706. arXiv:2406.10279. [https://doi.org/10.48550/arXiv.2406.10279](https://doi.org/10.48550/arXiv.2406.10279)

Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. _Scientific Reports_, 13, 14045. [https://doi.org/10.1038/s41598-023-41032-5](https://doi.org/10.1038/s41598-023-41032-5)

_All three figures are original. The Python scripts that produce them are available on GitHub: [Figure 1](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-21-llm-stance.py), [Figure 2](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-21-perception-gap.py) and [Figure 3](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-21-llm-error-rates.py)._
