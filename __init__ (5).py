{% extends 'placement/base.html' %}
{% block title %}Test questions — {{ job.title }}{% endblock %}

{% block content %}
<span class="eyebrow">Job #{{ job.id }} · {{ job.title }}</span>
<h1>Test questions</h1>
<p class="muted">Students must answer these when they apply. 80%+ correct marks them Selected.</p>

<form method="post" class="card">
  {% csrf_token %}
  <div class="field">
    <label for="{{ form.question_text.id_for_label }}">Question</label>
    {{ form.question_text }}
    {{ form.question_text.errors }}
  </div>
  <div class="grid grid-2">
    <div class="field"><label for="{{ form.option_a.id_for_label }}">Option A</label>{{ form.option_a }}</div>
    <div class="field"><label for="{{ form.option_b.id_for_label }}">Option B</label>{{ form.option_b }}</div>
    <div class="field"><label for="{{ form.option_c.id_for_label }}">Option C</label>{{ form.option_c }}</div>
    <div class="field"><label for="{{ form.option_d.id_for_label }}">Option D</label>{{ form.option_d }}</div>
  </div>
  <div class="field">
    <label for="{{ form.correct_option.id_for_label }}">Correct option</label>
    {{ form.correct_option }}
    {{ form.correct_option.errors }}
  </div>
  <button type="submit" class="btn btn-accent">Add question</button>
</form>

<h2>Questions added ({{ questions.count }})</h2>
{% if questions %}
  {% for q in questions %}
    <div class="card">
      <strong>{{ forloop.counter }}. {{ q.question_text }}</strong>
      <ul style="margin:0.5em 0 0; padding-left:1.2em; color:var(--text-muted);">
        <li {% if q.correct_option == 'A' %}style="color:var(--accent-dark); font-weight:600;"{% endif %}>A. {{ q.option_a }}</li>
        <li {% if q.correct_option == 'B' %}style="color:var(--accent-dark); font-weight:600;"{% endif %}>B. {{ q.option_b }}</li>
        <li {% if q.correct_option == 'C' %}style="color:var(--accent-dark); font-weight:600;"{% endif %}>C. {{ q.option_c }}</li>
        <li {% if q.correct_option == 'D' %}style="color:var(--accent-dark); font-weight:600;"{% endif %}>D. {{ q.option_d }}</li>
      </ul>
    </div>
  {% endfor %}
{% else %}
  <p class="muted">No questions yet — students can't take the test until you add at least one.</p>
{% endif %}

<a href="{% url 'company_home' %}" class="btn btn-outline">Done — back to dashboard</a>
{% endblock %}
