---
layout: default
title: Bologna Metropolitan Health Research Hub
permalink: /
---

<section class="hero">
  <div class="container">
    <p class="eyebrow">Horizon Europe · Cluster 1 Health</p>

    <h1>Bologna Metropolitan Health Research Hub</h1>

    <p class="lede">
      Scientific matchmaking portal connecting Horizon Europe Cluster 1 Health topics
      with research expertise, capabilities and infrastructures across the Bologna
      metropolitan research ecosystem.
    </p>

    <div class="button-row">
      <a class="button" href="{{ '/topics/' | relative_url }}">Explore Topics</a>
      <a class="button button-secondary" href="{{ '/researchers/' | relative_url }}">Explore Researchers</a>
    </div>
  </div>
</section>

<section class="container section">
  <h2>Explore the portal</h2>

  <div class="card-grid">

    <article class="card">
      <h3>Topics</h3>
      <p>
        Browse Horizon Europe Cluster 1 Health topics and explore relevant
        scientific contributions.
      </p>
      <a href="{{ '/topics/' | relative_url }}">Browse Topics</a>
    </article>

    <article class="card">
      <h3>Researchers</h3>
      <p>
        Explore scientific profiles and their possible contributions to
        Cluster 1 Health topics.
      </p>
      <a href="{{ '/researchers/' | relative_url }}">Browse Researchers</a>
    </article>

    <article class="card">
      <h3>Capabilities</h3>
      <p>
        Explore scientific capabilities represented across the research ecosystem.
      </p>
      <a href="{{ '/capabilities/' | relative_url }}">Browse Capabilities</a>
    </article>

  </div>
</section>

<section class="container section">
  {% include caveat.html text=site.disclaimer %}
</section>
