import streamlit as st
from navigation import show_navigation


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Dashboard | VanVidhya",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# NAVIGATION
# =========================================================

show_navigation()


# =========================================================
# HTML RENDER HELPER
# =========================================================

def render_html(content):
    clean_html = "\n".join(
        line.strip() for line in content.splitlines()
    )

    st.markdown(
        clean_html,
        unsafe_allow_html=True
    )


# =========================================================
# LOGIN CHECK
# =========================================================

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()


student_name = st.session_state.get(
    "student_name",
    "Student"
)

student_id = st.session_state.get(
    "student_id",
    "VV2026001"
)


# =========================================================
# PAGE CSS
# =========================================================

st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* =====================================================
   BACKGROUND
   ===================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 90% 5%,
            rgba(82,130,91,0.12),
            transparent 28%
        ),
        radial-gradient(
            circle at 5% 90%,
            rgba(201,168,93,0.07),
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #041F18 0%,
            #063328 50%,
            #05271F 100%
        );

    color: #F5F2E8;
    min-height: 100vh;
}

.block-container {
    max-width: 1380px;
    padding-top: 30px;
    padding-bottom: 50px;
}


/* =====================================================
   TOP BAR
   ===================================================== */

.dashboard-brand {
    font-family: Arial, sans-serif;
    font-size: 21px;
    font-weight: 700;
    letter-spacing: 2.5px;
    color: #F5F2E8;
}

.dashboard-brand span {
    color: #D2B56A;
}

.student-badge {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 20px;
    background: rgba(201,168,93,0.09);
    border: 1px solid rgba(201,168,93,0.22);
    color: rgba(245,242,232,0.72);
    font-size: 12px;
}


/* =====================================================
   WELCOME HEADER
   ===================================================== */

.welcome-label {
    color: #D2B56A;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-top: 35px;
    margin-bottom: 8px;
}

.welcome-title {
    font-family: Arial, sans-serif;
    font-size: 36px;
    font-weight: 700;
    color: #F7F3E8;
    margin-bottom: 7px;
}

.welcome-title span {
    color: #D2B56A;
}

.welcome-subtitle {
    color: rgba(245,242,232,0.53);
    font-size: 13px;
}


/* =====================================================
   SECTION HEADERS
   ===================================================== */

.section-heading {
    font-family: Arial, sans-serif;
    font-size: 21px;
    font-weight: 700;
    color: #F5F2E8;
    margin-top: 30px;
    margin-bottom: 5px;
}

.section-caption {
    color: rgba(245,242,232,0.48);
    font-size: 12px;
    margin-bottom: 18px;
}


/* =====================================================
   METRIC CARDS
   ===================================================== */

.metric-card {
    background:
        linear-gradient(
            145deg,
            rgba(18,70,53,0.90),
            rgba(5,39,30,0.96)
        );

    border:
        1px solid rgba(104,151,121,0.28);

    border-radius: 15px;

    padding: 20px;

    min-height: 108px;

    box-shadow:
        0 10px 28px rgba(0,0,0,0.12);
}

.metric-label {
    color: rgba(245,242,232,0.52);
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
}

.metric-value {
    color: #F7F3E8;
    font-family: Arial, sans-serif;
    font-size: 27px;
    font-weight: 700;
    margin-top: 9px;
}

.metric-icon {
    color: #D2B56A;
    font-size: 16px;
    margin-right: 5px;
}


/* =====================================================
   CURRENT APPLICATION
   ===================================================== */

.application-card {
    background:
        linear-gradient(
            145deg,
            rgba(17,68,51,0.90),
            rgba(5,39,30,0.96)
        );

    border:
        1px solid rgba(201,168,93,0.27);

    border-radius: 18px;

    padding: 25px;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.14);
}

.application-title {
    color: #F7F3E8;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 5px;
}

.application-status {
    color: #D2B56A;
    font-size: 12px;
    margin-bottom: 20px;
}

.progress-track {
    height: 7px;
    width: 100%;
    background: rgba(255,255,255,0.08);
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 20px;
}

.progress-fill {
    height: 100%;
    width: 55%;
    background: #D2B56A;
    border-radius: 10px;
}

