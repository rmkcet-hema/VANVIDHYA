import streamlit as st
import random
from navigation import show_navigation

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Apply Scholarship | VanVidhya",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOGIN CHECK
# =========================================================

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

show_navigation()

student_name = st.session_state.get("student_name", "Ananya")
student_id = st.session_state.get("student_id", "VV2026001")

# =========================================================
# VANVIDHYA THEME
# =========================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background:
            radial-gradient(circle at 85% 10%, rgba(185, 145, 55, 0.08), transparent 25%),
            linear-gradient(135deg, #071f18 0%, #0b2b22 45%, #071a15 100%);
        color: #f5f0df;
    }

    /* Main content */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Headings */
    h1, h2, h3, h4 {
        color: #f3ead0 !important;
    }

    p, label, .stMarkdown, .stCaption {
        color: #dcd6c5;
    }

    /* Selectbox */
    div[data-baseweb="select"] > div {
        background-color: #102f26 !important;
        border: 1px solid #8d7135 !important;
        color: #f5f0df !important;
        border-radius: 10px !important;
    }

    /* Text inputs */
    div[data-baseweb="input"] {
        background-color: #102f26 !important;
        border: 1px solid #8d7135 !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="input"] input {
        color: #f5f0df !important;
    }

    /* Number input */
    div[data-testid="stNumberInput"] input {
        background-color: #102f26 !important;
        color: #f5f0df !important;
    }

    /* Checkbox */
    div[data-testid="stCheckbox"] label {
        color: #ded8c7 !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #a9873d, #c4a557) !important;
        color: #10251d !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        padding: 0.65rem 1rem !important;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #c4a557, #d8bd73) !important;
        color: #071a15 !important;
        transform: translateY(-1px);
    }

    /* Divider */
    hr {
        border-color: rgba(196, 165, 87, 0.25) !important;
    }

    /* Info boxes */
    div[data-testid="stAlert"] {
        background-color: #102f26 !important;
        border: 1px solid rgba(196, 165, 87, 0.35) !important;
        color: #eee6d1 !important;
    }

    /* Progress */
    div[data-testid="stProgressBar"] > div > div {
        background-color: #b89a50 !important;
    }

    /* Metrics */
    div[data-testid="stMetric"] {
        background: linear-gradient(145deg, #102f26, #0d271f);
        border: 1px solid rgba(196, 165, 87, 0.35);
        border-radius: 14px;
        padding: 15px;
    }

    div[data-testid="stMetricLabel"] {
        color: #bcb6a5 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #e8ca76 !important;
    }

    /* Container borders */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: rgba(13, 39, 31, 0.85);
        border: 1px solid rgba(196, 165, 87, 0.28);
        border-radius: 14px;
    }

    /* File uploader */
    div[data-testid="stFileUploader"] {
        background-color: #102f26 !important;
        border: 1px dashed #8d7135 !important;
        border-radius: 12px;
        padding: 10px;
    }

    /* Small caption */
    .small-note {
        color: #aaa58f;
        font-size: 0.85rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# HEADER
# =========================================================

st.title("📝 Apply for Scholarship")
st.caption(
    "Submit your scholarship application through the unified VANVIDHYA platform."
)

st.divider()

# =========================================================
# STUDENT PROFILE
# =========================================================

st.subheader("👤 Student Profile")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Student Name", student_name)

with col2:
    st.metric("Student ID", student_id)

with col3:
    st.metric("Category", "ST")

with col4:
    st.metric("Application Mode", "Online")

st.write("")

# =========================================================
# APPLICATION STATUS
# =========================================================

if "application_submitted" not in st.session_state:
    st.session_state["application_submitted"] = False

if "application_id" not in st.session_state:
    st.session_state["application_id"] = None

if st.session_state["application_submitted"]:

    st.success(
        f"Application submitted successfully! "
        f"Application ID: {st.session_state['application_id']}"
    )

    st.subheader("📍 Application Tracking")

    stages = [
        "Application Submitted",
        "Institution Verification",
        "Document Verification",
        "Ministry Verification",
        "Sanction",
        "DBT / Disbursement"
    ]

    current_stage = 0

    for index, stage in enumerate(stages):

        if index <= current_stage:
            status = "🟢 Completed"
        else:
            status = "⚪ Pending"

        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(f"**{index + 1}. {stage}**")

        with col2:
            st.write(status)

    st.divider()

    st.info(
        "Your application has been successfully recorded in the "
        "VANVIDHYA prototype workflow."
    )

else:

    # =====================================================
    # SCHOLARSHIP SELECTION
    # =====================================================

    st.subheader("🎓 Select Scholarship Scheme")

    st.caption(
        "Choose the scholarship scheme you want to apply for."
    )

    schemes = [
        "Pre-Matric Scholarship",
        "Post-Matric Scholarship",
        "Top Class Scholarship",
        "National Fellowship for ST Students",
        "National Overseas Scholarship"
    ]

    selected_scheme = st.selectbox(
        "Scholarship Scheme",
        schemes
    )

    scheme_info = {
        "Pre-Matric Scholarship":
            "For eligible ST students studying at the pre-matric level.",

        "Post-Matric Scholarship":
            "For eligible ST students pursuing post-matric and higher studies.",

        "Top Class Scholarship":
            "For eligible ST students pursuing higher education in notified institutions.",

        "National Fellowship for ST Students":
            "Supports eligible ST students pursuing advanced research and doctoral studies.",

        "National Overseas Scholarship":
            "Supports eligible ST students pursuing higher studies abroad."
    }

    st.info(scheme_info[selected_scheme])

    st.write("")

    # =====================================================
    # PERSONAL DETAILS
    # =====================================================

    st.subheader("👤 Personal & Academic Details")

    st.caption(
        "Verify your basic information before continuing with the application."
    )

    col1, col2 = st.columns(2)

    with col1:

        full_name = st.text_input(
            "Full Name",
            value=student_name
        )

        community = st.selectbox(
            "Community Category",
            ["ST", "Other"]
        )

        annual_income = st.number_input(
            "Annual Family Income (₹)",
            min_value=0,
            value=150000,
            step=10000
        )

    with col2:

        student_id_input = st.text_input(
            "Student ID",
            value=student_id
        )

        education_level = st.selectbox(
            "Current Education Level",
            [
                "Higher Secondary",
                "Undergraduate",
                "Postgraduate",
                "Ph.D."
            ]
        )

        academic_score = st.number_input(
            "Academic Score (%)",
            min_value=0.0,
            max_value=100.0,
            value=75.0,
            step=0.5
        )

    st.write("")

    # =====================================================
    # INSTITUTION DETAILS
    # =====================================================

    st.subheader("🏫 Institution Details")

    institution = st.text_input(
        "Institution Name",
        value="Government Arts & Science College"
    )

    institution_type = st.selectbox(
        "Institution Type",
        [
            "Government Institution",
            "Government-Aided Institution",
            "Private Institution",
            "Other"
        ]
    )

    st.write("")

    # =====================================================
    # ELIGIBILITY CHECK
    # =====================================================

    st.subheader("✅ Eligibility & Existing Scholarship")

    st.caption(
        "These checks are prototype validations. Final eligibility "
        "depends on official scheme rules and verification."
    )

    col1, col2 = st.columns(2)

    with col1:

        existing_scholarship = st.radio(
            "Currently receiving another scholarship?",
            ["No", "Yes"]
        )

    with col2:

        eligibility_status = st.selectbox(
            "Eligibility Status",
            [
                "I meet the basic eligibility conditions",
                "I need to check eligibility"
            ]
        )

    st.write("")

    # =====================================================
    # DOCUMENT CHECKLIST
    # =====================================================

    st.subheader("📄 Required Documents")

    st.caption(
        "Select the documents you currently have available."
    )

    col1, col2 = st.columns(2)

    with col1:

        aadhaar = st.checkbox(
            "Aadhaar / Identity Document",
            value=True
        )

        st_certificate = st.checkbox(
            "ST Certificate",
            value=True
        )

        income_certificate = st.checkbox(
            "Income Certificate",
            value=True
        )

    with col2:

        marksheet = st.checkbox(
            "Academic Marksheet",
            value=True
        )

        domicile = st.checkbox(
            "Domicile / Residence Certificate",
            value=True
        )

        institution_certificate = st.checkbox(
            "Institution Certificate",
            value=False
        )

    st.info(
        "💡 In the complete VANVIDHYA system, verified documents can "
        "be reused from the Digital Document Wallet / DigiLocker integration."
    )

    st.write("")

    # =====================================================
    # DECLARATION
    # =====================================================

    st.subheader("📌 Declaration")

    declaration = st.checkbox(
        "I confirm that the information provided above is correct "
        "and I agree to the verification of my application details."
    )

    st.write("")

    # =====================================================
    # SUBMIT
    # =====================================================

    if st.button(
        "🚀 Submit Scholarship Application",
        use_container_width=True
    ):

        if not full_name.strip():
            st.error("Please enter your full name.")

        elif not institution.strip():
            st.error("Please enter your institution name.")

        elif not declaration:
            st.error(
                "Please accept the declaration before submitting."
            )

        else:

            application_id = (
                f"VV-APP-2026-"
                f"{random.randint(1000, 9999)}"
            )

            st.session_state["application_submitted"] = True
            st.session_state["application_id"] = application_id
            st.session_state["selected_scheme"] = selected_scheme

            st.success(
                f"🎉 Application submitted successfully!\n\n"
                f"Application ID: **{application_id}**"
            )

            st.balloons()

            st.info(
                "You can track your application status from "
                "the **Applications** section in the sidebar."
            )

# =========================================================
# QUICK NAVIGATION
# =========================================================

st.divider()

st.subheader("⚡ Quick Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button(
        "🎓 Scholarship Schemes",
        use_container_width=True
    ):
        st.switch_page("pages/scholarships.py")

with col2:
    if st.button(
        "📄 Document Wallet",
        use_container_width=True
    ):
        st.switch_page("pages/documents.py")

with col3:
    if st.button(
        "📋 My Applications",
        use_container_width=True
    ):
        st.switch_page("pages/applications.py")

st.divider()

# =========================================================
# FOOTER
# =========================================================

st.caption(
    "VANVIDHYA • A Unified Digital Gateway for Tribal Student Scholarships"
)

st.caption(
    "SMART INDIA HACKATHON 2026 • Team CoreSynch"
)