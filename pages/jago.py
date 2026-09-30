import streamlit as st
from navigation import show_navigation


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="JAGO | VanVidhya",
    page_icon="🤖",
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
# SIDEBAR
# =========================================================

show_navigation()


# =========================================================
# STUDENT DATA
# =========================================================

student_name = st.session_state.get("student_name", "Ananya")
student_id = st.session_state.get("student_id", "VV2026001")

student = {
    "name": student_name,
    "id": student_id,
    "category": "ST",
    "income": 150000,
    "education": "Undergraduate",

    "applications": {
        "Post-Matric Scholarship": {
            "id": "VV-PMS-2026-001",
            "status": "Under Institution Verification",
            "progress": 60,
            "amount": "₹18,500"
        },

        "Top Class Scholarship": {
            "id": "VV-TCS-2026-002",
            "status": "Sanctioned",
            "progress": 85,
            "amount": "₹42,000"
        }
    },

    "pending_documents": [
        "Income Certificate",
        "Institution Certificate"
    ],

    "processed_payment": "₹42,000",
    "pending_payment": "₹18,500"
}


# =========================================================
# VANVIDHYA THEME
# =========================================================

st.markdown(
    """
<style>

.stApp {
    background:
        radial-gradient(
            circle at 85% 5%,
            rgba(196, 165, 87, 0.10),
            transparent 25%
        ),
        radial-gradient(
            circle at 10% 90%,
            rgba(24, 91, 68, 0.14),
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


/* Main content */

.main .block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* Text */

h1, h2, h3, h4 {
    color: #f3ead0 !important;
}

p,
label,
.stMarkdown {
    color: #d9d4c4;
}


/* Select box */

div[data-baseweb="select"] > div {
    background-color: #102f26 !important;
    border: 1px solid #8d7135 !important;
    border-radius: 10px !important;
    color: #f5f0df !important;
}


/* Buttons */

.stButton > button {
    background:
        linear-gradient(
            135deg,
            #a9873d,
            #c4a557
        ) !important;

    color: #10251d !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    min-height: 44px;

    transition: all 0.2s ease;
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


/* Alert cards */

div[data-testid="stAlert"] {
    background:
        linear-gradient(
            145deg,
            #102f26,
            #0d271f
        ) !important;

    border-radius: 14px !important;

    border: 1px solid rgba(
        196,
        165,
        87,
        0.30
    ) !important;

    color: #eee7d4 !important;
}


/* Metrics */

div[data-testid="stMetric"] {
    background:
        linear-gradient(
            145deg,
            #102f26,
            #0d271f
        );

    border: 1px solid rgba(
        196,
        165,
        87,
        0.30
    );

    border-radius: 14px;
    padding: 14px;
}

div[data-testid="stMetricValue"] {
    color: #e5c76c !important;
}

div[data-testid="stMetricLabel"] {
    color: #bdb6a4 !important;
}


/* Chat input */

div[data-testid="stChatInput"] {
    background-color: #102f26 !important;
    border: 1px solid #8d7135 !important;
    border-radius: 14px !important;
}

div[data-testid="stChatInput"] textarea {
    color: #f5f0df !important;
}

div[data-testid="stChatInput"] textarea::placeholder {
    color: #9d9a8c !important;
}


/* Chat messages */

div[data-testid="stChatMessage"] {
    background: rgba(16, 47, 38, 0.90);
    border: 1px solid rgba(
        196,
        165,
        87,
        0.20
    );
    border-radius: 14px;
    padding: 10px 14px;
    margin-bottom: 10px;
}


/* Divider */

hr {
    border-color:
        rgba(
            196,
            165,
            87,
            0.25
        ) !important;
}


/* Section title */

.section-title {
    color: #e5c76c;
    font-size: 0.78rem;
    font-weight: 800;
    letter-spacing: 1.2px;
    text-transform: uppercase;
}


/* Profile container */

.profile-box {
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
        0.30
    );

    border-radius: 14px;
    padding: 16px;
}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# LANGUAGE SETTINGS
# =========================================================

LANGUAGES = {
    "English 🇬🇧": "english",
    "हिन्दी 🇮🇳": "hindi",
    "தமிழ் 🇮🇳": "tamil",
    "Thanglish 💬": "thanglish"
}


if "jago_language" not in st.session_state:
    st.session_state["jago_language"] = "english"


# =========================================================
# JAGO HEADER
# =========================================================

st.title("🤖 JAGO")

st.subheader(
    "Your AI Scholarship Assistant"
)

st.caption(
    "Multilingual scholarship assistance for students across India"
)

st.success(
    "🟢 AI Assistant Online"
)

st.divider()


# =========================================================
# LANGUAGE SELECTOR
# =========================================================

st.markdown(
    '<div class="section-title">LANGUAGE PREFERENCE</div>',
    unsafe_allow_html=True
)

st.caption(
    "Choose how you want to communicate with JAGO."
)

selected_language = st.selectbox(
    "🌐 Select JAGO Language",
    list(LANGUAGES.keys()),
    index=0,
    label_visibility="collapsed"
)

st.session_state["jago_language"] = LANGUAGES[selected_language]

language = st.session_state["jago_language"]


# =========================================================
# STUDENT PROFILE + INTRO
# =========================================================

st.write("")

col1, col2 = st.columns([1.7, 1])


# =========================================================
# JAGO INTRO
# =========================================================

with col1:

    st.markdown(
        '<div class="section-title">JAGO ASSISTANCE</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Ask JAGO about your scholarship journey."
    )

    if language == "english":

        st.info(
            "👋 **Hi! I'm JAGO.**\n\n"
            "I can help you with:\n\n"
            "🎓 Scholarship eligibility\n"
            "📋 Application status\n"
            "📄 Required documents\n"
            "🔍 Verification status\n"
            "💰 Scholarship payments\n"
            "⏳ Pending actions\n"
            "📢 Scholarship information"
        )

    elif language == "hindi":

        st.info(
            "👋 **नमस्ते! मैं JAGO हूँ।**\n\n"
            "मैं आपकी मदद कर सकता हूँ:\n\n"
            "🎓 छात्रवृत्ति पात्रता\n"
            "📋 आवेदन की स्थिति\n"
            "📄 आवश्यक दस्तावेज़\n"
            "🔍 सत्यापन की स्थिति\n"
            "💰 छात्रवृत्ति भुगतान\n"
            "⏳ लंबित कार्य\n"
            "📢 छात्रवृत्ति जानकारी"
        )

    elif language == "tamil":

        st.info(
            "👋 **வணக்கம்! நான் JAGO.**\n\n"
            "நான் உங்களுக்கு உதவ முடியும்:\n\n"
            "🎓 Scholarship eligibility\n"
            "📋 Application status\n"
            "📄 தேவையான documents\n"
            "🔍 Verification status\n"
            "💰 Scholarship payment\n"
            "⏳ Pending actions\n"
            "📢 Scholarship information"
        )

    else:

        st.info(
            "👋 **Hi! Naan JAGO.**\n\n"
            "Naan ungalukku help panna mudiyum:\n\n"
            "🎓 Scholarship eligibility\n"
            "📋 Application status\n"
            "📄 Required documents\n"
            "🔍 Verification status\n"
            "💰 Payment / DBT status\n"
            "⏳ Pending actions\n"
            "📢 Scholarship information"
        )


# =========================================================
# STUDENT PROFILE
# =========================================================

with col2:

    st.markdown(
        '<div class="section-title">STUDENT PROFILE</div>',
        unsafe_allow_html=True
    )

    st.write("🌿 **" + student["name"] + "**")

    st.caption(
        "🆔 Student ID: " + student["id"]
    )

    st.caption(
        "🏷️ Category: " + student["category"]
    )

    st.caption(
        "🎓 Education: " + student["education"]
    )

    st.caption(
        f"💰 Annual Income: ₹{student['income']:,}"
    )


st.divider()


# =========================================================
# QUICK QUESTIONS
# =========================================================

if language == "english":

    quick_questions = [
        "My scholarships",
        "Application status",
        "Pending documents",
        "Payment status",
        "Eligibility",
        "Verification",
        "Top Class",
        "Overseas Scholarship"
    ]

elif language == "hindi":

    quick_questions = [
        "मेरी छात्रवृत्ति",
        "आवेदन की स्थिति",
        "लंबित दस्तावेज़",
        "भुगतान की स्थिति",
        "पात्रता",
        "सत्यापन",
        "टॉप क्लास",
        "ओवरसीज़ छात्रवृत्ति"
    ]

elif language == "tamil":

    quick_questions = [
        "என் Scholarships",
        "Application Status",
        "Pending Documents",
        "Payment Status",
        "Eligibility",
        "Verification",
        "Top Class",
        "Overseas Scholarship"
    ]

else:

    quick_questions = [
        "En Scholarships",
        "Application Status enna?",
        "Pending Documents enna?",
        "Payment Status",
        "Naan eligible ah?",
        "Verification status",
        "Top Class",
        "Overseas Scholarship"
    ]


st.markdown(
    '<div class="section-title">QUICK ASSISTANCE</div>',
    unsafe_allow_html=True
)

st.caption(
    "Choose a question or type your own question below."
)

quick_columns = st.columns(4)

for index, question in enumerate(quick_questions):

    with quick_columns[index % 4]:

        if st.button(
            question,
            use_container_width=True,
            key=f"quick_{index}"
        ):

            st.session_state["jago_question"] = question


st.divider()


# =========================================================
# CHAT HISTORY
# =========================================================

if "jago_messages" not in st.session_state:
    st.session_state["jago_messages"] = []


st.markdown(
    '<div class="section-title">CONVERSATION</div>',
    unsafe_allow_html=True
)

st.caption(
    "Your conversation with JAGO will appear here."
)


if len(st.session_state["jago_messages"]) == 0:

    st.info(
        "💬 Start a conversation by selecting a quick question "
        "or typing your question below."
    )


for message in st.session_state["jago_messages"]:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# =========================================================
# RESPONSE FUNCTIONS
# =========================================================

def response_english(intent):

    if intent == "greeting":

        return (
            f"Hi {student['name']}! 👋\n\n"
            "I'm JAGO, your VanVidhya scholarship assistant. "
            "You can ask me about eligibility, applications, "
            "documents, verification and payments."
        )

    if intent == "scholarships":

        return (
            "🎓 **Your Scholarship Applications**\n\n"
            "1. **Post-Matric Scholarship**\n"
            "Status: 🟡 Under Institution Verification\n"
            "Progress: 60%\n\n"
            "2. **Top Class Scholarship**\n"
            "Status: 🟢 Sanctioned\n"
            "Progress: 85%"
        )

    if intent == "application":

        return (
            "📋 **Your Application Status**\n\n"
            f"🎓 Post-Matric Scholarship\n"
            f"Application ID: "
            f"{student['applications']['Post-Matric Scholarship']['id']}\n"
            "Status: 🟡 Under Institution Verification\n"
            "Progress: 60%\n\n"
            f"🏆 Top Class Scholarship\n"
            f"Application ID: "
            f"{student['applications']['Top Class Scholarship']['id']}\n"
            "Status: 🟢 Sanctioned\n"
            "Progress: 85%"
        )

    if intent == "documents":

        return (
            "📄 **Pending Documents**\n\n"
            "• Income Certificate\n"
            "• Institution Certificate\n\n"
            "Please upload these documents through your "
            "**Document Wallet**."
        )

    if intent == "payment":

        return (
            "💰 **Payment Status**\n\n"
            "🟢 Top Class Scholarship\n"
            "Processed Amount: ₹42,000\n"
            "Status: Processed\n\n"
            "🟡 Post-Matric Scholarship\n"
            "Pending Amount: ₹18,500\n"
            "Status: Awaiting Final Sanction"
        )

    if intent == "eligibility":

        return (
            "✅ **Eligibility Guidance**\n\n"
            f"Your category is **{student['category']}** "
            "and your profile is currently marked as an ST student.\n\n"
            "You can explore:\n"
            "• Pre-Matric Scholarship\n"
            "• Post-Matric Scholarship\n"
            "• Top Class Scholarship\n"
            "• National Fellowship for ST Students\n"
            "• National Overseas Scholarship\n\n"
            "⚠️ Final eligibility depends on official scheme "
            "rules, academic requirements, income limits and verification."
        )

    if intent == "verification":

        return (
            "🔍 **Verification Status**\n\n"
            "Your Post-Matric Scholarship is currently in:\n\n"
            "🟡 **Institution Verification**\n\n"
            "Next stages:\n"
            "1. Document Verification\n"
            "2. Ministry Verification\n"
            "3. Sanction\n"
            "4. DBT Processing"
        )

    if intent == "top_class":

        return (
            "🏆 **Top Class Scholarship**\n\n"
            "Status: 🟢 Sanctioned\n"
            "Sanctioned Amount: ₹42,000\n"
            "Progress: 85%\n\n"
            "The prototype shows the DBT payment as processed."
        )

    if intent == "overseas":

        return (
            "🌎 **National Overseas Scholarship (NOS)**\n\n"
            "NOS supports eligible ST students pursuing "
            "higher studies abroad.\n\n"
            "Final eligibility depends on the official NOS "
            "guidelines and verification."
        )

    return (
        "🤔 I couldn't fully understand that.\n\n"
        "Try asking about your application, documents, "
        "eligibility, verification or payment."
    )


# =========================================================
# HINDI RESPONSE
# =========================================================

def response_hindi(intent):

    if intent == "greeting":

        return (
            f"नमस्ते {student['name']}! 👋\n\n"
            "मैं JAGO हूँ, आपका VanVidhya छात्रवृत्ति सहायक। "
            "आप मुझसे पात्रता, आवेदन, दस्तावेज़, सत्यापन और भुगतान "
            "के बारे में पूछ सकते हैं।"
        )

    if intent == "scholarships":

        return (
            "🎓 **आपकी छात्रवृत्ति आवेदन स्थिति**\n\n"
            "1. **पोस्ट-मैट्रिक छात्रवृत्ति**\n"
            "स्थिति: 🟡 संस्थान सत्यापन में\n"
            "प्रगति: 60%\n\n"
            "2. **टॉप क्लास छात्रवृत्ति**\n"
            "स्थिति: 🟢 स्वीकृत\n"
            "प्रगति: 85%"
        )

    if intent == "application":

        return (
            "📋 **आपके आवेदन की स्थिति**\n\n"
            f"🎓 पोस्ट-मैट्रिक छात्रवृत्ति\n"
            f"आवेदन ID: "
            f"{student['applications']['Post-Matric Scholarship']['id']}\n"
            "स्थिति: 🟡 संस्थान सत्यापन में\n"
            "प्रगति: 60%\n\n"
            f"🏆 टॉप क्लास छात्रवृत्ति\n"
            f"आवेदन ID: "
            f"{student['applications']['Top Class Scholarship']['id']}\n"
            "स्थिति: 🟢 स्वीकृत\n"
            "प्रगति: 85%"
        )

    if intent == "documents":

        return (
            "📄 **लंबित दस्तावेज़**\n\n"
            "• आय प्रमाण पत्र\n"
            "• संस्थान प्रमाण पत्र\n\n"
            "कृपया इन्हें अपने **Document Wallet** में अपलोड करें।"
        )

    if intent == "payment":

        return (
            "💰 **भुगतान की स्थिति**\n\n"
            "🟢 टॉप क्लास छात्रवृत्ति\n"
            "प्रसंस्कृत राशि: ₹42,000\n"
            "स्थिति: भुगतान संसाधित\n\n"
            "🟡 पोस्ट-मैट्रिक छात्रवृत्ति\n"
            "लंबित राशि: ₹18,500\n"
            "स्थिति: अंतिम स्वीकृति की प्रतीक्षा"
        )

    if intent == "eligibility":

        return (
            "✅ **पात्रता जानकारी**\n\n"
            f"आपकी श्रेणी **{student['category']}** है और "
            "आपकी प्रोफ़ाइल ST छात्र के रूप में दर्ज है।\n\n"
            "आप इन योजनाओं को देख सकते हैं:\n"
            "• प्री-मैट्रिक छात्रवृत्ति\n"
            "• पोस्ट-मैट्रिक छात्रवृत्ति\n"
            "• टॉप क्लास छात्रवृत्ति\n"
            "• National Fellowship for ST Students\n"
            "• National Overseas Scholarship\n\n"
            "⚠️ अंतिम पात्रता आधिकारिक नियमों और सत्यापन पर निर्भर करती है।"
        )

    if intent == "verification":

        return (
            "🔍 **सत्यापन की स्थिति**\n\n"
            "आपका पोस्ट-मैट्रिक आवेदन अभी:\n\n"
            "🟡 **संस्थान सत्यापन** में है।\n\n"
            "अगले चरण:\n"
            "1. दस्तावेज़ सत्यापन\n"
            "2. मंत्रालय सत्यापन\n"
            "3. स्वीकृति\n"
            "4. DBT भुगतान प्रक्रिया"
        )

    if intent == "top_class":

        return (
            "🏆 **टॉप क्लास छात्रवृत्ति**\n\n"
            "स्थिति: 🟢 स्वीकृत\n"
            "स्वीकृत राशि: ₹42,000\n"
            "प्रगति: 85%\n\n"
            "प्रोटोटाइप में DBT भुगतान संसाधित दिखाया गया है।"
        )

    if intent == "overseas":

        return (
            "🌎 **National Overseas Scholarship (NOS)**\n\n"
            "यह योजना पात्र ST छात्रों को विदेश में उच्च शिक्षा "
            "के लिए सहायता प्रदान करती है।\n\n"
            "अंतिम पात्रता आधिकारिक NOS दिशानिर्देशों पर निर्भर करती है।"
        )

    return (
        "🤔 मैं आपके प्रश्न को पूरी तरह समझ नहीं पाया।\n\n"
        "आप आवेदन, दस्तावेज़, पात्रता, सत्यापन या भुगतान के बारे में पूछ सकते हैं।"
    )


# =========================================================
# TAMIL RESPONSE
# =========================================================

def response_tamil(intent):

    if intent == "greeting":

        return (
            f"வணக்கம் {student['name']}! 👋\n\n"
            "நான் JAGO, உங்கள் VanVidhya scholarship assistant. "
            "Eligibility, application, documents, verification மற்றும் "
            "payment பற்றி என்னிடம் கேட்கலாம்."
        )

    if intent == "scholarships":

        return (
            "🎓 **உங்கள் Scholarship Applications**\n\n"
            "1. **Post-Matric Scholarship**\n"
            "Status: 🟡 Institution Verification-ல் உள்ளது\n"
            "Progress: 60%\n\n"
            "2. **Top Class Scholarship**\n"
            "Status: 🟢 Sanctioned\n"
            "Progress: 85%"
        )

    if intent == "application":

        return (
            "📋 **உங்கள் Application Status**\n\n"
            f"🎓 Post-Matric Scholarship\n"
            f"Application ID: "
            f"{student['applications']['Post-Matric Scholarship']['id']}\n"
            "Status: 🟡 Institution Verification-ல் உள்ளது\n"
            "Progress: 60%\n\n"
            f"🏆 Top Class Scholarship\n"
            f"Application ID: "
            f"{student['applications']['Top Class Scholarship']['id']}\n"
            "Status: 🟢 Sanctioned\n"
            "Progress: 85%"
        )

    if intent == "documents":

        return (
            "📄 **Pending Documents**\n\n"
            "• Income Certificate\n"
            "• Institution Certificate\n\n"
            "இந்த documents-ஐ **Document Wallet** மூலம் upload செய்யலாம்."
        )

    if intent == "payment":

        return (
            "💰 **Payment Status**\n\n"
            "🟢 Top Class Scholarship\n"
            "Processed Amount: ₹42,000\n"
            "Status: Processed\n\n"
            "🟡 Post-Matric Scholarship\n"
            "Pending Amount: ₹18,500\n"
            "Status: Final Sanction-க்காக காத்திருக்கிறது."
        )

    if intent == "eligibility":

        return (
            "✅ **Eligibility Information**\n\n"
            f"உங்கள் category **{student['category']}**. "
            "Profile-ல் நீங்கள் ST student-ஆக பதிவு செய்யப்பட்டுள்ளீர்கள்.\n\n"
            "நீங்கள் இந்த schemes-ஐ explore செய்யலாம்:\n"
            "• Pre-Matric Scholarship\n"
            "• Post-Matric Scholarship\n"
            "• Top Class Scholarship\n"
            "• National Fellowship for ST Students\n"
            "• National Overseas Scholarship\n\n"
            "⚠️ Final eligibility official scheme rules மற்றும் verification-ஐ பொறுத்தது."
        )

    if intent == "verification":

        return (
            "🔍 **Verification Status**\n\n"
            "உங்கள் Post-Matric Scholarship தற்போது:\n\n"
            "🟡 **Institution Verification** stage-ல் உள்ளது.\n\n"
            "அடுத்த stages:\n"
            "1. Document Verification\n"
            "2. Ministry Verification\n"
            "3. Sanction\n"
            "4. DBT Processing"
        )

    if intent == "top_class":

        return (
            "🏆 **Top Class Scholarship**\n\n"
            "Status: 🟢 Sanctioned\n"
            "Sanctioned Amount: ₹42,000\n"
            "Progress: 85%\n\n"
            "Prototype-ல் DBT payment processed என்று காட்டப்படுகிறது."
        )

    if intent == "overseas":

        return (
            "🌎 **National Overseas Scholarship (NOS)**\n\n"
            "Eligible ST students higher studies abroad pursue "
            "செய்ய இந்த scheme support வழங்குகிறது.\n\n"
            "Final eligibility official NOS guidelines-ஐ பொறுத்தது."
        )

    return (
        "🤔 உங்கள் கேள்வியை முழுமையாக புரிந்து கொள்ள முடியவில்லை.\n\n"
        "Application, documents, eligibility, verification அல்லது payment பற்றி கேளுங்கள்."
    )


# =========================================================
# THANGlish RESPONSE
# =========================================================

def response_thanglish(intent):

    if intent == "greeting":

        return (
            f"Hi {student['name']}! 👋\n\n"
            "Naan JAGO, unga VanVidhya scholarship assistant. "
            "Eligibility, application, documents, verification "
            "and payment pathi enna kitta kekkalam."
        )

    if intent == "scholarships":

        return (
            "🎓 **Unga Scholarship Applications**\n\n"
            "1. **Post-Matric Scholarship**\n"
            "Status: 🟡 Institution Verification-la irukku\n"
            "Progress: 60%\n\n"
            "2. **Top Class Scholarship**\n"
            "Status: 🟢 Sanctioned\n"
            "Progress: 85%"
        )

    if intent == "application":

        return (
            "📋 **Unga Application Status**\n\n"
            f"🎓 Post-Matric Scholarship\n"
            f"Application ID: "
            f"{student['applications']['Post-Matric Scholarship']['id']}\n"
            "Status: 🟡 Institution Verification-la irukku\n"
            "Progress: 60%\n\n"
            f"🏆 Top Class Scholarship\n"
            f"Application ID: "
            f"{student['applications']['Top Class Scholarship']['id']}\n"
            "Status: 🟢 Sanctioned\n"
            "Progress: 85%"
        )

    if intent == "documents":

        return (
            "📄 **Pending Documents**\n\n"
            "• Income Certificate\n"
            "• Institution Certificate\n\n"
            "Indha documents-a **Document Wallet** moolama upload pannalam."
        )

    if intent == "payment":

        return (
            "💰 **Payment Status**\n\n"
            "🟢 Top Class Scholarship\n"
            "Processed Amount: ₹42,000\n"
            "Status: Processed\n\n"
            "🟡 Post-Matric Scholarship\n"
            "Pending Amount: ₹18,500\n"
            "Status: Final Sanction-kaga wait pannitu irukku."
        )

    if intent == "eligibility":

        return (
            "✅ **Eligibility Information**\n\n"
            f"Unga category **{student['category']}**. "
            "Profile-la neenga ST student-ah registered irukkinga.\n\n"
            "Explore panna mudiyura schemes:\n"
            "• Pre-Matric Scholarship\n"
            "• Post-Matric Scholarship\n"
            "• Top Class Scholarship\n"
            "• National Fellowship for ST Students\n"
            "• National Overseas Scholarship\n\n"
            "⚠️ Final eligibility official rules, academic requirements, "
            "income limits and verification-a depend pannum."
        )

    if intent == "verification":

        return (
            "🔍 **Verification Status**\n\n"
            "Unga Post-Matric Scholarship ippo:\n\n"
            "🟡 **Institution Verification** stage-la irukku.\n\n"
            "Next stages:\n"
            "1. Document Verification\n"
            "2. Ministry Verification\n"
            "3. Sanction\n"
            "4. DBT Processing"
        )

    if intent == "top_class":

        return (
            "🏆 **Top Class Scholarship**\n\n"
            "Status: 🟢 Sanctioned\n"
            "Sanctioned Amount: ₹42,000\n"
            "Progress: 85%\n\n"
            "Prototype-la DBT payment processed-nu show aagudhu."
        )

    if intent == "overseas":

        return (
            "🌎 **National Overseas Scholarship (NOS)**\n\n"
            "Eligible ST students higher studies abroad pursue panna "
            "indha scheme support pannum.\n\n"
            "Final eligibility official NOS guidelines-a depend pannum."
        )

    return (
        "🤔 Indha question-a full-ah understand panna mudiyala.\n\n"
        "Application, documents, eligibility, verification "
        "illa payment pathi kekkalam."
    )


# =========================================================
# INTENT DETECTION
# =========================================================

def detect_intent(question):

    q = question.lower().strip()

    q = q.replace("?", "")
    q = q.replace("!", "")
    q = q.replace(".", "")
    q = q.replace(",", "")

    # GREETING

    greeting_words = [
        "hi",
        "hello",
        "hey",
        "vanakkam",
        "வணக்கம்",
        "नमस्ते",
        "नमस्कार"
    ]

    if any(word in q for word in greeting_words):
        return "greeting"


    # PAYMENT

    payment_words = [
        "payment",
        "dbt",
        "money",
        "amount",
        "பணம்",
        "கட்டணம்",
        "भुगतान",
        "राशि",
        "पैसे",
        "payment status"
    ]

    if any(word in q for word in payment_words):
        return "payment"


    # DOCUMENTS

    document_words = [
        "document",
        "documents",
        "certificate",
        "upload",
        "ஆவணம்",
        "ஆவணங்கள்",
        "சான்றிதழ்",
        "दस्तावेज़",
        "दस्तावेज",
        "प्रमाण पत्र"
    ]

    if any(word in q for word in document_words):
        return "documents"


    # VERIFICATION

    verification_words = [
        "verification",
        "verify",
        "verified",
        "சரிபார்ப்பு",
        "சரிபார்க்க",
        "सत्यापन",
        "सत्यापित"
    ]

    if any(word in q for word in verification_words):
        return "verification"


    # TOP CLASS

    top_class_words = [
        "top class",
        "topclass",
        "टॉप क्लास",
        "டாப் கிளாஸ்"
    ]

    if any(word in q for word in top_class_words):
        return "top_class"


    # OVERSEAS

    overseas_words = [
        "overseas",
        "national overseas",
        "nos scholarship",
        "विदेश",
        "विदेशी",
        "வெளிநாடு",
        "வெளிநாட்டு"
    ]

    if any(word in q for word in overseas_words):
        return "overseas"


    # ELIGIBILITY

    eligibility_words = [
        "eligibility",
        "eligible",
        "apply",
        "am i eligible",
        "தகுதி",
        "தகுதியா",
        "விண்ணப்பிக்க",
        "पात्रता",
        "पात्र",
        "आवेदन कर"
    ]

    if any(word in q for word in eligibility_words):
        return "eligibility"


    # APPLICATION

    application_words = [
        "application status",
        "application",
        "status",
        "என் application",
        "application status enna",
        "விண்ணப்ப நிலை",
        "आवेदन की स्थिति",
        "आवेदन स्थिति",
        "स्थिति",
        "मेरा आवेदन"
    ]

    if any(word in q for word in application_words):
        return "application"


    # SCHOLARSHIPS

    scholarship_words = [
        "scholarship",
        "scholarships",
        "என் scholarship",
        "எந்த scholarship",
        "உதவித்தொகை",
        "छात्रवृत्ति",
        "मेरी छात्रवृत्ति",
        "कौन सी छात्रवृत्ति"
    ]

    if any(word in q for word in scholarship_words):
        return "scholarships"


    return "unknown"


# =========================================================
# CHAT INPUT
# =========================================================

user_question = st.chat_input(
    "Ask JAGO in English, Hindi, Tamil or Thanglish..."
)


# =========================================================
# QUICK QUESTION PROCESSING
# =========================================================

if st.session_state.get("jago_question"):

    user_question = st.session_state["jago_question"]

    st.session_state["jago_question"] = ""


# =========================================================
# PROCESS QUESTION
# =========================================================

if user_question:

    intent = detect_intent(user_question)

    language = st.session_state["jago_language"]

    if language == "hindi":

        response = response_hindi(intent)

    elif language == "tamil":

        response = response_tamil(intent)

    elif language == "thanglish":

        response = response_thanglish(intent)

    else:

        response = response_english(intent)


    # Save user message

    st.session_state["jago_messages"].append(
        {
            "role": "user",
            "content": user_question
        }
    )


    # Save JAGO response

    st.session_state["jago_messages"].append(
        {
            "role": "assistant",
            "content": response
        }
    )


    st.rerun()


# =========================================================
# CHAT CONTROLS
# =========================================================

st.divider()

col1, col2, col3 = st.columns(3)


with col1:

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state["jago_messages"] = []

        st.rerun()


with col2:

    if st.button(
        "🎓 Scholarships",
        use_container_width=True
    ):

        st.switch_page(
            "pages/scholarships.py"
        )


with col3:

    if st.button(
        "📄 Documents",
        use_container_width=True
    ):

        st.switch_page(
            "pages/documents.py"
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🤖 JAGO • Multilingual AI Scholarship Assistant • VANVIDHYA"
)

st.caption(
    "Your Education. Your Opportunities. One Platform."
)

st.caption(
    "SMART INDIA HACKATHON 2026 • CoreSynch"
)