import streamlit as st

st.set_page_config(
    page_title="Scholarships | VanVidhya",
    page_icon="🎓",
    layout="wide"
)

from navigation import show_navigation


# ---------------------------------------------------------
# LOGIN CHECK
# ---------------------------------------------------------

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()


# ---------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------

show_navigation()


# ---------------------------------------------------------
# PAGE STYLING
# ---------------------------------------------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 85% 10%, rgba(194, 150, 63, 0.08), transparent 28%),
        radial-gradient(circle at 10% 85%, rgba(30, 72, 57, 0.25), transparent 35%),
        #071812;
    color: #F4F0E6;
}

/* Main content */

.block-container {
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* Page Header */

.scholarship-eyebrow {
    color: #C9A45C;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

.scholarship-title {
    color: #F4F0E6;
    font-size: 2.35rem;
    font-weight: 700;
    margin-bottom: 0.25rem;
}

.scholarship-subtitle {
    color: #B9C4BC;
    font-size: 1rem;
    margin-bottom: 1.4rem;
}

/* Top info banner */

.info-banner {
    background: linear-gradient(
        135deg,
        rgba(28, 67, 51, 0.95),
        rgba(15, 42, 31, 0.95)
    );
    border: 1px solid rgba(201, 164, 92, 0.35);
    border-radius: 16px;
    padding: 18px 22px;
    margin-bottom: 1.8rem;
}

.info-title {
    color: #E0BD73;
    font-weight: 700;
    font-size: 0.95rem;
    margin-bottom: 5px;
}

.info-text {
    color: #D6DED8;
    font-size: 0.88rem;
    line-height: 1.55;
}

/* Cards */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(
        145deg,
        rgba(21, 48, 37, 0.96),
        rgba(10, 28, 21, 0.98)
    );
    border: 1px solid rgba(201, 164, 92, 0.20);
    border-radius: 18px;
    padding: 6px;
    transition: all 0.2s ease;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: rgba(201, 164, 92, 0.55);
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.28);
}

/* Card headings */

h3 {
    color: #F3EBD9 !important;
    font-size: 1.15rem !important;
}

/* Captions */

.stCaption {
    color: #C9A45C !important;
}

/* Normal text */

.stMarkdown,
.stText,
p,
label {
    color: #D8DED9;
}

/* Buttons */

.stButton > button {
    border-radius: 10px;
    min-height: 42px;
    font-weight: 600;
    transition: all 0.2s ease;
}

.stButton > button[kind="secondary"] {
    background: #173B2D;
    color: #F2EAD8;
    border: 1px solid rgba(201, 164, 92, 0.38);
}

.stButton > button[kind="secondary"]:hover {
    background: #214D3A;
    border-color: #C9A45C;
    color: #FFFFFF;
}

/* Info box */

div[data-testid="stAlert"] {
    background: rgba(20, 51, 38, 0.85);
    border: 1px solid rgba(201, 164, 92, 0.30);
    color: #E7E2D6;
    border-radius: 12px;
}

/* Divider */

hr {
    border-color: rgba(201, 164, 92, 0.15) !important;
}

/* Footer */

