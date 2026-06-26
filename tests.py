{% extends 'placement/base.html' %}
{% block title %}Recommendations{% endblock %}

{% block content %}
<span class="eyebrow">K-Nearest-Neighbours match</span>
<h1>Jobs matched to your skills</h1>
<p class="muted">
  Your skills: {% for s in profile.skills.all %}<span class="chip">{{ s.name }}</span>{% endfor %}
  {% if not profile.skills.all %}<span class="muted">none yet — </span><a href="{% url 'student_profile_edit' %}">add some</a>{% endif %}
</p>

{% if recommendations %}
  {% for rec in recommendations %}
    <div class="card" style="display:flex; gap:1.2rem; align-items:flex-start;">
      <div class="match-badge">
        <span class="pct">{{ rec.match_percent }}%</span>
        <span class="pct-label">match</span>
      </div>
      <div style="flex:1;">
        <div class="card-header-row" style="margin-bottom:0.4rem;">
          <h3 style="margin:0;">{{ rec.job.title }}</h3>
          <span class="text-mono muted">Job #{{ rec.job.id }}</span>
        </div>
        <p class="muted" style="margin:0 0 0.6rem;">{{ rec.job.company.display_name }} · {{ rec.job.salary }} · apply by {{ rec.job.last_date }}</p>
        <p>{{ rec.job.description|truncatewords:35 }}</p>
        <div style="margin-bottom:0.8rem;">
          {% for s in rec.job.required_skills.all %}<span class="chip">{{ s.name }}</span>{% endfor %}
        </div>
        <a href="{% url 'student_apply_job' rec.job.id %}" class="btn btn-accent btn-sm">Apply &amp; take test</a>
      </div>
    </div>
  {% endfor %}
{% else %}
  <div class="empty-state card">
    <h3>No matches right now</h3>
    <p>Either there are no open roles that overlap with your skills, or you've already applied to every match. Check back after companies post new roles, or broaden your skills list.</p>
  </div>
{% endif %}
{% endblock %}
