
# 📱 Expresso Churn Prediction

This project is a **Streamlit web application** that predicts whether a telecom customer is likely to churn based on their usage behavior. The dataset is based on the **Expresso Churn Prediction Challenge** hosted on Zindi.

---

## **Dataset**

- Expresso is a telecommunications company operating in **Mauritania** and **Senegal**.
- The dataset contains **2.5 million customers** and over **15 behavioral features**.
- Example features: `REGION`, `TENURE`, `MONTANT`, `FREQUENCE_RECH`, `REVENUE`, `ARPU_SEGMENT`, `DATA_VOLUME`, `ON_NET`, `ORANGE`, `TIGO`, `TOP_PACK`, etc.
- Target variable: `CHURN` (1 = customer churned, 0 = customer retained)

Dataset link (sample screenshot):  
![Dataset](https://i.imgur.com/OQKLgVy.png)

---

## **Project Steps**

1. **Environment Setup**  
   - Install Python 3.10+ and create a virtual environment.
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Data Exploration & Preprocessing**  
   - Imported dataset with `pandas`.
   - Handled missing and corrupted values.
   - Removed duplicates and handled outliers.
   - Encoded categorical features.

3. **Model Training**  
   - Trained a machine learning classifier to predict churn.
   - Saved the trained model using `joblib` as `expresso_model.pkl`.

4. **Streamlit App**  
   - Built a user interface to input customer details.
   - Integrated the trained model to make real-time predictions.
   - Run the app locally:
     ```bash
     streamlit run app.py
     ```

---

## **Input Features in the App**

- REGION  
- TENURE (months)  
- MONTANT (Recharge Amount)  
- FREQUENCE_RECH (Recharge Frequency)  
- REVENUE  
- ARPU_SEGMENT  
- FREQUENCE  
- DATA_VOLUME (MB)  
- ON_NET (On Net Calls)  
- ORANGE (Calls)  
- TIGO (Calls)  
- REGULARITY  
- TOP_PACK  
- FREQ_TOP_PACK  
- MRG  

> The input fields match the features used during model training.

---

## **How to Use**

1. Clone this repository.
2. Navigate to the project folder.
3. Create a virtual environment and install dependencies.
4. Run the Streamlit app:
   ```bash
   streamlit run app.py


5. Enter customer details and click **Predict Churn**.

---

## **Notes**

* This project is deployed **locally**.
* The `venv` folder is excluded from Git. Dependencies are listed in `requirements.txt`.

---

