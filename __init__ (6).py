{% extends 'placement/base.html' %}
{% block title %}Job status{% endblock %}

{% block content %}
<span class="eyebrow">Your applications</span>
<h1>Job status</h1>

{% if applications %}
<div class="card card-flush">
  <table class="ledger">
    <thead><tr><th>Job</th><th>Company</th><th>Applied</th><th>Score</th><th>Status</th></tr></thead>
    <tbody>
    {% for app in applications %}
      <tr>
        <td>{{ app.job.title }}</td>
        <td>{{ app.job.company.display_name }}</td>
        <td class="text-mono">{{ app.applied_at|date:"d M Y" }}</td>
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
</div>
{% else %}
  <div class="empty-state card">
    <h3>No applications yet</h3>
    <p>Once you apply to a recommended job and take its test, the result shows up here.</p>
    <a href="{% url 'student_recommendations' %}" class="btn btn-accent">Find a job</a>
  </div>
{% endif %}
{% endblock %}
