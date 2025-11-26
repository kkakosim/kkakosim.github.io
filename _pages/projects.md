---
layout: page
title: projects
permalink: /projects/
description: Funded projects that I lead or participated in. Look for the Highlights!
nav: true
nav_order: 6
display_categories: [EU, Industry, Education, Qatar]
horizontal: true
---

<!-- pages/projects.md -->
<div class="projects">

  <!-- Importance filter buttons -->
  <div class="project-filters mb-3">
    <button type="button" class="btn btn-sm btn-outline-primary project-filter active" data-importance-filter="all">
      All
    </button>
    <button type="button" class="btn btn-sm btn-outline-primary project-filter" data-importance-filter="1">
      Importance 1
    </button>
    <button type="button" class="btn btn-sm btn-outline-primary project-filter" data-importance-filter="2">
      Importance 2
    </button>
  </div>

{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "year" | reverse %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      <div class="col project-card" data-importance="{{ project.importance | default: 'all' }}">
        {% include projects_horizontal.liquid %}
      </div>
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      <div class="col project-card" data-importance="{{ project.importance | default: 'all' }}">
        {% include projects.liquid %}
      </div>
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->

{% assign sorted_projects = site.projects | sort: "year" | reverse %}

  <!-- Generate cards for each project -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      <div class="col project-card" data-importance="{{ project.importance | default: 'all' }}">
        {% include projects_horizontal.liquid %}
      </div>
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      <div class="col project-card" data-importance="{{ project.importance | default: 'all' }}">
        {% include projects.liquid %}
      </div>
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>

<script>
  // Simple client-side filter for project importance
  document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.project-filter');
    const cards = document.querySelectorAll('.project-card');

    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        const filter = btn.getAttribute('data-importance-filter');

        // active button styling
        buttons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        cards.forEach(card => {
          const importance = card.getAttribute('data-importance');
          if (filter === 'all' || importance === filter) {
            card.style.display = '';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  });
</script>
