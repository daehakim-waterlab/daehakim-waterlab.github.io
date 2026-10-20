---
layout: post
title: "Vibe coding, vibe writing, vibe working: what decides whether it works"
date: 2026-10-21 08:30:00 +0900
description: "Where the term vibe coding came from, how its accuracy is measured, the factors that decide whether AI-generated code is right, and how far the same approach goes for writing and for office work."
tags: llm coding writing research-integrity education
categories: notes
related_posts: false
---

In [the previous post]({% post_url 2026-10-21-llm-writing-coding %}) I looked at what we gain and lose when LLMs help us write and code. This one asks a narrower question that students in my group keep raising: when you hand a whole task to an AI and mostly look at the result, what decides whether the result is right? The practice has a name, vibe coding, and two newer cousins, vibe writing and vibe working. I wanted to know what the evidence says about each, and in particular how anyone measures their accuracy in a way that deserves to be called scientific.

As before, I have tried to report every number as the original authors did and to say when a source is a preprint, a company announcement or an industry report. Several of the most useful sources here are not peer-reviewed, because the field moves faster than journals do. That is itself part of the story.

## Where the term came from

On 2 February 2025 Andrej Karpathy, a founding member of OpenAI and former director of AI at Tesla, posted on X about a new way of programming he called "vibe coding," in which you "fully give in to the vibes, embrace exponentials, and forget that the code even exists" (Karpathy 2025). He described speaking his requests to an AI coding tool, accepting all of its changes without reading them and pasting error messages back without comment when something broke, and said the approach was fine for throwaway weekend projects. The post was viewed around 4.5 million times, and the term spread with unusual speed: Merriam-Webster listed it as a slang and trending entry in March 2025, and Collins English Dictionary named it Word of the Year for 2025 in November (Michels et al. 2026). Collins defines it as the use of artificial intelligence prompted by natural language to assist with the writing of computer code.

The definition that matters for this post came a few weeks after the original tweet. The programmer Simon Willison argued that using an LLM is not enough to make something vibe coding: if you have reviewed, tested and understood every line the model wrote, you are simply using it as a typing assistant (Willison 2025). Vibe coding, on this reading, is defined by not reading the code and judging it only by whether it seems to work. A recent review of the evidence adopts the same boundary (Michels et al. 2026), and so will I. The distinction is important because most of the questions below are about what happens when the human stops checking.

The other two terms came from industry. In late September 2025 Microsoft introduced an agent mode for Excel and Word and called the shift "vibe working," with "vibe writing" as its Word-specific form: you describe the document or analysis you want and the agent plans and carries out the steps (Microsoft 2025). Nobody has yet defined these terms as carefully as Willison defined vibe coding, so I use them loosely here: handing a writing or office task to an AI and judging mainly by the result.

## How accuracy is measured

There are three kinds of evidence, and they answer different questions.

**Benchmarks with hidden tests.** A benchmark gives a model a task and checks the result automatically. The first widely used one, HumanEval, had 164 short Python functions, each with unit tests; today's frontier models solve almost all of them, so it no longer tells models apart. Its successor for agentic coding, SWE-bench, gives an agent a real issue from a real open-source repository and counts it as solved only if the repository's own tests pass afterwards. Scores rose from under 2% on the original SWE-bench in late 2023 to 95% on its human-validated subset, SWE-bench Verified, by mid-2026 (Michels et al. 2026). That is the most compact summary of how fast coding capability has grown.

**Randomized trials with people.** Benchmarks measure the model alone. To know what happens when a person uses the model, someone has to randomly assign people to work with and without it and measure the outcome. The METR trial discussed in the previous post is the best-known example; a field experiment with 4,867 developers in three companies found 26% more completed tasks with an AI assistant (Cui et al. 2026); and a trial run by Anthropic found that developers learning a new library with AI help scored 17 percentage points lower (50% against 67%) on a test of what they had just learned (Shen & Tamkin 2026).

**Telemetry and audits.** Companies and researchers also measure what happens in real codebases over months: review time, bug counts, incidents and code duplication. These data are large but usually observational and often collected by vendors, so they show associations rather than causes.

Each kind has known traps, and they all push in the same direction, toward overestimating accuracy.

