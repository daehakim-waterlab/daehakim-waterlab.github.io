---
layout: page
title: Projects
permalink: /projects/
description: Funded research projects, ongoing and completed.
nav: true
nav_order: 4
---

{% assign this_year = site.time | date: "%Y" | plus: 0 %}
{% assign projects = site.data.projects | sort: "start" | reverse %}

{% for section in (1..2) %}
{% if section == 1 %}{% assign heading = "Ongoing" %}{% else %}{% assign heading = "Completed" %}{% endif %}

<h2>{{ heading }}</h2>

<table class="table table-sm table-borderless">
  <thead>
    <tr><th>Project</th><th>Funding agency</th><th style="white-space: nowrap">Period</th></tr>
  </thead>
  <tbody>
  {% for p in projects %}
    {% assign ongoing = false %}
    {% if p.end >= this_year %}{% assign ongoing = true %}{% endif %}
    {% if section == 1 and ongoing == false %}{% continue %}{% endif %}
    {% if section == 2 and ongoing %}{% continue %}{% endif %}
    <tr>
      <td>{{ p.title }}</td>
      <td>{{ p.funder }}</td>
      <td style="white-space: nowrap">{% if p.start == p.end %}{{ p.start }}{% else %}{{ p.start }}–{{ p.end }}{% endif %}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
{% endfor %}
