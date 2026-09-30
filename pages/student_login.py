import streamlit as st

st.set_page_config(
    page_title="Student Login | VanVidhya",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# HTML RENDER HELPER
# =========================================================

def render_html(content):
    clean_html = "\n".join(
        line.strip() for line in content.splitlines()
    )

    st.markdown(
        clean_html,
        unsafe_allow_html=True
    )


# =========================================================
# PAGE STYLING
# =========================================================

st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}


/* =====================================================
   MAIN BACKGROUND
   ===================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 15% 20%,
            rgba(82, 130, 91, 0.14),
            transparent 28%
        ),
        radial-gradient(
            circle at 85% 80%,
            rgba(201, 168, 93, 0.08),
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #041F18 0%,
            #063328 50%,
            #05271F 100%
        );

    color: #F5F2E8;
    min-height: 100vh;
}


.block-container {
    max-width: 1180px;
    padding-top: 35px;
    padding-bottom: 40px;
}


/* =====================================================
   BRAND
   ===================================================== */

.login-brand {
    font-family: Arial, sans-serif;
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 3px;
    color: #F5F2E8;
    margin-bottom: 55px;
}

.login-brand span {
    color: #D2B56A;
}


/* =====================================================
   LEFT CONTENT
   ===================================================== */

.welcome-label {
    color: #D2B56A;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 15px;
}

.welcome-title {
    font-family: Arial, sans-serif;
    font-size: 46px;
    line-height: 1.12;
    font-weight: 700;
    color: #F7F3E8;
    margin-bottom: 18px;
}

.welcome-title span {
    color: #D2B56A;
}

.welcome-text {
    color: rgba(245,242,232,0.65);
    font-size: 15px;
    line-height: 1.8;
    max-width: 450px;
}

.login-points {
    margin-top: 35px;
}

.login-point {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 17px;
    color: rgba(245,242,232,0.82);
    font-size: 14px;
}

.point-icon {
    color: #D2B56A;
    font-size: 17px;
}


/* =====================================================
   LOGIN CARD
   ===================================================== */

.login-card {
    background:
        linear-gradient(
            145deg,
            rgba(17,68,51,0.90),
            rgba(5,39,30,0.96)
        );

    border: 1px solid rgba(201,168,93,0.30);
    border-radius: 22px;
    padding: 34px;

    box-shadow:
        0 20px 55px rgba(0,0,0,0.28),
        inset 0 1px 0 rgba(255,255,255,0.03);
}

.login-card-title {
    font-family: Arial, sans-serif;
    font-size: 27px;
    font-weight: 700;
    color: #F7F3E8;
    margin-bottom: 7px;
}

.login-card-subtitle {
    color: rgba(245,242,232,0.55);
    font-size: 13px;
    margin-bottom: 25px;
}


/* =====================================================
   INPUTS
   ===================================================== */

.stTextInput input {
    background: #092E24 !important;
    color: #F5F2E8 !important;

    border: 1px solid rgba(104,151,121,0.40) !important;

    border-radius: 10px !important;
}

.stTextInput input:focus {
    border-color: #D2B56A !important;
    box-shadow: 0 0 0 1px #D2B56A !important;
}

.stTextInput label {
    color: #E8E5DB !important;
}


/* =====================================================
   SELECTBOX
   ===================================================== */

[data-baseweb="select"] > div {
    background: #092E24 !important;
    color: #F5F2E8 !important;

    border-color: rgba(104,151,121,0.40) !important;

    border-radius: 10px !important;
}

[data-baseweb="popover"] {
    background: #092E24 !important;
}

[role="option"] {
    background: #092E24 !important;
    color: #F5F2E8 !important;
}

[role="option"]:hover {
    background: #124C39 !important;
}


/* =====================================================
   BUTTONS
   ===================================================== */

div.stButton > button {
    background: #D2B56A;

    color: #09251D;

    border: 1px solid #DCC37F;

    border-radius: 10px;

    min-height: 46px;

    font-size: 14px;

    font-weight: 700;

    transition: all 0.25s ease;
}

div.stButton > button:hover {
    background: #E0C77D;

    color: #09251D;

    transform: translateY(-2px);

    box-shadow:
        0 8px 20px rgba(0,0,0,0.22);
}


/* =====================================================
   DEMO OTP BOX
   ===================================================== */

.demo-box {
    margin-top: 22px;

    padding: 13px 15px;

    border-radius: 10px;

    background:
        rgba(201,168,93,0.08);

    border:
        1px solid rgba(201,168,93,0.22);

    color:
        rgba(245,242,232,0.70);

    font-size: 12px;

    text-align: center;
}

