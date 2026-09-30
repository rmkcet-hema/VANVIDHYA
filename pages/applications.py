import streamlit as st
from navigation import show_navigation

st.set_page_config(
    page_title="Applications | VanVidhya",
    page_icon="📋",
    layout="wide"
)

# =========================================================
# LOGIN CHECK
# =========================================================

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

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
                circle at 85% 10%,
                rgba(180, 145, 70, 0.07),
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

    p, label, span, div {
        color: inherit;
    }

    [data-testid="stCaptionContainer"] {
        color: #bdb9a9 !important;
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
        color: #bdb9a9;
        font-size: 1rem;
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
        min-height: 115px;
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

    /* ================= APPLICATION CARD ================= */

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(
            145deg,
            rgba(17, 48, 39, 0.96),
            rgba(9, 31, 25, 0.96)
        );
        border: 1px solid rgba(200, 169, 91, 0.20) !important;
        border-radius: 20px !important;
        padding: 0.7rem !important;
        margin-bottom: 1.4rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.18);
    }

    /* ================= PROGRESS ================= */

    [data-testid="stProgressBar"] {
        background-color: #17372d !important;
        border-radius: 20px;
    }

    [data-testid="stProgressBar"] > div > div {
        background-color: #c8a95b !important;
        border-radius: 20px;
    }

    /* ================= STATUS BOXES ================= */

    [data-testid="stAlert"] {
        border-radius: 12px !important;
        border-width: 1px !important;
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

    /* ================= DIVIDER ================= */

    hr {
        border-color: rgba(200, 169, 91, 0.16) !important;
        margin: 1.5rem 0;
    }

    /* ================= TIMELINE ================= */

    .timeline-title {
        color: #c8a95b;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
    }

    /* ================= INFO ROW ================= */

    .info-label {
        color: #989d91;
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }

    .info-value {
        color: #f5f0df;
        font-size: 0.96rem;
        font-weight: 600;
        margin-top: 2px;
    }

    /* ================= FOOTER ================= */

    .page-footer {
        text-align: center;
        color: #737c72;
        font-size: 0.78rem;
        padding-top: 2rem;
        line-height: 1.7;
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
    '<div class="page-title">📋 My Applications</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="page-subtitle">'
    'Track your scholarship applications from submission to disbursement.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# APPLICATION DATA
# =========================================================

applications = [
    {
        "scheme": "Post-Matric Scholarship",
        "application_id": "VV-PMS-2026-001",
        "status": "Document Verification",
        "progress": 0.60,
        "institution": "Government Arts & Science College",
        "amount": "₹18,500",
    },
    {
        "scheme": "Top Class Scholarship",
        "application_id": "VV-TCS-2026-002",
        "status": "Sanctioned",
        "progress": 0.85,
        "institution": "Eligible Higher Education Institution",
        "amount": "₹42,000",
    }
]


# =========================================================
# SUMMARY
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Applications",
        "2"
    )

with col2:
    st.metric(
        "Under Verification",
        "1"
    )

with col3:
    st.metric(
        "Sanctioned",
        "1"
    )

with col4:
    st.metric(
        "Pending Action",
        "1"
    )


st.divider()


# =========================================================
# APPLICATION CARDS
# =========================================================

for app in applications:

    with st.container(border=True):

        # -------------------------------------------------
        # APPLICATION HEADER
        # -------------------------------------------------

        col1, col2 = st.columns([3.5, 1])

        with col1:

            st.markdown(
                f"### 🎓 {app['scheme']}"
            )

            st.markdown(
                f"""
                <div class="info-label">Application ID</div>
                <div class="info-value">{app['application_id']}</div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

            st.markdown(
                f"""
                <div class="info-label">Institution</div>
                <div class="info-value">{app['institution']}</div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.metric(
                "Scholarship Amount",
                app["amount"]
            )


        st.write("")


        # -------------------------------------------------
        # STATUS
        # -------------------------------------------------

        status_col, progress_col = st.columns([1.2, 3])

        with status_col:

            st.markdown(
                '<div class="info-label">Current Status</div>',
                unsafe_allow_html=True
            )

            if app["status"] == "Document Verification":

                st.warning(
                    "📄 Document Verification"
                )

            elif app["status"] == "Sanctioned":

                st.success(
                    "✓ Sanctioned"
                )


        with progress_col:

            st.markdown(
                '<div class="info-label">Application Progress</div>',
                unsafe_allow_html=True
            )

            st.progress(app["progress"])

            st.caption(
                f"{int(app['progress'] * 100)}% completed"
            )


        # -------------------------------------------------
        # APPLICATION JOURNEY
        # -------------------------------------------------

        st.markdown(
            '<div class="timeline-title">Application Journey</div>',
            unsafe_allow_html=True
        )

        stages = [
            (
                "1",
                "Application Submitted",
                True
            ),
            (
                "2",
                "Institution Verification",
                True
            ),
            (
                "3",
                "Document Verification",
                app["status"] in [
                    "Document Verification",
                    "Sanctioned"
                ]
            ),
            (
                "4",
                "Ministry Verification",
                app["status"] == "Sanctioned"
            ),
            (
                "5",
                "Sanction",
                app["status"] == "Sanctioned"
            ),
            (
                "6",
                "DBT / Disbursement",
                False
            )
        ]

        timeline_cols = st.columns(6)

        for index, (number, stage, completed) in enumerate(stages):

            with timeline_cols[index]:

                if completed:

                    st.success(
                        f"✓ {number}\n\n{stage}"
                    )

                else:

                    st.info(
                        f"○ {number}\n\n{stage}"
                    )


        # -------------------------------------------------
        # ACTION MESSAGE
        # -------------------------------------------------

        st.write("")

        if app["status"] == "Document Verification":

            st.warning(
                "⚠️ Action Required: "
                "Your documents are currently under verification."
            )

        elif app["status"] == "Sanctioned":

            st.success(
                "🎉 Scholarship sanctioned successfully!"
            )


# =========================================================
# NEW APPLICATION
# =========================================================

st.divider()

st.markdown(
    "### ➕ Start a New Application"
)

st.caption(
    "Explore available scholarship schemes and check your eligibility."
)

if st.button(
    "Browse Scholarship Schemes  →",
    use_container_width=True
):

    st.switch_page(
        "pages/scholarships.py"
    )


# =========================================================
# FOOTER
# =========================================================

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