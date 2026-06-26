{% extends 'placement/base.html' %}
{% block title %}Post a job{% endblock %}

{% block content %}
<span class="eyebrow">New posting</span>
<h1>Post a job</h1>

<form method="post" class="card">
  {% csrf_token %}
  <div class="field">
    <label for="{{ form.title.id_for_label }}">Job title</label>
    {{ form.title }}
    {{ form.title.errors }}
  </div>
  <div class="field">
    <label for="{{ form.description.id_for_label }}">Description</label>
    {{ form.description }}
    {{ form.description.errors }}
  </div>
  <div class="grid grid-2">
    <div class="field">
      <label for="{{ form.salary.id_for_label }}">Salary</label>
      {{ form.salary }}
      {{ form.salary.errors }}
    </div>
    <div class="field">
      <label for="{{ form.last_date.id_for_label }}">Last date to apply</label>
      {{ form.last_date }}
      {{ form.last_date.errors }}
    </div>
  </div>
  <div class="field">
    <label for="{{ form.required_skills.id_for_label }}">Required skills</label>
    {{ form.required_skills }}
    <div class="help-text">{{ form.required_skills.help_text }}</div>
    {{ form.required_skills.errors }}
  </div>
  {{ form.non_field_errors }}
  <button type="submit" class="btn btn-accent">Post job &amp; add test questions next</button>
</form>
{% endblock %}
