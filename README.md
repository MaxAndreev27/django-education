# Django 6 E-Learning Platform

A modern Learning Management System (LMS) web application built following Chapters 12–16 of **"Django 4 by Example" (2023) by Antonio Mele**. This application implements a full course management lifecycle, allowing instructors to build multi-type content, and enabling students to enroll in courses, access cached content, interact via a REST API, and communicate through a real-time chat room.

## 🚀 Core Features (By Chapters)

### Chapters 12–13: Content Management System (CMS)

- **Flexible Data Model:** Utilizes Django's `contenttypes` framework (Generic Relations) to allow course modules to contain diverse content types (text, video, images, files) without database table duplication.
- **Dynamic Forms (Formsets):** Provides an intuitive instructor interface to add, edit, and reorder course modules and their content dynamically on a single page.
- **Authorization & Access Control:** Implements role-based access control (Instructors vs. Students) using Django standard Mixins and Permission Groups.

### Chapter 14: Student Registration & Enrollment

- Dedicated student registration workflow and student dashboard.
- Course enrollment system allowing students to sign up for available courses.
- Seamless course viewer layout with dynamic switching between text lectures, video materials, and file downloads.

### Chapter 15: Caching & Optimization

- **Redis Integration:** Configures Redis as the primary caching backend for the Django application.
- **Content Caching:** Optimizes database query performance using template fragment caching and entire View caching to dramatically reduce server load under high traffic.

### Chapter 16: REST API & Real-Time Chat

- **Django REST Framework (DRF):** Exposes API endpoints for retrieving subjects, courses, and modules, alongside automatic student enrollment using Serializers and ViewSets.
- **API Authentication:** Uses Token and Basic authentication to secure endpoints for third-party or mobile application integrations.
- **WebSockets Chat (Django Channels):** Integrates a real-time chat room dedicated to each course. Features full ASGI architecture configuration running on top of the `daphne` server.

---

## 🛠 Tech Stack

- **Backend:** Python 3.13+ / Django 6+
- **Real-time & Async:** Django Channels / Daphne (ASGI)
- **API Engine:** Django REST Framework (DRF)
- **Database:** PostgreSQL (or SQLite for local development)
- **Key-Value Store / Cache:** Redis
- **Frontend:** HTML5, CSS3 (Tailwind CSS or book default styles), JavaScript (WebSockets API)

---

## ⚙️ Local Setup & Installation

### 1. Clone the Repository & Setup Environment

```bash
git clone https://github.com/MaxAndreev27/django-education.git
cd django-education

python -m venv .venv
source .venv/bin/activate  # For Linux/macOS
# .venv\Scripts\activate   # For Windows

pip install -r requirements.txt
```

### 2. Run the Project

```bash
python manage.py migrate
python manage.py runserver
```

### 3. Optional: Redis and Channels

This project uses Redis for caching and Django Channels. If you are running the full real-time stack locally, make sure Redis is installed and running before starting the app.

```bash
redis-server
```

---

## 🤝 Community Standards

This repository includes the standard GitHub community health files to make participation clearer and more welcoming:

- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — expected community behavior and enforcement guidance
- [CONTRIBUTING.md](CONTRIBUTING.md) — how to contribute and validate changes
- [SECURITY.md](SECURITY.md) — how to report vulnerabilities privately
- [LICENSE](LICENSE) — project license information

We welcome contributions, bug reports, and suggestions through GitHub issues and pull requests.

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
