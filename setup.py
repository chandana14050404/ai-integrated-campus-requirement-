{% extends 'placement/base.html' %}
{% block title %}Company dashboard{% endblock %}

{% block content %}
<div class="card-header-row">
  <div>
    <span class="eyebrow">Company desk</span>
    <h1>{{ user.display_name }}</h1>
  </div>
  <a href="{% url 'company_post_job' %}" class="btn btn-accent">Post a job</a>
</div>

{% if jobs %}
<div class="card card-flush">
  <table class="ledger">
    <thead><tr><th>Job ID</th><th>Title</th><th>Posted</th><th>Last date</th><th>Applicants</th><th></th></tr></thead>
    <tbody>
    {% for job in jobs %}
      <tr>
        <td class="text-mono">#{{ job.id }}</td>
        <td>{{ job.title }}</td>
        <td class="text-mono">{{ job.posted_date }}</td>
        <td class="text-mono">{{ job.last_date }}</td>
        <td class="text-mono">{{ job.num_applicants }}</td>
        <td>
          <a href="{% url 'company_view_applicants' job.id %}" class="btn btn-sm btn-outline">Applicants</a>
          <a href="{% url 'company_add_questions' job.id %}" class="btn btn-sm btn-outline">Questions ({{ job.questions.count }})</a>
        </td>
      </tr>
    {% endfor %}
    </tbody>
  </table>
</div>
{% else %}
  <div class="empty-state card">
    <h3>No jobs posted yet</h3>
    <p>Post your first role with required skills and a salary band, then add a short test for applicants.</p>
    <a href="{% url 'company_post_job' %}" class="btn btn-accent">Post a job</a>
  </div>
{% endif %}
{% endblock %}
