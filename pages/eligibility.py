import streamlit as st

st.set_page_config(
    page_title="Eligibility | VanVidhya",
    page_icon="✅",
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
   APP BACKGROUND
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
    max-width: 1400px;
}


/* =====================================================
   NORMAL TEXT
   ===================================================== */

p {
    color: #D6DED8;
}

h1, h2, h3 {
    color: #F4F0E6 !important;
}


/* =====================================================
   INPUT CARDS
   ===================================================== */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background:
        linear-gradient(
            145deg,
            rgba(21, 48, 37, 0.96),
            rgba(10, 28, 21, 0.98)
        );

    border: 1px solid rgba(201, 164, 92, 0.20);
    border-radius: 18px;
    padding: 8px;
}


/* =====================================================
   INPUT LABELS
   ===================================================== */

label {
    color: #D6DED8 !important;
    font-weight: 500;
}


/* =====================================================
   SELECT BOX
   ===================================================== */

div[data-baseweb="select"] > div {
    background-color: #10271E !important;
    border-color: rgba(201, 164, 92, 0.25) !important;
    color: #F2EAD8 !important;
}


/* =====================================================
   NUMBER INPUT
   ===================================================== */

input {
    background-color: #10271E !important;
    border-color: rgba(201, 164, 92, 0.25) !important;
    color: #F2EAD8 !important;
}


/* =====================================================
   BUTTON
   ===================================================== */

.stButton > button {
    min-height: 46px;
    border-radius: 11px;
    font-weight: 700;

    background: #B9914D;
    color: #101A15;

    border: 1px solid #D4B36E;

    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: #D2AE66;
    border-color: #E2C37F;
    color: #071812;

    box-shadow:
        0 6px 20px
        rgba(201, 164, 92, 0.18);
}


/* =====================================================
   ALERTS
   ===================================================== */

div[data-testid="stAlert"] {
    border-radius: 13px;
}


/* =====================================================
   EXPANDER
   ===================================================== */

div[data-testid="stExpander"] {
    background: rgba(14, 38, 28, 0.85);
    border: 1px solid rgba(201, 164, 92, 0.18);
    border-radius: 13px;
}


/* =====================================================
   DIVIDER
   ===================================================== */

hr {
    border-color: rgba(201, 164, 92, 0.15) !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# PAGE HEADER
# =========================================================

st.caption("SMART SCHOLARSHIP ASSISTANCE")

st.title("✅ Smart Eligibility Checker")

st.write(
    "Check your scholarship eligibility using the VanVidhya prototype."
)


# =========================================================
# SELECTED SCHOLARSHIP
# =========================================================

selected_scheme = st.session_state.get(
    "selected_scheme",
    "Select a Scholarship"
)

st.info(
    f"🎓 **Checking Eligibility For:** {selected_scheme}"
)


# =========================================================
# STUDENT INFORMATION
# =========================================================

st.subheader("👤 Student Information")

st.caption(
    "Provide your basic academic and scholarship information below."
)

st.write("")


# =========================================================
# INPUT COLUMNS
# =========================================================

col1, col2 = st.columns(2, gap="large")


# =========================================================
# PERSONAL & FINANCIAL DETAILS
# =========================================================

with col1:

    with st.container(border=True):

        st.subheader("🧾 Personal & Financial Details")

        community = st.selectbox(
            "Community Category",
            [
                "ST",
                "SC",
                "OBC",
                "General"
            ]
        )

        annual_income = st.number_input(
            "Annual Family Income (₹)",
            min_value=0,
            value=150000,
            step=10000
        )

        course_level = st.selectbox(
            "Current Education Level",
            [
                "School",
                "Diploma",
                "Undergraduate",
                "Postgraduate",
                "PhD",
                "Overseas Higher Education"
            ]
        )


# =========================================================
# ACADEMIC & SCHOLARSHIP DETAILS
# =========================================================

with col2:

    with st.container(border=True):

        st.subheader("🎓 Academic & Scholarship Details")

        academic_score = st.number_input(
            "Academic Score (%)",
            min_value=0.0,
            max_value=100.0,
            value=75.0
        )

        institution_type = st.selectbox(
            "Institution",
            [
                "Government Institution",
                "Government-Aided Institution",
                "Eligible Private Institution"
            ]
        )

        existing_scholarship = st.selectbox(
            "Currently Receiving Another Scholarship?",
            [
                "No",
                "Yes"
            ]
        )


# =========================================================
# CHECK BUTTON
# =========================================================

st.write("")

if st.button(
    "🔍  Check My Eligibility",
    use_container_width=True
):

    eligible = True
    reasons = []


    # -----------------------------------------------------
    # COMMUNITY
    # -----------------------------------------------------

    if community != "ST":

        eligible = False

        reasons.append(
            "Student does not belong to the ST category."
        )


    # -----------------------------------------------------
    # INCOME
    # -----------------------------------------------------

    if annual_income > 250000:

        reasons.append(
            "Income may exceed the assumed prototype threshold."
        )


    # -----------------------------------------------------
    # EXISTING SCHOLARSHIP
    # -----------------------------------------------------

    if existing_scholarship == "Yes":

        reasons.append(
            "Existing scholarship/fellowship must be checked "
            "before applying."
        )


    # =====================================================
    # ELIGIBLE
    # =====================================================

    if eligible:

        st.success(
            f"🎉 You appear eligible for **{selected_scheme}** "
            "based on the prototype criteria."
        )

        st.info(
            "Final eligibility is subject to official scheme rules "
            "and verification by the concerned authority."
        )


        # -------------------------------------------------
        # NEXT STEPS
        # -------------------------------------------------

        st.subheader("🚀 Next Steps")

        step1, step2, step3, step4 = st.columns(4)


        with step1:
            st.metric(
                "STEP 01",
                "Documents"
            )
            st.caption(
                "Verify your documents"
            )


        with step2:
            st.metric(
                "STEP 02",
                "Application"
            )
            st.caption(
                "Submit the application"
            )


        with step3:
            st.metric(
                "STEP 03",
                "Verification"
            )
            st.caption(
                "Complete institutional verification"
            )


        with step4:
            st.metric(
                "STEP 04",
                "DBT",
            )
            st.caption(
                "Track sanction and DBT status"
            )


    # =====================================================
    # NOT ELIGIBLE
    # =====================================================

    else:

        st.error(
            "⚠️ You may not currently meet the prototype "
            "eligibility criteria."
        )

        st.subheader(
            "📌 Reason / Action Required"
        )

        for reason in reasons:

            st.write(
                f"• {reason}"
            )


# =========================================================
# ABOUT
# =========================================================

st.write("")

with st.expander("ℹ️ About this Eligibility Checker"):

    st.write(
        "This is a prototype eligibility engine designed "
        "for the VanVidhya demonstration."
    )

    st.write(
        "In a production implementation, eligibility rules "
        "can be connected to authorized government scheme data, "
        "student records and verification services."
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "VANVIDHYA • A Unified Digital Gateway for Tribal Student Scholarships"
)

st.caption(
    "SMART INDIA HACKATHON 2026 • CoreSynch"
)