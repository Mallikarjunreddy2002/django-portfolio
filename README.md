# Django Portfolio Website / ಡಜಾಂಗೋ ಪೋರ್ಟ್‌ಫೋಲಿಯೊ ವೆಬ್‌ಸೈಟ್

A complete, production-ready personal portfolio built with **Python + Django**.
You can add **Projects** and **Skills** any time — either from a simple
website **Dashboard** (no code needed) or from the built-in **Django Admin** panel.

ಪೈಥಾನ್ + ಡಜಾಂಗೋ ಬಳಸಿ ನಿರ್ಮಿಸಿದ ಸಂಪೂರ್ಣ ಪರ್ಸನಲ್ ಪೋರ್ಟ್‌ಫೋಲಿಯೊ ವೆಬ್‌ಸೈಟ್ ಇದಾಗಿದೆ.
ನೀವು **ಪ್ರಾಜೆಕ್ಟ್‌ಗಳು** ಮತ್ತು **ಸ್ಕಿಲ್‌ಗಳನ್ನು** ಯಾವಾಗ ಬೇಕಾದರೂ ಸೇರಿಸಬಹುದು — ಕೋಡ್ ಬರೆಯದೆಯೇ
ವೆಬ್‌ಸೈಟ್‌ನ **ಡ್ಯಾಶ್‌ಬೋರ್ಡ್** ಮೂಲಕ, ಅಥವಾ ಡಜಾಂಗೋದ **ಅಡ್ಮಿನ್ ಪ್ಯಾನೆಲ್** ಮೂಲಕ.

---

## 1. Features / ವೈಶಿಷ್ಟ್ಯಗಳು

| Feature (EN) | ವೈಶಿಷ್ಟ್ಯ (KN) |
|---|---|
| Home page with hero, featured projects, skills, testimonials | ಹೀರೋ ಸೆಕ್ಷನ್, ಫೀಚರ್ಡ್ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳು, ಸ್ಕಿಲ್‌ಗಳು ಇರುವ ಹೋಂ ಪೇಜ್ |
| About page with bio, contact info, resume download | ಬಯೋ, ಸಂಪರ್ಕ ಮಾಹಿತಿ, ರೆಸ್ಯೂಮ್ ಡೌನ್‌ಲೋಡ್ ಇರುವ About ಪೇಜ್ |
| Projects page with search + filter by technology | ಟೆಕ್ನಾಲಜಿ ಪ್ರಕಾರ ಫಿಲ್ಟರ್ ಮತ್ತು ಸರ್ಚ್ ಇರುವ ಪ್ರಾಜೆಕ್ಟ್ಸ್ ಪೇಜ್ |
| Project detail page with related projects | ಸಂಬಂಧಿತ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳ ಜೊತೆ ಪ್ರಾಜೆಕ್ಟ್ ಡೀಟೇಲ್ ಪೇಜ್ |
| Skills page with animated progress bars | ಪ್ರೋಗ್ರೆಸ್ ಬಾರ್ ಇರುವ ಸ್ಕಿಲ್ಸ್ ಪೇಜ್ |
| Contact form (saves to DB + emails you) | ಸಂಪರ್ಕ ಫಾರ್ಮ್ (ಡೇಟಾಬೇಸ್‌ಗೆ ಸೇವ್ ಮತ್ತು ಇಮೇಲ್ ಕಳುಹಿಸುತ್ತದೆ) |
| **Login-protected Dashboard** to add/edit/delete Projects & Skills | ಪ್ರಾಜೆಕ್ಟ್/ಸ್ಕಿಲ್ ಸೇರಿಸಲು **ಲಾಗಿನ್ ಆಧಾರಿತ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್** |
| Full Django Admin panel (`/admin/`) as an alternative | ಪರ್ಯಾಯವಾಗಿ ಸಂಪೂರ್ಣ ಡಜಾಂಗೋ ಅಡ್ಮಿನ್ ಪ್ಯಾನೆಲ್ |
| Responsive Bootstrap 5 design | ರೆಸ್ಪಾನ್ಸಿವ್ Bootstrap 5 ಡಿಸೈನ್ |
| Image uploads for profile photo, project images, resume | ಪ್ರೊಫೈಲ್ ಫೋಟೋ, ಪ್ರಾಜೆಕ್ಟ್ ಇಮೇಜ್, ರೆಸ್ಯೂಮ್ ಅಪ್‌ಲೋಡ್ |
| Sample/demo data seeding command | ಡೆಮೊ ಡೇಟಾ ಸೇರಿಸುವ ಕಮಾಂಡ್ |

---

## 2. Project Structure / ಪ್ರಾಜೆಕ್ಟ್ ರಚನೆ

```
portfolio_project/
├── manage.py
├── requirements.txt
├── config/                # Django project settings/urls
│   ├── settings.py
│   ├── urls.py
├── portfolio/              # Main app
│   ├── models.py           # Profile, Skill, Project, Testimonial, ContactMessage
│   ├── views.py             # All page + dashboard views
│   ├── forms.py
│   ├── admin.py
│   ├── urls.py
│   └── management/commands/seed_demo_data.py
├── templates/               # HTML templates (Bootstrap 5)
├── static/css/style.css
└── media/                   # Uploaded images/resume go here
```

