---
layout: page
permalink: /research/
title: Research
description: Hydrologic processes and water resources management under climatic and socioeconomic uncertainty.
nav: true
nav_order: 1
toc:
  sidebar: left
---

Our work starts from the physics of the land water and energy balance and carries it through to decisions about water: how much water evaporates, when a dry spell becomes a drought, how much water a river will deliver where nobody measures it, and which adaptation options hold up when the future climate is uncertain. The six themes below overlap. Most projects combine process understanding, observations and climate model data, and an engineering or management question.

Full lists are on the [publications](/publications/) pages; funded work is on the [projects](/projects/) page.

## Evapotranspiration, the complementary relationship, and the Budyko framework

Evapotranspiration links the water and energy balances of the land surface, yet it is rarely measured directly. We work with the complementary relationship (CR) of evaporation, which estimates actual evapotranspiration from routinely available atmospheric data by exploiting the feedback between a drying land surface and the overlying air. A recurring question in our work is how to set the CR parameters, in particular the Priestley–Taylor coefficient, where there are no flux towers or streamflow records to calibrate against.

A second thread connects the CR with the Budyko framework for long-term catchment water balance. Conventional Budyko equations are usually driven with an atmospheric evaporative potential that itself responds to soil moisture deficits. We have shown analytically that a two-parameter Budyko equation effectively corrects this potential to the wet-environment evaporation of the CR, and we have used the Budyko equation to constrain CR parameters for ungauged areas in Australia and for global estimates of terrestrial evapotranspiration.

Representative publications

