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

  {% assign matches = site.data.contributions
    | where_exp: "c", "c.capability_ids contains capability.id" %}

  {% assign researcher_ids = matches
    | map: "researcher_id"
    | uniq %}

  <article class="card" id="{{ capability.id }}">
    <h2>{{ capability.name | default: capability.title | default: capability.id }}</h2>

    <p>
      {{ researcher_ids.size }} researchers
    </p>

    {% if capability.description %}
      <p>{{ capability.description }}</p>
    {% endif %}
  </article>

{% endfor %}
  </div>
</section>
