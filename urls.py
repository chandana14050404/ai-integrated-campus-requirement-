# Campus Placement System

A Django web app for managing campus placements — Students, Companies, and TPO (Training & Placement Officer).

## Quick Start (3 steps)

**Requirements:** Python 3.10+  *(no database server needed — uses SQLite)*

```bash
# 1. Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Run the one-command setup (installs packages, creates DB, seeds data)
python setup.py

# 3. Start the server
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

---

## Try It Out

1. **Register as a Company** → Post a job → Add MCQ test questions
2. **Register as a Student** → Update your profile & skills → Go to Recommendations → Apply & take the test
3. **Register as a TPO** → View the dashboard, students, companies, and respond to feedback

---

## User Roles

| Role | What they can do |
|------|-----------------|
| **Company** | Post jobs with required skills, add MCQ tests, view applicants & scores |
| **Student** | Build profile, get AI job recommendations, take tests, track status |
| **TPO** | View platform stats, manage students/companies, respond to feedback |

A student scores **≥ 80%** on the MCQ test → **Selected**, otherwise **Rejected**.

---

## Project Structure

```
campus_placement/    ← Django project settings & root URLs
placement/           ← Main app
  models.py          ← User, Skill, StudentProfile, Job, Question, JobApplication, Feedback
  views.py           ← All page logic (grouped by role)
  forms.py           ← All forms
  urls.py            ← URL routes
  ml_recommend.py    ← KNN job recommendation engine (scikit-learn)
templates/           ← HTML templates
static/              ← CSS
media/resumes/       ← Uploaded student resumes
db.sqlite3           ← Database (auto-created on first run)
```

## Admin Panel

Go to `/admin/` and log in with the superuser you created during setup. From there you can manage all data directly.
