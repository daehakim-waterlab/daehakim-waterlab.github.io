---
layout: page
permalink: /teaching/
title: Teaching
description: Courses in the Department of Civil Engineering, Jeonbuk National University. Each course is introduced in English and Korean.
nav: true
nav_order: 5
dropdown: true
_styles: ".course-description p { margin-bottom: 0.75rem; }"
children:
  - title: Engineering Hydrology
    permalink: /teaching/engineering-hydrology/
  - title: Hydraulics
    permalink: /teaching/hydraulics/
  - title: Physical Hydrology
    permalink: /teaching/physical-hydrology/
  - title: Statistical Hydrology
    permalink: /teaching/statistical-hydrology/
  - title: Terrestrial Hydrometeorology
    permalink: /teaching/terrestrial-hydrometeorology/
  - title: Earth System Science
    permalink: /teaching/earth-system-science/
  - title: A Brief History of Fluid Mechanics and Water Sciences
    permalink: /water-history/
---

<!-- Each course is one file in _teachings/. Online textbooks are separate Jupyter Book sites:
     add `textbook: <url>` to a course's front matter and the link replaces "coming soon". -->

<div class="courses">
  <div class="course-list">
    {% assign courses = site.teachings | sort: "order" %}
    {% for course in courses %}
    <div class="course-item">
      <h3 class="course-title">
        <a href="{{ course.url | relative_url }}">{{ course.title }}</a> <span lang="ko">· {{ course.title_ko }}</span>
      </h3>
      {% if course.graduate %}<div class="course-meta"><span class="course-term">Graduate course</span></div>{% endif %}
      <div class="course-description">
        <p>{{ course.summary_en }}</p>
        <p lang="ko">{{ course.summary_ko }}</p>
        <p>{% if course.textbook %}<a href="{{ course.textbook }}">Online textbook</a>{% else %}Online textbook — coming soon{% endif %}</p>
      </div>
    </div>
    {% endfor %}
  </div>
</div>
