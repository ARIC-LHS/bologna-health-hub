---
layout: default
title: Topics
permalink: /topics/
---

<section class="container section">

  <p class="eyebrow">
    Horizon Europe · Cluster 1 Health · Calls 2027
  </p>

  <h1>Topics</h1>

  <p class="lede">
    Explore the Horizon Europe Cluster 1 Health 2027 topics covered by
    the Bologna Metropolitan Health Research Hub.
  </p>

  <p>
    Each topic connects the call with relevant researchers, their
    proposed scientific contributions and the capabilities available
    across the Bologna metropolitan research ecosystem.
  </p>


  {% for destination in site.data.destinations %}

    {% assign destination_topics = site.data.topics
      | where: "destination", destination.id %}

    {% if destination_topics.size > 0 %}

      <section class="topic-destination">

        <p class="eyebrow">
          Destination {{ destination.id }}
        </p>

        <h2>{{ destination.name }}</h2>

        <div class="card-grid">

          {% for topic in destination_topics %}

            {% assign matches = site.data.contributions
              | where: "topic_id", topic.id %}

            <article class="card topic-card">

              <p class="topic-meta">
                <strong>{{ topic.action_type }}</strong>
                ·
                {{ matches.size }}
                {% if matches.size == 1 %}
                  Bologna research profile
                {% else %}
                  Bologna research profiles
                {% endif %}
              </p>

              <h3>
                <a href="{{ '/topics/' | append: topic.id | append: '/' | relative_url }}">
                  {{ topic.code }}
                </a>
              </h3>

              <p>
                {{ topic.title }}
              </p>

             {% assign capability_string = "|" %}

{% for contribution in matches %}
  {% for capability_id in contribution.capability_ids %}

    {% capture capability_token %}|{{ capability_id }}|{% endcapture %}

    {% unless capability_string contains capability_token %}
      {% capture capability_string %}{{ capability_string }}{{ capability_id }}|{% endcapture %}
    {% endunless %}

  {% endfor %}
{% endfor %}

{% assign topic_capabilities = capability_string | split: "|" %}

{% if topic_capabilities.size > 1 %}

  <ul class="tag-list capability-tags">

    {% for capability_id in topic_capabilities %}

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

              <p>
  <a href="{{ '/topics/' | append: topic.id | append: '/' | relative_url }}">
    Explore relevant profiles →
  </a>
</p>

            </article>

          {% endfor %}

        </div>

      </section>

    {% endif %}

  {% endfor %}

{% include contact-gate.html %}

</section>