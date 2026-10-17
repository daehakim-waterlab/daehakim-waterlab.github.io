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

I have worked in water resources since starting graduate school in 2005. For more than 20 years, that work has taken me from Korea University and Korea's Hydrological Survey Center to the Utah Water Research Laboratory at Utah State University, and then to the APEC Climate Center in Busan, before I joined Jeonbuk National University in 2020. Along the way I have worked with hydrologists, climate scientists, and water managers in Korea, the United States, and Southeast Asia on one recurring question: how a changing climate affects water, and how we can manage water better in response.

#### Education

- Ph.D., Civil and Environmental Engineering, Utah State University, Logan, Utah, USA, 2015
- M.Sc., Civil and Environmental Engineering, Korea University, Seoul, Korea, 2007
- B.Sc., Civil Engineering, Korea University, Seoul, Korea, 2005

#### Professional experience

- **2020–present** Associate Professor, Department of Civil Engineering, Jeonbuk National University
- **2015–2020** Research Fellow, APEC Climate Center, Busan, Korea
- **2011–2015** Research Assistant, Utah Water Research Laboratory, Utah State University, USA
- **2007–2010** Researcher, Hydrological Survey Center, Goyang, Korea

#### Editorial service

- Editor, _Scientific Reports_
- Editor, _Advances in Meteorology_
- Editor, _Journal of Korea Water Resources Association_

{% if site.data.people.members.size > 0 %}

## Lab members

<ul>
{% for person in site.data.people.members %}
  <li><strong>{{ person.name }}</strong>{% if person.role %}, {{ person.role }}{% endif %}{% if person.since %} (since {{ person.since }}){% endif %}{% if person.topic %}. {{ person.topic }}{% endif %}{% if person.scholar %} · <a href="{{ person.scholar }}">Google Scholar</a>{% endif %}</li>
{% endfor %}
</ul>
{% endif %}

{% if site.data.people.alumni.size > 0 %}

## Alumni

<ul>
{% for person in site.data.people.alumni %}
  <li><strong>{{ person.name }}</strong>{% if person.degree %}, {{ person.degree }}{% endif %}{% if person.now %}. Now {{ person.now }}{% endif %}</li>
{% endfor %}
</ul>
{% endif %}

Interested in joining? See [Join us](/join/).
