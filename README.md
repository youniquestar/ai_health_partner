# WellSync: AI-Powered Health Partner & Triage Engine

![WellSync Logo](assets/logo.png)

## 🩺 Project Overview
**WellSync** is an intelligent conversational engine designed to bridge the gap between overstrained healthcare systems and patient care. Developed during a high-stakes hackathon, this backend service automates the clinical triage process and maintains empathetic daily follow-ups to ensure treatment adherence.

As the **AI Backend Developer**, I architected a modular state-machine logic that parses unstructured patient natural language into validated clinical data without the unpredictability of raw LLM outputs.

---

## 🚀 Key Features
* **Automated Clinical Triage:** A 7-step onboarding flow that captures symptoms, duration, severity, and medical history.
* **Empathetic Daily Follow-Up:** A humanized check-in system that tracks medication doses taken vs. prescribed.
* **Health Score Analytics:** Algorithms that calculate a rolling 7-day "Wellness Percentage" based on self-reported data.
* **Escalation Logic:** Integrated regex-based triggers that instantly flag hazardous symptoms for human professional review.
* **Persistent Session Memory:** Secure SQLite implementation that maintains patient context across server restarts using JSON-encoded states.

---

## 🛠️ Technical Stack
* **Language:** Python 3.10+
* **Framework:** FastAPI (Asynchronous request handling)
* **Database:** SQLite (Persistent local storage)
* **Validation:** Pydantic (Strict data-type enforcement for medical reports)
* **Logic:** Custom Finite State Machine (FSM) for conversational routing

---

## 🏗️ System Architecture
The engine is built on a **Three-Tier Architecture** to ensure scalability and separation of concerns:

1. **Patient UI (Frontend):** A lightweight interface for low-friction data entry.
2. **Core Engine (Backend):** Asynchronous FastAPI routes managing data flow and session security.
3. **AI Logic Service:** The "Clinical Brain" utilizing state-machine logic to convert chat into structured JSON reports for doctor dashboards.

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/youniquestar/ai_health_partner.git](https://github.com/youniquestar/ai_health_partner.git)
   cd ai_health_partner

2. **Install dependencies:**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt

3. **Run the local development server:**
   Launch the FastAPI engine using Uvicorn:
   ```bash
   uvicorn main:app --reload

---
   
## 🛡️ Security & Compliance

1. **Data Sandboxing:** The architecture prevents cross-session data leaks between unique user_id keys by isolating session states in the SQLite backend.
2. **Scope Limitation:** Designed strictly as an administrative data-gathering tool; it does not independently diagnose or prescribe medication.
3. **Emergency Bypass:** Integrated triggers identify hazardous symptom keywords to immediately escalate the case to a licensed human practitioner.

---

## 👨‍💻 About the Developer
Developed by Alao Jeremiah, a Mechatronics Engineering student in Nigeria specializing in IoT, robotics, and AI-driven automation systems. This project reflects my commitment to building engineering solutions that address real-world healthcare infrastructure bottlenecks.
   git clone [https://github.com/alaojeremiah/wellsync-backend.git](https://github.com/alaojeremiah/wellsync-backend.git)
   cd wellsync-backend
