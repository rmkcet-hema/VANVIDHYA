# VANVIDHYA

## A Unified Digital Gateway for Tribal Student Scholarships

**SMART INDIA HACKATHON 2026**  
**Problem Statement ID:** 26238  
**Problem Statement:** Unified Scholarship Mobile Application for Tribal Students  
**Team:** CoreSynch  
**Category:** Software  
**Theme:** Smart Automation

---

## 1. About VANVIDHYA

VANVIDHYA is a mobile-first digital scholarship assistance platform designed to provide tribal students with a unified view of scholarship opportunities, applications, verification, documents, payment status and support services.

The platform is designed around a simple principle:

> **One Student. One Platform. Multiple Opportunities.**

Instead of requiring students to navigate multiple scholarship systems and separately track their application progress, VANVIDHYA brings the major stages of the scholarship journey into one unified interface.

The prototype focuses on improving accessibility, transparency, document reuse, verification visibility and student assistance.

---

## 2. Problem Statement

Tribal students may need to interact with multiple scholarship systems and processes depending on the scholarship scheme they are applying for.

The major challenges include:

- Multiple scholarship portals and systems
- Repeated submission of student information and documents
- Difficulty tracking application progress
- Limited visibility into verification stages
- Unclear reasons for pending or deficient applications
- Separate tracking of scholarship payments and DBT status
- Difficulty identifying suitable scholarship opportunities
- Lack of a consolidated student scholarship profile
- Students potentially remaining outside scholarship coverage despite being enrolled
- Limited access to personalized scholarship assistance

These challenges can make the scholarship process more difficult to understand and follow.

---

## 3. VANVIDHYA Solution

VANVIDHYA proposes a unified digital interface where students can manage and monitor their scholarship journey from a single platform.

The platform brings together:

- Scholarship discovery
- Eligibility assistance
- Application support
- Document management
- Application tracking
- Verification status
- Payment and DBT information
- AI-assisted scholarship support
- Beneficiary gap identification
- Unified verification and integration

The platform is designed to work as a common interface over authorized scholarship systems and government data sources.

---

## 4. Key Features

### 🎓 Unified Scholarship Module

Provides a single interface for major Ministry of Tribal Affairs scholarship schemes:

1. Pre-Matric Scholarship
2. Post-Matric Scholarship
3. Top Class Scholarship
4. National Fellowship for ST Students (NFST)
5. National Overseas Scholarship (NOS)

Students can explore scheme information and initiate the relevant scholarship workflow.

---

### ✅ Smart Eligibility Checker

The eligibility module provides preliminary scholarship guidance using student-provided information such as:

- Community category
- Annual family income
- Education level
- Academic performance
- Institution
- Existing scholarship status

The prototype demonstrates rule-based eligibility assistance.

Final eligibility remains subject to the applicable official scheme rules and authorized verification systems.

---

### 📄 Digital Document Wallet

VANVIDHYA provides a centralized document management interface for scholarship-related records.

Example documents include:

- Identity documents
- ST Certificate
- Income Certificate
- Academic Marksheet
- Domicile Certificate
- Institution Certificate

The concept supports document reuse and integration with digital document services such as DigiLocker, subject to authorized access.

---

### 📋 Application Tracking

Students can monitor the progress of their applications through stages such as:

**Application Submitted → Institution Verification → Document Verification → Ministry Verification → Sanction → DBT / Disbursement**

This provides a clearer view of where an application currently stands.

---

### 💰 Payment & DBT Tracking

The payment module provides a consolidated view of:

- Sanctioned amount
- Disbursed amount
- Pending amount
- DBT status
- Payment reference
- Scholarship-wise payment history

This helps students understand the status of scholarship disbursement.

---

### 🔔 Notifications

The notification module provides updates related to:

- Application submission
- Document verification
- Institution verification
- Payment processing
- Missing documents
- Required student actions

The prototype also demonstrates configurable notification preferences.

---

### 🤖 JAGO AI Scholarship Assistant

**JAGO – Your AI Scholarship Assistant**

JAGO is the conversational assistance component of VANVIDHYA.

It is designed to help students with:

- Scholarship information
- Eligibility guidance
- Application status
- Required documents
- Pending deficiencies
- Payment information
- Next steps

