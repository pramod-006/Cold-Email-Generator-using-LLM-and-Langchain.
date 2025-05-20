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
│
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

2. Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt

3. Add your API Key
Create a .env file in the root directory:

env
Copy
Edit
GROQ_API_KEY=your_chatgroq_api_key_here

4. Add Portfolio Data
Add your projects to app/resource/my_portfolio.csv with columns:

Techstack: Keywords/skills (e.g., Python, NLP, LLM, etc.)

Links: Corresponding portfolio/project links

🏗️ How It Works
Input a job/career page URL.

WebBaseLoader scrapes the HTML content.

The cleaned text is sent to an LLM (LLaMA 3.3-70B via ChatGroq).

LangChain prompts extract job roles, experience, and skills in structured JSON.

Skills are queried against ChromaDB to fetch relevant project links.

A final cold email is generated using another LangChain prompt.

The email appears in the UI as a copy-ready markdown block.

