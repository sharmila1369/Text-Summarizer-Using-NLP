# 🚀 Text-Summarizer-Using-NLP

## 📌 Project Overview

**Text-Summarizer-Using-NLP** is a Flask-based web application that takes long textual content as input and generates a concise and meaningful summary using Natural Language Processing (NLP) techniques.

The application uses **extractive text summarization**, where important sentences are identified from the original text and combined to create the final summary.

This project is useful for:

* Students
* Researchers
* Content writers
* Professionals
* Anyone who needs quick summaries of long documents

---

## ✨ Features

* User-friendly web interface
* Accepts long text as input
* Allows the user to select the number of sentences in the summary
* Generates an automatic extractive summary
* Uses NLP techniques to identify important sentences
* Fast and simple text processing
* Built using Python and Flask

---

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **NLTK**
* **NumPy**
* **scikit-learn**
* **NetworkX**
* **HTML**
* **CSS**
* **JavaScript**

### NLP Techniques Used

The summarization process uses:

* Sentence tokenization
* TF-IDF vectorization
* Sentence similarity
* PageRank-based sentence ranking
* Extractive summarization

---

## 📂 Project Structure

```text
Text-Summarizer-Using-NLP/
│
├── app.py
├── summary.py
├── requirements.txt
├── Procfile
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── js/
│
└── README.md
```

---

## 🔄 How It Works

The project follows these steps:

1. The user enters a long text into the web application.
2. The Flask application receives the input text.
3. The text is divided into individual sentences using NLTK.
4. TF-IDF is used to convert the sentences into numerical vectors.
5. A similarity matrix is created to identify relationships between sentences.
6. NetworkX PageRank is applied to rank the sentences based on their importance.
7. The top-ranked sentences are selected according to the number of sentences requested by the user.
8. The selected sentences are combined and displayed as the final summary.

---

## 🧠 Summarization Process

The main summarization logic is implemented in `summary.py`.

First, the input text is divided into sentences using NLTK sentence tokenization.

Then, **TF-IDF Vectorization** is used to represent the sentences numerically. Sentence-to-sentence similarity is calculated using the generated vectors.

A graph is then created using the similarity matrix, and **PageRank** is used to calculate the importance score of each sentence.

Finally, the highest-ranked sentences are selected and returned as the summary.

---

## 📸 Project Output

The application provides a simple interface where the user can enter text and specify the required number of sentences.

### Example Output

![Text Summarization Output](<img width="826" height="752" alt="output png" src="https://github.com/user-attachments/assets/89fafe60-34e2-4832-b4a3-74d6c521b327" />
)

The above output shows:

* Long text entered as input
* Number of sentences selected by the user
* Generated extractive summary

---

## 💻 Main Application

The `app.py` file handles the Flask web application.

It:

* Creates the Flask application
* Displays the main web page
* Receives text from the user
* Receives the requested number of summary sentences
* Calls the summarization function
* Returns the generated summary

---

## 📊 Example

### Input

Artificial Intelligence is becoming an important technology in many industries. It helps computers perform tasks that normally require human intelligence, such as understanding language, recognizing images, and making decisions. Natural Language Processing is a branch of Artificial Intelligence that focuses on communication between humans and computers using natural language. NLP is used in applications such as chatbots, machine translation, sentiment analysis, and text summarization.

### Output

The application extracts the most important sentences from the input and generates a shorter summary while retaining the main information.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sharmila1369/Text-Summarizer-Using-NLP.git
cd Text-Summarizer-Using-NLP
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

Then open the application in your browser:

```text
http://127.0.0.1:5000/
```

---

## 📦 Requirements

The project uses Python libraries including:

* Flask
* NLTK
* NumPy
* scikit-learn
* NetworkX

All required packages are listed in `requirements.txt`.

---

## 🎯 Project Objective

The main objective of this project is to reduce the time required to read and understand lengthy documents by automatically identifying and presenting the most important sentences.

---

## 🚀 Future Enhancements

Possible future improvements include:

* Adding abstractive summarization
* Supporting PDF and DOCX files
* Adding multi-language summarization
* Allowing users to download the generated summary
* Improving summary quality for different types of documents

---

## 👩‍💻 Author

**Sharmilambika Venna**

B.Tech – Computer Science
Artificial Intelligence & Data Science

---


