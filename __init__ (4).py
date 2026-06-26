{% extends 'placement/base.html' %}
{% block title %}Applicants — {{ job.title }}{% endblock %}

{% block content %}
<span class="eyebrow">Job #{{ job.id }}</span>
<h1>Applicants for {{ job.title }}</h1>

{% if applications %}
<div class="card card-flush">
  <table class="ledger">
    <thead><tr><th>Student</th><th>Qualification</th><th>Score</th><th>Status</th><th>Applied</th></tr></thead>
    <tbody>
    {% for app in applications %}
      <tr>
        <td>{{ app.student.get_full_name|default:app.student.username }}</td>
        <td>{{ app.student.student_profile.qualification|default:"—" }}</td>
        <td class="text-mono">{{ app.score_percent }}%</td>
        <td>
          {% if app.status == 'SELECTED' %}
            <span class="stamp stamp-selected">Selected</span>
          {% else %}
            <span class="stamp stamp-rejected">Rejected</span>
          {% endif %}
        </td>
        <td class="text-mono">{{ app.applied_at|date:"d M Y" }}</td>
      </tr>
    {% endfor %}
    </tbody>
  </table>
</div>
{% else %}
  <div class="empty-state card">
    <h3>No applicants yet</h3>
    <p>Once students apply and take the test, their scores and status will appear here.</p>
  </div>
{% endif %}
{% endblock %}
