import streamlit as st
import pandas as pd

from navigation import show_navigation


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="VanVidhya | Admin Dashboard",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# LOGIN CHECK
# =========================================================

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()


# =========================================================
# VANVIDHYA NAVIGATION
# =========================================================

show_navigation()


# =========================================================
# VANVIDHYA THEME
# =========================================================

st.markdown(
    """
<style>

/* ===================================================== */
/* MAIN APPLICATION                                      */
/* ===================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 88% 4%,
            rgba(196, 165, 87, 0.10),
            transparent 24%
        ),
        radial-gradient(
            circle at 8% 90%,
            rgba(24, 91, 68, 0.12),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #071f18 0%,
            #0b2b22 48%,
            #061812 100%
        );

    color: #f4efdf;
}


/* ===================================================== */
/* MAIN CONTAINER                                        */
/* ===================================================== */

.main .block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ===================================================== */
/* GENERAL TEXT                                          */
/* ===================================================== */

h1,
h2,
h3,
h4,
h5,
h6 {
    color: #f3ead0 !important;
}

p,
label,
.stMarkdown {
    color: #d8d2c1;
}


/* ===================================================== */
/* PAGE HEADER                                           */
/* ===================================================== */

.admin-eyebrow {
    color: #d1b15d;
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.admin-title {
    color: #f4ead0;
    font-size: 2.2rem;
    font-weight: 800;
    margin-top: 0.2rem;
}

.admin-subtitle {
    color: #a9aa9d;
    font-size: 0.92rem;
    margin-top: 0.15rem;
}


/* ===================================================== */
/* SECTION LABEL                                         */
/* ===================================================== */

.section-label {
    color: #d6b65e;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 1.4px;
    text-transform: uppercase;
}


/* ===================================================== */
/* SECTION DESCRIPTION                                   */
/* ===================================================== */

.section-description {
    color: #a9aa9d;
    font-size: 0.82rem;
    margin-top: -0.3rem;
    margin-bottom: 1rem;
}


/* ===================================================== */
/* ADMIN BADGE                                           */
/* ===================================================== */

.admin-badge {
    background:
        linear-gradient(
            145deg,
            #153c30,
            #0d281f
        );

    border: 1px solid rgba(
        196,
        165,
        87,
        0.35
    );

    border-radius: 14px;
    padding: 16px 18px;
    text-align: center;
}

.admin-badge-title {
    color: #e7cf84;
    font-weight: 800;
    font-size: 0.9rem;
}

.admin-badge-subtitle {
    color: #aab3a9;
    font-size: 0.72rem;
    margin-top: 3px;
}


/* ===================================================== */
/* METRIC CARDS                                          */
/* ===================================================== */

div[data-testid="stMetric"] {

    background:
        linear-gradient(
            145deg,
            #102f26,
            #0b251d
        ) !important;

    border: 1px solid rgba(
        196,
        165,
        87,
        0.27
    ) !important;

    border-radius: 15px !important;

    padding: 17px !important;

    box-shadow:
        0 8px 24px rgba(
            0,
            0,
            0,
            0.16
        ) !important;
}


div[data-testid="stMetric"] label {
    color: #aeb4aa !important;
    font-size: 0.72rem !important;
}


div[data-testid="stMetricValue"] {
    color: #ead078 !important;
    font-size: 1.7rem !important;
    font-weight: 800 !important;
}


div[data-testid="stMetricDelta"] {
    color: #a9c4b5 !important;
    font-size: 0.68rem !important;
}


/* ===================================================== */
/* DATAFRAME                                             */
/* ===================================================== */

div[data-testid="stDataFrame"] {

    background-color: #0f2d24 !important;

    border: 1px solid rgba(
        196,
        165,
        87,
        0.24
    ) !important;

    border-radius: 14px !important;

    overflow: hidden !important;
}


/* ===================================================== */
/* BUTTONS                                               */
/* ===================================================== */

.stButton > button {

    background:
        linear-gradient(
            135deg,
            #a9873d,
            #c4a557
        ) !important;

    color: #10241c !important;

    border: none !important;

    border-radius: 10px !important;

    font-weight: 800 !important;

    min-height: 42px;

    transition: 0.2s ease;
}


.stButton > button:hover {

    background:
        linear-gradient(
            135deg,
            #c4a557,
            #d8bd73
        ) !important;

    color: #071a15 !important;

    transform: translateY(-1px);
}


/* ===================================================== */
/* TEXT INPUT                                            */
/* ===================================================== */

.stTextInput input {

    background-color: #102f26 !important;

    color: #f5f0df !important;

    border: 1px solid rgba(
        196,
        165,
        87,
        0.35
    ) !important;

    border-radius: 10px !important;
}


.stTextInput input::placeholder {
    color: #7f8e85 !important;
}


/* ===================================================== */
/* SELECT BOX                                            */
/* ===================================================== */

div[data-baseweb="select"] > div {

    background-color: #102f26 !important;

    color: #f5f0df !important;

    border: 1px solid rgba(
        196,
        165,
        87,
        0.35
    ) !important;

    border-radius: 10px !important;
}


/* ===================================================== */
/* ALERTS                                                */
/* ===================================================== */

div[data-testid="stAlert"] {

    background:
        linear-gradient(
            145deg,
            #102f26,
            #0c271f
        ) !important;

    border-radius: 13px !important;

    border: 1px solid rgba(
        196,
        165,
        87,
        0.25
    ) !important;

    color: #eee7d4 !important;
}


/* ===================================================== */
/* DIVIDER                                               */
/* ===================================================== */

hr {

    border-color:
        rgba(
            196,
            165,
            87,
            0.22
        ) !important;
}


/* ===================================================== */
/* INFO / SUCCESS / WARNING                              */
/* ===================================================== */

div[data-testid="stAlert"] p {
    color: #ddd8c8 !important;
}


/* ===================================================== */
/* FOOTER                                                */
/* ===================================================== */

.admin-footer {
    text-align: center;
    color: #7f8e85;
    font-size: 0.72rem;
    padding-top: 20px;
    line-height: 1.7;
}


/* ===================================================== */
/* SMALL CARD                                            */
/* ===================================================== */

.feature-card {

    background:
        linear-gradient(
            145deg,
            #102f26,
            #0b251d
        );

    border: 1px solid rgba(
        196,
        165,
        87,
        0.25
    );

    border-radius: 14px;

    padding: 18px;

    min-height: 130px;
}


/* ===================================================== */
/* HIDE STREAMLIT BRANDING                               */
/* ===================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# PAGE HEADER
# =========================================================

header_left, header_right = st.columns(
    [4.3, 1],
    vertical_alignment="center"
)


with header_left:

    st.markdown(
        '<div class="admin-eyebrow">'
        'MINISTRY ADMINISTRATION PORTAL'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="admin-title">'
        'Scholarship Administration'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="admin-subtitle">'
        'Unified monitoring, verification and beneficiary intelligence'
        '</div>',
        unsafe_allow_html=True
    )


with header_right:

    st.markdown(
        """
        <div class="admin-badge">
            <div class="admin-badge-title">
                🛡️ Administrator
            </div>
            <div class="admin-badge-subtitle">
                Secure Administration Portal
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# =========================================================
# SYSTEM OVERVIEW
# =========================================================

st.markdown(
    '<div class="section-label">SYSTEM OVERVIEW</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Current scholarship ecosystem at a glance'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# ROW 1
# ---------------------------------------------------------

c1, c2, c3, c4 = st.columns(4)


with c1:

    st.metric(
        "👥 Registered ST Students",
        "12,480",
        "Enrolled students"
    )


with c2:

    st.metric(
        "📋 Total Applications",
        "8,742",
        "Across active schemes"
    )


with c3:

    st.metric(
        "⏳ Verification Pending",
        "1,286",
        "Requires action"
    )


with c4:

    st.metric(
        "✓ Sanctioned Applications",
        "7,456",
        "Approved applications"
    )


st.write("")


# ---------------------------------------------------------
# ROW 2
# ---------------------------------------------------------

c1, c2, c3, c4 = st.columns(4)


with c1:

    st.metric(
        "₹ DBT Processed",
        "6,914",
        "Successfully processed"
    )


with c2:

    st.metric(
        "⚠ Document Mismatches",
        "438",
        "Needs verification"
    )


with c3:

    st.metric(
        "🔎 Manual Review Cases",
        "192",
        "Official intervention"
    )


with c4:

    st.metric(
        "📢 Students Requiring Outreach",
        "1,034",
        "Potential gap cases"
    )


st.divider()


# =========================================================
# SCHEME-WISE APPLICATIONS
# =========================================================

st.markdown(
    '<div class="section-label">SCHOLARSHIP ANALYTICS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Application volume and processing status by scholarship scheme'
    '</div>',
    unsafe_allow_html=True
)


scheme_data = pd.DataFrame(
    {
        "Scholarship Scheme": [
            "Pre-Matric Scholarship",
            "Post-Matric Scholarship",
            "Top Class Scholarship",
            "National Fellowship for ST Students",
            "National Overseas Scholarship"
        ],

        "Applications": [
            2180,
            3945,
            1760,
            612,
            245
        ],

        "Under Verification": [
            320,
            610,
            210,
            118,
            28
        ],

        "Sanctioned": [
            1940,
            3280,
            1510,
            470,
            256
        ]
    }
)


st.dataframe(
    scheme_data,
    use_container_width=True,
    hide_index=True
)


st.write("")


st.bar_chart(
    scheme_data.set_index(
        "Scholarship Scheme"
    )[
        [
            "Applications",
            "Sanctioned"
        ]
    ],
    height=280
)


st.divider()


# =========================================================
# APPLICATION PROCESSING
# =========================================================

st.markdown(
    '<div class="section-label">APPLICATION PROCESSING</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Current distribution across the unified verification pipeline'
    '</div>',
    unsafe_allow_html=True
)


left, right = st.columns(
    [1.25, 0.75]
)


with left:

    status_data = pd.DataFrame(
        {
            "Status": [
                "Submitted",
                "Institution Verification",
                "Document Verification",
                "Ministry Verification",
                "Sanctioned",
                "DBT Processed"
            ],

            "Applications": [
                520,
                1286,
                438,
                732,
                1542,
                4224
            ]
        }
    )

    st.dataframe(
        status_data,
        use_container_width=True,
        hide_index=True
    )


with right:

    st.info(
        """
        🔄 **Unified Processing Flow**

        **01**  Application Submitted

        ↓

        **02**  Institution Verification

        ↓

        **03**  Document Verification

        ↓

        **04**  Ministry Verification

        ↓

        **05**  Sanction

        ↓

        **06**  DBT Processing
        """
    )


st.divider()


# =========================================================
# MANUAL REVIEW
# =========================================================

st.markdown(
    '<div class="section-label">MANUAL REVIEW QUEUE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Cases requiring official intervention'
    '</div>',
    unsafe_allow_html=True
)


st.warning(
    "⚠️ 192 CASES REQUIRE REVIEW"
)


review_cases = [
    {
        "Student ID": "VV2026001",
        "Issue": "Income Certificate Mismatch",
        "Source": "State e-District",
        "Status": "Pending Review"
    },

    {
        "Student ID": "VV2026048",
        "Issue": "ST Certificate Verification Failed",
        "Source": "State Database",
        "Status": "Pending Review"
    },

    {
        "Student ID": "VV2026091",
        "Issue": "Academic Record Mismatch",
        "Source": "APAAR / Institution",
        "Status": "Pending Review"
    },

    {
        "Student ID": "VV2026127",
        "Issue": "Duplicate Scholarship Record",
        "Source": "NSP / SFMP",
        "Status": "Under Investigation"
    }
]


st.dataframe(
    pd.DataFrame(review_cases),
    use_container_width=True,
    hide_index=True
)


b1, b2 = st.columns(2)


with b1:

    if st.button(
        "🔍 Review Selected Cases",
        use_container_width=True
    ):

        st.info(
            "Manual review workspace opened."
        )


with b2:

    if st.button(
        "✓ Mark Review Completed",
        use_container_width=True
    ):

        st.success(
            "Selected case marked for completion."
        )


st.divider()


# =========================================================
# INSTITUTION-WISE MONITORING
# =========================================================

st.markdown(
    '<div class="section-label">INSTITUTION MONITORING</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Scholarship activity across participating institutions'
    '</div>',
    unsafe_allow_html=True
)


institution_data = pd.DataFrame(
    {
        "Institution": [
            "Government Arts & Science College",
            "Tribal Welfare Residential College",
            "Government Engineering College",
            "State University",
            "Government Higher Secondary School"
        ],

        "Students": [
            1840,
            1260,
            980,
            2150,
            3050
        ],

        "Applications": [
            1420,
            980,
            720,
            1560,
            2180
        ],

        "Pending Verification": [
            210,
            164,
            92,
            238,
            310
        ]
    }
)


st.dataframe(
    institution_data,
    use_container_width=True,
    hide_index=True
)


st.divider()


# =========================================================
# BENEFICIARY GAP DETECTION
# =========================================================

st.markdown(
    '<div class="section-label">BENEFICIARY INTELLIGENCE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Identifying potentially eligible students outside the scholarship pipeline'
    '</div>',
    unsafe_allow_html=True
)


st.info(
    """
    🔎 **Beneficiary Gap Detection**

    VanVidhya can identify enrolled ST students who appear
    potentially eligible but are not currently receiving a
    scholarship by matching authorized student and scholarship
    records.
    """
)


g1, g2, g3 = st.columns(3)


with g1:

    st.metric(
        "👥 Enrolled ST Students",
        "12,480"
    )


with g2:

    st.metric(
        "✓ Receiving Scholarship",
        "11,446"
    )


with g3:

    st.metric(
        "⚠ Potential Unreached Students",
        "1,034"
    )


if st.button(
    "🔍 Run Beneficiary Gap Detection",
    use_container_width=True
):

    st.success(
        "Prototype matching completed. "
        "1,034 potential unreached students identified "
        "for further eligibility verification and outreach."
    )


st.divider()


# =========================================================
# GOVERNMENT INTEGRATION LAYER
# =========================================================

st.markdown(
    '<div class="section-label">GOVERNMENT INTEGRATION LAYER</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Data sources supporting unified scholarship intelligence'
    '</div>',
    unsafe_allow_html=True
)


st.success(
    "🟢 SYSTEM MONITORED"
)


integration_data = pd.DataFrame(
    {
        "Data Source": [
            "NSP",
            "SFMP",
            "NOS Portal",
            "DigiLocker",
            "UDISE+",
            "APAAR",
            "AISHE",
            "State e-District"
        ],

        "Integration": [
            "Connected",
            "Connected",
            "API Ready",
            "Connected",
            "API Ready",
            "API Ready",
            "API Ready",
            "API Ready"
        ],

        "Purpose": [
            "Scholarship Applications",
            "Scholarship Applications",
            "Overseas Scholarship",
            "Digital Documents",
            "Student Enrollment",
            "Student Identity / Academic Data",
            "Higher Education Data",
            "Certificate Verification"
        ]
    }
)


st.dataframe(
    integration_data,
    use_container_width=True,
    hide_index=True
)


st.caption(
    "Prototype status represents the proposed integration architecture. "
    "Production deployment requires authorized government APIs "
    "and access permissions."
)


st.divider()


# =========================================================
# STUDENT / APPLICATION SEARCH
# =========================================================

st.markdown(
    '<div class="section-label">RECORD SEARCH</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Quickly locate student or application records for verification'
    '</div>',
    unsafe_allow_html=True
)


s1, s2 = st.columns(
    [1, 2]
)


with s1:

    search_type = st.selectbox(
        "Search By",
        [
            "Student ID",
            "Application ID",
            "Mobile Number"
        ]
    )


with s2:

    search_value = st.text_input(
        "Enter Search Value",
        placeholder="Example: VV2026001"
    )


if st.button(
    "🔍 Search Record",
    use_container_width=True
):

    if search_value.strip():

        st.success(
            f"Search completed for "
            f"{search_type}: {search_value}"
        )

        st.info(
            """
            **Student Record Found**

            Student Category: ST

            Scholarship Status: Under Verification

            Pending Action: Income Certificate Verification
            """
        )

    else:

        st.warning(
            "Please enter a search value."
        )


st.divider()


# =========================================================
# ADMINISTRATIVE ACTIONS
# =========================================================

st.markdown(
    '<div class="section-label">ADMINISTRATIVE ACTIONS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Quick access to frequently used administration modules'
    '</div>',
    unsafe_allow_html=True
)


a1, a2, a3, a4 = st.columns(4)


with a1:

    st.markdown("### 📋")

    st.markdown(
        "**Applications**"
    )

    st.caption(
        "Monitor scholarship applications"
    )

    st.button(
        "Open Applications",
        key="open_applications",
        use_container_width=True
    )


with a2:

    st.markdown("### 📄")

    st.markdown(
        "**Documents**"
    )

    st.caption(
        "Verify submitted documents"
    )

    st.button(
        "Open Documents",
        key="open_documents",
        use_container_width=True
    )


with a3:

    st.markdown("### 💰")

    st.markdown(
        "**DBT Monitoring**"
    )

    st.caption(
        "Track payment processing"
    )

    st.button(
        "Open DBT",
        key="open_dbt",
        use_container_width=True
    )


with a4:

    st.markdown("### 📢")

    st.markdown(
        "**Outreach**"
    )

    st.caption(
        "Reach potential beneficiaries"
    )

    st.button(
        "Open Outreach",
        key="open_outreach",
        use_container_width=True
    )


st.divider()


# =========================================================
# ADMIN SUMMARY
# =========================================================

st.markdown(
    '<div class="section-label">ADMINISTRATION SUMMARY</div>',
    unsafe_allow_html=True
)


st.success(
    "🌿 VanVidhya Unified Scholarship Administration"
)


st.caption(
    "Centralized monitoring for scholarship applications, "
    "verification, beneficiary identification and transparent DBT tracking."
)


# =========================================================
# FOOTER
# =========================================================

st.divider()


st.caption(
    "🏛️ VANVIDHYA • MINISTRY ADMINISTRATION PORTAL"
)

st.caption(
    "Scholarship Intelligence & Beneficiary Access Platform"
)

st.caption(
    "SMART INDIA HACKATHON 2026 • CoreSynch"
)