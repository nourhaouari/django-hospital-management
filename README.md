
# Hospital Management System 
A complete Hospital Management web application built with Django and Bootstrap as part of a university Practical Work (TP). It allows staff to manage patient records through an intuitive dashboard and robust CRUD operations.

##  Features

- **Secure Authentication:** Built-in Django Login/Logout system.
- **Dynamic Dashboard:** Displays real-time statistics (e.g., total patient count).
- **Full CRUD Operations:** Seamlessly Create, Read, Update, and Delete patient records.
- **Optimized Architecture:** Views logic elegantly split into a dedicated `views/` folder (`auth_views`, `dashboard_views`, `patient_views`) for maximum maintainability.
- **Responsive UI:** Clean, modern interface styled using Bootstrap 5.
- **Isolated Environment:** Fully configured to run within a Python Virtual Environment (`venv`).

---

##  Technologies Used

- **Backend:** Python 3.11, Django 4.2 LTS
- **Database:** MySQL / MariaDB (via `mysqlclient`)
- **Frontend:** HTML5, CSS3, Bootstrap 5 (CDN)
- **Environment:** Python `venv`

---

##  Project Structure

```text
hospital/
├── manage.py
├── hospital/                 # Core project settings and URLs
├── patients/                 # Main application
│   ├── models.py             # Patient database model
│   ├── urls.py               # App-specific routes
│   └── views/                # Split modular views
│       ├── __init__.py
│       ├── auth_views.py     # Login & Logout logic
│       ├── dashboard_views.py # Dashboard statistics logic
│       └── patient_views.py  # CRUD operations
├── requirements.txt          # Python dependencies
├── templates/                # Global HTML templates
│   ├── base.html             # Bootstrap layout wrapper
│   ├── login.html
│   ├── dashboard.html
│   └── patients/             # Patient-specific interfaces
│       ├── list.html
│       ├── create.html
│       └── update.html
└── venv/                     # Python Virtual Environment
```

---

##  Installation & Setup

Follow these steps to get the project running on your local machine.

### 1. Clone or Download the Repository
Navigate to your desired workspace and place the project folder there.

### 2. Activate the Virtual Environment
The project comes pre-configured with a virtual environment. You must activate it before running any commands.
**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```
**Windows (Command Prompt):**
```cmd
.\venv\Scripts\activate.bat
```
**Mac / Linux:**
```bash
source venv/bin/activate
```
*(You should see `(venv)` appear at the beginning of your terminal prompt.)*

### 3. Install Dependencies
Ensure all required packages are installed (in case of a fresh clone):
```bash
pip install -r requirements.txt
```
*(Alternatively, manually run: `pip install "django<5.0" mysqlclient`)*

---

##  Database Configuration

This project expects a MySQL database. If you are using XAMPP/WAMP, start your Apache and MySQL services.

**1. Create the MySQL Database**
Open your MySQL shell, phpMyAdmin, or MySQL Workbench and run:
```sql
CREATE DATABASE hospital_db;
```

**2. Verify Credentials**
Open `hospital/settings.py` and ensure the MySQL credentials match your local development environment:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hospital_db',
        'USER': 'root',       # Your MySQL username
        'PASSWORD': '',       # Your MySQL password (leave empty for XAMPP default)
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

**3. Run Migrations**
With the `(venv)` activated, construct the database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

##  How to Run the Project

**1. Create an Admin Account (Optional but recommended)**
```bash
python manage.py createsuperuser
```
Follow the prompts to set up your username, email, and password.

**2. Start the Server**
```bash
python manage.py runserver
```

**3. Access the Application**
Open your web browser and navigate to:
 **[http://localhost:8000/](http://localhost:8000/)**

---

##  Testing Checklist

To ensure everything is working correctly, test the following flow:
- [x] **Authentication:** Log in using your superuser account. Verify it redirects you to the Dashboard.
- [x] **Dashboard:** Verify the "Total Patients" counter displays properly (starts at 0).
- [x] **Create:** Navigate to "Manage Patients" -> click "Add Patient" -> fill out the form.
- [x] **Read:** Verify the new patient appears instantly in the table.
- [x] **Update:** Click "Edit", modify the patient's phone number or name, and save. Ensure the table updates.
- [x] **Delete:** Click "Delete", accept the confirmation prompt, and verify the record is removed.
- [x] **Logout:** Click the Logout button in the navigation bar to return to the secure login screen.

---

**Author:** [Nour Haouari]  



