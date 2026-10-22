---
layout: post
title: "An abrupt shift to a hotter, drier climate in the Western Eurasian Steppe"
date: 2026-10-22 23:10:00 +0900
description: "A hydrologist's reading of Piao et al. (2026) in Nature Geoscience: how the steppe from Ukraine to Kazakhstan flipped into a drier regime in the 1990s, why soil moisture keeps it there, what the models project, and what it means for adaptation."
tags: climate-change drought abrupt-change land-atmosphere-interactions soil-moisture
categories: paper-highlights
related_posts: false
---

Most of what we say about climate change describes a slow, steady drift: a few tenths of a degree per decade, a few percent more or less rain. But the climate system also has places where a steady push produces a sudden response. The best-known candidates are large and remote, such as the Greenland Ice Sheet or the Atlantic overturning circulation (Lenton et al. 2008). A new paper in _Nature Geoscience_ by Jinling Piao, Jong-Seong Kug and colleagues argues that one has already happened much closer to where people live and farm: in the semiarid steppe that stretches from Ukraine across southern Russia to Kazakhstan (Piao et al. 2026).

Their finding, in one sentence: since the early 1990s, summers in the Western Eurasian Steppe have dried faster than anywhere else in the Northern Hemisphere, the region has moved into a hotter and drier regime outside the range of the past century, and it shows no sign of coming back. This post goes through the causes, the outlook and what the authors, and I as a hydrologist, think it means for adaptation.

## What changed, and when

The authors measure dryness with the Standardized Precipitation Evapotranspiration Index (SPEI), which compares precipitation with atmospheric evaporative demand (potential evapotranspiration, PET) and expresses the balance in standard deviations (Vicente-Serrano et al. 2010). A negative trend means summers are getting drier, either because less rain falls or because a warmer atmosphere pulls more water out of the land, or both.

Over 1991–2020, the steppe (defined as 40–55°N, 30–65°E) had the strongest summer drying trend in the Northern Hemisphere, −0.43 per decade. That is about 1.5 times the trend in the North American drying hotspot and twice that of Mongolia (Figure 1a). Three features make this an abrupt shift rather than a steady trend:

- **A turning point.** Piecewise regression places a break in 1992 or 1993 in every dataset combination tested: a slight wetting before, a sharp decline after.
- **A regime shift.** A sequential test for regime shifts finds a significant jump to drier conditions around 2006. After the early 2000s, the SPEI distribution separates from that of every earlier 20-year period since 1901.
- **No recovery.** Drying slowed after 2010, but SPEI has stayed well below its historical baseline through 2024, the end of the record.

Over 1992–2010, the region warmed by 0.63°C per decade, nearly twice the Northern Hemisphere land average (0.32°C per decade). Rain declined at the same time. Comparing SPEI computed with observed and with climatological PET shows that rising evaporative demand made the drying about 58% stronger than reduced rainfall alone would have.

