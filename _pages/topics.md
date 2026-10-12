---
layout: default
title: Topics
permalink: /topics/
---

<div class="container">
  <h1>Topics</h1>

  <div class="card-grid">
    {% for topic in site.data.topics %}
      <article class="card topic-card">
        <h2>
          {{ '/topics/' | append: topic.id | append: '/' | relative_url }}
            {{ topic.code }}
          </a>
        </h2>

        <p>{{ topic.title }}</p>
      </article>
    {% endfor %}
  </div>
</div>