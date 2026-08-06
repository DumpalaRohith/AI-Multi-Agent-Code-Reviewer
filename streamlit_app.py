import streamlit as st
from workflow import workflow

st.set_page_config(
    page_title="AI Multi-Agent Code Reviewer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Multi-Agent Code Reviewer")

st.write("Paste your Python code below and click **Review Code**.")

code = st.text_area(
    "Enter Python Code",
    height=300,
    placeholder="Paste your Python code here..."
)

if st.button("Review Code"):

    if code.strip() == "":
        st.warning("Please enter some Python code.")

    else:

        with st.spinner("🤖 Reviewing your code..."):

            result = workflow.invoke(
                {
                    "code": code,
                    "review": "",
                    "optimized_code": "",
                    "explanation": ""
                }
            )

        st.success("✅ Analysis completed successfully!")

        left, right = st.columns(2)

        with left:

            st.subheader("📋 Review Report")
            st.write(result["review"])

        with right:

            st.subheader("🚀 Optimized Code")
            st.code(
                result["optimized_code"],
                language="python"
            )

        st.subheader("📖 Explanation")
        st.write(result["explanation"])