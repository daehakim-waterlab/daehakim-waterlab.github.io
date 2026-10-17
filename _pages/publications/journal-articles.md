---
layout: page
permalink: /publications/journal-articles/
title: Peer-reviewed Journal Articles
description: Journal articles in reverse chronological order, linked to the publisher's version by DOI.
nav: false
_styles: ".publications .author em { font-weight: 700; font-style: normal; border-bottom: none; }"
---

{% include bib_search.liquid %}

<div class="publications">

{% bibliography --query @article %}

</div>
