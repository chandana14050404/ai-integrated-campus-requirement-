{% load static %}<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}Campus Placement{% endblock %} · Smart Campus Placement System</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{% static 'placement/css/style.css' %}">
</head>
<body>
<div class="shell">
  <header class="letterhead">
    <div class="letterhead-inner">
      <a class="brand" href="{% url 'index' %}">
        <span class="brand-mark">SCP</span>
        Smart Campus Placement
      </a>
      <nav class="nav-links">
        {% if user.is_authenticated %}
          {% if user.is_student %}
            <a href="{% url 'student_home' %}">Dashboard</a>
            <a href="{% url 'student_recommendations' %}">Recommendations</a>
            <a href="{% url 'student_job_status' %}">Status</a>
            <a href="{% url 'student_feedback' %}">Feedback</a>
          {% elif user.is_company %}
            <a href="{% url 'company_home' %}">Dashboard</a>
            <a href="{% url 'company_post_job' %}">Post a job</a>
          {% elif user.is_tpo %}
            <a href="{% url 'tpo_home' %}">Dashboard</a>
            <a href="{% url 'tpo_students' %}">Students</a>
            <a href="{% url 'tpo_companies' %}">Companies</a>
            <a href="{% url 'tpo_feedback_list' %}">Feedback</a>
          {% endif %}
          <span class="role-chip">{{ user.get_role_display }}</span>
          <form action="{% url 'logout' %}" method="post" style="margin:0;">
            {% csrf_token %}
            <button type="submit" class="btn btn-sm btn-outline" style="border-color:var(--paper); color:var(--paper) !important;">Log out</button>
          </form>
        {% else %}
          <a href="{% url 'login' %}">Log in</a>
          <a href="{% url 'register' %}" class="btn btn-sm btn-accent">Sign up</a>
        {% endif %}
      </nav>
    </div>
  </header>

  {% block prebody %}{% endblock %}

  <main class="container{% block container_modifier %}{% endblock %}">
    {% if messages %}
      {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">{{ message }}</div>
      {% endfor %}
    {% endif %}
    {% block content %}{% endblock %}
  </main>

  <footer class="ledger-footer">
    AI-Integrated Recruitment &amp; Campus Placement Management Platform — Company · Student · TPO
  </footer>
</div>
</body>
</html>
