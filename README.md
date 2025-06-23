# 🛡️ Policy API – Django CMS Project

This is a simple Django-based REST API that serves Privacy Policy and Terms & Conditions pages from the Django Admin panel, using a SQLite database and RichText content (via CKEditor).

---

## 📌 Features

- ✅ CMS-style content management via Django Admin
- ✅ RichText editing support using CKEditor
- ✅ Public API endpoints for Privacy Policy and Terms
- ✅ JSON responses with status, message, and HTML-rendered content
- ✅ SQLite (`db.sqlite3`) as the default database

---

## 🔗 API Endpoints

### 1. **GET** `/api/privacy-policy/`
Returns the **latest active** Privacy Policy content.

#### ✅ Example Response:
```json
{
  "status": true,
  "message": "Privacy Policy retrieved successfully.",
  "data": {
    "title": "Privacy Policy 2025",
    "content": "<h1>Privacy Policy</h1><p>...</p>",
    "is_active": true,
    "created_at": "2025-06-23T20:18:31.027579Z",
    "updated_at": "2025-06-23T20:18:31.027634Z"
  }
}
```
###2. **GET** `/api/terms-and-conditions/`
Returns the **latest active** Terms & Conditions content.

#### ✅ Example Response:
```json
{
  "status": true,
  "message": "Terms and Conditions retrieved successfully.",
  "data": {
    "title": "Terms and Conditions 2025",
    "content": "<h1><img alt=\"Terms Banner\" src=\"...\" />Terms And Conditions</h1><h3>...</h3>",
    "is_active": true,
    "created_at": "2025-06-23T20:18:31.027579Z",
    "updated_at": "2025-06-23T20:18:31.027634Z"
  }
}
```
---
## ⚙️ Setup Instructions
### 1. Clone the Repository

```bash
git clone https://github.com/Eradboi/PrivacyPolicyApi.git
cd Privacy_Policy
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies
``` bash
pip install -r requirements.txt
```

### 4. Run Migrations
``` bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin User
``` bash
python manage.py createsuperuser
```
### 6. Run the Development Server
``` bash
python manage.py runserver
```

---
## 🧠 Admin Usage (CMS)
Visit /admin/ and log in.
Go to Privacy Policy or Terms and Conditions models.
Create a new entry with:
- Title
- RichText Content (via CKEditor)
- is_active = True
Other fields; *created_at* and *updated_at* are created/updated automatically as their names imply.

---
✨ Author
Built with Django ❤️ by Erad Creates
