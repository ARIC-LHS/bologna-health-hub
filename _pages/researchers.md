---
layout: default
title: Researchers
permalink: /researchers/
---

<section class="container section">

  <p class="eyebrow">
    Scientific profiles
  </p>

  <h1>Researchers</h1>

  <p class="lede">
    Explore 75 researchers and clinical experts from the Bologna
    metropolitan research ecosystem contributing to Horizon Europe
    Cluster 1 Health 2027 topics.
  </p>


  {% assign researchers = site.data.researchers
    | sort: "sort_name" %}


  <div class="card-grid">

    {% for researcher in researchers %}

      {% assign institution = site.data.institutions
        | where: "id", researcher.institution_id
        | first %}

      {% assign contributions = site.data.contributions
        | where: "researcher_id", researcher.id %}


      <article class="card researcher-card researcher-index-card">

        <h2>

          <a href="{{ '/researchers/' | append: researcher.id | append: '/' | relative_url }}">
            {{ researcher.name }}
          </a>

        </h2>


        {% if institution %}

          <p class="researcher-institution">
            {{ institution.short_name }}
          </p>

        {% endif %}


        <p class="researcher-topic-count">

          <strong>{{ contributions.size }}</strong>

          {% if contributions.size == 1 %}
            topic contribution
          {% else %}
            topic contributions
          {% endif %}

        </p>


        {% if contributions.size > 0 %}

          <ul class="tag-list researcher-topic-tags">

            {% for contribution in contributions %}

              {% assign topic = site.data.topics
                | where: "id", contribution.topic_id
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


        {% assign capability_string = "|" %}

        {% for contribution in contributions %}

          {% for capability_id in contribution.capability_ids %}

            {% capture capability_token %}|{{ capability_id }}|{% endcapture %}

            {% unless capability_string contains capability_token %}

              {% capture capability_string %}{{ capability_string }}{{ capability_id }}|{% endcapture %}

            {% endunless %}

          {% endfor %}

        {% endfor %}

        {% assign researcher_capabilities = capability_string
          | split: "|" %}


        {% if researcher_capabilities.size > 1 %}

          <ul class="tag-list capability-tags">

            {% for capability_id in researcher_capabilities %}

              {% assign capability_id = capability_id | strip %}

              {% if capability_id != empty %}

                {% assign capability = site.data.capabilities
                  | where: "id", capability_id
                  | first %}

                {% if capability %}

                  <li class="capability-tag capability-tag--{{ capability.id }}">
                    {{ capability.name }}
                  </li>

                {% endif %}

              {% endif %}

            {% endfor %}

          </ul>

        {% endif %}


        <p class="researcher-profile-link">

          <a href="{{ '/researchers/' | append: researcher.id | append: '/' | relative_url }}">
            View profile →
          </a>

        </p>

      </article>

    {% endfor %}

  </div>

  {% include contact-gate.html %}

</section>
