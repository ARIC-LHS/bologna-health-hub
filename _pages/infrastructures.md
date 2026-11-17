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
    Research infrastructures and technology platforms that can support
    collaborative Horizon Europe Cluster 1 Health projects.
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

      {% if infrastructure.facilities and infrastructure.facilities.size > 0 %}

        <h3>Key facilities and platforms</h3>

        <ul>
          {% for facility in infrastructure.facilities %}

            {% assign institution = site.data.institutions
              | where: "id", facility.institution_id
              | first %}

            <li>
              <strong>{{ facility.name }}</strong>
              {% if institution %}
                — {{ institution.short_name }}
              {% endif %}
            </li>

          {% endfor %}
        </ul>

      {% endif %}

    </article>

    {% endfor %}

  </div>

  {% include caveat.html text=site.disclaimer %}

</section>