.scholarship-footer {
    margin-top: 3rem;
    padding-top: 1.2rem;
    border-top: 1px solid rgba(201, 164, 92, 0.16);
    text-align: center;
    color: #7F9287;
    font-size: 0.78rem;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# PAGE HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="scholarship-eyebrow">SCHOLARSHIP DISCOVERY</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="scholarship-title">Scholarship Schemes</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="scholarship-subtitle">'
    'Explore scholarship opportunities available through VanVidhya.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# INFORMATION BANNER
# ---------------------------------------------------------

st.markdown("""
<div class="info-banner">

<div class="info-title">
🎓 One Platform. Five Scholarship Opportunities.
</div>

<div class="info-text">
Explore Pre-Matric, Post-Matric, Top Class, National Fellowship
and National Overseas Scholarship schemes in one unified view.
Check your eligibility and continue directly to the application flow.
</div>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# SCHOLARSHIP DATA
# ---------------------------------------------------------

scholarships = [
    {
        "name": "Pre-Matric Scholarship",
        "level": "School Education",
        "icon": "📚",
        "description": (
            "Financial assistance for eligible ST students "
            "studying at the pre-matric level."
        ),
        "eligibility": [
            "Student must belong to ST community",
            "Must satisfy applicable income criteria",
            "Must be studying in an eligible institution"
        ]
    },
    {
        "name": "Post-Matric Scholarship",
        "level": "Higher Education",
        "icon": "🎓",
        "description": (
            "Financial support for eligible ST students "
            "pursuing post-matric education."
        ),
        "eligibility": [
            "Student must belong to ST community",
            "Must be pursuing an eligible course",
            "Must satisfy applicable income criteria"
        ]
    },
    {
        "name": "Top Class Scholarship",
        "level": "Higher / Professional Education",
        "icon": "🏆",
        "description": (
            "Support for eligible ST students pursuing "
            "higher education in notified institutions."
        ),
        "eligibility": [
            "Student must belong to ST community",
            "Must be admitted to an eligible institution",
            "Must satisfy scheme-specific conditions"
        ]
    },
    {
        "name": "National Fellowship for ST Students",
        "level": "Research / PhD",
        "icon": "🔬",
        "description": (
            "Fellowship support for eligible ST students "
            "pursuing higher research studies."
        ),
        "eligibility": [
            "Student must belong to ST community",
            "Must satisfy fellowship eligibility requirements",
            "Must meet applicable academic conditions"
        ]
    },
    {
        "name": "National Overseas Scholarship",
        "level": "Overseas Higher Education",
        "icon": "🌍",
        "description": (
            "Financial assistance for eligible ST students "
            "pursuing higher studies abroad."
        ),
        "eligibility": [
            "Student must belong to ST community",
            "Must satisfy academic requirements",
            "Must meet scheme-specific conditions"
        ]
    }
]


# ---------------------------------------------------------
# SCHOLARSHIP CARDS
# ---------------------------------------------------------

for i in range(0, len(scholarships), 2):

    cols = st.columns(2, gap="large")

    for j, col in enumerate(cols):

        index = i + j

        if index >= len(scholarships):
            break

        scheme = scholarships[index]

        with col:

            with st.container(border=True):

                # Scheme title
                st.subheader(
                    f"{scheme['icon']}  {scheme['name']}"
                )

                # Education level
                st.caption(
                    f"◈  {scheme['level']}"
                )

                st.write("")

                # Description
                st.write(
                    scheme["description"]
                )

                st.write("")

                # Eligibility heading
                st.markdown(
                    "**Basic Eligibility**"
                )

                # Eligibility points
                for item in scheme["eligibility"]:
                    st.markdown(
                        f"✓  {item}"
                    )

                st.write("")

                # Buttons
                col_a, col_b = st.columns(2, gap="small")

                with col_a:

                    if st.button(
                        "Check Eligibility →",
                        key=f"eligibility_{index}",
                        use_container_width=True
                    ):

                        st.session_state[
                            "selected_scheme"
                        ] = scheme["name"]

                        st.switch_page(
                            "pages/eligibility.py"
                        )

                with col_b:

                    if st.button(
                        "View Details",
                        key=f"details_{index}",
                        use_container_width=True
                    ):

                        st.session_state[
                            f"show_{index}"
                        ] = not st.session_state.get(
                            f"show_{index}",
                            False
                        )

                # Details
                if st.session_state.get(
                    f"show_{index}",
                    False
                ):

                    st.info(
                        f"""
**{scheme['name']}**

**Level:** {scheme['level']}

This section provides scheme information
and guides the student through eligibility,
documents and application requirements.

For the prototype, detailed government
rules can be connected through authorized
scheme data/API integration.
"""
                    )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("""
<div class="scholarship-footer">
VANVIDHYA &nbsp;•&nbsp;
A Unified Digital Gateway for Tribal Student Scholarships
<br>
SMART INDIA HACKATHON 2026 &nbsp;•&nbsp; CoreSynch
</div>
""", unsafe_allow_html=True)