.demo-box strong {
    color: #D2B56A;
}


/* =====================================================
   FOOTER
   ===================================================== */

.login-footer {
    margin-top: 65px;

    padding-top: 20px;

    border-top:
        1px solid rgba(201,168,93,0.14);

    text-align: center;

    color:
        rgba(245,242,232,0.40);

    font-size: 11px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# BRAND
# =========================================================

render_html("""
<div class="login-brand">
VAN<span>VIDHYA</span>
</div>
""")


# =========================================================
# MAIN LAYOUT
# =========================================================

left, right = st.columns(
    [1.15, 0.85],
    gap="large"
)


# =========================================================
# LEFT SIDE
# =========================================================

with left:

    render_html("""
<div class="welcome-label">
STUDENT PORTAL
</div>

<div class="welcome-title">
Your Scholarship<br>
Journey Starts <span>Here.</span>
</div>

<div class="welcome-text">
Access your scholarships, applications, documents,
verification status and DBT payments through one
unified digital platform.
</div>

<div class="login-points">

<div class="login-point">
<span class="point-icon">✦</span>
<span>Track all your scholarship applications</span>
</div>

<div class="login-point">
<span class="point-icon">✦</span>
<span>Manage documents through one digital wallet</span>
</div>

<div class="login-point">
<span class="point-icon">✦</span>
<span>Get assistance from JAGO AI</span>
</div>

<div class="login-point">
<span class="point-icon">✦</span>
<span>Monitor sanction and DBT payment status</span>
</div>

</div>
""")


# =========================================================
# RIGHT SIDE — LOGIN
# =========================================================

with right:

    render_html("""
<div class="login-card">

<div class="login-card-title">
Welcome Back
</div>

<div class="login-card-subtitle">
Login to access your VanVidhya dashboard
</div>

</div>
""")


    # -----------------------------------------------------
    # LOGIN TYPE
    # -----------------------------------------------------

    login_type = st.selectbox(
        "Login using",
        [
            "Student ID",
            "Mobile Number"
        ]
    )


    # -----------------------------------------------------
    # STUDENT ID
    # -----------------------------------------------------

    if login_type == "Student ID":

        student_id = st.text_input(
            "Student ID",
            placeholder="Example: VV2026001"
        )


    # -----------------------------------------------------
    # MOBILE NUMBER
    # -----------------------------------------------------

    else:

        mobile = st.text_input(
            "Mobile Number",
            placeholder="Example: 9876543210"
        )


    # -----------------------------------------------------
    # SEND OTP
    # -----------------------------------------------------

    if st.button(
        "Send OTP  →",
        use_container_width=True
    ):

        if (
            login_type == "Student ID"
            and student_id
        ):

            st.session_state["otp_sent"] = True

            st.success(
                "Demo OTP sent successfully!"
            )

        elif (
            login_type == "Mobile Number"
            and mobile
        ):

            st.session_state["otp_sent"] = True

            st.success(
                "Demo OTP sent successfully!"
            )

        else:

            st.warning(
                "Please enter your details."
            )


    # -----------------------------------------------------
    # OTP VERIFICATION
    # -----------------------------------------------------

    if st.session_state.get(
        "otp_sent",
        False
    ):

        st.markdown(
            "<div style='height:8px;'></div>",
            unsafe_allow_html=True
        )

        otp = st.text_input(
            "Verification OTP",
            type="password",
            placeholder="Enter 123456"
        )


        # -------------------------------------------------
        # VERIFY & LOGIN
        # -------------------------------------------------

        if st.button(
            "Verify & Login  →",
            use_container_width=True
        ):

            if otp == "123456":

                st.session_state["logged_in"] = True

                st.session_state[
                    "student_name"
                ] = "Ananya"

                st.session_state[
                    "student_id"
                ] = "VV2026001"


                st.success(
                    "Login successful!"
                )


                st.switch_page(
                    "pages/dashboard.py"
                )

            else:

                st.error(
                    "Invalid OTP. Use demo OTP: 123456"
                )


    # -----------------------------------------------------
    # DEMO OTP
    # -----------------------------------------------------

    render_html("""
<div class="demo-box">
Demo Login &nbsp;•&nbsp;
<strong>OTP: 123456</strong>
</div>
""")


# =========================================================
# FOOTER
# =========================================================

render_html("""
<div class="login-footer">

VANVIDHYA &nbsp;•&nbsp;
A Unified Digital Gateway for Tribal Student Scholarships

<br><br>

SMART INDIA HACKATHON 2026
&nbsp;•&nbsp;
CoreSynch

</div>
""")