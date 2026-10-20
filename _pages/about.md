---
layout: about
title: Home
permalink: /
subtitle: Department of Civil Engineering,<br><a href='https://www.jbnu.ac.kr'>Jeonbuk National University</a>

selected_papers: false
social: true

announcements:
  enabled: true
  scrollable: false
  limit: 5

latest_posts:
  enabled: true
  scrollable: false
  limit: 5
---

<style>
  /* Home hero: the lab name and department are HTML text (the page header); the
     illustration (1008x555, aspect 1.816, left edge faded into the box colour) is a text-free
     image beside them on wide screens and below them on narrow ones. The negative top margin
     collapses with the page's 3rem top margin, leaving 34px under the top bar (owner's request). */
  .post > .post-header {
    display: flex; flex-direction: column; justify-content: center;
    min-height: 14.5rem; padding: 2rem calc(14.5rem * 1.816 + 1rem) 2rem 2.5rem; margin: -0.875rem 0 1.75rem; border-radius: 0.75rem;
    background: #f7f1e7 url("/assets/img/home/hero-art.webp?v=2026-10-20c") no-repeat right center / auto 100%;
  }
  .post > .post-header .post-title { font-family: Georgia, "Times New Roman", serif; font-weight: 700; font-size: 2.6rem; line-height: 1.1; color: #2b2a28; margin: 0 0 0.75rem; }
  .post > .post-header .desc { color: #3b3a37; font-size: 1.1rem; margin: 0; }
  .post > .post-header .desc a { color: #0f2439; }
  .post > .post-header .desc a:hover { color: #246bac; }
  /* Section headings ("News", "Latest posts") at body-heading size, each with a rule above it */
  .post article > h2 { font-size: 1.6rem; font-weight: 400; margin-top: 2.5rem; margin-bottom: 0.5rem; padding-top: 1.5rem; border-top: 1px solid var(--global-divider-color); }
  .post article > h2::first-letter { text-transform: uppercase; }
  @media (min-width: 768px) and (max-width: 991.98px) {
    .post > .post-header { min-height: 12.5rem; padding: 1.75rem calc(12.5rem * 1.816 + 0.75rem) 1.75rem 2rem; }
    .post > .post-header .post-title { font-size: 2rem; }
    .post > .post-header .desc { font-size: 1rem; }
  }
  @media (max-width: 767.98px) {
    .post > .post-header { min-height: 0; padding: 1.5rem 1.25rem calc(55.06% + 0.75rem); background-position: center bottom; background-size: 100% auto; }
    .post > .post-header .post-title { font-size: 2rem; }
    .post > .post-header .desc { font-size: 1rem; }
  }
  @media (max-width: 576px) {
    .post > .post-header .post-title { font-size: 1.75rem; }
    .post article > h2 { font-size: 1.4rem; margin-top: 2rem; padding-top: 1.25rem; }
  }
</style>

**We study how water moves between the land and the atmosphere, and how to manage it when the climate and society are both changing.**

The lab is led by [Daeha Kim](/people/), Associate Professor in the Department of Civil Engineering at Jeonbuk National University. We work on evapotranspiration and the land water balance, droughts and flash droughts, climate change adaptation for water infrastructure, streamflow prediction in ungauged basins, climate services for agriculture, and wetlands.

Read more on the [research](/research/) page, see our [publications](/publications/), meet the [people](/people/), or find out how to [join us](/join/).
