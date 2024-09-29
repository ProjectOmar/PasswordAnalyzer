import streamlit as st
from streamlit_option_menu import option_menu
import zxcvbn

# Setting the page configuration to hide the Streamlit menu and adjust layout
st.set_page_config(page_title="Password Wizards", layout="wide")

# Creating pop-out navigation sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Password Wizards",
        options=["Password Analyzer", "Feedback", "About"],
        icons=["lock", "reply", "file-earmark-person"],
        default_index=0,
    )

# Password Analyzer
if selected == "Password Analyzer":

    # Header for password analyzer
    st.markdown(
        "<h1 style='text-align:left; border-radius:10px; font-size:50px;'>Password Analyzer</h1>",
        unsafe_allow_html=True,
    )
    st.info(
        "With passwords being used everywhere online, Password Analyzer helps improve security by checking the strength of any password you enter. It gives real-time feedback on how strong or weak the password is and suggests ways to make it better. The tool also shows how quickly a hacker could crack the password, helping users create more secure and complex passwords. This makes it a useful tool for anyone looking to protect their online accounts and personal information."
    )

    # Divider
    st.divider()

    # User input set as password
    password = st.text_input("Enter your password", type="password")

    # Button that triggers password analyzer logic
    if st.button("Analyze"):

        # Checks to see if password meets length
        if len(password) >= 12:

            # Pass results using zxcvbn
            result = zxcvbn.zxcvbn(password)

            # Password is given a score
            password_score = result['score']

            # Get feedback and crack times
            feedback = result.get('feedback', {})
            warning = feedback.get('warning', 'No warning')
            suggestions = feedback.get('suggestions', [])
            crack_time = result['crack_times_display']['online_no_throttling_10_per_second']

            # Format suggestions into a neat list
            suggestions_str = "".join([f"<li>{suggestion}</li>" for suggestion in suggestions])

            # Strength ratings and styling
            strength_ratings = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
            colors = ["#EF233C", "#EF233C", "orange", "#8B8000", "green"]
            background_colors = ["#f8d7da", "#f8d7da", "#fff3cd", "#FFFFC5", "#d4edda"]
            borders = ["#E85F5C", "#E85F5C", "orange", "#8B8000", "green"]

            # Display the password strength information
            st.markdown(f"""
                <div style="padding: 10px; border: 2px solid {borders[password_score]}; background-color: {background_colors[password_score]};">
                    <span style='color:{colors[password_score]};font-size: 20px;'>Score: {password_score}</span><br>
                    <span style='color:{colors[password_score]};'>Strength Rating: {strength_ratings[password_score]}</span><br>
                    <span style='color:{colors[password_score]}'>Warning: {warning}</span>
                    <ul style='color:{colors[password_score]};'>
                        {suggestions_str if suggestions else '<li>No suggestions</li>'}
                    </ul>
                    <span style='color:{colors[password_score]}'>Crack Time: {crack_time}</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Password should be at least 12 characters long.")
    elif password:
        st.info("Password must be at least 12 characters long to analyze.")

# Feedback Page
if selected == "Feedback":
    st.header("Rate us")

    # Sign-up form
    with st.form(key="form1"):
        firstname = st.text_input("First Name")
        lastname = st.text_input("Last Name")
        button = st.form_submit_button(label="Sign up")
        if button:
            st.success(f"Hello {firstname}, you have created an account")

    # Feedback form
    with st.form(key="feedback_form"):
        st.write("Please rate your satisfaction with Password Wizards for each of the following:")
        feedback_type = st.selectbox(
            "Overall Quality", 
            ["Dissatisfied", "Neither satisfied nor dissatisfied", "Somewhat satisfied", "Extremely satisfied"]
        )
        comments = st.text_area("Comments")
        button2 = st.form_submit_button(label="Submit")
        if button2:
            st.write(f"Thank you for your feedback: {comments.upper()}")

# About Page
if selected == "About":
    st.header("Purpose")
    st.info(
        "Password Analyzer is a web tool that helps users check the strength of their passwords in real time. "
        "It provides instant feedback along with tips for improving weak passwords and grades it from weak to strong "
        "based on a grading scale. The site features a resource hub with articles on best practices for creating strong passwords and information on common security policies, like two-factor authentication. "
        "Users can also input strong passwords and take quizzes to learn more about password safety. Overall, Password Wizards aims to help people improve their password security and protect their online accounts."
    )

