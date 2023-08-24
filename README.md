# Customer Churn Prediction Web Application 🚀📊

## Introduction

Welcome to the Customer Churn Prediction Web Application! This end-to-end solution predicts whether a customer is likely to churn based on their information. The application includes a front-end built using Streamlit and a backend API developed with FastAPI. The prediction model is trained using a Jupyter Notebook, covering data loading, preprocessing, feature engineering, modeling, hyperparameter tuning, and model persistence using Joblib.

## Getting Started 🏁

Directly access the application using this link: [link](https://customer-churn-prediction-ak.streamlit.app/)

OR 

Follow these steps to run the Customer Churn Prediction Web Application locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AdityaKulshrestha/Churn-Prediction.git
   cd Churn-Prediction
   ```
2. **Set up a virtual environment (recommended):**
    ```commandline
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate    
    ```
3. **Install the required packages:**
    ```
   pip install -r requirements.txt
   ```
4. **Run the FastAPI backend:**
    ```
   uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
    ```
5. **Run the Strealit Application:**
    ```
   streamtlit run main.py
   ```
6. **Access the application in your browser:**
   - FastAPI API documentation: http://localhost:8000/docs
   - Streamlit Web Application: http://localhost:8501

## Contribution Guide 🤝
We welcome contributions to make this project even better! Here's how you can contribute:

- Fork the repository.
- Create a new branch for your feature/bug fix.
- Make your changes and test thoroughly.
- Submit a pull request with a clear description of your changes.


## Jupyter Notebook 📓
A detailed Jupyter Notebook (Churn_Prediction.ipynb) covers the complete machine learning pipeline:

- Data loading and exploration.
- Data preprocessing and cleaning.
- Feature engineering and transformation.
- Model selection and training.
- Hyperparameter tuning using RandomizedSearchCV.
- Model evaluation and interpretation.
- Dumping the trained model using Joblib.
- Feel free to explore and adapt the notebook to your dataset and problem.


### Happy predicting! 🎉🔮
