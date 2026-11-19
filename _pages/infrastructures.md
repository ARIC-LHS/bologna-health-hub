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

  <p class="lede">
    Explore research infrastructures and technology platforms across
    the Bologna metropolitan research ecosystem that can support
    collaborative Horizon Europe Cluster 1 Health projects.
  </p>

  <p>
    Resources are organised into eight infrastructure families,
    highlighting key facilities and platforms available across UNIBO,
    IRCCS AOUBO, IRCCS IOR and IRCCS ISN.
  </p>


  {% assign sorted_infrastructures = site.data.infrastructures
    | sort: "name" %}


  <div class="card-grid">

    {% for infrastructure in sorted_infrastructures %}

      <article
        class="card infrastructure-card"
        id="{{ infrastructure.id }}"
      >

        <h2>
          {{ infrastructure.name }}
        </h2>


        {% assign availability = infrastructure.availability
          | split: ", " %}

        {% if availability.size > 0 %}

          <ul class="tag-list infrastructure-institution-tags">

            {% for institution_name in availability %}

              <li>
                {{ institution_name }}
              </li>

            {% endfor %}

          </ul>

        {% endif %}


        <p>
          {{ infrastructure.description }}
        </p>


        {% if infrastructure.facilities
          and infrastructure.facilities.size > 0 %}

          <p class="infrastructure-facility-count">

            <strong>{{ infrastructure.facilities.size }}</strong>

            {% if infrastructure.facilities.size == 1 %}
              key facility or platform
            {% else %}
              key facilities and platforms
            {% endif %}

          </p>


          {% assign sorted_facilities = infrastructure.facilities
            | sort: "name" %}


          <ul class="infrastructure-facility-list">

            {% for facility in sorted_facilities %}

              {% assign institution = site.data.institutions
                | where: "id", facility.institution_id
                | first %}

              <li>

                <strong>
                  {{ facility.name }}
                </strong>

                {% if institution %}

                  <span class="facility-institution">
                    {{ institution.short_name }}
                  </span>

                {% endif %}

              </li>

            {% endfor %}

          </ul>

        {% endif %}

      </article>

    {% endfor %}

  </div>


  <section class="contact-gate infrastructure-contact">

    <p class="eyebrow">
      Infrastructure matchmaking
    </p>

    <h2>
      Interested in a research infrastructure?
    </h2>

    <p>
      Access, availability and project-specific use of research
      infrastructures require direct verification. The ARIC Life &amp;
      Health Sciences team can help identify the most relevant resources
      for a Horizon Europe Health consortium.
    </p>

    <p class="button-row">

      <a class="button" href="mailto:lhs@unibo.it">
        Contact the Life &amp; Health Sciences team
      </a>

    </p>

    <p class="contact-email">
      <a href="mailto:lhs@unibo.it">
        lhs@unibo.it
      </a>
    </p>

  </section>


  {% include caveat.html text=site.disclaimer %}

</section>