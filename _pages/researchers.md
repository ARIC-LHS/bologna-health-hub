---
layout: default
title: Researchers
permalink: /researchers/
---

# Researchers

{% assign researchers = site.data.researchers | sort: "name" %}

<ul>
{% for researcher in researchers %}
  <li>{{ researcher.name }}</li>
{% endfor %}
</ul>