import streamlit as st
from navigation import show_navigation

st.set_page_config(
    page_title="Document Wallet | VanVidhya",
    page_icon="📄",
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
        padding: 0.75rem !important;
        margin-bottom: 1rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.16);
    }

    /* ================= DOCUMENT CARD ================= */

    .document-description {
        color: #aaa998;
        font-size: 0.88rem;
        line-height: 1.5;
        margin-bottom: 0.8rem;
    }

    .document-icon {
        font-size: 2rem;
        margin-bottom: 0.25rem;
    }

    .document-status {
        font-size: 0.8rem;
        font-weight: 650;
        letter-spacing: 0.2px;
    }

    /* ================= SECTION ================= */

    .section-eyebrow {
        color: #c8a95b;
        font-size: 0.76rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 0.3rem;
    }

    /* ================= UPLOAD AREA ================= */

    [data-testid="stFileUploader"] {
        background: rgba(16, 45, 36, 0.55);
        border: 1px dashed rgba(200, 169, 91, 0.35);
        border-radius: 15px;
        padding: 0.5rem;
    }

    /* ================= SELECTBOX ================= */

    div[data-baseweb="select"] > div {
        background-color: #102d24 !important;
        border-color: rgba(200, 169, 91, 0.25) !important;
        color: #f5f0df !important;
        border-radius: 10px !important;
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

    /* ================= ALERTS ================= */

    [data-testid="stAlert"] {
        border-radius: 13px !important;
        border-width: 1px !important;
    }

    /* ================= DIGILOCKER ================= */

    .digilocker-card {
        background:
            linear-gradient(
                145deg,
                rgba(20, 54, 43, 0.95),
                rgba(10, 31, 25, 0.95)
            );
        border: 1px solid rgba(200, 169, 91, 0.25);
        border-radius: 18px;
        padding: 1.4rem;
        margin-top: 0.5rem;
    }

    .digilocker-title {
        color: #f5f0df;
        font-size: 1.1rem;
        font-weight: 700;
    }

    .digilocker-text {
        color: #aaa998;
        font-size: 0.9rem;
        line-height: 1.6;
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
    '<div class="page-title">📄 Document Wallet</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="page-subtitle">'
    'Store, verify and reuse your scholarship documents from one place.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# DOCUMENT SUMMARY
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Documents",
        "6"
    )

with col2:
    st.metric(
        "Verified",
        "4"
    )

with col3:
    st.metric(
        "Pending / Missing",
        "2"
    )


# =========================================================
# DOCUMENT DATA
# =========================================================

documents = [
    {
        "name": "Identity / Aadhaar Document",
        "status": "Verified",
        "icon": "🪪"
    },
    {
        "name": "ST Certificate",
        "status": "Verified",
        "icon": "📜"
    },
    {
        "name": "Income Certificate",
        "status": "Pending Verification",
        "icon": "💰"
    },
    {
        "name": "Academic Marksheet",
        "status": "Verified",
        "icon": "🎓"
    },
    {
        "name": "Domicile Certificate",
        "status": "Verified",
        "icon": "🏠"
    },
    {
        "name": "Institution Certificate",
        "status": "Missing",
        "icon": "🏫"
    }
]


# =========================================================
# MY DOCUMENTS
# =========================================================

st.divider()

st.markdown("### 📁 My Documents")

st.caption(
    "Documents available for scholarship verification and reuse."
)


for i in range(0, len(documents), 2):

    cols = st.columns(2)

    for j, col in enumerate(cols):

        index = i + j

        if index >= len(documents):
            break

        doc = documents[index]

        with col:

            with st.container(border=True):

                st.markdown(
                    f"""
                    <div class="document-icon">
                        {doc['icon']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"### {doc['name']}"
                )

                if doc["status"] == "Verified":

                    st.success(
                        "✓ Verified"
                    )

                    st.caption(
                        "Available for reuse in eligible applications."
                    )

                elif doc["status"] == "Pending Verification":

                    st.warning(
                        "⚠ Pending Verification"
                    )

                    st.caption(
                        "Submitted and awaiting verification."
                    )

                else:

                    st.error(
                        "✕ Missing"
                    )

                    st.caption(
                        "Required before submitting the application."
                    )


                if st.button(
                    "View Details",
                    key=f"view_{index}",
                    use_container_width=True
                ):

                    if doc["status"] == "Verified":

                        st.info(
                            "Document is verified and available "
                            "for reuse in eligible scholarship applications."
                        )

                    elif doc["status"] == "Pending Verification":

                        st.warning(
                            "This document has been submitted "
                            "and is awaiting verification."
                        )

                    else:

                        st.warning(
                            "This document is required. "
                            "Please upload it before submitting the application."
                        )


# =========================================================
# UPLOAD DOCUMENT
# =========================================================

st.divider()

st.markdown("### 📤 Upload a Document")

st.caption(
    "Upload a new document for verification and future scholarship applications."
)

document_type = st.selectbox(
    "Select Document Type",
    [
        "Identity / Aadhaar Document",
        "ST Certificate",
        "Income Certificate",
        "Academic Marksheet",
        "Domicile Certificate",
        "Institution Certificate"
    ]
)

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["pdf", "jpg", "jpeg", "png"]
)

if uploaded_file:

    st.success(
        f"✓ Uploaded: {uploaded_file.name}"
    )

    if st.button(
        "🔍 Submit for Verification",
        use_container_width=True
    ):

        st.success(
            f"{document_type} submitted successfully for verification."
        )

        st.info(
            "Prototype verification layer: document received. "
            "In the production system, authorized verification "
            "services can validate the document."
        )


# =========================================================
# DIGILOCKER
# =========================================================

st.divider()

st.markdown("### 🔐 DigiLocker Integration")

with st.container(border=True):

    st.markdown(
        '<div class="digilocker-title">'
        'Secure Digital Document Access'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        '<div class="digilocker-text">'
        'Securely retrieve eligible digital documents instead of '
        'repeatedly uploading the same files. Connected documents '
        'can be reused across eligible scholarship applications.'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "🔗 Connect DigiLocker",
        use_container_width=True
    ):

        st.session_state["digilocker_connected"] = True


    if st.session_state.get(
        "digilocker_connected",
        False
    ):

        st.success(
            "✓ DigiLocker connected successfully!"
        )

        st.info(
            "Demo Integration: Digital documents are available "
            "for retrieval through the connected document wallet."
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown("📜 **ST Certificate**")
            st.success("Available")

        with col2:

            st.markdown("🎓 **Academic Record**")
            st.success("Available")

        with col3:

            st.markdown("🏠 **Domicile Certificate**")
            st.success("Available")


# =========================================================
# SECURITY
# =========================================================

st.divider()

st.markdown("### 🛡️ Document Security")

st.info(
    "🔒 Documents are intended to be protected through "
    "authentication, authorization and encrypted storage "
    "in the production system."
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