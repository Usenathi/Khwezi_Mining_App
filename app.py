import streamlit as st
from functions.auth import current_user, login_form, require_access, page_header
from functions.data_loader import load_workers, load_incidents, load_equipment
from functions.rules import equipment_alerts

st.set_page_config(page_title="Mine Safety & Equipment Monitor", page_icon="⛏️", layout="wide")

if not current_user():
    st.title("⛏️ Mine Safety & Equipment Monitor")
    login_form()
    st.stop()

require_access("dashboard")
page_header("⛏️ Dashboard", "Overview of workers, incidents and equipment.")

w, i, e = load_workers(), load_incidents(), load_equipment()
alerts = [a for _, r in e.iterrows() for a in equipment_alerts(r)]

c = st.columns(4)
c[0].metric("Workers", len(w))
c[1].metric("PPE compliance", f"{(w.PPE_Compliance == 'Compliant').mean() * 100:.0f}%")
c[2].metric("High/Critical risk workers", int(w.Risk_Level.isin(["High", "Critical"]).sum()))
c[3].metric("Open incidents", int((i.Incident_Status != "Closed").sum()))
c = st.columns(4)
c[0].metric("Equipment", len(e))
c[1].metric("Critical equipment", int((e.Condition == "CRITICAL").sum()))
c[2].metric("Avg availability", f"{e.Availability_percent.mean():.1f}%")
c[3].metric("Active alerts", len(alerts))

a, b = st.columns(2)
a.subheader("Incidents by type")
a.bar_chart(i.Incident_Type.value_counts())
b.subheader("Equipment condition")
b.bar_chart(e.Condition.value_counts())
