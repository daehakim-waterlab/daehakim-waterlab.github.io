---
layout: post
title: "From chatbot to coworker: three years of LLMs in hydrology"
date: 2026-10-18 09:00:00
description: "Re-reading a 2023 editorial on ChatGPT in hydrology next to two new papers and a book on AI: what LLMs could not do then, what agents can do now, and why most research has not switched yet."
tags: llm ai-agents hydrologic-modelling calibration education
categories: notes
related_posts: false
---

In September 2023, _Water Resources Research_ published an editorial by Foroumandi and colleagues titled "ChatGPT in Hydrology and Earth Sciences: Opportunities, Prospects, and Concerns." It was one of the first careful attempts by our community to say what these tools were good for and where they should be kept away. Three years and several model generations later, it is worth reading again next to two recent hydrology papers and Christopher Summerfield's book _These Strange New Minds_. Together they show how quickly the question has changed: from "can it write a correct loop?" to "can it run a 531-basin experiment overnight, and should we let it?"

## 2023: a useful but unreliable writing partner

The 2023 editorial was balanced, and most of its observations held up. ChatGPT was good at beginner-to-intermediate coding (reading and cleaning data, explaining syntax, translating between languages, adding comments), at polishing prose for non-native writers, and at summarizing text. The problems began with anything harder:

- **Complex code.** In one test, after several rounds of error messages, the model "fixed" a shape mismatch in a deep-learning script by inserting an array of zeros. The code ran, and the answer was meaningless.
- **Unstable physics.** Asked how shortwave radiation affects precipitation in humid regions, it gave one plausible explanation, then reversed itself as soon as the authors said it was wrong.
- **Invented references.** All three citations it supplied for that answer turned out not to exist.
- **Arguing a bad case.** When asked to help convince a reviewer that an uncalibrated model was valid, it obliged with persuasive talking points.
- **Frozen knowledge.** It had no internet access and knew nothing after its training cutoff.

The authors' conclusion was that ChatGPT was a compiler rather than an author, and their recommendations followed from that: never use it as the sole source of information, disclose its use, keep teaching programming so researchers can check AI-written code, and redesign assignments around critical thinking. One recommendation aged badly. AI-text detectors were suggested for screening manuscripts, but they proved unreliable; OpenAI withdrew its own classifier in 2023 because of low accuracy. The rest still reads as sound advice, and some of it has become more important, not less.

## What changed: from answering to acting

The biggest change since 2023 is not that models know more hydrology, although they do. It is that they can now **act**. Current assistants search the web, read and write files, run code, see the errors, and try again. Open standards such as the Model Context Protocol (MCP) let a model call external tools in a structured way. "Agentic" coding tools can take a goal, plan the steps, edit a whole project and test the result with little hand-holding. I built this website that way, by describing what I wanted and reviewing what came back.

The market has changed too. ChatGPT is now one of many: Claude, Gemini, DeepSeek, Qwen and Moonshot's Kimi compete closely, and several strong models have openly released weights. Competition has moved from raw capability toward cost. By one industry index, frontier token prices in late 2026 are about 85% below their March 2023 level, and open-weight models are typically far cheaper than proprietary ones, although the newest frontier models have become more expensive again over the past year. For agents, which can consume more than a million tokens per task, cost per task now matters as much as cost per token.

The figure below summarizes how the role of the LLM has shifted across the three hydrology papers discussed here.