- Kim, D., and Chun, J. A. (2021). Revisiting a two-parameter Budyko equation with the complementary evaporation principle for proper consideration of surface energy balance. _Water Resources Research_, 57, e2021WR030838. [doi:10.1029/2021WR030838](https://doi.org/10.1029/2021WR030838)
- Kim, D., Choi, M., and Chun, J. A. (2022). Linking the complementary evaporation relationship with the Budyko framework for ungauged areas in Australia. _Hydrology and Earth System Sciences_, 26, 5955–5969. [doi:10.5194/hess-26-5955-2022](https://doi.org/10.5194/hess-26-5955-2022)
- Kim, D., Cho, E., and Chun, J. A. (2024). Constraining the power-function complementary relationship with a steady-state Budyko equation for predicting terrestrial evapotranspiration globally. _Agricultural and Forest Meteorology_, 344, 109808. [doi:10.1016/j.agrformet.2023.109808](https://doi.org/10.1016/j.agrformet.2023.109808)

## Droughts and flash droughts

Most drought indices are built on precipitation, sometimes adjusted by potential evapotranspiration. We track drought through the evaporative side of the water balance instead. The Standardized Evapotranspiration Deficit Index, built on actual evapotranspiration from the Bouchet hypothesis, identifies droughts consistently with established indices without using precipitation data. We have applied evapotranspiration-deficit approaches to historical droughts over the contiguous United States, Uganda, and East Asia, and to drought projections from CMIP6 models.

Rapid-onset flash droughts are a particular focus. Offline drought indices computed from climate model output depend on how atmospheric evaporative demand is formulated, and the standard Penman–Monteith formulation ignores the response of plant stomata to elevated CO₂. We have shown that flash drought projections from evaporative stress and from soil moisture diverge for this reason, and we develop corrected formulations of evaporative demand that bring offline aridity diagnostics closer to Earth system model projections.

Representative publications

- Kim, D., and Rhee, J. (2016). A drought index based on actual evapotranspiration from the Bouchet hypothesis. _Geophysical Research Letters_, 43, 10277–10285. [doi:10.1002/2016GL070302](https://doi.org/10.1002/2016GL070302)
- Kim, D., Chun, J. A., Yeo, J.-H., and Ha, K.-J. (2023). Divergent flash drought risks indicated by evaporative stress and soil moisture projections under warming scenarios. _Environmental Research Letters_, 18, 094023. [doi:10.1088/1748-9326/ace921](https://doi.org/10.1088/1748-9326/ace921)
- Kim, D., and Choi, M. (2026). A structural correction to atmospheric evaporative demand narrows the gap between offline aridity diagnostics and Earth system model projections. _npj Climate and Atmospheric Science_, 9, 34. [doi:10.1038/s41612-025-01306-3](https://doi.org/10.1038/s41612-025-01306-3)

## Climate change adaptation and decision-centric assessment

Water infrastructure is planned and operated on the assumption of a known climate, and projections of future climate remain uncertain. Rather than starting from a few climate scenarios, decision-centric (bottom-up, or scenario-neutral) assessments start from the system: they stress-test a reservoir, a dam, or a river basin across a wide range of climate conditions and ask where its performance becomes unacceptable. Climate information is then used to judge how likely those conditions are.

We have extended this approach in several ways: replacing response surfaces with logistic surfaces that express the risk of system failure, refining flood stress tests to hourly scale with a random cascade model, and evaluating adaptation options such as additional reservoir storage or changed instream-flow management in Korean river basins, including the Geum and Dongjin rivers and the Yongdam Dam.

Representative publications

- Kim, D., Chun, J. A., and Aikins, C. M. (2018). An hourly-scale scenario-neutral flood risk assessment in a mesoscale catchment under climate change. _Hydrological Processes_, 32, 3416–3430. [doi:10.1002/hyp.13273](https://doi.org/10.1002/hyp.13273)
- Kim, D., Eum, H.-I., Kaluarachchi, J. J., and Chun, J. A. (2019). A sensitivity-based analysis for managing storage capacity of a small agricultural reservoir under drying climate. _Agricultural Water Management_, 213, 410–418. [doi:10.1016/j.agwat.2018.10.040](https://doi.org/10.1016/j.agwat.2018.10.040)
- Kim, D., Chun, J. A., and Choi, S. J. (2019). Incorporating the logistic regression into a decision-centric assessment of climate change impacts on a complex river system. _Hydrology and Earth System Sciences_, 23, 1145–1162. [doi:10.5194/hess-23-1145-2019](https://doi.org/10.5194/hess-23-1145-2019)

## Streamflow prediction in ungauged basins and machine learning

Most catchments have no streamflow gauge, so the parameters of a rainfall–runoff model cannot be calibrated where they are needed. We compare ways of transferring information to ungauged sites, such as calibrating a model against regional flow duration curves instead of transferring parameters from neighbouring catchments, and we have applied flow-duration-curve methods to regulated, snowmelt-driven watersheds in the western United States.

More recently we test where machine learning helps and where it does not. Our studies compare conceptual models, machine-learning models, and hybrids that combine the two for daily streamflow in ungauged basins, and evaluate how well tree-based classifiers trained at some locations predict fog at locations and times they have not seen.

Representative publications

- Kim, D., Jung, I. W., and Chun, J. A. (2017). A comparative assessment of rainfall–runoff modelling against regional flow duration curves for ungauged catchments. _Hydrology and Earth System Sciences_, 21, 5647–5661. [doi:10.5194/hess-21-5647-2017](https://doi.org/10.5194/hess-21-5647-2017)
- Kim, D., Kim, E., and Kim, E. (2023). Performance of decision-tree-based ensemble classifiers in predicting fog frequency in ungauged areas. _Weather and Forecasting_, 38, 2379–2393. [doi:10.1175/WAF-D-23-0024.1](https://doi.org/10.1175/WAF-D-23-0024.1)
- Lee, S. C., and Kim, D. (2025). A comparative assessment of a hybrid approach against conventional and machine-learning daily streamflow prediction in ungauged basins. _Journal of Hydrology: Regional Studies_, 62, 102854. [doi:10.1016/j.ejrh.2025.102854](https://doi.org/10.1016/j.ejrh.2025.102854)

## Climate services for agriculture

Seasonal climate forecasts are only useful to farmers if they are translated into decisions about planting, fertilizer, or water. Much of this work began at the APEC Climate Center and continues with partners in Southeast Asia and the Pacific. We couple probabilistic seasonal forecasts with crop models such as AquaCrop to manage climate risks for rainfed rice in Lao PDR, and we study how forecast information can be delivered as a service that supports food security.

Related work uses remote sensing to validate crop models and examines how the agriculture and water sectors are linked, from national water scarcity to the exposure of crop prices and supply chains to droughts elsewhere in the world.

Representative publications

- Kim, D., Chun, J. A., and Inthavong, T. (2021). Managing climate risks in a nutrient-deficient paddy rice field using seasonal climate forecasts and AquaCrop. _Agricultural Water Management_, 256, 107073. [doi:10.1016/j.agwat.2021.107073](https://doi.org/10.1016/j.agwat.2021.107073)
- Park, S., Chun, J. A., Kim, D., and Sitthikone, M. (2022). Climate risk management for the rainfed rice yield in Lao PDR using APCC MME seasonal forecasts. _Agricultural Water Management_, 274, 107976. [doi:10.1016/j.agwat.2022.107976](https://doi.org/10.1016/j.agwat.2022.107976)
- Park, S., Lee, S., Chun, J. A., Leo, P., Kader, M. A., and Kim, D. (2026). Integrating crop simulation and climate service delivery for food security in Pacific Island Countries: a taro case study in Vanuatu. _Climate Services_, 44, 100708. [doi:10.1016/j.cliser.2026.100708](https://doi.org/10.1016/j.cliser.2026.100708)

## Wetlands under climate change

Wetlands store water and carbon and support biodiversity, and their extent depends on the same water and energy balance that controls evapotranspiration. We map where wetlands can exist by combining a topographic wetness index with the climatic water balance, and project how that extent changes under warming. Our results show that present-day wetland identification is robust to how atmospheric evaporative demand is formulated, whereas future projections diverge strongly under high-emission scenarios; accounting for vegetation physiology and land–atmosphere feedbacks moderates the projected wetland loss. We also estimate how much carbon restored wetlands in South Korea could sequester. This work supports a national project on adaptive management practices for wetland ecosystems under climate change.

Representative work

- Kim, D., and Kim, E. (2024). Diverging estimates of future global wetland areas under warming scenarios. European Meteorological Society Annual Meeting 2024, Barcelona, Spain.
- Lee, S., Kim, D., and Jang, S. H. (2026). Quantifying carbon sequestration capacity of potential wetland restoration in South Korea using a high-resolution dynamic vegetation model. European Geosciences Union General Assembly 2026, Vienna, Austria.
- Kim, D., and Kim, E. (in revision). Influence of potential evaporation formulations on global wetland projections derived from a topo–climate index. _Journal of Hydrology_.
