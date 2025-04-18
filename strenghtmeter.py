import streamlit as st # type:ignore
import re

st.set_page_config(
    page_title="Strength Meter",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="expanded",
)
st.title("Password Strength Meter")
st.write(
    "This app evaluates the strength of your password based on length, character variety, and common patterns."
)
st.write(
    "Enter a password to see its strength score and suggestions for improvement."
)
def password_strength(password: str) -> int:
    """
    Evaluate the strength of a password based on length, character variety, and common patterns.
    Returns a score from 0 (weak) to 5 (very strong).
    """
    length_score = len(password) >= 8
    variety_score = (
        bool(re.search(r"[a-z]", password))
        + bool(re.search(r"[A-Z]", password))
        + bool(re.search(r"[0-9]", password))
        + bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    )
    common_patterns = [
        r"1234",
        r"password",
        r"qwerty",
        r"abc",
        r"letmein",
    ]
    pattern_score = not any(re.search(pattern, password) for pattern in common_patterns)

    score = length_score + variety_score + pattern_score
    return score
def strength_description(score: int) -> str:
    """
    Provide a description of the password strength based on the score.
    """
    if score == 0:
        return "Very Weak: Your password is too short and lacks variety."
    elif score == 1:
        return "Weak: Your password is short and lacks variety."
    elif score == 2:
        return "Fair: Your password is of moderate length but lacks variety."
    elif score == 3:
        return "Good: Your password is of good length and has some variety."
    elif score == 4:
        return "Strong: Your password is strong with good length and variety."
    else:
        return "Very Strong: Your password is very strong with excellent length and variety."
def main():
    password = st.text_input("Enter your password:", type="password")
    if password:
        score = password_strength(password)
        description = strength_description(score)
        st.write(f"Password Strength Score: {score}/5")
        st.write(description)
        if score < 3:
            st.warning("Consider using a longer password with a mix of characters.")
        else:
            st.success("Your password is strong!")
if __name__ == "__main__":
    main()
# Streamlit app to evaluate password strength
# based on length, character variety, and common patterns.
# The app provides a score and suggestions for improvement.
# The password strength is evaluated based on:
# - Length: Minimum 8 characters
# - Variety: At least one lowercase letter, one uppercase letter, one digit, and one special character
# - Common patterns: Avoid common passwords like "1234", "password", etc.
# The score is calculated as follows:
# - 0: Very Weak
# - 1: Weak
# - 2: Fair     

