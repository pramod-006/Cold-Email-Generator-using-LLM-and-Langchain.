# 📧 Cold Email Generator using LLaMA-3, ChatGroq, LangChain & ChromaDB

A fully automated AI-powered cold email generator that scrapes job postings from career pages, extracts job details using **LLM-powered NLP**, and generates personalized cold emails with relevant portfolio links using **vector search** via **ChromaDB**.

---

## 🚀 Features

- 🔎 **Job Scraping & Parsing**  
  Extracts job descriptions, required skills, and role data from any career page URL.

- 🧠 **LLM-Powered Intelligence**  
  Uses **ChatGroq** with the **LLaMA 3.3-70B model** for job data extraction and dynamic email generation.

- 🔗 **Intelligent Portfolio Linking**  
  Matches extracted skills with internal projects using **ChromaDB** for relevant link embedding.

- 🧵 **LangChain Orchestration**  
  LangChain pipelines for prompt chaining, job extraction, and response formatting.

- 🌐 **Interactive UI with Streamlit**  
  Simple web interface for job URL input and cold email generation preview.

---

## 🧠 Tech Stack

| Category           | Tools / Libraries                                      |
|--------------------|--------------------------------------------------------|
| Large Language Model | `LLaMA 3.3 70B`, `ChatGroq`, `LangChain`            |
| Vector Database    | `ChromaDB` (for semantic portfolio search)             |
| Web UI             | `Streamlit`                                            |
| Web Scraping       | `LangChain WebBaseLoader`                              |
| Parsing & Prompting| `LangChain PromptTemplate`, `JsonOutputParser`        |
| Backend Logic      | `Python`, `UUID`, `Pandas`                             |
| Deployment Support | `.env` via `python-dotenv`                             |

---

## 📁 Folder Structure

cold-email-generator/

│
├── app/

│ └── resource/

│ └── my_portfolio.csv # Portfolio dataset with Techstack & Links

├── main.py # Streamlit entry point

├── chain.py # LangChain logic for job extraction & email generation

├── portfolio.py # ChromaDB vector store for portfolio matching

├── utils.py # Text cleaning utility

├── .env # Environment variables (GROQ_API_KEY)

├── requirements.txt # Python dependencies

└── README.md # Project documentation


---

## 🔧 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/cold-email-generator.git
   cd cold-email-generator
2. **Install Dependencies**
    pip install -r requirements.txt
3. **Add your API Key**   
    ROQ_API_KEY=your_chatgroq_api_key_here
4. Add Portfolio Data
      Add Portfolio Data
      Add your projects to app/resource/my_portfolio.csv with the following columns:

      Techstack: Keywords/skills (e.g., Python, NLP, LLM, etc.)

      Links: Corresponding portfolio/project links
---

🏗️ How It Works


🔗 Input a job/career page URL
The user provides a link to a job listing or career page.

🌐 Web Scraping with LangChain
WebBaseLoader scrapes and loads the HTML content from the page.

🧹 Text Cleaning & Preprocessing
The raw text is cleaned to remove HTML tags and unnecessary noise.

🧠 Job Data Extraction via LLM
The cleaned text is passed to LLaMA 3.3-70B via ChatGroq using a LangChain prompt to extract structured job information (role, skills, experience).

📚 Skill Matching with ChromaDB
The extracted skill keywords are searched semantically against a vector store of portfolio projects using ChromaDB.

✉️ Cold Email Generation
Another prompt combines the job details and matched projects to generate a personalized cold email.

🖥️ Interactive Output
The generated email is displayed in the Streamlit UI as a clean, copyable Markdown block.


