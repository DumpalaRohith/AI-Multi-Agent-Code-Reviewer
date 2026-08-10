import streamlit as st
import requests


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Multi-Agent Code Reviewer",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# FastAPI Backend URL
# --------------------------------------------------

API_URL = "https://multi-agent-code-reviewer-api.onrender.com/review"


# --------------------------------------------------
# Application Title
# --------------------------------------------------

st.title("🤖 AI Multi-Agent Code Reviewer")

st.write(
    "Paste your Python code below and click **Review Code**."
)


# --------------------------------------------------
# Code Input
# --------------------------------------------------

code = st.text_area(
    "Enter Python Code",
    height=350,
    placeholder="Paste your Python code here..."
)


# --------------------------------------------------
# Review Button
# --------------------------------------------------

if st.button("🔍 Review Code", use_container_width=True):

    # Check if code is empty
    if not code.strip():

        st.warning("⚠️ Please enter some Python code.")

    else:

        # Show loading message
        with st.spinner("🤖 AI agents are reviewing your code..."):

            try:

                # --------------------------------------------------
                # Send request to FastAPI
                # --------------------------------------------------

                response = requests.post(
                    API_URL,
                    json={
                        "code": code
                    },
                    timeout=180
                )


                # --------------------------------------------------
                # Successful Response
                # --------------------------------------------------

                if response.status_code == 200:

                    result = response.json()

                    st.success(
                        "✅ Code review completed successfully!"
                    )


                    # --------------------------------------------------
                    # Display Results
                    # --------------------------------------------------

                    left, right = st.columns(2)


                    # --------------------------------------------------
                    # Review Report
                    # --------------------------------------------------

                    with left:

                        st.subheader("📋 Review Report")

                        st.markdown(
                            result.get(
                                "review",
                                "No review available."
                            )
                        )


                    # --------------------------------------------------
                    # Optimized Code
                    # --------------------------------------------------

                    with right:

                        st.subheader("🚀 Optimized Code")

                        st.code(
                            result.get(
                                "optimized_code",
                                "# No optimized code available."
                            ),
                            language="python"
                        )


                    # --------------------------------------------------
                    # Explanation
                    # --------------------------------------------------

                    st.subheader("📖 Explanation")

                    st.markdown(
                        result.get(
                            "explanation",
                            "No explanation available."
                        )
                    )


                # --------------------------------------------------
                # API Error
                # --------------------------------------------------

                else:

                    st.error(
                        f"❌ API request failed "
                        f"(HTTP {response.status_code})"
                    )

                    st.code(
                        response.text
                    )


            # --------------------------------------------------
            # FastAPI Connection Error
            # --------------------------------------------------

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Could not connect to the FastAPI backend."
                )

                st.info(
                    "The backend may be starting up. "
                    "Please wait a few seconds and try again."
                )


            # --------------------------------------------------
            # Timeout Error
            # --------------------------------------------------

            except requests.exceptions.Timeout:

                st.error(
                    "⏱️ The request timed out."
                )

                st.info(
                    "The AI agents may still be processing the code. "
                    "Please try again."
                )


            # --------------------------------------------------
            # Other Request Errors
            # --------------------------------------------------

            except requests.exceptions.RequestException as e:

                st.error(
                    f"❌ Request error: {e}"
                )


            # --------------------------------------------------
            # Unexpected Errors
            # --------------------------------------------------

            except Exception as e:

                st.error(
                    f"❌ Unexpected error: {e}"
                )