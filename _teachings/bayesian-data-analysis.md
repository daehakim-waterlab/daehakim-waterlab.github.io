---
layout: course
title: Bayesian Data Analysis
title_ko: 베이지안 자료분석
permalink: /teaching/bayesian-data-analysis/
order: 8
graduate: true
instructor: Daeha Kim
description: Graduate course, Department of Civil Engineering, Jeonbuk National University
summary_en: >-
  A graduate course on the basics of Bayesian data analysis, built around one workflow: write down a model, simulate from its priors, fit it, and examine the posterior and its predictions. Topics include Bayesian updating and posterior sampling, linear and multiple regression, causal graphs and confounding, overfitting and model comparison, interactions, Markov chain Monte Carlo, generalized linear models for counts and categories, multilevel models and partial pooling, Gaussian processes, and measurement error and missing data, all illustrated with hydrological examples where observations are sparse and uncertain.
summary_ko: >-
  모형을 세우고, 사전분포로 시뮬레이션하고, 적합한 뒤 사후분포와 예측을 살펴보는 하나의 흐름을 중심으로 베이지안 자료분석의 기초를 다루는 대학원 과목이다. 베이지안 갱신과 사후표본, 선형·다중회귀, 인과 그래프와 교란, 과적합과 모형 비교, 상호작용, 마르코프 연쇄 몬테카를로, 계수·범주 자료의 일반화선형모형, 다층모형과 부분 합동(partial pooling), 가우시안 과정, 측정오차와 결측 자료를 학습하며, 관측이 드물고 불확실한 수문 자료의 예제로 설명한다.
# Online study notes (Jupyter Book, repository daehakim-waterlab/bayesian-data-analysis).
textbook: /bayesian-data-analysis/
---

{{ page.summary_en }}

## Course content

{% if page.textbook %}<a class="textbook-link" href="{{ page.textbook }}">Online textbook &rarr;</a>{% else %}<span class="textbook-link">Online textbook — coming soon</span>{% endif %}
