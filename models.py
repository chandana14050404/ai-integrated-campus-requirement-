{% extends 'placement/base.html' %}
{% block title %}Sign up{% endblock %}

{% block content %}
<div class="container-narrow" style="margin:0 auto;">
  <span class="eyebrow">New User Sign Up</span>
  <h1>Create your account</h1>
  <p class="muted">Register as a Student, Company or Training &amp; Placement Officer.</p>

  <form method="post" class="card" novalidate>
    {% csrf_token %}

    <div class="field">
      <label for="{{ form.role.id_for_label }}">Register as</label>
      {{ form.role }}
      {{ form.role.errors }}
    </div>

    <div class="grid grid-2">
      <div class="field">
        <label for="{{ form.username.id_for_label }}">Username</label>
        {{ form.username }}
        {{ form.username.errors }}
      </div>
      <div class="field">
        <label for="{{ form.first_name.id_for_label }}">Full name</label>
        {{ form.first_name }}
        {{ form.first_name.errors }}
      </div>
    </div>

    <div class="field" id="company-name-field">
      <label for="{{ form.company_name.id_for_label }}">Company name</label>
      {{ form.company_name }}
      <div class="help-text">{{ form.company_name.help_text }}</div>
      {{ form.company_name.errors }}
    </div>

    <div class="grid grid-2">
      <div class="field">
        <label for="{{ form.email.id_for_label }}">Email</label>
        {{ form.email }}
        {{ form.email.errors }}
      </div>
      <div class="field">
        <label for="{{ form.contact_number.id_for_label }}">Contact number</label>
        {{ form.contact_number }}
        {{ form.contact_number.errors }}
      </div>
    </div>

    <div class="field">
      <label for="{{ form.address.id_for_label }}">Address</label>
      {{ form.address }}
      {{ form.address.errors }}
    </div>

    <div class="grid grid-2">
      <div class="field">
        <label for="{{ form.password1.id_for_label }}">Password</label>
        {{ form.password1 }}
        <div class="help-text">8+ characters, not too common, not all numeric.</div>
        {{ form.password1.errors }}
      </div>
      <div class="field">
        <label for="{{ form.password2.id_for_label }}">Confirm password</label>
        {{ form.password2 }}
        {{ form.password2.errors }}
      </div>
    </div>

    {{ form.non_field_errors }}

    <button type="submit" class="btn btn-accent btn-block">Create account</button>
    <p class="muted" style="text-align:center; margin-top:1rem;">
      Already registered? <a href="{% url 'login' %}">Log in</a>
    </p>
  </form>
</div>
{% endblock %}
