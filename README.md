# 🩺 Diabetes Prediction using Machine Learning

## 📌 Project Overview

The **Diabetes Prediction System** is a Machine Learning web application that predicts whether a person is likely to have diabetes based on medical attributes such as glucose level, blood pressure, BMI, insulin level, age, and other health-related features.

The application is developed using **Python**, **Streamlit**, and **Scikit-learn**. A Machine Learning classification model is trained on the diabetes dataset and deployed through an interactive web interface, allowing users to enter their health details and receive an instant prediction.

This project demonstrates the complete Machine Learning pipeline, including data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment.

---

## 🚀 Features

- Predicts whether a person is diabetic or non-diabetic.
- User-friendly and interactive web interface.
- Real-time prediction using trained Machine Learning model.
- Data preprocessing and feature scaling.
- Responsive Streamlit application.
- Fast and accurate predictions.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Pickle

---

## 📂 Project Structure

```
Diabetes_Prediction/
│
├── app.py
├── model.pkl
├── diabetes.csv
├── model_training.ipynb
├── requirements.txt
├── README.md
│
├── static/
│
└── images/
```

---

## 📊 Dataset Information

The dataset contains the following medical features:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age

**Target Variable**

- Outcome
  - **0** → Non-Diabetic
  - **1** → Diabetic

---

## ⚙️ Machine Learning Workflow

1. Load the diabetes dataset.
2. Perform data cleaning and preprocessing.
3. Handle missing or invalid values.
4. Split the dataset into training and testing sets.
5. Train the Machine Learning classification model.
6. Evaluate the model using performance metrics.
7. Save the trained model using Pickle.
8. Build the Streamlit web application.
9. Accept user input.
10. Predict whether the person has diabetes.

---

## 📈 Machine Learning Model

- **Algorithm:** Gaussian Naive Bayes *(or your chosen algorithm such as Logistic Regression, Random Forest, Decision Tree, etc.)*
- **Problem Type:** Binary Classification
- **Library:** Scikit-learn

---

## ▶️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Diabetes_Prediction.git
```

### Navigate to the project directory

```bash
cd Diabetes_Prediction
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

## 📊 Model Evaluation

The model performance can be evaluated using:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC-AUC Score

---

## 💻 Application Screenshots

### Home Page

Add your application's home page screenshot here.

```text
![alt text](<diabetes home page.png>)
```

### Prediction Result

Add your prediction result screenshot here.

```text
![alt text](<diabetes result page.png>)
```

---

## 🌟 Future Enhancements

- Improve prediction accuracy using advanced algorithms.
- Add graphical health analytics.
- Deploy the application on Streamlit Community Cloud.
- Store prediction history using a database.
- Add user authentication.
- Integrate health recommendations based on prediction results.
- Support batch predictions using CSV uploads.

---

## 📚 Learning Outcomes

This project helped me gain practical experience in:

- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Classification Algorithms
- Model Evaluation
- Streamlit Application Development
- Machine Learning Model Deployment
- End-to-End Data Science Workflow

---

## 👩‍💻 Author

**Vasavi Maradugu**

GitHub: https://github.com/your-github-username

LinkedIn: https://linkedin.com/in/your-linkedin-profile

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

