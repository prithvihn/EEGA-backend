# 🚨 EEGA — Emergency Extreme Guidance Assistant

> **Your AI-powered lifeline in critical moments.**
> Instant emergency guidance, nearby hospital discovery, and ambulance services — all in one intelligent backend.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=flat-square&logo=fastapi)
![AI Powered](https://img.shields.io/badge/AI--Powered-ML%20Backend-orange?style=flat-square&logo=openai)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/status-active-brightgreen?style=flat-square)

---

## 🆘 What is EEGA?

**EEGA (Emergency Extreme Guidance Assistant)** is a smart, AI-driven backend system built to assist users during life-threatening emergencies. When every second counts, EEGA steps in with calm, accurate, and actionable guidance.

Whether someone is experiencing a **🔥 fire breakout**, a **🐍 snake bite**, a **cardiac arrest**, a **drowning incident**, a **road accident**, or any other emergency — EEGA instantly:

- 📋 **Identifies the emergency type** from user input
- ✅ **Provides step-by-step first-aid and precautionary guidance**
- 🏥 **Locates the nearest hospitals and emergency care centers**
- 🚑 **Connects to nearby ambulance services**
- 📍 **Uses real-time geolocation** to serve location-aware results

> *Built for the moments when people need help the most.*

---

## 🌐 System Overview

```
User (Web App)
      │
      ▼
 EEGA Frontend
      │
      ▼
 EEGA Backend (This Repo)
      ├── 🤖 AI/ML Emergency Classifier
      ├── 📋 Guidance Engine (precautions & first-aid steps)
      ├── 🗺️  Location Services (nearby hospitals & ambulances)
      └── 🔔 Alert & Notification System
```

---

## 🔥 Supported Emergency Types

| Emergency | Guidance | Nearby Services |
|-----------|----------|-----------------|
| 🔥 Fire / Burn | Yes | Fire Station, Hospital |
| 🐍 Snake Bite | Yes | Hospital, Poison Control |
| ❤️ Cardiac Arrest | Yes | Hospital, Ambulance |
| 🚗 Road Accident | Yes | Hospital, Ambulance, Police |
| 🌊 Drowning | Yes | Hospital, Rescue |
| ⚡ Electric Shock | Yes | Hospital, Emergency Care |
| 🤕 Fracture / Injury | Yes | Hospital, Ambulance |
| 🧠 Stroke | Yes | Hospital, Ambulance |
| 🐶 Animal Bite | Yes | Hospital, Vet (if applicable) |
| 🌪️ Natural Disaster | Yes | Rescue Center, Shelter |
| ➕ More Emergencies... | Yes | Contextual Services |

---

## 📁 Project Structure

```
EEGA-backend/
├── app/
│   ├── main.py                  # App entry point
│   ├── routes/
│   │   ├── emergency.py         # Emergency detection & guidance routes
│   │   ├── location.py          # Nearby hospital & ambulance routes
│   │   └── health.py            # Health check routes
│   ├── services/
│   │   ├── classifier.py        # AI/ML emergency type classifier
│   │   ├── guidance_engine.py   # First-aid & precaution generator
│   │   └── location_service.py  # Geolocation & nearby services finder
│   ├── models/
│   │   └── emergency_model/     # Trained ML model files
│   ├── data/
│   │   └── guidance_db.json     # Emergency guidance knowledge base
│   └── utils/
│       ├── geoutils.py          # Location helpers
│       └── formatter.py         # Response formatters
├── tests/                       # Unit & integration tests
├── requirements.txt
├── .env.example
├── Dockerfile
└── README.md
```

---

## 🚀 Installation & Setup

### ✅ Prerequisites

- **Python 3.10+**
- **pip**
- A Google Maps API key *(for location services)*
- (Optional) **Docker**

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/prithvihn/EEGA-backend.git
cd EEGA-backend
```

### Step 2 — Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure Environment Variables

```bash
cp .env.example .env
```

Update the `.env` file:

```env
APP_ENV=development
HOST=0.0.0.0
PORT=8000

# Google Maps / Places API for locating hospitals & ambulances
MAPS_API_KEY=your_google_maps_api_key

# ML Model config
MODEL_PATH=./app/models/emergency_model/
CONFIDENCE_THRESHOLD=0.75

# App Secret
SECRET_KEY=your_secret_key_here
```

### Step 5 — Run the Server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

🟢 Server live at: `http://localhost:8000`
📖 Swagger Docs: `http://localhost:8000/docs`

---

### 🐳 Docker Setup (Optional)

```bash
# Build
docker build -t eega-backend .

# Run
docker run -p 8000:8000 --env-file .env eega-backend
```

---

## 📡 API Endpoints

**Base URL:** `http://localhost:8000/api/v1`

---

### 🔍 Health Check

| Method | Endpoint  | Description        |
|--------|-----------|--------------------|
| `GET`  | `/health` | Server status check |

**Response:**
```json
{
  "status": "ok",
  "service": "EEGA Backend",
  "version": "1.0.0"
}
```

---

### 🆘 Emergency Detection & Guidance

| Method | Endpoint              | Description                                      |
|--------|-----------------------|--------------------------------------------------|
| `POST` | `/emergency/detect`   | Detect emergency type from user description      |
| `POST` | `/emergency/guidance` | Get step-by-step first-aid & precaution guidance |
| `GET`  | `/emergency/types`    | List all supported emergency categories          |

---

**`POST /emergency/detect`**

Classifies the type of emergency from natural language input.

Request:
```json
{
  "description": "I just got bitten by a snake on my leg and it's swelling fast",
  "language": "en"
}
```

Response:
```json
{
  "emergency_type": "snake_bite",
  "confidence": 0.97,
  "severity": "critical",
  "immediate_action": "Stay calm and immobilize the affected limb. Call emergency services immediately."
}
```

---

**`POST /emergency/guidance`**

Returns detailed, ordered first-aid steps and precautions for a given emergency.

Request:
```json
{
  "emergency_type": "snake_bite",
  "user_location": {
    "latitude": 12.9716,
    "longitude": 77.5946
  }
}
```

Response:
```json
{
  "emergency_type": "snake_bite",
  "severity": "critical",
  "do": [
    "Keep the victim calm and still",
    "Immobilize the bitten limb below heart level",
    "Remove tight clothing or jewelry near the bite",
    "Mark the edge of swelling with a pen and note the time",
    "Call emergency services or get to a hospital immediately"
  ],
  "do_not": [
    "Do NOT suck out the venom",
    "Do NOT apply a tourniquet",
    "Do NOT apply ice or cold water",
    "Do NOT give the victim alcohol or pain killers"
  ],
  "call_immediately": true
}
```

---

### 🏥 Nearby Services

| Method | Endpoint                       | Description                               |
|--------|--------------------------------|-------------------------------------------|
| `POST` | `/location/hospitals`          | Find nearest hospitals based on location  |
| `POST` | `/location/ambulance`          | Get nearby ambulance service contacts     |
| `POST` | `/location/emergency-services` | Get all nearby emergency services         |

---

**`POST /location/hospitals`**

Request:
```json
{
  "latitude": 12.9716,
  "longitude": 77.5946,
  "emergency_type": "snake_bite",
  "radius_km": 10
}
```

Response:
```json
{
  "results": [
    {
      "name": "City General Hospital",
      "address": "123 MG Road, Bengaluru",
      "distance_km": 1.4,
      "phone": "+91-80-12345678",
      "open_now": true,
      "has_emergency_ward": true,
      "maps_url": "https://maps.google.com/?q=..."
    },
    {
      "name": "Apollo Hospital",
      "address": "456 Bannerghatta Road, Bengaluru",
      "distance_km": 3.1,
      "phone": "+91-80-98765432",
      "open_now": true,
      "has_emergency_ward": true,
      "maps_url": "https://maps.google.com/?q=..."
    }
  ],
  "total": 2
}
```

---

**`POST /location/ambulance`**

Request:
```json
{
  "latitude": 12.9716,
  "longitude": 77.5946
}
```

Response:
```json
{
  "national_helpline": "108",
  "nearby_services": [
    {
      "name": "Ziqitza Ambulance",
      "phone": "+91-98XXXXXXXX",
      "eta_minutes": 7,
      "distance_km": 2.1
    }
  ]
}
```

---

### 🔔 Alert System

| Method | Endpoint      | Description                                     |
|--------|---------------|-------------------------------------------------|
| `POST` | `/alert/send` | Send emergency alert to registered contacts     |

Request:
```json
{
  "user_id": "user_001",
  "emergency_type": "fire",
  "location": {
    "latitude": 12.9716,
    "longitude": 77.5946,
    "address": "12th Cross, Indiranagar, Bengaluru"
  },
  "contacts": ["+91-9876543210"]
}
```

Response:
```json
{
  "alert_sent": true,
  "notified_contacts": 1,
  "message": "Emergency alert dispatched successfully."
}
```

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

For coverage report:
```bash
pytest tests/ --cov=app --cov-report=html
```

---

## 🛠️ Tech Stack

| Layer              | Technology                          |
|--------------------|-------------------------------------|
| Language           | Python 3.10+                        |
| Framework          | FastAPI / Flask                     |
| AI/ML              | scikit-learn / TensorFlow / PyTorch |
| NLP Classification | Transformers / spaCy                |
| Location Services  | Google Maps & Places API            |
| Database           | PostgreSQL / MongoDB                |
| Server             | Uvicorn / Gunicorn                  |
| Containerization   | Docker                              |

---

## 🤝 Contributing

We welcome contributions! This is a life-saving project and every improvement matters. 💙

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "feat: describe your change"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 💙 A Note from the Team

> *"In emergencies, people panic — EEGA doesn't."*
>
> This project was built with the belief that technology should save lives.
> Every line of code here exists to give someone, somewhere, a fighting chance. 🙏

---

<div align="center">
  <sub>Built with ❤️ and purpose by <a href="https://github.com/prithvihn">prithvihn</a> & the EEGA Team</sub>
</div># EEGA_backend
