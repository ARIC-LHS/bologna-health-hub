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

 {% assign sorted_researchers = site.data.researchers | sort: "name" %}

  <article class="card" id="{{ capability.id }}">
    <h2>{{ capability.name | default: capability.title | default: capability.id }}</h2>

    <p>
      {{ researcher_ids.size }} researchers
    </p>
<ul>

{% assign sorted_researchers = site.data.researchers | sort: "name" %}

{% for researcher in sorted_researchers %}

  {% assign researcher_match = matches
    | where: "researcher_id", researcher.id
    | first %}

  {% if researcher_match %}
    <li>
      {{ '/researchers/' | append: researcher.id | append: '/' | relative_url }}
        {{ researcher.name }}
      </a>
    </li>
  {% endif %}

{% endfor %}

 </ul>

{% assign topic_ids = matches
  | map: "topic_id"
  | uniq %}

{% if topic_ids.size > 0 %}

<p><strong>Related topics</strong></p>

<ul>
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
      <p>{{ capability.description }}</p>
    {% endif %}
  </article>

{% endfor %}
  </div>
</section>
