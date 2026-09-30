import streamlit as st
from navigation import show_navigation

st.set_page_config(
    page_title="Notifications | VanVidhya",
    page_icon="🔔",
    layout="wide"
)

# =========================================================
# LOGIN CHECK
# =========================================================

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

student_name = st.session_state.get("student_name", "Student")
student_id = st.session_state.get("student_id", "VV2026001")

show_navigation()


# =========================================================
# CUSTOM UI
# =========================================================

st.markdown("""
<style>

    /* ================= GLOBAL ================= */

    .stApp {
        background:
            radial-gradient(
                circle at 85% 8%,
                rgba(200, 169, 91, 0.07),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #071b16 0%,
                #0b241d 45%,
                #071914 100%
            );
        color: #f5f0df;
    }

    .main .block-container {
        padding-top: 2.2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    /* ================= TEXT ================= */

    h1, h2, h3, h4 {
        color: #f5f0df !important;
        letter-spacing: -0.3px;
    }

    [data-testid="stCaptionContainer"] {
        color: #aaa998 !important;
    }

    /* ================= HEADER ================= */

    .page-eyebrow {
        color: #c8a95b;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 0.35rem;
    }

    .page-title {
        font-size: 2.35rem;
        font-weight: 750;
        color: #f5f0df;
        margin-bottom: 0.25rem;
    }

    .page-subtitle {
        color: #aaa998;
        font-size: 0.98rem;
        margin-bottom: 1.5rem;
    }

    /* ================= METRICS ================= */

    [data-testid="stMetric"] {
        background: linear-gradient(
            145deg,
            #102d24,
            #0b211b
        );
        border: 1px solid rgba(200, 169, 91, 0.22);
        border-radius: 16px;
        padding: 1.15rem 1.2rem;
        min-height: 110px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.18);
    }

    [data-testid="stMetricLabel"] {
        color: #aaa998 !important;
        font-size: 0.82rem;
    }

    [data-testid="stMetricValue"] {
        color: #f4df9b !important;
        font-size: 1.75rem;
        font-weight: 700;
    }

    /* ================= CARDS ================= */

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(
            145deg,
            rgba(17, 48, 39, 0.96),
            rgba(9, 31, 25, 0.96)
        );
        border: 1px solid rgba(200, 169, 91, 0.20) !important;
        border-radius: 18px !important;
        padding: 0.65rem !important;
        margin-bottom: 1rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.16);
    }

    /* ================= NOTIFICATION CARD ================= */

    .notification-title {
        color: #f5f0df;
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 0.25rem;
    }

    .notification-message {
        color: #aaa998;
        font-size: 0.91rem;
        line-height: 1.55;
    }

    .notification-date {
        color: #858d82;
        font-size: 0.78rem;
        margin-bottom: 0.45rem;
    }

    .notification-icon {
        font-size: 2rem;
        text-align: center;
        padding-top: 0.45rem;
    }

    /* ================= BUTTONS ================= */

    .stButton > button {
        background: linear-gradient(
            135deg,
            #c8a95b,
            #a98a43
        );
        color: #102018 !important;
        border: none;
        border-radius: 10px;
        font-weight: 700;
        min-height: 44px;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(
            135deg,
            #ddc276,
            #c8a95b
        );
        color: #071b16 !important;
        transform: translateY(-1px);
    }

    /* ================= ALERTS ================= */

    [data-testid="stAlert"] {
        border-radius: 13px !important;
        border-width: 1px !important;
    }

    /* ================= SECTION LABEL ================= */

    .section-label {
        color: #c8a95b;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }

    /* ================= FOOTER ================= */

    .page-footer {
        text-align: center;
        color: #737c72;
        font-size: 0.78rem;
        padding-top: 2rem;
        line-height: 1.7;
    }

    hr {
        border-color: rgba(200, 169, 91, 0.16) !important;
        margin: 1.6rem 0;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="page-eyebrow">MY SCHOLARSHIP</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="page-title">🔔 Notifications & Alerts</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="page-subtitle">'
    f'{student_name} &nbsp;•&nbsp; Student ID: {student_id}'
    f'</div>',
    unsafe_allow_html=True
)


# =========================================================
# NOTIFICATION SUMMARY
# =========================================================

st.markdown(
    '<div class="section-label">Notification Overview</div>',
    unsafe_allow_html=True
)

st.markdown("### 📊 Notification Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Notifications",
        "6"
    )

with col2:
    st.metric(
        "Unread",
        "3"
    )

with col3:
    st.metric(
        "Action Required",
        "2"
    )


# =========================================================
# ACTION REQUIRED
# =========================================================

st.divider()

st.markdown("### ⚠️ Action Required")

st.warning(
    "📄 **Income Certificate Verification Pending**\n\n"
    "Your income certificate is currently under verification. "
    "Please check the Documents section for more details."
)

st.warning(
    "🏫 **Institution Certificate Missing**\n\n"
    "Upload your institution certificate to complete the "
    "document verification process."
)


# =========================================================
# RECENT NOTIFICATIONS
# =========================================================

st.divider()

st.markdown("### 🕒 Recent Notifications")

notifications = [
    {
        "icon": "💰",
        "title": "DBT Payment Processed",
        "message": (
            "Your Top Class Scholarship payment of ₹42,000 "
            "has been successfully processed."
        ),
        "date": "18 Sep 2026",
        "type": "success"
    },
    {
        "icon": "🔍",
        "title": "Institution Verification Started",
        "message": (
            "Your Post-Matric Scholarship application has "
            "entered the institution verification stage."
        ),
        "date": "17 Sep 2026",
        "type": "info"
    },
    {
        "icon": "📄",
        "title": "Document Verification Pending",
        "message": (
            "Your income certificate is awaiting verification."
        ),
        "date": "16 Sep 2026",
        "type": "warning"
    },
    {
        "icon": "🎓",
        "title": "Application Submitted",
        "message": (
            "Your Post-Matric Scholarship application was "
            "successfully submitted."
        ),
        "date": "15 Sep 2026",
        "type": "success"
    },
    {
        "icon": "📋",
        "title": "Document Uploaded",
        "message": (
            "Your academic marksheet has been uploaded "
            "to your digital document wallet."
        ),
        "date": "14 Sep 2026",
        "type": "info"
    },
    {
        "icon": "🌿",
        "title": "Welcome to VanVidhya",
        "message": (
            "Your unified scholarship dashboard is ready. "
            "You can track applications, documents and payments "
            "from one place."
        ),
        "date": "12 Sep 2026",
        "type": "info"
    }
]


for notification in notifications:

    with st.container(border=True):

        col1, col2, col3 = st.columns([0.8, 5.5, 1.5])

        # ---------------- ICON ----------------

        with col1:

            st.markdown(
                f"""
                <div class="notification-icon">
                    {notification['icon']}
                </div>
                """,
                unsafe_allow_html=True
            )

        # ---------------- MESSAGE ----------------

        with col2:

            st.markdown(
                f"""
                <div class="notification-title">
                    {notification['title']}
                </div>

                <div class="notification-message">
                    {notification['message']}
                </div>
                """,
                unsafe_allow_html=True
            )

        # ---------------- DATE / TYPE ----------------

        with col3:

            st.markdown(
                f"""
                <div class="notification-date">
                    {notification['date']}
                </div>
                """,
                unsafe_allow_html=True
            )

            if notification["type"] == "success":

                st.success("Completed")

            elif notification["type"] == "warning":

                st.warning("Action Needed")

            else:

                st.info("Update")


# =========================================================
# APPLICATION STATUS ALERTS
# =========================================================

st.divider()

st.markdown("### 📌 Application Status Alerts")

col1, col2 = st.columns(2)

with col1:

    st.info(
        "**Post-Matric Scholarship**\n\n"
        "🟡 Institution Verification → In Progress"
    )

with col2:

    st.success(
        "**Top Class Scholarship**\n\n"
        "🟢 Sanctioned → DBT Processed"
    )


# =========================================================
# NOTIFICATION PREFERENCES
# =========================================================

st.divider()

st.markdown("### ⚙️ Notification Preferences")

col1, col2 = st.columns(2)

with col1:

    st.checkbox(
        "Application status updates",
        value=True
    )

    st.checkbox(
        "Document verification alerts",
        value=True
    )

with col2:

    st.checkbox(
        "Scholarship payment alerts",
        value=True
    )

    st.checkbox(
        "Important deadline reminders",
        value=True
    )


if st.button(
    "💾 Save Notification Preferences",
    use_container_width=True
):

    st.success(
        "Notification preferences saved successfully."
    )


# =========================================================
# NAVIGATION
# =========================================================

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    if st.button(
        "← Dashboard",
        use_container_width=True
    ):
        st.switch_page(
            "pages/dashboard.py"
        )

with col2:

    if st.button(
        "📋 Applications",
        use_container_width=True
    ):
        st.switch_page(
            "pages/applications.py"
        )

with col3:

    if st.button(
        "💰 Payments",
        use_container_width=True
    ):
        st.switch_page(
            "pages/payment.py"
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="page-footer">
        VANVIDHYA<br>
        A Unified Digital Gateway for Tribal Student Scholarships<br>
        SMART INDIA HACKATHON 2026 · CoreSynch
    </div>
    """,
    unsafe_allow_html=True
)