# Mine Safety & Equipment Monitor

A Streamlit app built from the group's Python scripts and CSV databases.

## Run it
1. Open this folder in VS Code (File > Open Folder).
2. Open a terminal (Ctrl+`) and create an environment:
   - `python -m venv .venv`
   - Windows: `.venv\Scripts\activate`   Mac/Linux: `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `streamlit run app.py` (or press F5 and choose "Run Streamlit app").

Sign in with a username and password from `data/login_database.csv`.

## Structure
- `app.py` - login + dashboard
- `pages/` - Worker Safety, Incidents, Equipment, Maintenance, Risk Assessment, Reports, Users
- `functions/` - `auth.py` (login + roles), `data_loader.py`, `rules.py` (thresholds and risk logic)
- `data/` - the CSV databases (new incidents are appended to `safety_incidents_database.csv`)
- `original_scripts/` - your original files, untouched

## Notes
- Availability rule changed: the originals flagged "low availability" above 90/100; the app uses below 90% = warning, below 80% = critical.
- Passwords in the login CSV are plain text. Fine for a class project; hash them for real use.