![Three panels showing the role of the LLM in 2023 (writer), 2025 (decision-maker inside a calibration loop) and 2026 (orchestrator of an agentic workflow)](/assets/img/blog/2026-10-18-llm-roles.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 1.** How the role of the LLM changed across three studies. In 2023 the human did all the running and checking. In the GRL study, the LLM proposed parameters inside a loop built by the researchers. In the Journal of Hydrology study, agents planned, coded, ran and debugged entire modelling workflows within an expert-designed process. Original schematic by Daeha Kim, based on Foroumandi et al. (2023), Zhu et al. (2026) and Li et al. (2026)._

## 2025: the LLM inside the calibration loop

Zhu et al. (2026, _Geophysical Research Letters_) asked whether an LLM could replace the optimization algorithm in calibrating the VIC model for a sub-basin of the Yangtze. Judging from the models tested (GPT-4o-mini, DeepSeek-R1, DeepSeek-V3 and two Llama models) and the submission date of October 2025, the experiments reflect LLMs of roughly mid-2025. The researchers wrote a Python program that ran VIC, computed NSE, RMSE and bias, and sent the results and hydrograph to the LLM, which proposed the next parameter set. The LLM never ran or imitated the model; it only made the decisions that SCE-UA or NSGA-III would normally make.

The result was mixed in an informative way. DeepSeek-R1 reached an NSE of about 0.89 within roughly 200 iterations and matched SCE-UA's best NSE using fewer model runs. It also focused early on the parameters hydrologists know to be sensitive, such as infiltration shape and soil depth. The other four models did worse than the standard algorithms. One basin, one model and six parameters is a small test, and "fewer iterations" says nothing about API cost or about whether the result repeats on a second run. But it showed that a reasoning model could act like a sensible, if inexperienced, calibrator.

## 2026: agents that build the whole workflow

Li et al. (2026, _Journal of Hydrology_), submitted in May 2026, used the next generation of models: GPT-5.5, Claude Sonnet 4.5, Gemini 2.5 Pro, DeepSeek-V3.2 and Qwen-Plus. Their system, HydroAIM, uses several cooperating agents connected through MCP. Given a task, the agents prepare the data, write and run the training code, read the error messages, fix them and evaluate the result, all without a human in the loop.

Three findings stand out.

- **It works most of the time.** Across 125 modelling tasks with five different LLMs, 92.8% of runs succeeded. On 531 CAMELS basins, the agent-built models reached a median NSE of 0.58 for basin-by-basin LSTMs (close to the 0.61 of the calibrated SAC-SMA benchmark) and 0.73 for a single LSTM trained on all basins, which is in line with published LSTM benchmarks.
- **Planning, not knowledge, is the bottleneck.** When the researchers removed the expert-designed workflow and let the agents organize the task themselves, the success rate fell to **0%**. Agents declared victory after one sub-step, looped on the same tool calls, or lost track of file paths after their context was summarized.
- **Experts are still needed.** In one run, weak performance turned out to come from a data-loading error that withheld same-day weather inputs. When prompts pushed the agents toward "bigger" architectures, they switched to models that performed worse. Newer versions of some models also had to be used partway through the study, which makes exact reproduction harder.

The cost appendix of the same paper makes the price competition concrete. A successful end-to-end run used between half a million and two million tokens, and the price of that run differed by a factor of 25 to 45 depending on the model, even though all five models completed the tasks at similar rates.

![Dot plot of the API cost of one successful modelling run for five LLMs: about $0.09 for Qwen-Plus and DeepSeek-V3.2, and $2–4 for Claude Sonnet 4.5, GPT-5.5 and Gemini 2.5 Pro](/assets/img/blog/2026-10-18-agent-cost.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 2.** API cost of one representative successful run for each LLM and each of five task types. Data from Table A1 of Li et al. (2026); plotted by Daeha Kim. Costs reflect list prices at the time of the study and will change._

## Checking a book's predictions

Christopher Summerfield, a cognitive neuroscientist, wrote _These Strange New Minds_ in 2024. His closing chapter makes a few claims that are easy to check against what has happened since.

He argued that LLMs are not minds like ours: they have no body, no friends and no motivation of their own, and so no built-in curiosity about the world. Nothing in the papers above contradicts that. In both studies, the question, the data, the success criterion and the judgement of what counts as physically plausible all came from people.

He identified two engineering limits, short memory and weak long-term planning, and expected both to be solved soon. That has **partly** happened. Assistants now remember across conversations and agents routinely complete multi-step tasks. But the 0% result without an expert workflow shows that open-ended, long-horizon scientific work still breaks down unless someone gives the agent a structure to follow.

He predicted that we would drift gradually toward AI that acts rather than merely answers, starting with simple, well-defined tasks. That is exactly the path we have seen. Software was first, because code can be run and tested automatically. Scientific modelling, with its many judgement calls, is following more slowly.

He also cited early evidence that AI help lifts the least-skilled workers the most and could act as a leveller. In research, the early picture points the other way. In a 2026 survey of 1,260 social scientists, 81% had used AI chatbots for research, but only 20% used coding agents weekly. Use was concentrated among economists, doctoral students and researchers at top universities. That sample was self-selected, so the true share is probably lower, and I know of no equivalent survey for hydrology. My impression matches it: agentic workflows are still rare in our field.

Finally, he warned that forecasts about AI replacing professionals have often been wrong. His example was the 2016 prediction that we would soon stop training radiologists, which has not come true. The hydrology papers suggest a similar story for us. The agents did not replace the hydrologist; they moved the hydrologist's work from writing code to designing workflows, checking assumptions and judging results.

## Why most research has not switched yet

Agentic tools have spread quickly in software development but slowly in research. I think the reasons are specific to science.

- **Verification costs time.** A program that runs is not a program that is right. The zero-array "fix" from 2023 and the missing-forcing bug from 2026 are the same kind of error at different scales.
- **Reproducibility is harder.** The same prompt can give different code from day to day, and model versions change underneath you. Li et al. recommend recording model identifiers, prompts, tool definitions and execution logs; few groups do this yet.
- **Costs are real.** A single agentic run is cheap, but sensitivity analyses across hundreds of basins add up, and frontier models can cost tens of times more than open ones.
- **You still need to know the craft.** To supervise an agent, you need enough coding and enough hydrology to recognize a wrong answer. Ironically, this keeps the people who would benefit most from the tools from trusting them.

## What I tell students now

The 2023 editorial ended with the advice to use AI as a tool for problem-solving, but never to let it solve the problem by itself. In 2026 I would phrase it slightly differently: treat the agent as a fast, tireless junior colleague whose work you must check.

- **Do** let agents handle the plumbing: downloading data, reformatting files, plotting, writing tests and rerunning experiments.
- **Do** use them to run more checks than you could by hand, such as sensitivity tests, additional basins or alternative model structures.
- **Do not** let them choose your research question, your success criterion or your interpretation of the physics.
- **Do not** report a number you cannot reproduce. Record the model and version, the prompt and the code that was actually run.
- **Keep learning to code and keep learning hydrology.** In 2023 that was needed to fix the AI's mistakes. In 2026 it is needed to notice them.

**Questions to think about**

1. The GRL study accepted parameter sets based on NSE alone. What could go wrong if an agent optimizes only one metric for you?
2. Why might an agent that cannot plan on its own still succeed when given an expert workflow? What does that suggest about the value of writing down your own modelling procedures?
3. If a cheap model and an expensive model both succeed 90% of the time, what else would you want to know before choosing one for a 500-basin study?

---

**한 줄 요약 (Korean summary).** 2023년 WRR 사설은 ChatGPT를 "저자가 아니라 편집 도구"로 보고, 복잡한 코드·물리적 설명·인용에서 믿을 수 없다고 경고했다. 2025–2026년 연구에서 LLM은 보정 루프 안에서 매개변수를 결정하고(GRL), 여러 에이전트가 531개 유역의 LSTM 모형을 처음부터 끝까지 만들어 낼 정도로 발전했다(J. Hydrol.). 하지만 전문가가 설계한 작업 절차를 빼면 성공률이 0%로 떨어졌고, 데이터 오류를 잡아낸 것도 사람이었다. 모델 간 비용 차이는 25–45배에 이른다. 연구 현장에서 에이전트 사용이 아직 드문 이유는 검증, 재현성, 비용, 그리고 결과를 판단할 전문성 때문이다. 학생들에게 필요한 것은 여전히 코딩과 수문학에 대한 탄탄한 이해다.

---

**References**

Foroumandi, E., Moradkhani, H., Sanchez-Vila, X., Singha, K., Castelletti, A., & Destouni, G. (2023). ChatGPT in hydrology and Earth sciences: Opportunities, prospects, and concerns. _Water Resources Research_, 59, e2023WR036288. [https://doi.org/10.1029/2023WR036288](https://doi.org/10.1029/2023WR036288)

Zhu, Z., Tang, Y., Tang, X., et al. (2026). Large language models as calibration agents in hydrological modeling: Feasibility and limitations. _Geophysical Research Letters_, 53, e2025GL120043. [https://doi.org/10.1029/2025GL120043](https://doi.org/10.1029/2025GL120043)

Li, Y., Hu, S., Zhang, F., et al. (2026). Grounding large language models in hydrologic modelling. _Journal of Hydrology_, 679, 136358. [https://doi.org/10.1016/j.jhydrol.2026.136358](https://doi.org/10.1016/j.jhydrol.2026.136358)

Summerfield, C. (2025). _These Strange New Minds: How AI Learned to Talk and What It Means._

Lyttelton, Massenkoff & Wilmers (2026). Coding agents in the social sciences. Anthropic. [https://www.anthropic.com/research/coding-agents-social-sciences](https://www.anthropic.com/research/coding-agents-social-sciences)

BenchLM (2026). LLM pricing statistics. [https://benchlm.ai/stats/llm-pricing](https://benchlm.ai/stats/llm-pricing)

_Both figures are original. The Python scripts that produce them are available on GitHub: [Figure 1](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-18-llm-roles.py) and [Figure 2](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-18-agent-cost.py)._
