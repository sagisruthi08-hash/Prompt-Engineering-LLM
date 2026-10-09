import streamlit as st
from llm import generate_response

st.set_page_config(
    page_title="Prompt Engineering Playground",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Prompt Engineering Playground")
st.write("Experiment with Zero-Shot, One-Shot and Two-Shot Prompting")

# Sidebar
st.sidebar.header("⚙️ Settings")

prompt_type = st.sidebar.selectbox(
    "Choose Prompting Technique",
    [
        "Zero-Shot",
        "One-Shot",
        "Two-Shot"
    ]
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.5,
    value=0.7,
    step=0.1
)

# User input
st.subheader("📝 Enter Your Task")

user_input = st.text_area(
    "Enter your question or task:",
    placeholder="Example: Classify this sentence as Positive or Negative: I love this product."
)

# Create prompt based on technique
def create_prompt(prompt_type, user_input):

    if prompt_type == "Zero-Shot":

        prompt = f"""
You are an AI assistant.

Perform the following task without using any examples.

Task:
{user_input}

Give a clear and accurate answer.
"""

    elif prompt_type == "One-Shot":

        prompt = f"""
You are an AI assistant.

Here is one example:

Example:
Input: I love this product.
Output: Positive

Now perform the same task for:

Input: {user_input}

Give only the appropriate answer with a short explanation.
"""

    else:  # Two-Shot

        prompt = f"""
You are an AI assistant.

Here are two examples:

Example 1:
Input: I love this product.
Output: Positive

Example 2:
Input: This product is terrible.
Output: Negative

Now perform the same task for:

Input: {user_input}

Give only the appropriate answer with a short explanation.
"""

    return prompt


# Generate response
if st.button("🚀 Generate Response"):

    if user_input.strip() == "":
        st.warning("Please enter a task first.")

    else:
        prompt = create_prompt(prompt_type, user_input)

        # Display generated prompt
        st.subheader("🔍 Generated Prompt")

        with st.expander("View Prompt"):
            st.code(prompt)

        # Generate LLM response
        with st.spinner("Generating response..."):

            response = generate_response(
                prompt,
                temperature=temperature
            )

        # Display response
        st.subheader("🤖 LLM Response")

        st.write(response)

        # Display settings
        st.info(
            f"Prompting Technique: {prompt_type} | "
            f"Temperature: {temperature}"
        )