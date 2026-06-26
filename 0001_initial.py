{% extends 'placement/base.html' %}
{% block title %}Student dashboard{% endblock %}

{% block content %}
<span class="eyebrow">Student desk</span>
<h1>Welcome, {{ user.first_name|default:user.username }}</h1>

{% if not profile %}
  <div class="card">
    <h3>Finish your profile to get matched</h3>
    <p class="muted">Add your academics, skills and resume so the recommendation engine has something to work with.</p>
    <a href="{% url 'student_profile_edit' %}" class="btn btn-accent">Complete profile</a>
  </div>
{% else %}
  <div class="grid grid-3">
    <div class="stat-tile">
      <span class="num">{{ profile.skills.count }}</span>
      <div class="label">Skills listed</div>
    </div>
    <div class="stat-tile">
      <span class="num">{{ recent_applications|length }}</span>
      <div class="label">Recent applications</div>
    </div>
    <div class="stat-tile">
      <span class="num">{{ profile.latest_score|floatformat:0 }}%</span>
      <div class="label">Last test score</div>
    </div>
  </div>

  <div class="grid grid-2" style="margin-top:1.4rem;">
    <div class="card">
      <h3>Your skills</h3>
      {% if profile.skills.all %}
        {% for s in profile.skills.all %}<span class="chip">{{ s.name }}</span>{% endfor %}
      {% else %}
        <p class="muted">No skills added yet.</p>
      {% endif %}
      <hr class="divider">
      <a href="{% url 'student_profile_edit' %}" class="btn btn-outline btn-sm">Edit profile</a>
      <a href="{% url 'student_recommendations' %}" class="btn btn-accent btn-sm">View recommendations</a>
    </div>

    <div class="card">
      <h3>Recent applications</h3>
      {% if recent_applications %}
        <table class="ledger">
          <thead><tr><th>Job</th><th>Score</th><th>Status</th></tr></thead>
          <tbody>
          {% for app in recent_applications %}
            <tr>
              <td>{{ app.job.title }}</td>
              <td class="text-mono">{{ app.score_percent }}%</td>
              <td>
                {% if app.status == 'SELECTED' %}
                  <span class="stamp stamp-selected">Selected</span>
                {% else %}
                  <span class="stamp stamp-rejected">Rejected</span>
                {% endif %}
              </td>
            </tr>
          {% endfor %}
          </tbody>
        </table>
      {% else %}
        <p class="muted">You haven't applied to anything yet.</p>
      {% endif %}
    </div>
  </div>
{% endif %}
{% endblock %}
