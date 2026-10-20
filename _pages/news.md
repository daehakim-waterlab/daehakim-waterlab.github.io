---
layout: page
title: News
permalink: /news/
description: All lab news, newest first.
---

{%- comment -%} Archive of every item in _news/, grouped by year (Home shows only the latest few). {%- endcomment -%}
{% assign news_by_year = site.news | reverse | group_by_exp: "item", "item.date | date: '%Y'" %}

<div class="news news-archive">
{% for year in news_by_year %}
  <h2 class="news-year">{{ year.name }}</h2>
  <table class="table table-sm table-borderless">
    {% for item in year.items %}
    <tr>
      <th scope="row" class="news-date">{{ item.date | date: '%b %-d' }}</th>
      <td>
        {% if item.inline %}
          {{ item.content | remove: '<p>' | remove: '</p>' | emojify }}
        {% else %}
          <a class="news-title" href="{{ item.url | relative_url }}">{{ item.title }}</a>
        {% endif %}
      </td>
    </tr>
    {% endfor %}
  </table>
{% endfor %}
</div>