- **Contamination.** Models may have seen the test problems during training. When OpenAI audited SWE-bench Verified in early 2026, it found that every frontier model it tested could reproduce the reference solution or verbatim details of the problem for some tasks, and among the 138 problems that its own o3 model could not solve consistently, 59.4% had defects in the tests or the problem description. It stopped reporting the benchmark in February 2026 (Michels et al. 2026).
- **Weak tests.** A patch can pass the tests and still be wrong. An audit of the top 30 agents on SWE-bench found that about one in five "solved" patches was semantically incorrect but passed weak test suites (Yu et al. 2026).
- **Who runs the test.** On the harder, contamination-resistant SWE-bench Pro, the best scores reported by model developers were around 80%, while the benchmark's maintainer, running the same class of models itself, found about 59–61%, although it had not yet tested the newest models (Michels et al. 2026).

![Scores of AI coding systems under different definitions of success](/assets/img/blog/2026-10-21-vibe-correctness.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 1.** The same kind of system scores very differently depending on who runs the test, what counts as correct and how much of the task must work. Left: best scores on SWE-bench Verified and on the harder SWE-bench Pro, as reported by model developers and as measured independently (Michels et al. 2026). Middle: share of solutions from one agent that were functionally correct, and correct and secure (Zhao et al. 2026). Right: share of scientific coding subproblems and of whole problems solved by the best model in the published study, o1-preview, without background information (Tian et al. 2024). The three panels come from different studies and years and should not be compared with one another. Figure by Daeha Kim._

So "how accurate is vibe coding?" has no single answer. The answer depends on what is checked, by whom and how strictly. That observation turns out to be the key to the rest of this post.

## What decides whether the code is right

Reading across the studies, I find eight factors with reasonably direct evidence behind them. They are not independent, and the first one runs through all the others.

**1. Whether the result can be checked.** The review by Michels and colleagues (2026) concludes that the decisive variable is not difficulty but verifiability. Where a mechanical check exists (a test suite, a compiler, a crash that can be reproduced), current systems are strong and improving fast, because they can try, fail and try again. Where no such check exists, failures are silent. The effect of a feedback loop is visible even in older work: letting a model run its code against unit tests and explain its own mistakes improved accuracy by up to 12% on benchmarks with unit tests, while on a text-to-SQL benchmark with no unit tests the gains were only 2–3% (Chen et al. 2024). The catch is that the model can also write the tests. AI-written tests usually compile and pass, but they detect real faults less well than human-written ones (Michels et al. 2026), because a model trying to pass its own tests writes tests that confirm its code rather than tests that could break it.

**2. How completely the task is specified.** Benchmarks give the model a complete, precise task. Real requests rarely are. When researchers removed key information from SWE-bench Verified issues, models were poor at noticing that anything was missing; but when they were allowed to ask the user questions, performance on the underspecified tasks improved by up to 74% over working without interaction (Vijayvargiya et al. 2025). A vague request is not a neutral starting point. The model fills the gaps with plausible assumptions, and nothing tells you which ones it chose.

**3. How large and how old the codebase is.** Scores drop sharply from short, self-contained tasks to long tasks in large repositories (the gap between SWE-bench Verified and Pro in Figure 1). The one independent trial that measured a slowdown studied experienced developers working in their own mature repositories (Becker et al. 2025). Michels and colleagues offer a testable conjecture for much of the disagreement in the literature, which no study has yet been designed to test: AI gains are real on new code and shrink or reverse in mature codebases, where years of undocumented decisions form a specification that cannot be checked. Long inputs are also a problem in themselves. In a controlled study of 18 models, performance became less reliable as input length grew, even on simple tasks whose difficulty was held constant (Hong et al. 2025).

**4. How common the language and library are.** Models are much better at languages with abundant training data. The largest public code corpus, The Stack v2, contains roughly 200 GB of Python but only about 2 GB of Julia and Fortran (Boruch-Gruszecki et al. 2025), and performance on low-resource languages such as R and Racket lags well behind Python and Java (Cassano et al. 2024). Library versions matter too: on 328 Python problems that required code compatible with a specific version of a library, the best commercial models succeeded only 48–51% of the time in the baseline setting (Misra et al. 2026). For hydrologists this is not abstract. Much of our legacy modeling code is in Fortran, and much of our analysis depends on fast-moving packages.

**5. How much domain knowledge the task needs.** General coding skill does not transfer automatically to scientific code. SciCode, built by scientists from 16 subfields of the natural sciences, splits 80 research problems into 338 subproblems. In the published study the best model, o1-preview, solved 28.5% of the subproblems but only 7.7% of whole problems, because every step has to be right for the whole to be right (Tian et al. 2024). Models have improved since, but the structure of the result has not changed: errors compound across steps, and a scientific workflow has many steps.

**6. What "correct" means.** Functional correctness is only one property. SusVibes gives agents 186 real feature requests from open-source projects for which human developers had originally committed vulnerable code. The best configuration produced functionally correct solutions 57% of the time, but only 11.8% were also secure, and adding security hints to the request did not fix this (Zhao et al. 2026). If you only check whether the code runs, you are measuring the easier of the two numbers.

**7. The model and the tool around it.** Model generation is the factor everyone notices, and it is real: the rise on SWE-bench from under 2% to 95% happened in about two and a half years. But the same model behaves differently depending on the harness: how many attempts it gets, whether it can run tests, which tools it can call. A benchmark score belongs to a model and its setup, and your setup is probably not the one on the leaderboard.

**8. The person.** In Anthropic's trial, participants who relied heavily on the AI, by delegating the code to it or letting it debug for them, scored below 40% on the comprehension test, while those who asked conceptual questions or requested explanations alongside the code scored 65–86%, although these subgroups were very small (Shen & Tamkin 2026). The developers in the METR trial believed they were faster when they were slower (Becker et al. 2025). The person decides how well the task is specified, whether a check exists and whether anyone reads the output. Vibe coding, by definition, removes the last of these.

Put together, the factors suggest a simple rule. Vibe coding is most accurate when the task is small, well specified, in a common language and checkable by a test you trust; it is least accurate when the task is long, vague, scientific, security-sensitive or embedded in a large old codebase. Most research code in our field falls somewhere in between.

## Vibe writing: how far does it go?

Writing has the same factors, but the first one, verifiability, works against it. There is no compiler for an argument and no unit test for a literature review.

**Prose quality can be very high.** In a preregistered study, writers trained in Master of Fine Arts programs and frontier models each wrote short passages in the style of 50 award-winning authors, and 28 expert readers and 516 general readers compared them blind. When the models were simply prompted, expert readers strongly preferred the human writing. When a model was fine-tuned on each author's complete works, the result reversed: expert readers now preferred the AI text for both style and quality, and detectors flagged only 3% of the fine-tuned passages as machine-written, against 97% of the prompted ones (Chakrabarty et al. 2025). At the level of the sentence, AI writing can already pass for expert work.

**Facts and sources are where it fails.** The detector company GPTZero scanned 4,841 of the 5,290 papers accepted at NeurIPS 2025, one of the most selective AI conferences, and confirmed at least 100 fabricated citations in about 50 papers, roughly 1% of those it scanned, each of which had passed three or more reviewers (GPTZero 2026). The figure comes from a company that sells a citation checker, but the citations it lists can be checked by anyone. Tools designed for research do better but not well enough: an audit of AI search engines and deep-research agents found that a large share of their statements were not supported by the sources they themselves cited, with citation accuracy between 40% and 80% across systems (Venkit et al. 2025). Generated documentation shows the same pattern in code: early frontier models wrote inaccurate statements in about one fifth of generated code comments, and standard automatic metrics did not detect them (Michels et al. 2026).

**Whole papers are possible, but rarely good ones.** In 2025 Sakana AI submitted three papers written entirely by its AI Scientist system to an ICLR workshop, with the organizers' agreement. One received an average score of 6.33, just above the acceptance threshold; the company said none of the three met its own bar for the main conference, and its internal review found citation errors (Sakana AI 2025). Later that year, Agents4Science accepted only papers with an AI as first author: of 315 submissions, 253 complete papers were reviewed by three LLM reviewers, 79 were also assessed by humans and 48 were accepted (Bianchi et al. 2025). One human reviewer, an astrophysicist, judged the papers she saw technically correct but neither interesting nor important (Hulick 2025).

**And plain text is still the weak spot in office benchmarks.** On GDPval tasks whose deliverable was plain text, models were rated better than professionals far less often than on tasks with spreadsheets, slides or PDFs (Patwardhan et al. 2025).

My reading is that vibe writing works for text whose value lies in its surface: a summary of a document you have read, a routine email, a first structure for a report. It fails for text whose value lies in its claims, because nothing in the process checks them. The previous post showed a second, quieter failure: even light editing shifts what the text says. A scientific paper is almost entirely claims.

## Vibe working: how far does it go?

Office work sits between coding and writing: some of it has checkable outputs (a spreadsheet formula, a filled form), some does not (a recommendation, a slide narrative). The benchmarks reflect that.

![Success rates of AI agents on office and freelance work benchmarks](/assets/img/blog/2026-10-21-vibe-working.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 2.** Success rates of AI agents on benchmarks of office and freelance work. Each benchmark defines success differently (accepted by a client, all checkpoints completed, cell-level accuracy, judged at least as good as an expert's deliverable), so the rows should not be compared with one another. The SpreadsheetBench and the December 2025 GDPval figures are reported by the companies that built the products. Figure by Daeha Kim, drawn from numbers reported in Mazeika et al. (2025), CAIS (2026), Xu et al. (2025), Microsoft (2025), Patwardhan et al. (2025) and OpenAI (2025)._

- **Well-defined spreadsheet tasks.** Microsoft reported that its Excel agent solved 57.2% of SpreadsheetBench tasks, against a human baseline of 71.3% (Microsoft 2025).
- **Simulated workplace.** In TheAgentCompany, a simulated software company with internal websites, documents, chat and simulated colleagues, the best agent in the published version completed about 30% of 175 tasks on its own. Administrative, finance and data science tasks, which people find easy, were harder for agents than software engineering (Xu et al. 2025).
- **Expert deliverables.** On GDPval, professionals with an average of 14 years of experience judged the best model's deliverables at least as good as an expert's in 47.6% of comparisons in the original paper (Patwardhan et al. 2025); a model released two months later was reported at 70.9% (OpenAI 2025). These are well-specified, one-shot tasks with all the necessary files provided.
- **Whole paid projects.** The Remote Labor Index gives agents 240 real projects, mostly from freelance platforms, from architecture to data analysis to video, and asks whether the result would be accepted by a reasonable client as the commissioned work. At release in October 2025 the best agent succeeded on 2.5% (Mazeika et al. 2025). By mid-2026 the best model reached 15.8% (CAIS 2026): a sixfold increase in under a year, but still far from most projects.

The spread in Figure 2 is the same pattern as in Figure 1. The more the task is specified in advance and the narrower the definition of success, the higher the number. The closer the task is to a whole job, with an underspecified brief and a client who judges the result as a whole, the lower it is. One real-world example shows the cost of forgetting this. In 2024 the payment company Klarna announced that its AI assistant was doing the work of 700 customer-service agents; in 2025 its chief executive acknowledged that quality had suffered and the company began hiring people again (Michels et al. 2026).

## A working rule for our group

The factors above can be turned into a few questions to ask before handing a task to an AI and judging it by the result.

- **Can I check the result with something I trust and did not let the model write?** A water balance that must close, an analytical solution, a published benchmark catchment, a table I can recompute by hand. If yes, vibe away and run the check. If no, read the output as if a new student wrote it.
- **Have I said everything the task needs?** Ask the model to list its assumptions or ask you questions before it starts. The evidence says it will not do this on its own, and it helps a great deal when it does.
- **Is the task in familiar territory for the model?** Python and common packages are; old Fortran code, a specific library version or a specialized hydrological model are less so.
- **How long is the chain of steps?** Errors compound. Break long work into pieces you can check one at a time.
- **Is "it runs" the right definition of correct?** For anything that handles files, credentials, other people's data or design decisions, it is not.
- **Is the value of the output in its claims?** If so, as in a paper, a proposal or a report, every claim and every reference needs a source you have opened.
- **Am I learning this skill right now?** If so, ask for explanations, not answers.

## Bottom line

- "Vibe coding" was coined by Andrej Karpathy on 2 February 2025 and was Collins Word of the Year for 2025. What defines it is not using an AI but not reading what the AI wrote. "Vibe writing" and "vibe working" were introduced by Microsoft in September 2025.
- Its accuracy is measured with benchmarks, randomized trials and field data. All three tend to overestimate it, through contamination, weak tests and self-reporting.
- The decisive factor is whether the result can be checked. Specification, codebase size and age, language and library, domain knowledge, the definition of correctness, the tool setup and the person all matter as well.
- Vibe writing produces prose that can pass for expert work, but fabricated citations and unsupported claims are common, and nothing in the process catches them.
- Vibe working succeeds on well-defined tasks and mostly fails on whole projects, though that is changing quickly.
- The narrower and more checkable the task, the more you can trust the vibes. For research, that usually means building the check first.

**Questions to think about**

1. For the last piece of code an AI wrote for you, what was the check that told you it was right? Did the AI write that check?
2. Take one routine task in your research and write down everything the AI would need to know to do it correctly. How much of that would you normally leave unsaid?
3. Which parts of a scientific paper could you check mechanically, and which could only be checked by reading the sources? What does that imply for how you use AI to write?

---

**한 줄 요약 (Korean summary).** "바이브 코딩"은 안드레이 카파시가 2025년 2월 2일 X에 올린 글에서 처음 쓴 말로, 코드가 존재한다는 사실조차 잊고 AI에 맡기는 방식을 가리키며, 콜린스 사전의 2025년 올해의 단어로 뽑혔다. 핵심은 AI를 쓰는 것이 아니라 AI가 쓴 코드를 읽지 않는다는 데 있다. "바이브 라이팅"과 "바이브 워킹"은 2025년 9월 마이크로소프트가 엑셀·워드 에이전트를 내놓으며 붙인 이름이다. 정확도는 숨겨진 테스트가 있는 벤치마크, 사람을 무작위로 배정한 실험, 실제 현장 데이터로 측정하지만, 학습 데이터 오염, 허술한 테스트, 개발사 자체 보고 때문에 대체로 과대평가된다. 예를 들어 SWE-bench Verified에서는 95%까지 올랐지만 더 어려운 SWE-bench Pro를 독립 기관이 직접 돌리면 약 60%였고, 기능상 맞는 코드가 57%여도 보안까지 갖춘 코드는 11.8%에 그쳤다. 정확도를 가르는 가장 큰 요인은 결과를 기계적으로 검증할 수 있는가이며, 과제를 얼마나 완전하게 명시했는가(질문을 허용하면 최대 74% 향상), 코드베이스의 크기와 연식, 언어와 라이브러리의 흔한 정도, 필요한 전문 지식(과학 코딩 문제 전체 정답률 7.7%), "정답"의 정의, 도구 환경, 그리고 사람이 함께 작용한다. 바이브 라이팅은 전문가 수준으로 읽히는 문장을 만들 수 있지만(작가별로 미세조정한 모델의 글을 전문가 독자가 더 선호), 가짜 인용과 근거 없는 주장을 걸러 주는 장치가 없다(NeurIPS 2025 채택 논문의 약 1%에서 가짜 인용 확인, 딥리서치 도구의 인용 정확도 40–80%). 바이브 워킹은 잘 정의된 과제에서는 상당히 잘하지만(스프레드시트 57.2%, 사람 71.3%) 실제 유료 프리랜서 프로젝트 전체를 맡기면 대부분 실패한다(2025년 10월 2.5%에서 2026년 15.8%로 빠르게 상승 중). 결국 과제가 좁고 검증 가능할수록 맡겨도 되고, 연구에서는 AI에게 일을 맡기기 전에 믿을 수 있는 검증 기준부터 직접 만들어야 한다.

---

**References**

Becker, J., Rush, N., Barnes, E., & Rein, D. (2025). Measuring the impact of early-2025 AI on experienced open-source developer productivity. arXiv:2507.09089. [https://doi.org/10.48550/arXiv.2507.09089](https://doi.org/10.48550/arXiv.2507.09089)

Bianchi, F., Queen, O., Thakkar, N., Sun, E., & Zou, J. (2025). Exploring the use of AI authors and reviewers at Agents4Science. arXiv:2511.15534. [https://doi.org/10.48550/arXiv.2511.15534](https://doi.org/10.48550/arXiv.2511.15534)

Boruch-Gruszecki, A., Zi, Y., Wu, Z., Oberoi, T., Anderson, C. J., Biswas, J., & Guha, A. (2025). Agnostics: Learning to code in any programming language via reinforcement with a universal learning environment. arXiv:2508.04865 (accepted at ICLR 2026). [https://doi.org/10.48550/arXiv.2508.04865](https://doi.org/10.48550/arXiv.2508.04865)

CAIS (2026). A significant increase in digital labor automation. Center for AI Safety blog, 1 July 2026. Not peer-reviewed. [https://safe.ai/blog/significant-increase-in-digital-labor-automation](https://safe.ai/blog/significant-increase-in-digital-labor-automation)

Cassano, F., Gouwar, J., Lucchetti, F., Schlesinger, C., Freeman, A., Anderson, C. J., Feldman, M. Q., Greenberg, M., Jangda, A., & Guha, A. (2024). Knowledge transfer from high-resource to low-resource programming languages for Code LLMs. _Proceedings of the ACM on Programming Languages_, 8(OOPSLA2), 295. [https://doi.org/10.1145/3689735](https://doi.org/10.1145/3689735)

Chakrabarty, T., Ginsburg, J. C., & Dhillon, P. (2025). Readers prefer outputs of AI trained on copyrighted books over expert human writers. arXiv:2510.13939. [https://doi.org/10.48550/arXiv.2510.13939](https://doi.org/10.48550/arXiv.2510.13939)

Chen, X., Lin, M., Schärli, N., & Zhou, D. (2024). Teaching large language models to self-debug. In _International Conference on Learning Representations (ICLR 2024)_. arXiv:2304.05128. [https://doi.org/10.48550/arXiv.2304.05128](https://doi.org/10.48550/arXiv.2304.05128)

Cui, K. Z., Demirer, M., Jaffe, S., Musolff, L., Peng, S., & Salz, T. (2026). The effects of generative AI on high-skilled work: Evidence from three field experiments with software developers. _Management Science_, advance online publication. [https://doi.org/10.1287/mnsc.2025.00535](https://doi.org/10.1287/mnsc.2025.00535)

GPTZero (2026). GPTZero finds 100 new hallucinations in NeurIPS 2025 accepted papers. Company report, 21 January 2026. Not peer-reviewed. [https://gptzero.me/news/neurips/](https://gptzero.me/news/neurips/)

Hong, K., Troynikov, A., & Huber, J. (2025). Context rot: How increasing input tokens impacts LLM performance. Chroma technical report, July 2025. Not peer-reviewed. [https://www.trychroma.com/research/context-rot](https://www.trychroma.com/research/context-rot)

Hulick, K. (2025). A conference just tested AI agents' ability to do science. _Science News_, 24 October 2025. [https://www.sciencenews.org/article/science-conference-test-ai-agents](https://www.sciencenews.org/article/science-conference-test-ai-agents)

Karpathy, A. (2025). "There's a new kind of coding I call 'vibe coding'…" Post on X, 2 February 2025. [https://x.com/karpathy/status/1886192184808149383](https://x.com/karpathy/status/1886192184808149383)

Mazeika, M., Gatti, A., Menghini, C., Sehwag, U. M., Singhal, S., Orlovskiy, Y., Basart, S., Sharma, M., Peskoff, D., Lau, E., et al. (2025). Remote Labor Index: Measuring AI automation of remote work. arXiv:2510.26787. [https://doi.org/10.48550/arXiv.2510.26787](https://doi.org/10.48550/arXiv.2510.26787)

Michels, D. L., Abu Ghazaleh, M., Lazzari, F., Kassem, N., & Klein, J. (2026). Vibe coding: Practice, performance, productivity, and risk—A state-of-the-art review. arXiv:2608.20446. Not peer-reviewed. [https://doi.org/10.48550/arXiv.2608.20446](https://doi.org/10.48550/arXiv.2608.20446)

Microsoft (2025). Vibe working: Introducing Agent Mode and Office Agent in Microsoft 365 Copilot. Microsoft 365 blog, 29 September 2025. Product announcement, not peer-reviewed. [https://www.microsoft.com/en-us/microsoft-365/blog/2025/09/29/vibe-working-introducing-agent-mode-and-office-agent-in-microsoft-365-copilot/](https://www.microsoft.com/en-us/microsoft-365/blog/2025/09/29/vibe-working-introducing-agent-mode-and-office-agent-in-microsoft-365-copilot/)

Misra, D., Islah, N., May, V., Rauby, B., Wang, Z., Gehring, J., Orvieto, A., Chaudhary, M. S., Muller, E. B., Rish, I., Kahou, S. E., & Caccia, M. (2026). GitChameleon 2.0: Evaluating AI code generation against Python library version incompatibilities. In _Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_, 46792–46831. [https://doi.org/10.18653/v1/2026.acl-long.2170](https://doi.org/10.18653/v1/2026.acl-long.2170)

OpenAI (2025). Introducing GPT-5.2. Product announcement, December 2025. Not peer-reviewed. [https://openai.com/index/introducing-gpt-5-2/](https://openai.com/index/introducing-gpt-5-2/)

Patwardhan, T., Dias, R., Proehl, E., Kim, G., Wang, M., Watkins, O., Posada Fishman, S., Aljubeh, M., Thacker, P., Fauconnet, L., Kim, N. S., Chao, P., Miserendino, S., Chabot, G., Li, D., Sharman, M., Barr, A., Glaese, A., & Tworek, J. (2025). GDPval: Evaluating AI model performance on real-world economically valuable tasks. arXiv:2510.04374. [https://doi.org/10.48550/arXiv.2510.04374](https://doi.org/10.48550/arXiv.2510.04374)

Sakana AI (2025). The AI Scientist generates its first peer-reviewed scientific publication. Company blog, 12 March 2025. Not peer-reviewed. [https://sakana.ai/ai-scientist-first-publication/](https://sakana.ai/ai-scientist-first-publication/)

Shen, J. H., & Tamkin, A. (2026). How AI impacts skill formation. arXiv:2601.20245. [https://doi.org/10.48550/arXiv.2601.20245](https://doi.org/10.48550/arXiv.2601.20245)

Tian, M., Gao, L., Zhang, S. D., Chen, X., Fan, C., Guo, X., Haas, R., Ji, P., Krongchon, K., Li, Y., et al. (2024). SciCode: A research coding benchmark curated by scientists. In _Advances in Neural Information Processing Systems 37 (NeurIPS 2024), Datasets and Benchmarks Track_. [https://doi.org/10.52202/079017-0963](https://doi.org/10.52202/079017-0963)

Venkit, P. N., Laban, P., Zhou, Y., Huang, K.-H., Mao, Y., & Wu, C.-S. (2025). DeepTRACE: Auditing deep research AI systems for tracking reliability across citations and evidence. arXiv:2509.04499. [https://doi.org/10.48550/arXiv.2509.04499](https://doi.org/10.48550/arXiv.2509.04499)

Vijayvargiya, S., Zhou, X., Yerukola, A., Sap, M., & Neubig, G. (2025). Ambig-SWE: Interactive agents to overcome underspecificity in software engineering. arXiv:2502.13069 (accepted at ICLR 2026). [https://doi.org/10.48550/arXiv.2502.13069](https://doi.org/10.48550/arXiv.2502.13069)

Willison, S. (2025). Will the future of software development run on vibes? Blog post, 6 March 2025. [https://simonwillison.net/2025/Mar/6/vibe-coding/](https://simonwillison.net/2025/Mar/6/vibe-coding/)

Xu, F. F., Song, Y., Li, B., Tang, Y., Jain, K., Bao, M., Wang, Z. Z., Zhou, X., Guo, Z., Cao, M., et al. (2025). TheAgentCompany: Benchmarking LLM agents on consequential real world tasks. In _Advances in Neural Information Processing Systems 38 (NeurIPS 2025)_, 10291–10321. [https://doi.org/10.52202/085713-0315](https://doi.org/10.52202/085713-0315)

Yu, B., Cao, Y., Zhang, Y., Lin, L., Xu, J., Zhong, Z., Xu, Q., Wang, G., Cao, J., Cheung, S.-C., et al. (2026). SWE-ABS: Adversarial benchmark strengthening exposes inflated success rates on test-based benchmark. arXiv:2603.00520. [https://doi.org/10.48550/arXiv.2603.00520](https://doi.org/10.48550/arXiv.2603.00520)

Zhao, S., Wang, D., Zhang, K., Luo, J., Li, Z., & Li, L. (2026). Is vibe coding safe? Benchmarking vulnerability of agent-generated code in real-world tasks. In _Proceedings of the 43rd International Conference on Machine Learning_, PMLR 306, 162269–162292. [https://proceedings.mlr.press/v306/zhao26ax.html](https://proceedings.mlr.press/v306/zhao26ax.html)

_Both figures are original. The Python scripts that produce them are available on GitHub: [Figure 1](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-21-vibe-correctness.py) and [Figure 2](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-21-vibe-working.py)._
