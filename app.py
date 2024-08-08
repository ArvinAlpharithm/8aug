# streamlit_app.py

import streamlit as st
from groq import Groq

# Initialize the Groq LLM with your API key
llm = Groq(api_key="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")

# Streamlit app title
st.title("Ask Elon Musk Anything")

# User input for the question
question = st.text_input("Enter your question:")

# Button to submit the question
if st.button("Get Answer"):
    if question:
        # Construct AI Functionality
        response = llm.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are Elon Musk."},
                {"role": "user", "content": question}
            ]
        )

        # Extract the content of the response
        response_content = response.choices[0].message.content

        # Show the response in Streamlit
        st.write("**Elon Musk's Response:**")
        st.write(response_content)
    else:
        st.write("Please enter a question.")