---

## 3. Prerequisites / ಅಗತ್ಯತೆಗಳು

- Python 3.10+ installed
- pip (Python package manager)
- (Optional) `virtualenv` for an isolated environment

**EN:** Check Python is installed by running `python --version` in your terminal.
**KN:** ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ `python --version` ಎಂದು ಟೈಪ್ ಮಾಡಿ ಪೈಥಾನ್ ಇನ್‌ಸ್ಟಾಲ್ ಆಗಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ.

---

## 4. Step-by-Step Setup / ಹಂತ ಹಂತವಾಗಿ ಸೆಟಪ್

### Step 1 — Extract the project / ಪ್ರಾಜೆಕ್ಟ್ ಎಕ್ಸ್‌ಟ್ರಾಕ್ಟ್ ಮಾಡಿ
**EN:** Unzip the downloaded file and open a terminal inside the `portfolio_project` folder.
**KN:** ಡೌನ್‌ಲೋಡ್ ಮಾಡಿದ ಫೈಲ್ ಅನ್‌ಜಿಪ್ ಮಾಡಿ, `portfolio_project` ಫೋಲ್ಡರ್ ಒಳಗೆ ಟರ್ಮಿನಲ್ ತೆರೆಯಿರಿ.

```bash
cd portfolio_project
```

### Step 2 — Create a virtual environment / ವರ್ಚುವಲ್ ಎನ್ವಿರಾನ್ಮೆಂಟ್ ರಚಿಸಿ
**EN:** This keeps your project's packages separate from other Python projects.
**KN:** ಇದು ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನ ಪ್ಯಾಕೇಜ್‌ಗಳನ್ನು ಇತರ ಪೈಥಾನ್ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳಿಂದ ಪ್ರತ್ಯೇಕವಾಗಿ ಇಡುತ್ತದೆ.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install dependencies / ಡಿಪೆಂಡೆನ್ಸಿಗಳನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ
```bash
pip install -r requirements.txt
```

### Step 4 — Run database migrations / ಡೇಟಾಬೇಸ್ ಮೈಗ್ರೇಶನ್ ರನ್ ಮಾಡಿ
**EN:** This creates the database tables (uses SQLite by default — no extra setup needed).
**KN:** ಇದು ಡೇಟಾಬೇಸ್ ಟೇಬಲ್‌ಗಳನ್ನು ರಚಿಸುತ್ತದೆ (ಡೀಫಾಲ್ಟ್ ಆಗಿ SQLite ಬಳಸುತ್ತದೆ — ಹೆಚ್ಚುವರಿ ಸೆಟಪ್ ಬೇಡ).

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5 — Create your admin/owner account / ನಿಮ್ಮ ಅಡ್ಮಿನ್ ಖಾತೆ ರಚಿಸಿ

