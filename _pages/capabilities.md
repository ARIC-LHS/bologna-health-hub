---
layout: default
title: Capabilities
permalink: /capabilities/
---

<section class="container section">

  <p class="eyebrow">
    Scientific capabilities
  </p>

  <h1>Capabilities</h1>

  <p class="lede">
    Explore the scientific, clinical, methodological and technological
    capabilities available across the Bologna metropolitan research
    ecosystem for Horizon Europe Cluster 1 Health 2027.
  </p>


  {% assign capabilities = site.data.capabilities | sort: "name" %}


  <div class="card-grid">

    {% for capability in capabilities %}

      {% assign matches = site.data.contributions
        | where_exp: "c", "c.capability_ids contains capability.id" %}

      {% assign researcher_ids = matches
        | map: "researcher_id"
        | uniq %}

      {% assign topic_ids = matches
        | map: "topic_id"
        | uniq %}


      <article class="card capability-index-card" id="{{ capability.id }}">

        <h2>

          <a href="{{ '/capabilities/' | append: capability.id | append: '/' | relative_url }}">
            {{ capability.name | default: capability.title | default: capability.id }}
          </a>

        </h2>


        <p class="capability-index-meta">

          <strong>{{ researcher_ids.size }}</strong>

          {% if researcher_ids.size == 1 %}
            research profile
          {% else %}
            research profiles
          {% endif %}

          <span aria-hidden="true"> · </span>

          <strong>{{ topic_ids.size }}</strong>

          {% if topic_ids.size == 1 %}
            2027 topic
          {% else %}
            2027 topics
          {% endif %}

        </p>


        {% if topic_ids.size > 0 %}

          <ul class="tag-list capability-topic-tags">

            {% for topic_id in topic_ids %}

              {% assign topic = site.data.topics
                | where: "id", topic_id
                | first %}

              {% if topic %}

                <li>
                  <a href="{{ '/topics/' | append: topic.id | append: '/' | relative_url }}">
                    {{ topic.code }}
                  </a>
                </li>

              {% endif %}

            {% endfor %}

          </ul>

        {% endif %}


        {% if capability.description %}

          <p>
            {{ capability.description }}
          </p>

        {% endif %}


        <p class="capability-index-link">

          <a href="{{ '/capabilities/' | append: capability.id | append: '/' | relative_url }}">
            Explore relevant profiles →
          </a>

        </p>

      </article>

    {% endfor %}

  </div>

</section>