![Summer SPEI trends in drying hotspots and in climate model ensembles](/assets/img/blog/2026-10-22-steppe-drying.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 1.** (a) Summer (June–August) SPEI trends over 1991–2020 in the three Northern Hemisphere drying hotspots. (b) The observed SPEI trend over the Western Eurasian Steppe during the abrupt drying of 1992–2010, compared with the mean of three climate model ensembles. Because every run in an ensemble shares the same external forcing, the ensemble mean estimates the forced response; the gap to the observed trend is attributed to internal variability. Figure by Daeha Kim, drawn from numbers reported in Piao et al. (2026)._

## Cause 1: global warming sets the background

To separate the forced signal from natural fluctuations, the authors use large ensembles: the same climate model run many times with identical greenhouse gases and aerosols but slightly different starting conditions. The ensemble mean is the externally forced response, and the spread between runs is internal variability (Deser et al. 2020).

All three ensembles (the 100-member MPI Grand Ensemble, 50 runs of MIROC6, and 18 CMIP6 models) produce summer drying over the steppe, at −0.14 to −0.19 per decade (Figure 1b). That is 42–58% of the observed −0.33 per decade, my calculation from their numbers. So human-caused warming accounts for roughly half of the trend, and rising PET is a large part of it in the models as well.

The authors add a test that hydrologists will appreciate. They compare the observed drying with 14 CMIP6 pre-industrial control runs, which have no human forcing. The observed post-shift SPEI anomaly lies well outside the range of these runs, and 10 of 12 CMIP6 models with historical forcing simulate drying below the 5th percentile of their own control runs. Drying of this size is very unlikely without human forcing.

## Cause 2: an atmospheric wave train amplifies it

Why was the observed drying stronger and more sudden than the forced response? The model runs that dried the most share a common circulation pattern: a train of alternating high and low pressure anomalies from Western Europe to Northeast Asia, guided by the jet stream. Its high-pressure centers bring sinking air, fewer clouds, more sunshine and less rain. The authors find a similar wave train in the ERA5 reanalysis since the early 1990s.

This is internal variability, the kind of pattern that can arise in any model run by chance. In the real world it happened to line up with the forced drying in the 1990s, and the two together produced a change far faster than the steady pace of global warming. The authors note that the abruptness itself points to a key role for internal variability.

## Cause 3: drier soils lock it in

The most important part of the paper, from a hydrologist's point of view, is what kept the steppe dry after the push. The answer is the soil moisture feedback, sketched in Figure 2 (Seneviratne et al. 2010; Miralles et al. 2014).

When soil is moist, much of the sun's energy goes into evaporation, which cools the surface. As soil dries, evaporation is limited by water rather than energy, so more energy goes into heating the air directly (sensible heat). The Bowen ratio, sensible over latent heat flux, has risen in the steppe since the early 1990s. A warmer lower atmosphere raises evaporative demand and also strengthens the high-pressure system aloft, which suppresses clouds and rain. Drier soil makes hotter air, hotter air makes drier soil.

![Schematic of the soil moisture–temperature feedback in the Western Eurasian Steppe](/assets/img/blog/2026-10-22-steppe-feedback.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 2.** The feedback loop that sustains the hot, dry regime, as described by Piao et al. (2026). Global warming and an internally generated Eurasian wave train push the system; the soil moisture–temperature feedback amplifies and maintains the push. Figure by Daeha Kim, a schematic drawn from the paper's description._

The observations follow this loop:

- Before the early 1990s, soil moisture rose and heatwave frequency stayed flat. After 1992 the two moved in strong opposition, and by around 2010 both had left the range of the preceding 60 years.
- A coupling index (π) measures how much soil-moisture limits on evaporation feed surface warming. It rose for decades and then jumped around 2006, the same year as the SPEI regime shift.

The cleanest test uses seven CMIP6 models run twice: once with interactive soil moisture and once with soil moisture fixed at its climatology, so the feedback is switched off. In five of the seven models, the feedback explains about 24–44% of the regional warming trend and 37–68% of the rise in PET. Five of seven coupled runs show a significant post-1990 regime shift in SPEI; none of the runs with fixed soil moisture does (Figure 3). An observed-size drying trend lies below the 1st percentile of the fixed-soil-moisture runs. Without the land feeding back on the atmosphere, the abrupt shift does not appear.

![Contribution of the soil moisture feedback in CMIP6 experiments](/assets/img/blog/2026-10-22-steppe-coupling.png){: style="width: 100%; height: auto;" data-zoomable="" }

_**Figure 3.** (a) Share of the warming and PET trends over the Western Eurasian Steppe explained by interactive soil moisture–atmosphere coupling, in the five of seven CMIP6 models where switching it off markedly weakens the trends. (b) Number of models showing a significant post-1990 regime shift in summer SPEI with interactive and with fixed soil moisture. Figure by Daeha Kim, drawn from numbers reported in Piao et al. (2026)._

## What it has done to the land

The shift is visible from space. After the early 2000s, grassland cover declined and barren land expanded: in 2021–2023, grassland was about 5% smaller and barren land nearly 26% larger than the pre-2010 average. Gross primary productivity in croplands and grasslands has dropped to anomalies beyond two standard deviations, so the region now takes up less carbon. Heatwave days have increased across the whole domain, and the region has become a hotspot for flash droughts and concurrent drought–heatwave events. The record-breaking heatwave of 2010 over Eastern Europe and western Russia (Barriopedro et al. 2011) happened in this regime; the paper notes that such compound events have brought heat deaths, wildfires and, through lost grain harvests, a global spike in food prices.

## The outlook

Projections from all three ensembles agree that summer drought in the steppe will intensify as temperatures rise under most future scenarios. The only partial exception is the low-emission RCP2.6 scenario in the MPI ensemble, which roughly reaches carbon neutrality by mid-century. Even there, drying fluctuates but does not return to pre-1990 conditions within the simulation period.

The authors draw two conclusions. First, regional hydroclimate may respond more slowly than global temperature, because land–atmosphere feedbacks and ecological change (lost vegetation, bare soil) carry inertia. Stabilizing global temperature is essential, but it may not quickly restore the water balance of vulnerable drylands. Second, the steppe may be an early warning for other mid-latitude drylands in the Northern Hemisphere, where the same feedback could trigger similar shifts. A comparable abrupt shift to hotter and drier conditions has already been reported for inner East Asia, covering Mongolia and northern China (Zhang et al. 2020).

The authors are careful about one point. They describe a regime shift, not a proven irreversible tipping point: whether the steppe could recover under different emission pathways remains uncertain. What the observations and projections show is that the dry state has persisted through every period they examined.

## What it means for adaptation

The paper's own policy message is short: anticipating and managing such shifts should be a central focus of climate policy, and cutting emissions remains necessary but will not be sufficient on its own. It does not propose specific adaptation measures. The points below are my reading as a hydrologist of what follows from the results, not the authors' recommendations.

**Plan for the new regime, not for a return to the old one.** Water allocation, reservoir operation and crop insurance in such regions are usually designed around a long-term average. After a regime shift, the average of 1961–1990 describes a climate that no longer exists. This is nonstationarity in its sharpest form (Milly et al. 2008): design statistics should be estimated from the post-shift period, or from projections, and revised as the record grows.

**Watch the land, not only the rain.** In this paper the land surface drives the shift. Soil moisture, evapotranspiration and indicators of land–atmosphere coupling such as the Bowen ratio rose or fell years before the regime shift was statistically detectable. Satellite soil moisture and evaporation products are good enough now to monitor these quantities in operational drought systems.

**Prepare for compound events.** Heatwaves and droughts in the steppe now arrive together and intensify each other. Early warning systems that treat heat and drought separately will underestimate the risk to crops, health and wildfire.

**Keep water in the soil.** Because the feedback runs through soil moisture and vegetation, land management that protects ground cover and soil water (preventing overgrazing, keeping crop residue, restoring degraded grassland) works with the same physics that drives the shift. Whether it can weaken the feedback at a regional scale has not been tested, and this paper does not test it. It would be a valuable experiment for land surface models.

## Bottom line

The Western Eurasian Steppe moved into a hotter, drier summer climate in the 1990s and 2000s and has stayed there. Global warming supplied the background drying, an atmospheric wave train amplified it, and the soil moisture feedback turned a fast change into a persistent one. Models project more drying under most scenarios, with only partial relief even under strong mitigation. For hydrologists, the lesson is that the land surface is not a passive recipient of climate change: in water-limited regions it can push the climate into a new state and hold it there.

**Questions to think about**

1. SPEI uses PET, which rises with temperature. How would the drying trend look with a drought index based on actual evapotranspiration or soil moisture, and why might the answers differ?
2. If a region's climate shifted around 2006, how many post-shift years would you need before estimating a new 100-year drought with confidence?
3. Which semiarid regions in East Asia have the strong land–atmosphere coupling that would make a similar shift possible, and what would you monitor there?

---

**한 줄 요약 (Korean summary).** Piao 등(2026, 『Nature Geoscience』)은 우크라이나에서 카자흐스탄에 이르는 서유라시아 스텝 지역이 1990년대 이후 더 덥고 건조한 기후 체제로 급격히 바뀌었다고 보고했다. 1991–2020년 이 지역의 여름 SPEI 감소 추세(−0.43/10년)는 북반구에서 가장 컸고, 1992–1993년에 전환점이, 2006년경에 체제 전환이 나타났으며, 2024년까지 회복의 징후가 없다. 1992–2010년 기온 상승률은 10년에 0.63°C로 북반구 육지 평균의 약 두 배였고, 증발 수요(PET) 증가가 건조화를 약 58% 더 강하게 만들었다. 원인은 세 가지다. 지구온난화가 배경 건조화(관측 추세의 약 절반)를 만들고, 내부 변동성인 유라시아 파동열(wave train)이 이를 증폭했으며, 토양수분–기온 되먹임이 건조한 상태를 고착시켰다. 토양수분을 고정한 모델 실험에서는 급격한 전환이 나타나지 않았다(7개 모델 중 0개, 되먹임을 허용하면 5개). 그 결과 초지는 약 5% 줄고 나지는 약 26% 늘었으며 식생 생산성도 크게 떨어졌다. 미래 전망에서는 대부분의 시나리오에서 건조화가 심해지고, 탄소중립에 가까운 RCP2.6에서도 1990년 이전 상태로 돌아가지 않는다. 저자들은 전지구 기온 안정화가 필수적이지만 건조지역의 물순환을 곧바로 회복시키지는 못할 수 있으므로, 이런 체제 전환을 예측하고 관리하는 것이 기후정책의 중심이 되어야 한다고 강조한다. 수문학자의 입장에서 보면, 과거 평균이 아닌 새로운 체제를 기준으로 물 관리를 계획하고, 강수뿐 아니라 토양수분과 증발산을 감시하며, 폭염과 가뭄을 함께 대비하고, 토양에 물을 붙잡아 두는 토지 관리가 필요하다.

---

**References**

Piao, J., Kug, J.-S., Chen, W., Sung, M.-K., Chen, S., Wang, Z., Cai, Q., & Lee, D. (2026). An abrupt shift towards a hotter and drier climate regime in the Western Eurasian Steppe. _Nature Geoscience_. [https://doi.org/10.1038/s41561-026-02125-8](https://doi.org/10.1038/s41561-026-02125-8)

Barriopedro, D., Fischer, E. M., Luterbacher, J., Trigo, R. M., & García-Herrera, R. (2011). The hot summer of 2010: redrawing the temperature record map of Europe. _Science_, 332, 220–224. [https://doi.org/10.1126/science.1201224](https://doi.org/10.1126/science.1201224)

Deser, C., Lehner, F., Rodgers, K. B., Ault, T., Delworth, T. L., DiNezio, P. N., et al. (2020). Insights from Earth system model initial-condition large ensembles and future prospects. _Nature Climate Change_, 10, 277–286. [https://doi.org/10.1038/s41558-020-0731-2](https://doi.org/10.1038/s41558-020-0731-2)

Lenton, T. M., Held, H., Kriegler, E., Hall, J. W., Lucht, W., Rahmstorf, S., & Schellnhuber, H. J. (2008). Tipping elements in the Earth's climate system. _Proceedings of the National Academy of Sciences_, 105, 1786–1793. [https://doi.org/10.1073/pnas.0705414105](https://doi.org/10.1073/pnas.0705414105)

Milly, P. C. D., Betancourt, J., Falkenmark, M., Hirsch, R. M., Kundzewicz, Z. W., Lettenmaier, D. P., & Stouffer, R. J. (2008). Stationarity is dead: whither water management? _Science_, 319, 573–574. [https://doi.org/10.1126/science.1151915](https://doi.org/10.1126/science.1151915)

Miralles, D. G., Teuling, A. J., van Heerwaarden, C. C., & Vilà-Guerau de Arellano, J. (2014). Mega-heatwave temperatures due to combined soil desiccation and atmospheric heat accumulation. _Nature Geoscience_, 7, 345–349. [https://doi.org/10.1038/ngeo2141](https://doi.org/10.1038/ngeo2141)

Seneviratne, S. I., Corti, T., Davin, E. L., Hirschi, M., Jaeger, E. B., Lehner, I., Orlowsky, B., & Teuling, A. J. (2010). Investigating soil moisture–climate interactions in a changing climate: a review. _Earth-Science Reviews_, 99, 125–161. [https://doi.org/10.1016/j.earscirev.2010.02.004](https://doi.org/10.1016/j.earscirev.2010.02.004)

Vicente-Serrano, S. M., Beguería, S., & López-Moreno, J. I. (2010). A multiscalar drought index sensitive to global warming: the Standardized Precipitation Evapotranspiration Index. _Journal of Climate_, 23, 1696–1718. [https://doi.org/10.1175/2009JCLI2909.1](https://doi.org/10.1175/2009JCLI2909.1)

Zhang, P., Jeong, J.-H., Yoon, J.-H., Kim, H., Wang, S.-Y. S., Linderholm, H. W., Fang, K., Wu, X., & Chen, D. (2020). Abrupt shift to hotter and drier climate over inner East Asia beyond the tipping point. _Science_, 370, 1095–1099. [https://doi.org/10.1126/science.abb3368](https://doi.org/10.1126/science.abb3368)

_All three figures are original. The Python scripts that produce them are available on GitHub: [Figure 1](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-22-steppe-drying.py), [Figure 2](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-22-steppe-feedback.py), [Figure 3](https://github.com/daehakim-waterlab/daehakim-waterlab.github.io/blob/main/scripts/blog/2026-10-22-steppe-coupling.py)._
