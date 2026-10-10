# SOC Dashboard

A web-based Security Operations Center (SOC) dashboard built to monitor network assets, resolve security threats, and track live hardware telemetry. 

**Tech:** Django (Backend) and AdminLTE 3.2 (Frontend).

## Guide

The included `db.sqlite3` database is already pre-populated with test data, so no migrations are needed.

1. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the local server:**
   ```bash
   python manage.py runserver
   ```

3. **View the dashboard:**
   Open your browser and navigate to: `http://127.0.0.1:8000/`