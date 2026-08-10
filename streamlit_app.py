import streamlit as st
import requests


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Multi-Agent Code Reviewer",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------

st.title("🤖 AI Multi-Agent Code Reviewer")

st.write(
    "Paste your Python code below and click **Review Code**."
)


# -----------------------------
# Code Input
# -----------------------------

code = st.text_area(
    "Enter Python Code",
    height=300,
    placeholder="Paste your Python code here..."
)


# -----------------------------
# Review Button
# -----------------------------

if st.button("Review Code"):

    # Check whether code was entered
    if code.strip() == "":
        st.warning("Please enter some Python code.")

    else:

        # Show loading message
        with st.spinner("Reviewing your code..."):

            try:

                # Send code to FastAPI
                response = requests.post(
                    "http://127.0.0.1:8000/review",
                    json={
                        "code": code
                    },
                    timeout=120
                )

                # Check API response
                if response.status_code == 200:

                    result = response.json()

                    st.success(
                        "✅ Analysis completed successfully!"
                    )

                    # -----------------------------
                    # Display Results
                    # -----------------------------

                    left, right = st.columns(2)

                    # Review
                    with left:

                        st.subheader("📋 Review Report")

                        st.write(
                            result["review"]
                        )

                    # Optimized Code + Explanation
                    with right:

                        st.subheader("🚀 Optimized Code")

                        st.code(
                            result["optimized_code"],
                            language="python"
                        )

                        st.subheader("📖 Explanation")

                        st.write(
                            result["explanation"]
                        )

                else:

                    st.error(
                        f"API request failed: "
                        f"{response.status_code}"
                    )

                    st.write(
                        response.text
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Could not connect to the FastAPI server."
                )

                st.info(
                    "Make sure FastAPI is running with:\n\n"
                    "`python -m uvicorn api.review:app --reload`"
                )

            except requests.exceptions.Timeout:

                st.error(
                    "⏱️ The request took too long. "
                    "Please try again."
                )

            except requests.exceptions.RequestException as e:

                st.error(
                    f"❌ Request error: {e}"
                )