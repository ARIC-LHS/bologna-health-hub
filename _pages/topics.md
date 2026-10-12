---
layout: default
title: Topics
permalink: /topics/
---

<section class="container section">
  <p class="eyebrow">Horizon Europe · Cluster 1 Health</p>
  <h1>Topics</h1>

  <div class="card-grid">
    {% for topic in site.data.topics %}
      <article class="card topic-card">
        <h2>
          <a href="{{ '/topics/' | append: topic.id | append: '/' | relative_url }}">
            {{ topic.code }}
          </a>
        </h2>

        <p>{{ topic.title }}</p>
      </article>
    {% endfor %}
  </div>
</section>