.application-info {
    color: rgba(245,242,232,0.50);
    font-size: 11px;
    margin-bottom: 5px;
}

.application-value {
    color: #F5F2E8;
    font-size: 13px;
    font-weight: 600;
}


/* =====================================================
   SERVICE CARDS
   ===================================================== */

.service-card {
    background:
        linear-gradient(
            145deg,
            rgba(14,62,47,0.88),
            rgba(5,39,30,0.95)
        );

    border:
        1px solid rgba(104,151,121,0.25);

    border-radius: 15px;

    padding: 19px;

    min-height: 112px;

    transition: 0.25s ease;
}

.service-card:hover {
    border-color: rgba(201,168,93,0.45);
    transform: translateY(-2px);
}

.service-icon {
    color: #D2B56A;
    font-size: 22px;
    margin-bottom: 8px;
}

.service-title {
    color: #F5F2E8;
    font-size: 14px;
    font-weight: 700;
}

.service-description {
    color: rgba(245,242,232,0.47);
    font-size: 11px;
    margin-top: 5px;
    line-height: 1.5;
}


/* =====================================================
   BUTTONS
   ===================================================== */

div.stButton > button {
    background: #D2B56A;
    color: #09251D;

    border:
        1px solid #DCC37F;

    border-radius: 10px;

    min-height: 43px;

    font-size: 13px;
    font-weight: 700;

    transition: all 0.25s ease;
}

div.stButton > button:hover {
    background: #E0C77D;
    color: #09251D;

    transform: translateY(-2px);

    box-shadow:
        0 8px 20px rgba(0,0,0,0.22);
}


/* =====================================================
   UPDATE CARDS
   ===================================================== */

.update-success {
    background: rgba(58,130,87,0.12);
    border: 1px solid rgba(91,170,113,0.25);
    border-radius: 11px;
    padding: 13px 16px;
    color: #A9D5B0;
    font-size: 12px;
    margin-bottom: 9px;
}

.update-pending {
    background: rgba(201,168,93,0.10);
    border: 1px solid rgba(201,168,93,0.25);
    border-radius: 11px;
    padding: 13px 16px;
    color: #DCC37F;
    font-size: 12px;
    margin-bottom: 9px;
}


/* =====================================================
   SMART ASSISTANCE
   ===================================================== */

.smart-card {
    background:
        linear-gradient(
            145deg,
            rgba(17,68,51,0.88),
            rgba(5,39,30,0.96)
        );

    border:
        1px solid rgba(104,151,121,0.28);

    border-radius: 17px;

    padding: 23px;

    min-height: 165px;
}

.smart-card.gold {
    border-color: rgba(201,168,93,0.32);
}

.smart-icon {
    color: #D2B56A;
    font-size: 24px;
}

.smart-title {
    color: #F5F2E8;
    font-size: 16px;
    font-weight: 700;
    margin-top: 8px;
}

.smart-text {
    color: rgba(245,242,232,0.52);
    font-size: 12px;
    line-height: 1.6;
    margin-top: 7px;
}


/* =====================================================
   ADMIN
   ===================================================== */

.admin-box {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(104,151,121,0.18);
    border-radius: 13px;
    padding: 17px;
    color: rgba(245,242,232,0.55);
    font-size: 12px;
}


/* =====================================================
   FOOTER
   ===================================================== */

.dashboard-footer {
    text-align: center;

    margin-top: 45px;

    padding-top: 22px;

    border-top:
        1px solid rgba(201,168,93,0.14);

    color:
        rgba(245,242,232,0.40);

    font-size: 11px;
}

