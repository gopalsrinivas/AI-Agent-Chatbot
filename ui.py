import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")

API_URL = "http://127.0.0.1:8000/chat"
MODEL_NAMES = ["llama3-70b-8192", "mixtral-8x7b-32768"]

st.title("LangGraph Chatbot Agent")
st.write("Interact with the LangGraph-based agent using this interface.")

given_system_prompt = st.text_area(
    "Define you AI Agent:", height=10, placeholder="Type your system prompt here..."
)
selected_model = st.selectbox("Select Model:", MODEL_NAMES)
user_input = st.text_area(
    "Enter your message(s):", height=150, placeholder="Type your message here..."
)

if st.button("Submit"):
    if user_input.strip():
        try:
            payload = {
                "messages": [user_input],
                "model_name": selected_model,
                "system_prompt": given_system_prompt,
            }
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                response_data = response.json()

                if "error" in response_data:
                    st.error(response_data["error"])
                else:
                    ai_responses = [
                        message.get("content", "")
                        for message in response_data.get("messages", [])
                        if message.get("type") == "ai"
                    ]
                    if ai_responses:
                        st.subheader("Agent Response:")
                        st.markdown(f"**Final Response:** {ai_responses[-1]}")
                    else:
                        st.warning("No AI response found in the agent output.")
            else:
                st.error(
                    f"Request failed with status code {response.status_code}: {response.text}"
                )
        except requests.exceptions.RequestException as req_err:
            st.error(f"Request error: {str(req_err)}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
    else:
        st.warning("Please enter a message before clicking 'Send Query'.")
