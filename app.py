import streamlit as st


# =========================================================
# HTML RENDER HELPER
# =========================================================

def render_html(content):
    clean_html = "\n".join(
        line.strip() for line in content.splitlines()
    )
    st.markdown(clean_html, unsafe_allow_html=True)


# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 85% 10%,
            rgba(82, 130, 91, 0.13),
            transparent 30%
        ),
        radial-gradient(
            circle at 10% 85%,
            rgba(201, 168, 93, 0.06),
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #041F18 0%,
            #063328 48%,
            #05271F 100%
        );

    color: #F5F2E8;
    min-height: 100vh;
}

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

.block-container {
    max-width: 1380px;
    padding-top: 20px;
    padding-bottom: 50px;
}


/* =====================================================
   TOP BAR
   ===================================================== */

.top-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 8px 5px 22px 5px;

    border-bottom: 1px solid rgba(201,168,93,0.16);
}

.brand {
    font-family: 'Poppins', sans-serif;

    font-size: 25px;
    font-weight: 700;

    letter-spacing: 2.8px;

    color: #F7F3E8;
}

.brand-gold {
    color: #D2B56A;
}

.nav-right {
    color: rgba(245,242,232,0.65);

    font-size: 13px;

    letter-spacing: 0.4px;
}


/* =====================================================
   HERO
   ===================================================== */

.hero {
    position: relative;

    min-height: 520px;

    margin-top: 0;

    padding: 80px 75px;

    overflow: hidden;

    background:
        radial-gradient(
            circle at 82% 40%,
            rgba(105,135,67,0.16),
            transparent 27%
        ),
        linear-gradient(
            115deg,
            #05281F 0%,
            #073B2E 50%,
            #05271F 100%
        );

    border-bottom: 1px solid rgba(201,168,93,0.12);
}

.hero-circle {
    position: absolute;

    width: 470px;
    height: 470px;

    right: -80px;
    top: -70px;

    border: 1px solid rgba(201,168,93,0.20);

    border-radius: 50%;
}

.hero-circle-two {
    position: absolute;

    width: 300px;
    height: 300px;

    right: 60px;
    top: 20px;

    border: 1px solid rgba(201,168,93,0.10);

    border-radius: 50%;
}

.hero-content {
    position: relative;

    z-index: 5;

    max-width: 820px;
}

.hero-label {
    color: #D7BB73;

    font-size: 13px;

    font-weight: 700;

    letter-spacing: 2.5px;

    text-transform: uppercase;

    margin-bottom: 20px;
}

.hero-title {
    font-family: 'Poppins', sans-serif;

    font-size: 70px;

    line-height: 1;

    font-weight: 700;

    letter-spacing: 5px;

    margin-bottom: 22px;

    color: #F8F5EC;
}

.hero-title span {
    color: #D2B56A;
}

.hero-tagline {
    font-family: 'Poppins', sans-serif;

    font-size: 24px;

    line-height: 1.45;

    font-weight: 500;

    color: #F3F1E8;

    max-width: 760px;
}

.hero-subtitle {
    margin-top: 16px;

    font-size: 15px;

    color: rgba(245,242,232,0.72);

    letter-spacing: 0.3px;
}


/* =====================================================
   BUTTON
   ===================================================== */

.button-space {
    height: 26px;
}

div.stButton > button {
    background: #D2B56A;

    color: #09251D;

    border: 1px solid #DCC37F;

    border-radius: 30px;

    min-height: 52px;

    padding: 0 30px;

    font-size: 15px;

    font-weight: 700;

    box-shadow:
        0 8px 22px rgba(0,0,0,0.20);

    transition: all 0.25s ease;
}

div.stButton > button:hover {
    background: #E0C77D;

    color: #09251D;

    transform: translateY(-2px);

    box-shadow:
        0 12px 28px rgba(0,0,0,0.28);
}


/* =====================================================
   SECTION
   ===================================================== */

.section {
    padding-top: 48px;
}

.section-heading {
    text-align: center;

    font-family: 'Poppins', sans-serif;

    color: #F5F2E8;

    font-size: 30px;

    font-weight: 600;

    margin-bottom: 7px;
}

