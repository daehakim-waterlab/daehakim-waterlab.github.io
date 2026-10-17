---
layout: page
permalink: /people/
title: People
description: Principal investigator, lab members, and alumni.
nav: true
nav_order: 2
---

## Principal investigator

### Daeha Kim

Associate Professor, Department of Civil Engineering, Jeonbuk National University

I am an instructor and researcher focused on scientific and engineering challenges in hydrologic processes and water resources management. Over more than 15 years, I have worked on water-related problems under climatic and socioeconomic uncertainty at a research center and at universities. I have authored and co-authored over 50 peer-reviewed journal articles aimed at practical solutions for water resources management, addressing large-scale drought monitoring, the prediction of water availability at local, regional, and global scales, and strategies for managing water resources under climatic challenges.

I have also worked in international collaborations, including programs with Southeast Asian organizations and official sessions of the Intergovernmental Panel on Climate Change. I share ideas with fellow researchers and students to foster innovation and collaboration, and keep working to bridge scientific research and real-world water issues.

#### Education

- Ph.D., Civil and Environmental Engineering, Utah State University, Logan, Utah, USA, 2015
- M.Sc., Civil and Environmental Engineering, Korea University, Seoul, Korea, 2007
- B.Sc., Civil Engineering, Korea University, Seoul, Korea, 2005

#### Professional experience

- **2020–present** Associate Professor, Department of Civil Engineering, Jeonbuk National University
- **2015–2020** Research Fellow, APEC Climate Center, Busan, Korea
- **2011–2015** Research Assistant, Utah Water Research Laboratory, Utah State University, USA
- **2007–2010** Researcher, Hydrological Survey Center, Goyang, Korea

#### Honors and awards

- Jeonbuk State Governor's Commendation for Construction Revitalization, 2025
- Best Research Paper Award, Korea Water Resources Association, 2024
- Best Research Paper Award, APEC Climate Center, 2019

#### Editorial service

- Editor, _Advances in Meteorology_
- Editor, _Journal of Korea Water Resources Association_

#### Professional activities

- Participant, 42nd and 43rd Sessions of the Intergovernmental Panel on Climate Change (IPCC)
- Participant, 4th and 5th Board of Council Meetings, Asia Water Council
- Board committee member: Korea Water Resources Association; Korean Wetlands Society; Korean Society of Climate Change Research
- Member: American Geophysical Union; European Geosciences Union; European Meteorological Society; Korean Meteorological Society

{% if site.data.people.members.size > 0 %}

## Lab members

<ul>
{% for person in site.data.people.members %}
  <li><strong>{{ person.name }}</strong>{% if person.role %}, {{ person.role }}{% endif %}{% if person.since %} (since {{ person.since }}){% endif %}{% if person.topic %}. {{ person.topic }}{% endif %}</li>
{% endfor %}
</ul>
{% endif %}

{% if site.data.people.alumni.size > 0 %}

## Alumni

<ul>
{% for person in site.data.people.alumni %}
  <li><strong>{{ person.name }}</strong>{% if person.degree %}, {{ person.degree }}{% endif %}{% if person.now %}. Now: {{ person.now }}{% endif %}</li>
{% endfor %}
</ul>
{% endif %}

Interested in joining? See [Join us](/join/).
