---
layout: default
title: Infrastructures
permalink: /infrastructures/
---

<section class="container section">
  <p class="eyebrow">Research ecosystem</p>
  <h1>Infrastructures</h1>

  {% if site.data.infrastructures.size > 0 %}
    <div class="card-grid">
      {% for infrastructure in site.data.infrastructures %}
        <article class="card">
          <h2>{{ infrastructure.name | default: infrastructure.title | default: infrastructure.id }}</h2>

          {% if infrastructure.description %}
            <p>{{ infrastructure.description }}</p>
          {% endif %}
        </article>
      {% endfor %}
    </div>
  {% else %}
    <p>
      Infrastructure information is not yet available in the portal dataset.
    </p>
  {% endif %}
</section>
