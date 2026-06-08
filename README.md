# Precision Oncology AI System

## Overview

Precision Oncology AI System is a Flask-based web application that predicts cancer risk and recommends medicines and treatments based on patient information.

Users can:

- Upload CSV files
- Upload TXT files
- Upload PDF reports
- Enter patient details manually
- Receive cancer risk prediction
- Get medicine recommendations
- Get treatment recommendations

---

## Features

- Cancer Risk Prediction
- Medicine Recommendation
- Treatment Recommendation
- PDF File Support
- CSV File Support
- TXT File Support
- Manual Patient Data Input
- Responsive Web Interface
- Flask Backend

---

## Technology Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Libraries
- Pandas
- PDFPlumber
- Regular Expressions (re)

---

## Project Structure

```text
Precision-Oncology-AI/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Precision-Oncology-AI.git
```

### Open Project Folder

```bash
cd Precision-Oncology-AI
```

### Install Dependencies

```bash
pip install flask pandas pdfplumber
```

---

## Run Application

```bash
python app.py
```

Output:

```text
* Running on http://127.0.0.1:5000
```

Open Browser:

```text
http://127.0.0.1:5000
```

---

## Supported Input Formats

### CSV

Example:

```csv
Age,BMI,Tumor
55,31,4
```

### TXT

```text
Age 55
BMI 31
Tumor 4
```

### PDF

Any PDF report containing:

```text
Age 55
BMI 31
Tumor 4
```

### Manual Input

Example:

```text
Age 55 BMI 31 Tumor 4
```

---

## Risk Categories

| Risk Score | Category |
|------------|----------|
| 0-24 | Low |
| 25-49 | Moderate |
| 50-74 | High |
| 75-100 | Very High |

---

## Medicine Recommendations

### Low Risk

Medicines:
- Vitamin D Supplements
- Antioxidant Supplements

Treatments:
- Regular Screening
- Healthy Diet
- Exercise

### Moderate Risk

Medicines:
- Tamoxifen
- Anastrozole

Treatments:
- Oncologist Consultation
- Diagnostic Screening

### High Risk

Medicines:
- Cisplatin
- Carboplatin
- Paclitaxel

Treatments:
- Chemotherapy
- Radiation Therapy
- Targeted Therapy

### Very High Risk

Medicines:
- Pembrolizumab
- Nivolumab
- Osimertinib

Treatments:
- Immunotherapy
- Precision Oncology
- Personalized Treatment

---

## How It Works

1. User uploads a file or enters patient details.
2. Flask processes the input.
3. Patient information is extracted.
4. Cancer risk score is calculated.
5. Risk category is determined.
6. Recommended medicines and treatments are displayed.

---

## Future Improvements

- Deep Learning Model Integration
- Real Clinical Datasets
- Patient Dashboard
- User Authentication
- Report Generation
- Database Integration
- Cloud Deployment

---

## Author

Venkat

## License

This project is developed for educational and research purposes.
