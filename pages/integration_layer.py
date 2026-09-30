import streamlit as st
import pandas as pd

from navigation import show_navigation


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Integration Layer | VanVidhya",
    page_icon="🔗",
    layout="wide"
)


# =========================================================
# LOGIN CHECK
# =========================================================

if not st.session_state.get("logged_in", False):
    st.switch_page("pages/student_login.py")


show_navigation()


# =========================================================
# CUSTOM THEME
# =========================================================

st.markdown(
    """
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 85% 5%,
                rgba(184, 150, 74, 0.08),
                transparent 25%
            ),
            linear-gradient(
                135deg,
                #071c17 0%,
                #0b241e 45%,
                #061712 100%
            );
        color: #f4f0e6;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1450px;
    }

    h1, h2, h3, h4 {
        color: #f4f0e6 !important;
    }

    p, label, .stCaption {
        color: #c9d0c8 !important;
    }

    hr {
        border-color: rgba(184, 150, 74, 0.22) !important;
    }


    /* ---------- HEADER ---------- */

    .hero-title {
        font-size: 2.35rem;
        font-weight: 800;
        color: #f5f0e4;
        letter-spacing: -0.5px;
        margin-bottom: 0.15rem;
    }

    .hero-subtitle {
        color: #bfc8bf;
        font-size: 1rem;
        margin-bottom: 1.4rem;
    }


    /* ---------- METRICS ---------- */

    div[data-testid="stMetric"] {
        background: linear-gradient(
            145deg,
            #102c24,
            #0b211b
        );
        border: 1px solid rgba(184, 150, 74, 0.30);
        border-radius: 14px;
        padding: 16px 18px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.18);
    }

    div[data-testid="stMetricLabel"] {
        color: #bfc8bf !important;
    }

    div[data-testid="stMetricValue"] {
        color: #e7c875 !important;
    }


    /* ---------- CONTAINERS ---------- */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(12, 35, 29, 0.78);
        border: 1px solid rgba(184, 150, 74, 0.22);
        border-radius: 14px;
    }


    /* ---------- BUTTONS ---------- */

    .stButton > button {
        border-radius: 10px;
        min-height: 44px;
        font-weight: 650;
        border: 1px solid rgba(184, 150, 74, 0.40);
        background: #12352b;
        color: #f4f0e6;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #d1af5b;
        color: #f2d27c;
        background: #174237;
        transform: translateY(-1px);
    }


    /* ---------- TABLE ---------- */

    div[data-testid="stDataFrame"] {
        border: 1px solid rgba(184, 150, 74, 0.20);
        border-radius: 12px;
        overflow: hidden;
    }


    /* ---------- SELECTBOX ---------- */

    div[data-baseweb="select"] > div {
        background: #102c24;
        border-color: rgba(184, 150, 74, 0.30);
        color: #f4f0e6;
    }


    /* ---------- INFO / SUCCESS / WARNING ---------- */

    div[data-testid="stAlert"] {
        border-radius: 12px;
    }


    /* ---------- CODE BLOCK ---------- */

    pre {
        border: 1px solid rgba(184, 150, 74, 0.20) !important;
        border-radius: 12px !important;
    }


    /* ---------- SIDEBAR ---------- */

    section[data-testid="stSidebar"] {
        background: #071a15;
        border-right: 1px solid rgba(184, 150, 74, 0.20);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="hero-title">🔗 Unified Verification & Integration Layer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'Connect scholarship systems, government data sources and verification services through one unified layer.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# SYSTEM OVERVIEW
# =========================================================

st.subheader("📊 Integration Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Connected Sources",
        "8",
        "All systems configured"
    )

with col2:
    st.metric(
        "Records Synced",
        "12,480",
        "Student records"
    )

with col3:
    st.metric(
        "Verified Records",
        "11,892",
        "95.3% verified"
    )

with col4:
    st.metric(
        "Exceptions",
        "588",
        "Requires attention"
    )

st.divider()


# =========================================================
# GOVERNMENT DATA SOURCES
# =========================================================

st.subheader("🏛️ Connected Government Systems")

st.caption(
    "Unified connectivity status across scholarship and authorized government data sources."
)

integration_data = pd.DataFrame({
    "System": [
        "National Scholarship Portal (NSP)",
        "SFMP",
        "National Overseas Scholarship (NOS)",
        "DigiLocker",
        "UDISE+",
        "APAAR",
        "AISHE",
        "State e-District"
    ],
    "Purpose": [
        "Scholarship Applications",
        "Scholarship Applications",
        "Overseas Scholarship",
        "Digital Documents",
        "School Enrollment",
        "Academic Identity",
        "Higher Education Records",
        "Certificate Verification"
    ],
    "Connection": [
        "API Ready",
        "API Ready",
        "API Ready",
        "API Ready",
        "API Ready",
        "API Ready",
        "API Ready",
        "API Ready"
    ],
    "Status": [
        "🟢 Active",
        "🟢 Active",
        "🟢 Active",
        "🟢 Active",
        "🟢 Active",
        "🟢 Active",
        "🟢 Active",
        "🟢 Active"
    ]
})

st.dataframe(
    integration_data,
    use_container_width=True,
    hide_index=True
)

st.divider()


# =========================================================
# SYNC CONTROLS
# =========================================================

st.subheader("🔄 Data Synchronization")

st.caption(
    "Synchronize records from connected systems and initiate unified verification."
)

selected_source = st.selectbox(
    "Select Data Source",
    [
        "All Systems",
        "NSP",
        "SFMP",
        "NOS",
        "DigiLocker",
        "UDISE+",
        "APAAR",
        "AISHE",
        "State e-District"
    ]
)

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "🔄 Synchronize Records",
        use_container_width=True
    ):
        st.success(
            f"Synchronization completed successfully for {selected_source}."
        )

with col2:
    if st.button(
        "🔍 Start Verification",
        use_container_width=True
    ):
        st.success(
            "Unified verification process started successfully."
        )

st.divider()


# =========================================================
# VERIFICATION ENGINE
# =========================================================

st.subheader("⚙️ Unified Verification Engine")

st.info(
    "The verification engine compares student information across connected "
    "sources and identifies matching records, missing information and data inconsistencies."
)

verification_data = pd.DataFrame({
    "Verification Field": [
        "Student Identity",
        "ST Certificate",
        "Income Certificate",
        "Academic Record",
        "Institution",
        "Scholarship Application",
        "Previous Scholarship"
    ],
    "Primary Source": [
        "APAAR / Authorized Identity",
        "State e-District",
        "State e-District",
        "APAAR / AISHE / UDISE+",
        "UDISE+ / AISHE",
        "NSP / SFMP / NOS",
        "Scholarship Databases"
    ],
    "Verification": [
        "Match",
        "Match",
        "Mismatch",
        "Match",
        "Match",
        "Match",
        "Match"
    ],
    "Action": [
        "Auto Process",
        "Auto Process",
        "Manual Review",
        "Auto Process",
        "Auto Process",
        "Auto Process",
        "Auto Process"
    ]
})

st.dataframe(
    verification_data,
    use_container_width=True,
    hide_index=True
)

st.divider()


# =========================================================
# EXCEPTION MANAGEMENT
# =========================================================

st.subheader("⚠️ Exception & Mismatch Management")

st.caption(
    "Records requiring additional verification are routed to the appropriate review process."
)

exceptions = [
    {
        "Student ID": "VV2026001",
        "Field": "Income Certificate",
        "Expected": "₹1,50,000",
        "Received": "₹2,40,000",
        "Action": "Manual Review"
    },
    {
        "Student ID": "VV2026048",
        "Field": "ST Certificate",
        "Expected": "Verified",
        "Received": "Verification Pending",
        "Action": "Manual Review"
    },
    {
        "Student ID": "VV2026091",
        "Field": "Academic Record",
        "Expected": "72%",
        "Received": "68%",
        "Action": "Review Required"
    },
    {
        "Student ID": "VV2026127",
        "Field": "Previous Scholarship",
        "Expected": "No Active Scholarship",
        "Received": "Record Found",
        "Action": "Eligibility Review"
    }
]

exception_df = pd.DataFrame(exceptions)

st.dataframe(
    exception_df,
    use_container_width=True,
    hide_index=True
)

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "👨‍💼 Send to Manual Review",
        use_container_width=True
    ):
        st.success(
            "Selected exception has been forwarded to the manual verification queue."
        )

with col2:
    if st.button(
        "✅ Resolve Verified Exceptions",
        use_container_width=True
    ):
        st.success(
            "Verified exceptions have been marked as resolved."
        )

st.divider()


# =========================================================
# VERIFICATION WORKFLOW
# =========================================================

st.subheader("🔄 Unified Verification Workflow")

st.caption(
    "End-to-end flow from student information capture to automated processing or manual review."
)

workflow = [
    ("1", "Student Profile"),
    ("2", "Data Synchronization"),
    ("3", "Identity Matching"),
    ("4", "Document Verification"),
    ("5", "Eligibility Rules"),
    ("6", "Match / Mismatch"),
    ("7", "Auto Process / Manual Review")
]

cols = st.columns(7)

for col, (number, step) in zip(cols, workflow):
    with col:
        with st.container(border=True):
            st.markdown(
                f"### {number}"
            )
            st.caption(step)

st.divider()


# =========================================================
# INTEGRATION ARCHITECTURE
# =========================================================

st.subheader("🧩 Integration Architecture")

st.caption(
    "Prototype architecture showing how VanVidhya coordinates scholarship systems, "
    "verification services and government data sources."
)

st.code(
"""
                         VANVIDHYA
                             │
                   Unified API Gateway
                             │
              ┌──────────────┴──────────────┐
              │                             │
      Verification Engine           Eligibility Engine
              │                             │
       ┌──────┼──────┐                ┌─────┼─────┐
       │      │      │                │     │     │
      NSP    SFMP   NOS              ST   Income Academic
       │      │      │
       └──────┼──────┘
              │
       Government Data Layer
              │
    ┌─────────┼────────────────┐
    │         │        │       │
DigiLocker  UDISE+   APAAR    AISHE
    │         │        │       │
    └─────────┴────────┴───────┘
              │
       State e-District
              │
       Verification Result
              │
        ┌─────┴─────┐
        │           │
      Match      Mismatch
        │           │
   Auto Process  Manual Review
""",
    language="text"
)

st.divider()


# =========================================================
# SECURITY
# =========================================================

st.subheader("🔐 Security & Privacy")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🔑 OTP Authentication")

with col2:
    st.info("👥 Role-Based Access")

with col3:
    st.info("🔒 Encrypted Data")

with col4:
    st.info("📝 Audit Logs")

st.warning(
    "Production deployment requires authorized government API access, "
    "consent mechanisms, privacy controls and secure handling of student information."
)

st.divider()


# =========================================================
# NAVIGATION
# =========================================================

st.subheader("Quick Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button(
        "⬅️ Admin Dashboard",
        use_container_width=True
    ):
        st.switch_page("pages/admin_dashboard.py")

with col2:
    if st.button(
        "🔎 Gap Detection",
        use_container_width=True
    ):
        st.switch_page("pages/beneficiary_gap.py")

with col3:
    if st.button(
        "🤖 JAGO",
        use_container_width=True
    ):
        st.switch_page("pages/jago.py")


st.divider()


# =========================================================
# FOOTER
# =========================================================

st.caption(
    "VANVIDHYA • Unified Verification & Integration Layer • SMART INDIA HACKATHON 2026 • CoreSynch"
)