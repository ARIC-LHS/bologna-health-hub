---
layout: default
title: Capabilities
permalink: /capabilities/
---

<section class="container section">
  <p class="eyebrow">Scientific capabilities</p>
  <h1>Capabilities</h1>

  <div class="card-grid">
    {% for capability in site.data.capabilities %}
      <article class="card" id="{{ capability.id }}">
        <h2>{{ capability.name | default: capability.title | default: capability.id }}</h2>

        {% if capability.description %}
          <p>{{ capability.description }}</p>
        {% endif %}
      </article>
    {% endfor %}
  </div>
</section>
