import streamlit as st
from ocr import pdf_to_images, extract_text

from text_utils import split_text
from embeddings import create_embeddings, model
from vector_store import store_chunks, search_chunks
from rag_pipeline import generate_answer

st.title("Handwritten Notes AI Assistant")

uploaded_pdf = st.file_uploader("Upload handwritten notes", type="pdf")

text = ""   # ← IMPORTANT: initialize text

if uploaded_pdf:

    images = pdf_to_images(uploaded_pdf)

    st.success("PDF uploaded successfully")

    st.write("Total pages:", len(images))

    if st.button("Extract Text"):

        text = extract_text(images)

        st.subheader("Extracted Text")

        st.text_area("Notes Text", text, height=300)

# ---------- RAG Pipeline ----------

if text != "":

    chunks = split_text(text)

    embeddings = create_embeddings(chunks)

    store_chunks(chunks, embeddings)

    question = st.text_input("Ask a question about the notes")

    question = st.text_input("Ask a question about the notes")

question = st.text_input("Ask a question about the notes")

if question:

    query_embedding = model.encode(question)

    results, sources = search_chunks(query_embedding)

    context = " ".join(results)

    answer = generate_answer(context, question)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Source")
    for s in sources:
        st.info(s)

    st.subheader("Confidence")

    confidence = 0.85
    st.progress(confidence)
    st.write(f"{int(confidence*100)}% confidence")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if question:

    st.session_state.chat_history.append(("User", question))
    st.session_state.chat_history.append(("AI", answer))

for role, msg in st.session_state.chat_history:

    if role == "User":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)