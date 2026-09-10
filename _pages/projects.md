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
    <button type="button" class="project-filter-btn project-filter active" data-importance-filter="all">
      All
    </button>
    <button type="button" class="project-filter-btn project-filter" data-importance-filter="highlighted">
      Highlighted
    </button>
  </div>

{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "year" | reverse %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">
      {{ category }} [{{ categorized_projects | size }}]
    </h2>
  </a>
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

<style>
/* Use theme variables from _sass/_base and _sass/_themes (minimal override) */
.project-filters {
  margin-bottom: 1rem;
}

/* Base button look – follow site button/link styling */
.project-filter-btn {
  display: inline-block;
  margin-right: 0.5rem;
  padding: 0.25rem 0.75rem;
  border-radius: 999px;
  border: 1px solid var(--border-color, #d0d7de);
  background: var(--bg, transparent);
  color: var(--text-color, inherit);
  font-size: 0.9rem;
  cursor: pointer;
}

/* Hover uses primary color outline from theme */
.project-filter-btn:hover {
  border-color: var(--link-color, #0969da);
  color: var(--link-color, #0969da);
}

/* Active uses filled primary style (similar to primary buttons in theme) */
.project-filter-btn.active {
  background: var(--link-color, #0969da);
  border-color: var(--link-color, #0969da);
  color: #fff;
}
</style>

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
          if (
            filter === 'all' ||
            (filter === 'highlighted' && (importance === '1' || importance === '2'))
          ) {
            card.style.display = '';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  });
</script>