.section-heading::before,
.section-heading::after {
    content: "—";

    color: #C9A85D;

    margin: 0 18px;
}

.section-subtitle {
    text-align: center;

    color: rgba(245,242,232,0.64);

    font-size: 14px;

    margin-bottom: 30px;
}


/* =====================================================
   FEATURE CARDS
   ===================================================== */

.feature-card {
    position: relative;

    background:
        linear-gradient(
            145deg,
            rgba(20,75,57,0.82),
            rgba(5,42,32,0.88)
        );

    border: 1px solid rgba(104,151,121,0.34);

    border-radius: 15px;

    padding: 25px 24px;

    min-height: 178px;

    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.03),
        0 12px 30px rgba(0,0,0,0.14);

    transition: all 0.25s ease;
}

.feature-card:hover {
    border-color: rgba(210,181,106,0.55);

    transform: translateY(-4px);

    box-shadow:
        0 15px 35px rgba(0,0,0,0.25);
}

.feature-icon {
    display: inline-flex;

    align-items: center;
    justify-content: center;

    width: 43px;
    height: 43px;

    border-radius: 50%;

    background: rgba(201,168,93,0.20);

    border: 1px solid rgba(201,168,93,0.30);

    color: #E0C77D;

    font-size: 19px;

    margin-bottom: 15px;
}

.feature-number {
    color: #D2B56A;

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 1.5px;

    margin-bottom: 8px;
}

.feature-title {
    font-family: 'Poppins', sans-serif;

    color: #F5F2E8;

    font-size: 17px;

    font-weight: 600;

    margin-bottom: 8px;
}

.feature-text {
    color: rgba(245,242,232,0.64);

    font-size: 13px;

    line-height: 1.6;
}

.feature-arrow {
    position: absolute;

    right: 20px;
    top: 27px;

    color: rgba(210,181,106,0.75);

    font-size: 19px;
}


/* =====================================================
   VALUE BOX
   ===================================================== */

.value-box {
    margin-top: 42px;

    padding: 30px 34px;

    background:
        linear-gradient(
            120deg,
            rgba(20,75,57,0.80),
            rgba(7,47,36,0.90)
        );

    border: 1px solid rgba(201,168,93,0.50);

    border-radius: 17px;
}

.value-title {
    font-family: 'Poppins', sans-serif;

    color: #F5F2E8;

    font-size: 22px;

    font-weight: 600;

    margin-bottom: 7px;
}

.value-text {
    color: rgba(245,242,232,0.67);

    font-size: 14px;

    line-height: 1.7;

    max-width: 950px;
}


/* =====================================================
   FOOTER
   ===================================================== */

.footer {
    text-align: center;

    margin-top: 48px;

    padding-top: 26px;

    border-top: 1px solid rgba(201,168,93,0.16);

    color: rgba(245,242,232,0.55);

    font-size: 12px;

    line-height: 1.8;
}

.footer-brand {
    font-family: 'Poppins', sans-serif;

    color: #D2B56A;

    font-size: 14px;

    font-weight: 600;

    letter-spacing: 2px;
}

