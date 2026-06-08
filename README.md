# Precision Oncology AI System

## Overview

Precision Oncology AI System is a Flask-based web application that predicts cancer risk using a Deep Learning model and provides medicine and treatment recommendations based on the predicted risk level.

Users can upload patient data in CSV format through a web interface and receive:

- Cancer Risk Percentage
- Risk Category
- Recommended Medicines
- Recommended Treatments

---

## Features

- Deep Learning based Cancer Risk Prediction
- User-friendly Flask Web Interface
- CSV File Upload Support
- Automatic Risk Classification
- Medicine Recommendation System
- Treatment Recommendation System

---

## Technologies Used

### Backend
- Python
- Flask
- TensorFlow / Keras
- Pandas
- Scikit-Learn

### Frontend
- HTML
- CSS
- JavaScript

---

## Project Structure

```text
Precision-Oncology-AI/
│
├── app.py
├── sample_100_records.csv
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── README.md
```

---

## Dataset

The model is trained using a cancer dataset containing features such as:

- Age
- BMI
- Smoking
- FamilyHistory
- TumorSize
- Total.Rate (Target Variable)

---

## Model Architecture

```text
Input Layer
     ↓
Dense (64 ReLU)
     ↓
Dense (32 ReLU)
     ↓
Dense (16 ReLU)
     ↓
Output Layer (Sigmoid)
```

### Training Parameters

- Optimizer: Adam
- Loss Function: Mean Squared Error (MSE)
- Metric: Mean Absolute Error (MAE)
- Epochs: 50
- Batch Size: 8

---

## Risk Categories

| Risk Percentage | Category |
|---------------|----------|
| 0 - 24 | Low |
| 25 - 49 | Moderate |
| 50 - 74 | High |
| 75 - 100 | Very High |

---

## Medicine Recommendations

### Low Risk
- Vitamin D Supplements
- Antioxidant Supplements

### Moderate Risk
- Tamoxifen
- Anastrozole

### High Risk
- Cisplatin
- Carboplatin
- Paclitaxel

### Very High Risk
- Pembrolizumab
- Nivolumab
- Osimertinib

---

## Treatment Recommendations

### Low Risk
- Regular Screening
- Healthy Diet
- Exercise

### Moderate Risk
- Oncologist Consultation
- Diagnostic Screening

### High Risk
- Chemotherapy
- Radiation Therapy
- Targeted Therapy

### Very High Risk
- Immunotherapy
- Precision Oncology
- Personalized Treatment

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Precision-Oncology-AI.git
```

Move into project directory:

```bash
cd Precision-Oncology-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Usage

1. Open the web application.
2. Upload a patient CSV file.
3. Click "Predict Cancer Risk".
4. View:
   - Predicted Cancer Risk
   - Risk Category
   - Recommended Medicines
   - Recommended Treatments

---

## Future Enhancements

- PDF Patient Report Analysis
- Multiple Cancer Type Prediction
- Medical Image Analysis
- Explainable AI Dashboard
- Cloud Deployment
- Real-Time Prediction API

---

## Disclaimer

This project is developed for educational and research purposes only.

The medicine and treatment recommendations provided are example outputs and should not be considered professional medical advice. Clinical decisions must always be made by qualified healthcare professionals.

---

## Author

Venkat
G PULLA REDDY ENGINEERING ,KURNOOL.

B.Tech Project – Precision Oncology AI System
