import streamlit as st


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def main():
    st.title("Age Calculator with BMI")

    # Age Calculator
    st.header("Age Calculator")
    birth_year = st.number_input("Enter your birth year", min_value=1900, max_value=2024, value=1990)
    current_year = st.number_input("Enter the current year", min_value=1900, max_value=2024, value=2024)

    age = current_year - birth_year
    st.write(f"Your age is {age} years.")

    # BMI Calculator
    st.header("BMI Calculator")
    weight = st.number_input("Enter your weight (kg)", min_value=0.0, max_value=300.0, value=70.0)
    height = st.number_input("Enter your height (m)", min_value=0.0, max_value=3.0, value=1.75)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is {bmi:.2f}")
        if bmi < 18.5:
            st.write("Underweight")
        elif 18.5 <= bmi < 25:
            st.write("Normal weight")
        elif 25 <= bmi < 30:
            st.write("Overweight")
        else:
            st.write("Obese")


if __name__ == "__main__":
    main()