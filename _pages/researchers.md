---
layout: default
title: Researchers
permalink: /researchers/
---

<section class="container section">

  <p class="eyebrow">Scientific profiles</p>
  <h1>Researchers</h1>

  {% assign researchers = site.data.researchers | sort: "name" %}

  <div class="card-grid">

    {% for researcher in researchers %}

      {% assign institution = site.data.institutions
        | where: "id", researcher.institution_id
        | first %}

      {% assign contributions = site.data.contributions
        | where: "researcher_id", researcher.id %}

      <article class="card researcher-card">

        <h2>
          <a href="{{ '/researchers/' | append: researcher.id | append: '/' | relative_url }}">
            {{ researcher.name }}
          </a>
        </h2>

        {% if institution %}
        <p>
          <strong>{{ institution.short_name }}</strong>
        </p>
        {% endif %}

        {% assign topic_codes = "" | split: "" %}

        {% for contribution in contributions %}
          {% assign topic = site.data.topics
            | where: "id", contribution.topic_id
            | first %}

          {% if topic %}
            {% assign topic_codes = topic_codes | push: topic.code %}
          {% endif %}
        {% endfor %}

        {% if topic_codes.size > 0 %}
        <p>
          <strong>Topics:</strong><br>
          {{ topic_codes | uniq | join: ", " }}
        </p>
        {% endif %}

        {% assign capability_names = "" | split: "" %}

        {% for contribution in contributions %}
          {% for capability_id in contribution.capability_ids %}
            {% assign capability = site.data.capabilities
              | where: "id", capability_id
              | first %}

            {% if capability %}
              {% assign capability_names = capability_names | push: capability.name %}
            {% endif %}
          {% endfor %}
        {% endfor %}

        {% if capability_names.size > 0 %}
        <p>
          <strong>Capabilities:</strong><br>
          {{ capability_names | uniq | join: ", " }}
        </p>
        {% endif %}

      </article>

    {% endfor %}

  </div>

</section>
