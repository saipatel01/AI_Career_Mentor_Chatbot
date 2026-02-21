# Production-Ready AI Career Chatbot

## 🚀 Project Overview
This project implements a production-ready domain-specific chatbot powered by Google Gemini 2.5 Flash API.

The chatbot is designed to provide structured career guidance related to Generative AI internships and job preparation.

## 🏗 Architecture

User  
→ Streamlit UI  
→ Chat Controller  
→ Prompt Engineering Module  
→ Gemini API Service  
→ Response Processing  
→ UI Rendering  

## 🧠 Features

- Domain responses 
- Multi-turn contextual conversation
- Secure API key management via environment variables
- Modular clean architecture
- Logging and error handling
- AWS EC2 deployment

## 🛠 Tech Stack

- Python
- Streamlit
- Google Gemini API (gemini-2.5-flash)
- AWS EC2 (Ubuntu)
- Virtual Environment (venv)

## 🔐 Environment Setup

Create `.env` file:


gemini_class ='AIzaSyAFj4DTmwemTBigIkqn2A43b6w6fGboVng'


Install dependencies:


pip install -r requirements.txt


Run locally:


streamlit run app.py


## ☁️ Deployment Steps (AWS EC2)

1. Launch Ubuntu EC2 instance
2. Open ports 22 and 8501
3. Install Python and venv
4. Upload project
5. Install dependencies
6. Run:


nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &


## 🌍 Live Deployment Link

http://13.126.93.128:8501
