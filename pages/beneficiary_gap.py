import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Beneficiary Gap Detection | VanVidhya",
    page_icon="🔎",
    layout="wide"
)

from navigation import show_navigation


# =========================================================
# LOGIN CHECK
# =========================================================

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()


# =========================================================
# NAVIGATION
# =========================================================

show_navigation()


# =========================================================
# CSS ONLY
# =========================================================

st.markdown("""
<style>

/* =====================================================
   APP
   ===================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 85% 8%,
            rgba(201, 164, 92, 0.08),
            transparent 28%
        ),
        radial-gradient(
            circle at 8% 85%,
            rgba(31, 76, 57, 0.24),
            transparent 35%
        ),
        #071812;

    color: #F4F0E6;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}


/* =====================================================
   TEXT
   ===================================================== */

p {
    color: #D6DED8;
}

h1,
h2,
h3 {
    color: #F4F0E6 !important;
}


/* =====================================================
   METRIC CARDS
   ===================================================== */

div[data-testid="stMetric"] {
    background:
        linear-gradient(
            145deg,
            rgba(21, 48, 37, 0.96),
            rgba(10, 28, 21, 0.98)
        );

    border:
        1px solid
        rgba(201, 164, 92, 0.20);

    border-radius: 16px;

    padding: 18px;
}

div[data-testid="stMetricLabel"] {
    color: #9DAEA3 !important;
}

div[data-testid="stMetricValue"] {
    color: #E2BE73 !important;
}


/* =====================================================
   BORDER CONTAINERS
   ===================================================== */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background:
        linear-gradient(
            145deg,
            rgba(21, 48, 37, 0.96),
            rgba(10, 28, 21, 0.98)
        );

    border:
        1px solid
        rgba(201, 164, 92, 0.20);

    border-radius: 18px;

    padding: 8px;
}


/* =====================================================
   BUTTONS
   ===================================================== */

.stButton > button {
    min-height: 44px;

    border-radius: 10px;

    font-weight: 650;

    background: #173B2D;

    color: #F2EAD8;

    border:
        1px solid
        rgba(201, 164, 92, 0.38);

    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: #214D3A;

    border-color: #C9A45C;

    color: #FFFFFF;

    box-shadow:
        0 5px 18px
        rgba(0, 0, 0, 0.20);
}


/* =====================================================
   PRIMARY MATCHING BUTTON
   ===================================================== */

div[data-testid="stButton"] button[kind="primary"] {
    background: #B9914D;
    color: #101A15;
    border-color: #D4B36E;
}

div[data-testid="stButton"] button[kind="primary"]:hover {
    background: #D2AE66;
    color: #071812;
}


/* =====================================================
   TABLE
   ===================================================== */

div[data-testid="stDataFrame"] {
    border:
        1px solid
        rgba(201, 164, 92, 0.18);

    border-radius: 12px;

    overflow: hidden;
}


/* =====================================================
   ALERTS
   ===================================================== */

div[data-testid="stAlert"] {
    border-radius: 13px;
}


/* =====================================================
   DIVIDER
   ===================================================== */

hr {
    border-color:
        rgba(201, 164, 92, 0.15) !important;
}


/* =====================================================
   EXPANDER
   ===================================================== */

div[data-testid="stExpander"] {
    background:
        rgba(14, 38, 28, 0.85);

    border:
        1px solid
        rgba(201, 164, 92, 0.18);

    border-radius: 13px;
}


/* =====================================================
   CAPTIONS
   ===================================================== */

.stCaption {
    color: #899C91 !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# PAGE HEADER
# =========================================================

st.caption("BENEFICIARY INTELLIGENCE")

st.title("🔎 Beneficiary Gap Detection")

st.write(
    "Identify enrolled ST students who may not be receiving "
    "available scholarship support."
)


# =========================================================
# OVERVIEW
# =========================================================

st.subheader("📊 Beneficiary Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Enrolled ST Students",
        "12,480"
    )

with col2:
    st.metric(
        "Scholarship Beneficiaries",
        "11,446"
    )

with col3:
    st.metric(
        "Potential Gaps",
        "1,034"
    )

with col4:
    st.metric(
        "Records Matched",
        "91.7%"
    )


# =========================================================
# DATA SOURCES
# =========================================================

st.divider()

st.subheader("🔗 Data Matching Sources")

col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.subheader("UDISE+")
        st.caption("Student Enrollment")
        st.write(
            "Enrollment records used to identify "
            "students currently studying in eligible institutions."
        )

with col2:
    with st.container(border=True):
        st.subheader("APAAR")
        st.caption("Academic Identity")
        st.write(
            "Academic identity information used for "
            "student-level record matching."
        )

with col3:
    with st.container(border=True):
        st.subheader("OTR")
        st.caption("Scholarship Registration")
        st.write(
            "Scholarship registration records used "
            "to identify existing scholarship activity."
        )

with col4:
    with st.container(border=True):
        st.subheader("Scholarship Records")
        st.caption("Application & Beneficiary Data")
        st.write(
            "Application, sanction and beneficiary "
            "records used for consolidated matching."
        )


# =========================================================
# MATCHING PROCESS
# =========================================================

st.divider()

st.subheader("⚙️ Beneficiary Matching Process")

st.info(
    "Student records are matched using authorized identifiers "
    "and verified attributes. Potential gaps are flagged for "
    "further eligibility verification."
)

steps = [
    "Student Enrollment",
    "Identity Matching",
    "Scholarship Record Matching",
    "Eligibility Check",
    "Gap Detection",
    "Student Outreach"
]

step_cols = st.columns(6)

for index, step in enumerate(steps):

    with step_cols[index]:

        with st.container(border=True):

            st.caption(
                f"STEP {index + 1:02d}"
            )

            st.write(
                f"**{step}**"
            )


st.write("")


# =========================================================
# RUN MATCHING
# =========================================================

if st.button(
    "🚀 Run Beneficiary Matching",
    use_container_width=True,
    type="primary"
):

    st.success(
        "Matching completed successfully."
    )

    st.session_state[
        "gap_detection_run"
    ] = True

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Records Processed",
            "12,480"
        )

    with col2:
        st.metric(
            "Successful Matches",
            "11,446"
        )

    with col3:
        st.metric(
            "Potential Gaps",
            "1,034"
        )


# =========================================================
# POTENTIAL UNREACHED STUDENTS
# =========================================================

st.divider()

st.subheader("⚠️ Potential Unreached Students")

st.caption(
    "Students identified through prototype record matching "
    "who do not currently have a corresponding scholarship record."
)

gap_data = pd.DataFrame({

    "Student ID": [
        "VV-GAP-001",
        "VV-GAP-002",
        "VV-GAP-003",
        "VV-GAP-004",
        "VV-GAP-005",
        "VV-GAP-006"
    ],

    "Education Level": [
        "Class 10",
        "Undergraduate",
        "Class 12",
        "Undergraduate",
        "Postgraduate",
        "Class 11"
    ],

    "Enrollment Source": [
        "UDISE+",
        "APAAR",
        "UDISE+",
        "AISHE",
        "AISHE",
        "UDISE+"
    ],

    "Scholarship Record": [
        "Not Found",
        "Not Found",
        "Not Found",
        "Not Found",
        "Not Found",
        "Not Found"
    ],

    "Potential Action": [
        "Eligibility Verification",
        "Eligibility Verification",
        "Eligibility Verification",
        "Eligibility Verification",
        "Eligibility Verification",
        "Eligibility Verification"
    ]
})

st.dataframe(
    gap_data,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# GAP CATEGORIES
# =========================================================

st.divider()

st.subheader("📌 Potential Gap Categories")

gap_reason_data = pd.DataFrame({

    "Potential Reason": [
        "No Scholarship Application Found",
        "Application Incomplete",
        "Documents Pending",
        "Eligibility Not Checked",
        "Application Rejected / Closed"
    ],

    "Students": [
        482,
        176,
        148,
        136,
        92
    ]
})

st.dataframe(
    gap_reason_data,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# OUTREACH
# =========================================================

st.divider()

st.subheader("📢 Student Outreach")

col1, col2 = st.columns(2, gap="large")


# ---------------------------------------------------------
# ACTIONS
# ---------------------------------------------------------

with col1:

    with st.container(border=True):

        st.subheader("🎯 Outreach Actions")

        if st.button(
            "📱 Send Student Notifications",
            use_container_width=True
        ):

            st.success(
                "Prototype notification campaign created "
                "for identified students."
            )

        if st.button(
            "🏫 Notify Institutions",
            use_container_width=True
        ):

            st.success(
                "Prototype institution outreach notification created."
            )


# ---------------------------------------------------------
# MESSAGE
# ---------------------------------------------------------

with col2:

    with st.container(border=True):

        st.subheader("📢 Outreach Message")

        st.write(
            "You may be eligible for a Government scholarship. "
            "Please check your scholarship eligibility and "
            "complete the required application process."
        )

        st.info(
            "Students can use **VanVidhya + JAGO** "
            "for scholarship assistance."
        )


# =========================================================
# PROTOTYPE NOTICE
# =========================================================

st.divider()

st.warning(
    "⚠️ **Prototype Notice**\n\n"
    "The records shown here are simulated demo data. "
    "Production implementation would require authorized "
    "access to UDISE+, APAAR, OTR and scholarship databases "
    "with appropriate privacy, security and consent controls."
)


# =========================================================
# NAVIGATION
# =========================================================

st.divider()

st.subheader("🔗 Quick Navigation")

col1, col2, col3 = st.columns(3)

with col1:

    if st.button(
        "⬅️ Admin Dashboard",
        use_container_width=True
    ):

        st.switch_page(
            "pages/admin_dashboard.py"
        )


with col2:

    if st.button(
        "🤖 JAGO",
        use_container_width=True
    ):

        st.switch_page(
            "pages/jago.py"
        )


with col3:

    if st.button(
        "🏠 Student Dashboard",
        use_container_width=True
    ):

        st.switch_page(
            "pages/dashboard.py"
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "VANVIDHYA • Beneficiary Gap Detection & Student Outreach"
)

st.caption(
    "SMART INDIA HACKATHON 2026 • CoreSynch"
)