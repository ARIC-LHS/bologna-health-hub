---
layout: default
title: Researchers
permalink: /researchers/
---

<h1>Researchers</h1>

<div class="card-grid">

{% for researcher in site.data.researchers %}

  <article class="card">

    <h2>{{ researcher.name }}</h2>

    <p>{{ researcher.institution_id }}</p>

  </article>

{% endfor %}

</div>