.dashboard-footer-brand {
    color: #D2B56A;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 7px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TOP BRAND
# =========================================================

col1, col2 = st.columns([1, 1])

with col1:
    render_html("""
<div class="dashboard-brand">
VAN<span>VIDHYA</span>
</div>
""")

with col2:
    st.markdown(
        f"""
        <div style="
            text-align:right;
            padding-top:3px;
        ">
            <span class="student-badge">
                Student ID • {student_id}
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# WELCOME
# =========================================================

render_html(f"""
<div class="welcome-label">
STUDENT DASHBOARD
</div>

<div class="welcome-title">
Welcome, <span>{student_name}</span> 👋
</div>

<div class="welcome-subtitle">
Your scholarships, applications, documents and payments — all in one place.
</div>
""")


# =========================================================
# SCHOLARSHIP OVERVIEW
# =========================================================

render_html("""
<div class="section-heading">
Scholarship Overview
</div>

<div class="section-caption">
A quick view of your current scholarship journey.
</div>
""")

col1, col2, col3, col4 = st.columns(4)

with col1:
    render_html("""
<div class="metric-card">
<div class="metric-label">
Applications
</div>
<div class="metric-value">
<span class="metric-icon">▣</span> 2
</div>
</div>
""")

with col2:
    render_html("""
<div class="metric-card">
<div class="metric-label">
Under Verification
</div>
<div class="metric-value">
<span class="metric-icon">◌</span> 1
</div>
</div>
""")

with col3:
    render_html("""
<div class="metric-card">
<div class="metric-label">
Sanctioned
</div>
<div class="metric-value">
<span class="metric-icon">✓</span> 1
</div>
</div>
""")

with col4:
    render_html("""
<div class="metric-card">
<div class="metric-label">
DBT Status
</div>
<div class="metric-value">
<span class="metric-icon">↗</span> Done
</div>
</div>
""")


# =========================================================
# CURRENT APPLICATION
# =========================================================

render_html("""
<div class="section-heading">
Current Application
</div>

<div class="section-caption">
Track the latest stage of your active scholarship application.
</div>

<div class="application-card">

<div class="application-title">
🎓 Post-Matric Scholarship
</div>

<div class="application-status">
● Institution Verification in Progress
</div>

<div class="progress-track">
<div class="progress-fill"></div>
</div>

</div>
""")

col1, col2, col3 = st.columns(3)

with col1:
    render_html("""
<div style="padding-top:14px;">
<div class="application-info">
APPLICATION STATUS
</div>
<div class="application-value">
🟡 Under Verification
</div>
</div>
""")

with col2:
    render_html("""
<div style="padding-top:14px;">
<div class="application-info">
CURRENT STAGE
</div>
<div class="application-value">
Institution Verification
</div>
</div>
""")

with col3:
    render_html("""
<div style="padding-top:14px;">
<div class="application-info">
PROGRESS
</div>
<div class="application-value">
55% Completed
</div>
</div>
""")


# =========================================================
# QUICK ACTIONS
# =========================================================

render_html("""
<div class="section-heading">
Quick Actions
</div>

<div class="section-caption">
Access the most frequently used scholarship services.
</div>
""")

col1, col2, col3, col4 = st.columns(4)

with col1:
    render_html("""
<div class="service-card">
<div class="service-icon">🎓</div>
<div class="service-title">Scholarships</div>
<div class="service-description">
Explore available scholarship schemes.
</div>
</div>
""")

    if st.button(
        "Open Scholarships",
        use_container_width=True
    ):
        st.switch_page("pages/scholarships.py")


with col2:
    render_html("""
<div class="service-card">
<div class="service-icon">📝</div>
<div class="service-title">Apply Scholarship</div>
<div class="service-description">
Start a new scholarship application.
</div>
</div>
""")

    if st.button(
        "Start Application",
        use_container_width=True
    ):
        st.switch_page("pages/apply_scholarship.py")


with col3:
    render_html("""
<div class="service-card">
<div class="service-icon">📄</div>
<div class="service-title">Documents</div>
<div class="service-description">
Manage and verify your documents.
</div>
</div>
""")

    if st.button(
        "Open Documents",
        use_container_width=True
    ):
        st.switch_page("pages/documents.py")


with col4:
    render_html("""
<div class="service-card">
<div class="service-icon">🤖</div>
<div class="service-title">JAGO AI</div>
<div class="service-description">
Get instant scholarship assistance.
</div>
</div>
""")

    if st.button(
        "Ask JAGO",
        use_container_width=True
    ):
        st.switch_page("pages/jago.py")


# =========================================================
# MORE SERVICES
# =========================================================

render_html("""
<div class="section-heading">
More Services
</div>

<div class="section-caption">
Everything else you need to manage your scholarship journey.
</div>
""")

col1, col2, col3, col4 = st.columns(4)

with col1:
    render_html("""
<div class="service-card">
<div class="service-icon">📋</div>
<div class="service-title">Applications</div>
<div class="service-description">
Track all submitted applications.
</div>
</div>
""")

    if st.button(
        "View Applications",
        use_container_width=True
    ):
        st.switch_page("pages/applications.py")


with col2:
    render_html("""
<div class="service-card">
<div class="service-icon">💰</div>
<div class="service-title">Payments & DBT</div>
<div class="service-description">
View scholarship payment status.
</div>
</div>
""")

    if st.button(
        "View Payments",
        use_container_width=True
    ):
        st.switch_page("pages/payment.py")


with col3:
    render_html("""
<div class="service-card">
<div class="service-icon">🔔</div>
<div class="service-title">Notifications</div>
<div class="service-description">
Stay updated on important actions.
</div>
</div>
""")

    if st.button(
        "View Notifications",
        use_container_width=True
    ):
        st.switch_page("pages/notifications.py")


with col4:
    render_html("""
<div class="service-card">
<div class="service-icon">✓</div>
<div class="service-title">Eligibility</div>
<div class="service-description">
Check your scholarship eligibility.
</div>
</div>
""")

    if st.button(
        "Check Eligibility",
        use_container_width=True
    ):
        st.switch_page("pages/eligibility.py")


# =========================================================
# APPLICATION TRACKING
# =========================================================

render_html("""
<div class="section-heading">
Application Tracking
</div>

<div class="section-caption">
Follow your scholarship from submission to final disbursement.
</div>
""")

if st.button(
    "View All Applications  →",
    use_container_width=True
):
    st.switch_page("pages/applications.py")


# =========================================================
# RECENT UPDATES
# =========================================================

render_html("""
<div class="section-heading">
Recent Updates
</div>

<div class="section-caption">
Latest activity related to your scholarship applications.
</div>
""")

render_html("""
<div class="update-success">
✓ &nbsp; Post-Matric Scholarship application submitted successfully.
</div>

<div class="update-pending">
⏳ &nbsp; Institution verification is currently in progress.
</div>

<div class="update-success">
✓ &nbsp; Previous scholarship DBT payment has been processed.
</div>
""")


# =========================================================
# SMART ASSISTANCE
# =========================================================

render_html("""
<div class="section-heading">
Smart Assistance
</div>

<div class="section-caption">
Get help and manage your scholarship documents with ease.
</div>
""")

col1, col2 = st.columns(2)

with col1:

    render_html("""
<div class="smart-card gold">

<div class="smart-icon">
✦
</div>

<div class="smart-title">
JAGO — Your AI Scholarship Assistant
</div>

<div class="smart-text">
Ask about eligibility, documents, application status,
verification, deficiencies and scholarship payments.
</div>

</div>
""")

    if st.button(
        "💬 Open JAGO",
        use_container_width=True
    ):
        st.switch_page("pages/jago.py")


with col2:

    render_html("""
<div class="smart-card">

<div class="smart-icon">
▣
</div>

<div class="smart-title">
Digital Document Wallet
</div>

<div class="smart-text">
Store, verify and reuse your scholarship documents
through one digital document space.
</div>

</div>
""")

    if st.button(
        "📂 Open Document Wallet",
        use_container_width=True
    ):
        st.switch_page("pages/documents.py")


# =========================================================
# ADMIN / DEMO CONTROLS
# =========================================================

st.write("")

with st.expander("🏛️ Administration / Demo Controls"):

    render_html("""
<div class="admin-box">
Prototype administration controls for demonstration
and judge evaluation.
</div>
""")

    if st.button(
        "Open Admin Dashboard",
        use_container_width=True
    ):
        st.switch_page("pages/admin_dashboard.py")


# =========================================================
# FOOTER
# =========================================================

render_html("""
<div class="dashboard-footer">

<div class="dashboard-footer-brand">
✦ &nbsp; VANVIDHYA &nbsp; ✦
</div>

A Unified Digital Gateway for Tribal Student Scholarships

<br><br>

SMART INDIA HACKATHON 2026
&nbsp; • &nbsp;
CoreSynch

</div>
""")