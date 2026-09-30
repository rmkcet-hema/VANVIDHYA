import streamlit as st
from navigation import show_navigation

st.set_page_config(
    page_title="Payments | VanVidhya",
    page_icon="💰",
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
        min-height: 115px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.18);
    }

    [data-testid="stMetricLabel"] {
        color: #aaa998 !important;
        font-size: 0.82rem;
    }

    [data-testid="stMetricValue"] {
        color: #f4df9b !important;
        font-size: 1.7rem;
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
        padding: 0.7rem !important;
        margin-bottom: 1rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.16);
    }

    /* ================= INFO BOXES ================= */

    [data-testid="stAlert"] {
        border-radius: 13px !important;
        border-width: 1px !important;
    }

    /* ================= BUTTON ================= */

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

    /* ================= LABELS ================= */

    .info-label {
        color: #929a8d;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.25rem;
    }

    .info-value {
        color: #f5f0df;
        font-size: 1.05rem;
        font-weight: 650;
    }

    /* ================= PAYMENT AMOUNT ================= */

    .amount-display {
        color: #f4df9b;
        font-size: 2rem;
        font-weight: 750;
        margin-top: 0.2rem;
    }

    /* ================= FLOW ================= */

    .flow-card {
        background: linear-gradient(
            145deg,
            #102d24,
            #0b211b
        );
        border: 1px solid rgba(200, 169, 91, 0.20);
        border-radius: 15px;
        padding: 1.15rem 0.7rem;
        text-align: center;
        min-height: 125px;
    }

    .flow-number {
        color: #c8a95b;
        font-size: 1.35rem;
        font-weight: 750;
        margin-bottom: 0.5rem;
    }

    .flow-name {
        color: #f5f0df;
        font-size: 0.88rem;
        font-weight: 650;
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
    '<div class="page-title">💰 Scholarship Payments & DBT</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="page-subtitle">'
    f'{student_name} &nbsp;•&nbsp; Student ID: {student_id}'
    f'</div>',
    unsafe_allow_html=True
)


# =========================================================
# PAYMENT SUMMARY
# =========================================================

st.markdown("### 📊 Payment Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Sanctioned",
        "₹60,500"
    )

with col2:
    st.metric(
        "Amount Disbursed",
        "₹42,000"
    )

with col3:
    st.metric(
        "Pending Amount",
        "₹18,500"
    )

with col4:
    st.metric(
        "DBT Status",
        "Processed"
    )


# =========================================================
# CURRENT PAYMENT
# =========================================================

st.divider()

st.markdown("### 💳 Current Scholarship Payment")

st.success(
    "🎓 Top Class Scholarship — Payment successfully processed through DBT."
)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        '<div class="info-label">Sanctioned Amount</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="amount-display">₹42,000</div>',
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        '<div class="info-label">Payment Status</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="info-value">🟢 Processed</div>',
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        '<div class="info-label">Payment Date</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="info-value">18 Sep 2026</div>',
        unsafe_allow_html=True
    )


# =========================================================
# DBT DETAILS
# =========================================================

st.divider()

st.markdown("### 🏦 DBT Transaction Details")

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            '<div class="info-label">Beneficiary ID</div>',
            unsafe_allow_html=True
        )

        st.code("VV-BEN-2026-001")

        st.markdown(
            '<div class="info-label">Payment Reference</div>',
            unsafe_allow_html=True
        )

        st.code("DBT202609180042")


    with col2:

        st.markdown(
            '<div class="info-label">Bank Account</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="info-value">XXXX XXXX 4521</div>',
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            '<div class="info-label">Transaction Status</div>',
            unsafe_allow_html=True
        )

        st.success(
            "Payment successfully credited"
        )


# =========================================================
# PAYMENT HISTORY
# =========================================================

st.divider()

st.markdown("### 📜 Payment History")

payments = [
    {
        "scheme": "Top Class Scholarship",
        "amount": "₹42,000",
        "date": "18 Sep 2026",
        "status": "🟢 Processed",
        "reference": "DBT202609180042"
    },
    {
        "scheme": "Post-Matric Scholarship",
        "amount": "₹18,500",
        "date": "Pending",
        "status": "🟡 Awaiting Sanction",
        "reference": "Not Generated"
    }
]

for payment in payments:

    with st.container(border=True):

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.markdown(
                '<div class="info-label">Scholarship</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="info-value">'
                f'{payment["scheme"]}'
                f'</div>',
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                '<div class="info-label">Amount</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="info-value">'
                f'{payment["amount"]}'
                f'</div>',
                unsafe_allow_html=True
            )

        with col3:

            st.markdown(
                '<div class="info-label">Date</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="info-value">'
                f'{payment["date"]}'
                f'</div>',
                unsafe_allow_html=True
            )

        with col4:

            st.markdown(
                '<div class="info-label">Status</div>',
                unsafe_allow_html=True
            )

            if "Processed" in payment["status"]:

                st.success(
                    payment["status"]
                )

            else:

                st.warning(
                    payment["status"]
                )

        st.caption(
            f"Payment Reference: {payment['reference']}"
        )


# =========================================================
# PENDING PAYMENT
# =========================================================

st.divider()

st.markdown("### ⏳ Pending Payment")

st.warning(
    "Post-Matric Scholarship payment is currently waiting "
    "for final sanction. Payment will be initiated after "
    "the sanction stage is completed."
)

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        '<div class="info-label">Expected Amount</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="amount-display">₹18,500</div>',
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        '<div class="info-label">Current Stage</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="info-value">Ministry Sanction</div>',
        unsafe_allow_html=True
    )


# =========================================================
# PAYMENT FLOW
# =========================================================

st.divider()

st.markdown("### 🔄 Scholarship Payment Flow")

steps = [
    ("1", "Application"),
    ("2", "Verification"),
    ("3", "Sanction"),
    ("4", "DBT Processing"),
    ("5", "Bank Credit")
]

cols = st.columns(5)

for col, (number, step) in zip(cols, steps):

    with col:

        st.markdown(
            f"""
            <div class="flow-card">
                <div class="flow-number">{number}</div>
                <div class="flow-name">{step}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


st.write("")

st.success(
    "✅ Your sanctioned scholarship amount can be tracked "
    "from sanction to final DBT credit in one place."
)


# =========================================================
# NAVIGATION
# =========================================================

st.divider()

if st.button(
    "← Back to Dashboard",
    use_container_width=True
):
    st.switch_page(
        "pages/dashboard.py"
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