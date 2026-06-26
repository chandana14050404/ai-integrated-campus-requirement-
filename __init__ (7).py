{% extends 'placement/base.html' %}
{% block title %}Test — {{ job.title }}{% endblock %}

{% block content %}
<span class="eyebrow">Assessment</span>
<h1>{{ job.title }}</h1>
<p class="muted">{{ job.company.display_name }} · Answer every question, then submit. You need 80% or higher to be marked Selected.</p>

<form method="post" class="card">
  {% csrf_token %}
  {% for field in form %}
    <fieldset>
      <legend style="font-weight:600; margin-bottom:0.5em;">{{ forloop.counter }}. {{ field.label }}</legend>
      {% for choice in field %}
        <div class="radio-option">{{ choice.tag }} <label for="{{ choice.id_for_label }}" style="font-weight:400; margin:0;">{{ choice.choice_label }}</label></div>
      {% endfor %}
      {{ field.errors }}
    </fieldset>
  {% endfor %}
  <button type="submit" class="btn btn-accent">Submit answers</button>
</form>
{% endblock %}
