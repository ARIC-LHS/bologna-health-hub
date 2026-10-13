---
layout: default
title: Infrastructures
permalink: /infrastructures/
---

<section class="container section">

  <p class="eyebrow">
    Research ecosystem
  </p>

  <h1>Research Infrastructures</h1>

  <p>
    Research infrastructures and technology platforms that can support collaborative Horizon Europe Cluster 1 Health projects.
  </p>

  <div class="card-grid">

    {% for infrastructure in site.data.infrastructures %}

    <article class="card" id="{{ infrastructure.id }}">

      <h2>{{ infrastructure.name }}</h2>

      <p>
        <strong>Available across:</strong>
        {{ infrastructure.availability }}
      </p>

      <p>
        {{ infrastructure.description }}
      </p>

    </article>

    {% endfor %}

  </div>

</section>