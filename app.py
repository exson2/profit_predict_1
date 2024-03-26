import streamlit as st
from joblib import load

loaded_model = load("profit_model.pkl")

def predict_profit(features):
    prediction = loaded_model.predict([features])
    return prediction[0]

def main():
    st.title("Profit Predictor")

    rd_spend = st.number_input("R&D Spend", value=0)
    adminstration = st.number_input("Administration Spend", value=0)
    marketing = st.number_input("Marketing Spend", value=0)

    if st.button("Predict"):
        features = [rd_spend, adminstration, marketing]
        predicition = predict_profit(features)
        st.success(f"Predicted profit is {predicition:.2f}")

if __name__ == "__main__":
    main()