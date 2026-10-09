
def basic_prompt(topic):
    return f"""
Explain {topic} in simple words.

Include:
1. Definition
2. Key points
3. Example
4. Advantages
5. Real-world application
"""


def role_prompt(topic):
    return f"""
You are an expert teacher.

Explain {topic} to a beginner.
Use simple language and practical examples.
Avoid unnecessary technical terms.
"""


def few_shot_prompt(text):
    return f"""
Classify the following text as Positive, Negative, or Neutral.

Examples:
"I love this product." → Positive
"This product is terrible." → Negative
"The product is okay." → Neutral

Now classify:
"{text}"

Return only the sentiment.
"""


def code_prompt(language, problem):
    return f"""
You are an experienced {language} programmer.

Solve the following programming problem:

{problem}

Provide:
1. Approach
2. {language} code
3. Explanation
4. Example input
5. Example output
"""


def exam_prompt(topic, marks):
    return f"""
You are an expert academic tutor.

Explain "{topic}" as a {marks}-mark examination answer.

Requirements:
- Start with a definition
- Use clear headings
- Include important points
- Give examples where appropriate
- End with a conclusion
- Use simple and easy-to-understand language
"""


def summarize_prompt(text):
    return f"""
Summarize the following text.

Requirements:
- Identify the main points
- Remove unnecessary information
- Use simple language
- Present the result as bullet points

Text:
{text}
"""