The concept supports multilingual interaction to improve accessibility for students from different linguistic backgrounds.

The current prototype demonstrates the interaction and response workflow using simulated student data.

---

### 🔎 Beneficiary Gap Detection

The Beneficiary Gap Detection module demonstrates how enrolled student records can potentially be compared against scholarship records.

The prototype uses sources such as:

- UDISE+
- APAAR
- OTR
- AISHE
- Scholarship records

The objective is to identify students who may require scholarship outreach because no corresponding scholarship record is found.

The prototype demonstrates the matching workflow and simulated outreach process.

---

### 🔗 Unified Verification & Integration Layer

The Integration Layer acts as the conceptual backbone of VANVIDHYA.

It provides a unified interface for scholarship and government data sources such as:

- National Scholarship Portal (NSP)
- SFMP
- National Overseas Scholarship Portal
- DigiLocker
- UDISE+
- APAAR
- AISHE
- State e-District

The verification engine demonstrates comparison of:

- Student identity
- ST certificate
- Income certificate
- Academic records
- Institution information
- Scholarship applications
- Previous scholarship records

Matching records can proceed through automated processing, while mismatches can be routed for manual review.

---

## 5. Proposed Verification Workflow

```text
Student Profile
       ↓
Data Synchronization
       ↓
Identity Matching
       ↓
Document Verification
       ↓
Eligibility Rules
       ↓
Match / Mismatch Detection
       ↓
 ┌───────────────┐
 │               │
Match         Mismatch
 │               │
 ↓               ↓
Auto Process   Manual Review
 │               │
 └───────┬───────┘
         ↓
Application Processing
         ↓
Sanction
         ↓
DBT / Disbursement

## 6. Proposed System Architecture

                    VANVIDHYA
                        │
                Unified Interface
                        │
               Unified API Gateway
                        │
          ┌─────────────┴─────────────┐
          │                           │
 Verification Engine          Eligibility Engine
          │                           │
    ┌─────┼─────┐              ┌─────┼─────┐
    │     │     │              │     │     │
   NSP   SFMP   NOS            ST   Income Academic
    │     │     │
    └─────┼─────┘
          │
   Government Data Layer
          │
 ┌────────┼───────────────┐
 │        │       │       │
DigiLocker UDISE+ APAAR AISHE
          │
    State e-District
          │
   Verification Result
          │
     ┌────┴────┐
     │         │
   Match    Mismatch
     │         │
Auto Process Manual Review

7. Technology Stack

Frontend / Application
Streamlit
Python
Responsive web interface
Custom CSS-based UI
Data Processing
Pandas
Python-based rule processing
Structured application and verification data
AI / Assistance
JAGO conversational assistant concept
Rule-based scholarship assistance
Future integration with NLP/LLM services
Proposed Integration Technologies
REST APIs
API Gateway
JSON-based data exchange
Authorized government APIs
Secure authentication mechanisms
Proposed Data Sources
NSP
SFMP
NOS
DigiLocker
UDISE+
APAAR
AISHE
State e-District

8. Security & Privacy

Scholarship systems involve sensitive student information. VANVIDHYA therefore considers security and privacy as important components of the proposed architecture.

The prototype demonstrates the concept of:

OTP-based authentication
Role-based access control
Secure API access
Encrypted data transmission
Document protection
Audit logging
Controlled access to student information

A production implementation would require compliance with applicable government security, privacy, consent and data-governance requirements.

9. Prototype vs Production

VANVIDHYA is currently a functional prototype demonstrating the proposed user experience, workflow and system architecture.

Prototype

The current demonstration includes:

Simulated student profiles
Sample scholarship applications
Demonstration verification records
Mock payment information
Simulated government integration status
Demonstration beneficiary matching
JAGO conversational workflow
Prototype administrative dashboard
Production Implementation

A production deployment would require:

Official government API access
Authentication and authorization integration
Real-time scholarship database connectivity
Verified DigiLocker integration
Authorized identity verification
Secure document storage
Government-approved consent mechanisms
Production-grade monitoring and logging
Security and privacy audits
Integration approval from respective departments

No real government database is accessed by the current prototype.

10. Expected Impact

VANVIDHYA aims to improve the scholarship experience by providing:

For Students
One scholarship interface
Easier scholarship discovery
Reduced repeated documentation
Clear application tracking
Better visibility of deficiencies
Consolidated payment information
Personalized assistance
For Institutions
Better visibility of verification requirements
Easier identification of pending student actions
Structured verification workflows
For Administrators
Unified application monitoring
Exception management
Verification visibility
Beneficiary gap identification
Institution-level monitoring
Consolidated administrative insights
For Government Systems
Interoperability-oriented architecture
Structured verification workflow
Reduced information fragmentation
Potentially improved outreach to unreached beneficiaries

11. Accessibility

VANVIDHYA follows a mobile-first approach because students may access scholarship services primarily through mobile devices.

The proposed platform emphasizes:

Simple navigation
Clear application status
Accessible assistance
Multilingual support
Reduced information repetition
Centralized document access
Student-friendly terminology

12. Scalability

The proposed architecture is modular.

Individual components can be expanded independently:

Student Application
        ↓
Unified API Layer
        ↓
Verification Services
        ↓
Government Systems
        ↓
Analytics & Administration

Additional scholarship schemes, government data sources and verification services can be integrated without redesigning the entire student-facing interface.

13. Future Enhancements

Potential future development areas include:

Real-time government API integration
Advanced multilingual JAGO assistant
Voice-based scholarship assistance
Automated document OCR
Intelligent document classification
Advanced anomaly detection
Real-time DBT notifications
Mobile application deployment
Aadhaar/identity verification through authorized systems
Digital consent management
Advanced beneficiary prediction and outreach
Institution-level analytics
Government administrative analytics dashboard

14. Demonstration Flow

The prototype demonstration follows this journey:

Landing Page
     ↓
Student Login
     ↓
Student Dashboard
     ↓
Scholarship Discovery
     ↓
Eligibility Check
     ↓
Document Wallet
     ↓
Apply Scholarship
     ↓
Application Tracking
     ↓
Verification
     ↓
Sanction
     ↓
DBT / Payment
     ↓
Notifications
     ↓
JAGO Assistance

Administrative workflow:

Admin Dashboard
       ↓
Application Monitoring
       ↓
Verification Queue
       ↓
Integration Layer
       ↓
Exception Management
       ↓
Beneficiary Gap Detection
       ↓
Student / Institution Outreach

15. Project Status

Current Status: Functional Prototype

The prototype demonstrates the complete conceptual workflow of VANVIDHYA, including student services, administrative monitoring, verification workflows, integration architecture and beneficiary outreach.

The current implementation is intended for demonstration and hackathon evaluation and uses simulated data where real government integrations are not available.

16. Team CoreSynch

SMART INDIA HACKATHON 2026

Problem Statement ID: 26238

Unified Scholarship Mobile Application for Tribal Students

17. Conclusion

VANVIDHYA proposes a unified digital experience for tribal student scholarship services by bringing scholarship discovery, eligibility, documentation, verification, application tracking, payment visibility, AI assistance and beneficiary outreach into one platform.

The platform is designed to reduce fragmentation for students while providing a structured foundation for verification, interoperability and administrative monitoring.

Your Education. Your Opportunities. One Platform.

18. Disclaimer

VANVIDHYA is a prototype developed for Smart India Hackathon 2026.

All student records, application IDs, payment details, verification results and integration statuses displayed in the prototype are demonstration data unless explicitly stated otherwise.

Actual production deployment would require authorization, official API access, appropriate security controls, privacy safeguards, consent mechanisms and integration with the respective government systems.


### Final project root

```text
VanVidhya/
│
├── app.py
├── navigation.py
├── requirements.txt
├── ABOUT.md
│
├── pages/
│   ├── student_login.py
│   ├── dashboard.py
│   ├── scholarships.py
│   ├── apply_scholarship.py
│   ├── eligibility.py
│   ├── documents.py
│   ├── applications.py
│   ├── payment.py
│   ├── notifications.py
│   ├── jago.py
│   ├── beneficiary_gap.py
│   ├── integration_layer.py
│   └── admin_dashboard.py
│
├── assets