from flask import Flask, render_template, request
import pandas as pd
import pdfplumber
import re
import random
import os

app = Flask(__name__)

medicine_data = {
    "Low": {
        "Medicines": ["Vitamin D Supplements", "Antioxidant Supplements"],
        "Treatment": ["Regular Screening", "Healthy Diet", "Exercise"]
    },
    "Moderate": {
        "Medicines": ["Tamoxifen", "Anastrozole"],
        "Treatment": ["Oncologist Consultation", "Diagnostic Screening"]
    },
    "High": {
        "Medicines": ["Cisplatin", "Carboplatin", "Paclitaxel"],
        "Treatment": ["Chemotherapy", "Radiation Therapy", "Targeted Therapy"]
    },
    "Very High": {
        "Medicines": ["Pembrolizumab", "Nivolumab", "Osimertinib"],
        "Treatment": ["Immunotherapy", "Precision Oncology", "Personalized Treatment"]
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    text = ""

    file = request.files.get("file")

    if file and file.filename:

        filename = file.filename.lower()

        if filename.endswith(".csv"):
            df = pd.read_csv(file)
            text = df.to_string()

        elif filename.endswith(".txt"):
            text = file.read().decode("utf-8")

        elif filename.endswith(".pdf"):
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text

    prompt_text = request.form.get("prompt", "")
    text += " " + prompt_text

    age = 50
    bmi = 25
    tumor = 2

    age_match = re.search(r'age[: ]*(\d+)', text, re.IGNORECASE)
    if age_match:
        age = int(age_match.group(1))

    bmi_match = re.search(r'bmi[: ]*(\d+)', text, re.IGNORECASE)
    if bmi_match:
        bmi = int(bmi_match.group(1))

    tumor_match = re.search(r'tumor[: ]*(\d+)', text, re.IGNORECASE)
    if tumor_match:
        tumor = int(tumor_match.group(1))

    risk = min(
        100,
        int(age * 0.5 + bmi + tumor * 5 + random.randint(0, 15))
    )

    if risk < 25:
        level = "Low"
    elif risk < 50:
        level = "Moderate"
    elif risk < 75:
        level = "High"
    else:
        level = "Very High"

    medicines = medicine_data[level]["Medicines"]
    treatments = medicine_data[level]["Treatment"]

    return render_template(
        "index.html",
        prediction=risk,
        risk_level=level,
        medicines=medicines,
        treatments=treatments
    )

if __name__ == '__main__':
    app.run(debug=True)