**Option A (recommended) — interactive:**
```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

**Option B — quick demo data (creates username `admin` / password `admin12345`, plus sample profile, skills and one project):**
```bash
python manage.py seed_demo_data
```
**EN:** ⚠️ If you use Option B, log in and change the password immediately.
**KN:** ⚠️ Option B ಬಳಸಿದರೆ, ಲಾಗಿನ್ ಆದ ಕೂಡಲೇ ಪಾಸ್‌ವರ್ಡ್ ಬದಲಾಯಿಸಿ.

### Step 6 — Run the development server / ಡೆವಲಪ್‌ಮೆಂಟ್ ಸರ್ವರ್ ಚಾಲನೆ ಮಾಡಿ
```bash
python manage.py runserver
```
**EN:** Open your browser at **http://127.0.0.1:8000/** to see your portfolio.
**KN:** ನಿಮ್ಮ ಬ್ರೌಸರ್‌ನಲ್ಲಿ **http://127.0.0.1:8000/** ತೆರೆದು ಪೋರ್ಟ್‌ಫೋಲಿಯೊ ನೋಡಿ.

---

## 5. Adding Projects & Skills / ಪ್ರಾಜೆಕ್ಟ್ ಮತ್ತು ಸ್ಕಿಲ್ ಸೇರಿಸುವುದು

You have **two ways** to add content — use whichever you prefer.
ಕಂಟೆಂಟ್ ಸೇರಿಸಲು **ಎರಡು ವಿಧಾನಗಳಿವೆ** — ನಿಮಗೆ ಇಷ್ಟವಾದದ್ದನ್ನು ಬಳಸಿ.

### Option A — Website Dashboard (easiest, no admin knowledge needed)
1. Go to **http://127.0.0.1:8000/accounts/login/** and log in.
2. Click **Dashboard** in the top navigation bar.
3. Click **"Add Project"** or **"Add Skill"**, fill the form, and click Save.
4. Edit your name/bio/photo/resume anytime via **"Edit My Profile"** on the Dashboard.

**ಕನ್ನಡ:**
1. **http://127.0.0.1:8000/accounts/login/** ಗೆ ಹೋಗಿ ಲಾಗಿನ್ ಆಗಿ.
2. ಮೇಲಿನ ನ್ಯಾವಿಗೇಶನ್‌ನಲ್ಲಿ **Dashboard** ಕ್ಲಿಕ್ ಮಾಡಿ.
3. **"Add Project"** ಅಥವಾ **"Add Skill"** ಕ್ಲಿಕ್ ಮಾಡಿ, ಫಾರ್ಮ್ ತುಂಬಿ, Save ಒತ್ತಿ.
4. **"Edit My Profile"** ಮೂಲಕ ಹೆಸರು/ಬಯೋ/ಫೋಟೋ/ರೆಸ್ಯೂಮ್ ಯಾವಾಗ ಬೇಕಾದರೂ ಬದಲಾಯಿಸಿ.

### Option B — Django Admin Panel (more powerful, bulk editing)
1. Go to **http://127.0.0.1:8000/admin/** and log in with your superuser account.
2. Click **Projects** or **Skills** → **Add**.
3. Fill in the fields and click **Save**.

**ಕನ್ನಡ:**
1. **http://127.0.0.1:8000/admin/** ಗೆ ಹೋಗಿ ಸೂಪರ್‌ಯೂಸರ್ ಖಾತೆಯಿಂದ ಲಾಗಿನ್ ಆಗಿ.
2. **Projects** ಅಥವಾ **Skills** → **Add** ಕ್ಲಿಕ್ ಮಾಡಿ.
3. ಫೀಲ್ಡ್‌ಗಳನ್ನು ತುಂಬಿ **Save** ಒತ್ತಿ.

---

## 6. Customizing / ಕಸ್ಟಮೈಸ್ ಮಾಡುವುದು

- **Colors/branding:** edit `static/css/style.css` — change the `--accent` and `--dark` CSS variables.
- **Site name shown in navbar/footer:** comes automatically from your Profile's "Full Name".
- **Contact form emails:** by default emails print to your terminal (`EMAIL_BACKEND` in `config/settings.py`). To send real emails, switch to an SMTP backend and add your email credentials (e.g. Gmail App Password).

**ಕನ್ನಡ:**
- **ಬಣ್ಣಗಳು:** `static/css/style.css` ನಲ್ಲಿ `--accent` ಮತ್ತು `--dark` ಬದಲಾಯಿಸಿ.
- **ವೆಬ್‌ಸೈಟ್ ಹೆಸರು:** ಇದು ನಿಮ್ಮ ಪ್ರೊಫೈಲ್‌ನ "Full Name" ಇಂದ ತಾನಾಗಿಯೇ ಬರುತ್ತದೆ.
- **ಕಾಂಟ್ಯಾಕ್ಟ್ ಫಾರ್ಮ್ ಇಮೇಲ್:** ಡೀಫಾಲ್ಟ್ ಆಗಿ ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಪ್ರಿಂಟ್ ಆಗುತ್ತದೆ. ನಿಜವಾದ ಇಮೇಲ್ ಕಳುಹಿಸಲು SMTP ಸೆಟಪ್ ಮಾಡಿ.

---

## 7. Deploying to Production / ಪ್ರೊಡಕ್ಷನ್‌ಗೆ ಡಿಪ್ಲಾಯ್ ಮಾಡುವುದು

Before going live:
1. Set `DJANGO_DEBUG=False` as an environment variable.
2. Set a strong, secret `DJANGO_SECRET_KEY` environment variable.
3. Set `ALLOWED_HOSTS` in `config/settings.py` to your real domain.
4. Run `python manage.py collectstatic`.
5. Use a real database (e.g. PostgreSQL) for anything beyond a hobby project.
6. Popular free/low-cost hosts for Django: Railway, Render, PythonAnywhere.

**ಕನ್ನಡ:** ಲೈವ್‌ಗೆ ಹೋಗುವ ಮೊದಲು DEBUG ಆಫ್ ಮಾಡಿ, ಸೀಕ್ರೆಟ್ ಕೀ ಬದಲಾಯಿಸಿ, ALLOWED_HOSTS ಸೆಟ್ ಮಾಡಿ, ಮತ್ತು ನಿಜವಾದ ಡೇಟಾಬೇಸ್ (PostgreSQL) ಬಳಸಿ. Railway, Render, PythonAnywhere ನಂತಹ ಸೇವೆಗಳಲ್ಲಿ ಡಜಾಂಗೋ ಡಿಪ್ಲಾಯ್ ಮಾಡಬಹುದು.

---

## 8. Troubleshooting / ಸಮಸ್ಯೆ ಪರಿಹಾರ

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: No module named 'django'` | Run `pip install -r requirements.txt` again, make sure your virtual environment is activated. |
| Images not showing after upload | Make sure `DEBUG=True` in development; in production, configure a media file server. |
| "Page not found" on `/admin/` | Make sure you ran `python manage.py migrate` first. |
| Forgot admin password | Run `python manage.py changepassword <username>`. |

---

Enjoy your new portfolio! / ನಿಮ್ಮ ಹೊಸ ಪೋರ್ಟ್‌ಫೋಲಿಯೊ ಆನಂದಿಸಿ! 🎉
