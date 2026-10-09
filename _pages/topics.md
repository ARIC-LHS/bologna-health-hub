---
layout: default
title: Topics
permalink: /topics/
---

<h1>Topics</h1>

<div class="card-grid">

{% for topic in site.data.topics %}

  <article class="card">

    <h2>{{ topic.code }}</h2>

    <p>{{ topic.title }}</p>

  </article>

{% endfor %}

</div>