{% extends 'placement/base.html' %}
{% block title %}Feedback{% endblock %}

{% block content %}
<span class="eyebrow">Raise a challenge</span>
<h1>Feedback to the TPO</h1>
<p class="muted">Facing trouble with an exam or interview? Let the placement office know.</p>

<form method="post" class="card">
  {% csrf_token %}
  <div class="field">
    <label for="{{ form.job.id_for_label }}">{{ form.job.label }}</label>
    {{ form.job }}
    {{ form.job.errors }}
  </div>
  <div class="field">
    <label for="{{ form.message.id_for_label }}">What happened?</label>
    {{ form.message }}
    {{ form.message.errors }}
  </div>
  <button type="submit" class="btn btn-accent">Submit feedback</button>
</form>

<h2 style="margin-top:2rem;">Your feedback history</h2>
{% if history %}
  {% for f in history %}
    <div class="card">
      <div class="card-header-row">
        <span class="text-mono muted">{{ f.created_at|date:"d M Y, H:i" }}{% if f.job %} · {{ f.job.title }}{% endif %}</span>
        {% if f.resolved %}<span class="stamp stamp-selected">Resolved</span>{% else %}<span class="stamp stamp-pending">Pending</span>{% endif %}
      </div>
      <p>{{ f.message }}</p>
      {% if f.tpo_response %}
        <hr class="divider">
        <p class="muted"><strong>TPO response:</strong> {{ f.tpo_response }}</p>
      {% endif %}
    </div>
  {% endfor %}
{% else %}
  <p class="muted">No feedback submitted yet.</p>
{% endif %}
{% endblock %}
