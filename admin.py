{% extends 'placement/base.html' %}
{% block title %}{% if is_update %}Update{% else %}Build{% endif %} profile{% endblock %}

{% block content %}
<span class="eyebrow">Academic &amp; skills profile</span>
<h1>{% if is_update %}Update your profile{% else %}Build your profile{% endif %}</h1>
<p class="muted">This feeds the job-recommendation engine — keep your skills list current.</p>

<form method="post" enctype="multipart/form-data" class="card">
  {% csrf_token %}
  <div class="grid grid-2">
    <div class="field">
      <label for="{{ form.qualification.id_for_label }}">Qualification</label>
      {{ form.qualification }}
      {{ form.qualification.errors }}
    </div>
    <div class="field">
      <label for="{{ form.percentage.id_for_label }}">Percentage / CGPA×10</label>
      {{ form.percentage }}
      {{ form.percentage.errors }}
    </div>
  </div>
  <div class="grid grid-2">
    <div class="field">
      <label for="{{ form.passout_year.id_for_label }}">Passing year</label>
      {{ form.passout_year }}
      {{ form.passout_year.errors }}
    </div>
    <div class="field">
      <label for="{{ form.experience.id_for_label }}">Experience (optional)</label>
      {{ form.experience }}
      {{ form.experience.errors }}
    </div>
  </div>
  <div class="field">
    <label for="{{ form.resume.id_for_label }}">Resume</label>
    {% if form.instance.resume %}
      <div class="help-text">Current file: {{ form.instance.resume.name }}</div>
    {% endif %}
    {{ form.resume }}
    <div class="help-text">{{ form.resume.help_text }}</div>
    {{ form.resume.errors }}
  </div>
  <div class="field">
    <label for="{{ form.skills.id_for_label }}">Skills</label>
    {{ form.skills }}
    <div class="help-text">{{ form.skills.help_text }}</div>
    {{ form.skills.errors }}
  </div>
  {{ form.non_field_errors }}
  <button type="submit" class="btn btn-accent">Save profile</button>
</form>
{% endblock %}
