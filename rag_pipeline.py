import ollama

def generate_answer(context, question):

    prompt = f"""
You are a study assistant.

Answer ONLY using the provided notes.

Context:
{context}

Question:
{question}

Return output in this format:

Answer:
<short answer>

Key Points:
- point 1
- point 2
- point 3

If the answer is not in the notes say:
"I don't have enough information."
"""

    response = ollama.chat(
        model="phi3",
        messages=[{"role":"user","content":prompt}]
    )

    return response["message"]["content"]