.gold-line {
    width: 55px;

    height: 2px;

    background: #C9A85D;

    margin: 12px auto;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 768px) {

    .block-container {
        padding-left: 18px;
        padding-right: 18px;
    }

    .hero {
        padding: 55px 30px;

        min-height: 500px;
    }

    .hero-title {
        font-size: 45px;

        letter-spacing: 3px;
    }

    .hero-tagline {
        font-size: 18px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TOP BRAND BAR
# =========================================================

render_html("""
<div class="top-nav">

<div class="brand">
VAN<span class="brand-gold">VIDHYA</span>
</div>

<div class="nav-right">
A Unified Digital Gateway for Tribal Student Scholarships
</div>

</div>
""")


# =========================================================
# HERO
# =========================================================

render_html("""
<div class="hero">

<div class="hero-circle"></div>
<div class="hero-circle-two"></div>

<div class="hero-content">

<div class="hero-label">
SMART INDIA HACKATHON 2026
</div>

<div class="hero-title">
VAN<span>VIDHYA</span>
</div>

<div class="hero-tagline">
A Unified Digital Gateway for Tribal Student Scholarships
</div>

<div class="hero-subtitle">
Your Education. Your Opportunities. One Platform.
</div>

</div>

</div>
""")


st.markdown(
    '<div class="button-space"></div>',
    unsafe_allow_html=True
)


# =========================================================
# GET STARTED
# =========================================================

if st.button(
    "Get Started   →",
    use_container_width=False
):
    st.switch_page("pages/student_login.py")


# =========================================================
# FEATURES TITLE
# =========================================================

render_html("""
<div class="section">

<div class="section-heading">
Everything in One Place
</div>

<div class="section-subtitle">
One platform designed to simplify the complete scholarship journey.
</div>

</div>
""")


# =========================================================
# FEATURE ROW 1
# =========================================================

col1, col2, col3 = st.columns(3, gap="medium")


with col1:

    render_html("""
<div class="feature-card">

<div class="feature-icon">⌂</div>

<div class="feature-number">
01
</div>

<div class="feature-title">
Unified Scholarships
</div>

<div class="feature-text">
Explore and track multiple tribal student scholarship schemes through a single interface.
</div>

<div class="feature-arrow">
→
</div>

</div>
""")


with col2:

    render_html("""
<div class="feature-card">

<div class="feature-icon">◇</div>

<div class="feature-number">
02
</div>

<div class="feature-title">
Smart Verification
</div>

<div class="feature-text">
Connect student records and documents through a unified verification and integration layer.
</div>

<div class="feature-arrow">
→
</div>

</div>
""")


with col3:

    render_html("""
<div class="feature-card">

<div class="feature-icon">✦</div>

<div class="feature-number">
03
</div>

<div class="feature-title">
JAGO AI Assistant
</div>

<div class="feature-text">
Get scholarship guidance, application updates, document help and payment information.
</div>

<div class="feature-arrow">
→
</div>

</div>
""")


st.write("")


# =========================================================
# FEATURE ROW 2
# =========================================================

col1, col2, col3 = st.columns(3, gap="medium")


with col1:

    render_html("""
<div class="feature-card">

<div class="feature-icon">▣</div>

<div class="feature-number">
04
</div>

<div class="feature-title">
Digital Document Wallet
</div>

<div class="feature-text">
Store, verify and reuse scholarship documents through one secure digital space.
</div>

<div class="feature-arrow">
→
</div>

</div>
""")


with col2:

    render_html("""
<div class="feature-card">

<div class="feature-icon">↗</div>

<div class="feature-number">
05
</div>

<div class="feature-title">
Application Tracking
</div>

<div class="feature-text">
Follow every stage from submission and verification to sanction and DBT disbursement.
</div>

<div class="feature-arrow">
→
</div>

</div>
""")


with col3:

    render_html("""
<div class="feature-card">

<div class="feature-icon">♧</div>

<div class="feature-number">
06
</div>

<div class="feature-title">
Beneficiary Outreach
</div>

<div class="feature-text">
Identify potential scholarship gaps and help reach eligible students who may be left out.
</div>

<div class="feature-arrow">
→
</div>

</div>
""")


# =========================================================
# VALUE BOX
# =========================================================

render_html("""
<div class="value-box">

<div class="value-title">
One Student. One Platform. Multiple Opportunities.
</div>

<div class="value-text">
VANVIDHYA brings scholarship discovery, eligibility, documents,
verification, application tracking, assistance and DBT information
together in one digital experience.
</div>

</div>
""")


# =========================================================
# FOOTER
# =========================================================

render_html("""
<div class="footer">

<div class="footer-brand">
✦ &nbsp; VANVIDHYA &nbsp; ✦
</div>

<div class="gold-line"></div>

A Unified Digital Gateway for Tribal Student Scholarships

<br>

SMART INDIA HACKATHON 2026
&nbsp; • &nbsp;
CoreSynch

</div>
""")