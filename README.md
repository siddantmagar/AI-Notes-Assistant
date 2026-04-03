# AI Handwritten Notes Assistant

An AI-powered system that extracts text from handwritten/scanned PDFs and allows users to ask questions based on the content using a local LLM.

---

## 📌 Overview

This project solves the problem of accessing information from handwritten or unstructured documents by combining OCR, vector search, and a local language model.

Users can upload scanned notes and interact with them through natural language queries.

---

## ⚙️ Technologies Used

- **Python**
- **Streamlit** – UI for interaction
- **EasyOCR** – Extract text from handwritten/scanned images
- **PyMuPDF (fitz)** – Convert PDF pages to images
- **Sentence Transformers** – Generate embeddings
- **ChromaDB** – Vector database for semantic search
- **Ollama (Phi-3)** – Local LLM for answering questions
- **NumPy / OpenCV** – Image preprocessing

---

## 🚀 Features

- Upload scanned handwritten PDFs  
- Extract text using OCR  
- Convert text into semantic embeddings  
- Store embeddings in a vector database  
- Ask questions about the notes  
- Get context-aware answers using a local AI model  

---

## 🧠 How It Works

1. **PDF Upload**
   - User uploads a scanned document

2. **Text Extraction**
   - PDF → Images using PyMuPDF  
   - Images → Text using EasyOCR  

3. **Text Processing**
   - Extracted text is split into smaller chunks  

4. **Embedding Generation**
   - Each chunk is converted into vector embeddings  

5. **Vector Storage**
   - Embeddings stored in ChromaDB  

6. **Query Handling**
   - User asks a question  
   - System finds most relevant chunks  

7. **Answer Generation**
   - Relevant context sent to local LLM (Phi-3 via Ollama)  
   - Model generates answer strictly based on context  

---

## 🖥️ Installation & Setup

### 1. Clone Repository

---

### 2. Create Virtual Environment

---

### 3. Install Dependencies

---

### 4. Install Ollama

Download from: https://ollama.com/download  

---

### 5. Pull Model

---

### 6. Run Ollama

---

### 7. Run Application

---

## ⚠️ Notes

- Ollama must be running before starting the app  
- First run may download OCR and embedding models  
- Works fully offline after setup  

---

## 📌 Future Improvements

- Highlight source text in PDF  
- Improve OCR accuracy for messy handwriting  
- Add chat history memory  
- Optimize performance for faster responses  

---

## 👨‍💻 Author

Siddant Magar
