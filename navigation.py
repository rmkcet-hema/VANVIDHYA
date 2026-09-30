import streamlit as st


def show_navigation():

    # =====================================================
    # STUDENT DETAILS
    # =====================================================

    student_name = st.session_state.get(
        "student_name",
        "Ananya"
    )

    student_id = st.session_state.get(
        "student_id",
        "VV2026001"
    )


    # =====================================================
    # SIDEBAR STYLE
    # =====================================================

    st.markdown(
        """
        <style>

        /* ================================================
           SIDEBAR
           ================================================ */

        [data-testid="stSidebar"] {
            background:
                linear-gradient(
                    180deg,
                    #041F18 0%,
                    #063328 55%,
                    #05271F 100%
                );

            border-right:
                1px solid rgba(201,168,93,0.18);
        }


        [data-testid="stSidebar"] > div:first-child {
            padding-top: 25px;
        }


        /* ================================================
           SIDEBAR TEXT
           ================================================ */

        [data-testid="stSidebar"] * {
            color: #F5F2E8;
        }


        /* ================================================
           NAVIGATION BUTTONS
           ================================================ */

        [data-testid="stSidebar"] .stButton > button {

            width: 100%;

            background: transparent;

            color:
                rgba(245,242,232,0.72);

            border:
                1px solid transparent;

            border-radius: 10px;

            text-align: left;

            padding:
                10px 14px;

            margin-bottom: 5px;

            min-height: 42px;

            font-size: 13px;

            font-weight: 500;

            box-shadow: none;

            transition:
                all 0.2s ease;
        }


        [data-testid="stSidebar"] .stButton > button:hover {

            background:
                rgba(201,168,93,0.10);

            color:
                #D2B56A;

            border-color:
                rgba(201,168,93,0.20);

            transform: none;

            box-shadow: none;
        }


        /* ================================================
           BRAND
           ================================================ */

        .nav-brand {

            font-family:
                Arial, sans-serif;

            font-size: 22px;

            font-weight: 700;

            letter-spacing: 2.5px;

            color:
                #F7F3E8;

            margin-bottom: 4px;
        }


        .nav-brand span {
            color:
                #D2B56A;
        }


        .nav-tagline {

            color:
                rgba(245,242,232,0.45);

            font-size: 10px;

            line-height: 1.5;

            margin-bottom: 25px;
        }


        /* ================================================
           SECTION TITLE
           ================================================ */

        .nav-section {

            color:
                #D2B56A;

            font-size: 10px;

            font-weight: 700;

            letter-spacing: 1.8px;

            text-transform: uppercase;

            margin:
                14px 0 10px 4px;
        }


        /* ================================================
           DIVIDER
           ================================================ */

        .nav-divider {

            height: 1px;

            background:
                rgba(201,168,93,0.15);

            margin:
                18px 0;
        }


        /* ================================================
           FOOTER
           ================================================ */

        .nav-footer {

            margin-top: 22px;

            padding-bottom: 10px;

            text-align: center;

            color:
                rgba(245,242,232,0.32);

            font-size: 9px;

            line-height: 1.6;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # SIDEBAR
    # =====================================================

    with st.sidebar:

        # =================================================
        # BRAND
        # =================================================

        st.markdown(
            """
            <div class="nav-brand">
                VAN<span>VIDHYA</span>
            </div>

            <div class="nav-tagline">
                A Unified Digital Gateway for<br>
                Tribal Student Scholarships
            </div>
            """,
            unsafe_allow_html=True
        )


        # =================================================
        # MAIN
        # =================================================

        st.markdown(
            '<div class="nav-section">Main</div>',
            unsafe_allow_html=True
        )


        if st.button(
            "🏠   Home",
            use_container_width=True
        ):
            st.switch_page(
                "pages/dashboard.py"
            )


        if st.button(
            "🎓   Scholarships",
            use_container_width=True
        ):
            st.switch_page(
                "pages/scholarships.py"
            )


        if st.button(
            "📝   Apply Scholarship",
            use_container_width=True
        ):
            st.switch_page(
                "pages/apply_scholarship.py"
            )


        # =================================================
        # MY SCHOLARSHIP
        # =================================================

        st.markdown(
            '<div class="nav-section">My Scholarship</div>',
            unsafe_allow_html=True
        )


        if st.button(
            "📋   Applications",
            use_container_width=True
        ):
            st.switch_page(
                "pages/applications.py"
            )


        if st.button(
            "📄   Documents",
            use_container_width=True
        ):
            st.switch_page(
                "pages/documents.py"
            )


        if st.button(
            "💰   Payments & DBT",
            use_container_width=True
        ):
            st.switch_page(
                "pages/payment.py"
            )


        if st.button(
            "🔔   Notifications",
            use_container_width=True
        ):
            st.switch_page(
                "pages/notifications.py"
            )


        # =================================================
        # ASSISTANCE
        # =================================================

        st.markdown(
            '<div class="nav-section">Assistance</div>',
            unsafe_allow_html=True
        )


        if st.button(
            "🤖   JAGO AI",
            use_container_width=True
        ):
            st.switch_page(
                "pages/jago.py"
            )


        if st.button(
            "✅   Check Eligibility",
            use_container_width=True
        ):
            st.switch_page(
                "pages/eligibility.py"
            )


        # =================================================
        # ADMINISTRATION
        # =================================================

        st.markdown(
            '<div class="nav-divider"></div>',
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="nav-section">Administration</div>',
            unsafe_allow_html=True
        )


        if st.button(
            "🏛️   Admin Dashboard",
            use_container_width=True
        ):
            st.switch_page(
                "pages/admin_dashboard.py"
            )


        # =================================================
        # STUDENT PROFILE
        # IMPORTANT:
        # NO HTML DIV USED HERE
        # =================================================

        st.markdown("---")

        st.markdown(
            f"🌿 **{student_name}**"
        )

        st.caption(
            student_id
        )


        # =================================================
        # LOGOUT
        # =================================================

        if st.button(
            "↪   Logout",
            use_container_width=True
        ):

            st.session_state.clear()

            st.switch_page(
                "pages/student_login.py"
            )


        # =================================================
        # FOOTER
        # =================================================

        st.markdown("---")

st.caption("VANVIDHYA")
st.caption("SMART INDIA HACKATHON 2026")
st.caption("CoreSynch")
