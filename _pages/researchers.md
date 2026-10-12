---
layout: default
title: Researchers
permalink: /researchers/
---

<div class="container">
  <h1>Researchers</h1>

  {% assign researchers = site.data.researchers | sort: "name" %}

  <div class="card-grid">
    {% for researcher in researchers %}
      <article class="card researcher-card">
        <h2>
          {{ '/researchers/' | append: researcher.id | append: '/' | relative_url }}
            {{ researcher.name }}
          </a>
        </h2>

        {% if researcher.institution_id %}
          <p>{{ researcher.institution_id }}</p>
        {% endif %}
      </article>
    {% endfor %}
  </div>
</div>