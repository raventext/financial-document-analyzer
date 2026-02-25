# Financial Document Analyzer - Debug Assignment

## Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents.

## Getting Started

### Install Required Libraries
```sh
pip install -r requirements.txt
```

### Sample Document
The system analyzes financial documents like Tesla's Q2 2025 financial update.

**To add Tesla's financial document:**
1. Download the Tesla Q2 2025 update from: https://www.tesla.com/sites/default/files/downloads/TSLA-Q2-2025-Update.pdf
2. Save it as `data/sample.pdf` in the project directory
3. Or upload any financial PDF through the API endpoint

**Note:** Current `data/sample.pdf` is a placeholder - replace with actual Tesla financial document for proper testing.

# You're All Not Set!
🐛 **Debug Mode Activated!** The project has bugs waiting to be squashed - your mission is to fix them and bring it to life.

## Debugging Instructions

1. **Identify the Bug**: Carefully read the code in each file and understand the expected behavior. There is a bug in each line of code. So be careful.
2. **Fix the Bug**: Implement the necessary changes to fix the bug.
3. **Test the Fix**: Run the project and verify that the bug is resolved.
4. **Repeat**: Continue this process until all bugs are fixed.

## Expected Features
- Upload financial documents (PDF format)
- AI-powered financial analysis
- Investment recommendations
- Risk assessment
- Market insights

## OUTPUT
📊 Financial Document Analyzer (CrewAI + Gemini)

An AI-powered financial document analysis system built with FastAPI, CrewAI, and Google Gemini API.
The system processes uploaded PDF financial reports and generates structured investment insights using agent-based orchestration.

### 🚀 Project Overview

This project implements an AI-driven financial document analyzer that:

Accepts financial PDF uploads

Extracts document text

Uses AI agents to generate:

Investment insights

Risk analysis

Market observations

Exposes functionality through a FastAPI REST API

### 🐛 Debugging & Issues Resolved

During development, several major issues were identified and fixed.

### 1️⃣ Dependency Conflicts (Python 3.13 Issue)
Problem:

numpy, onnxruntime, and crewai dependencies failed to install.

GCC version errors.

Metadata build failures.

Root Cause:

Python 3.13 was incompatible with several dependencies.

Fix:

Downgraded to:

Python 3.11 (64-bit)

Created fresh virtual environment and reinstalled dependencies.

### 2️⃣ CrewAI API Changes
Problem:
ImportError: cannot import name 'Agent' from 'crewai.agents'
Root Cause:

CrewAI 0.130.0 changed import structure.

Fix:

Updated import:

from crewai import Agent
### 3️⃣ Tool Validation Errors (Pydantic v2)
Problem:
ValidationError: tools.0 Input should be a valid BaseTool
Root Cause:

CrewAI now requires tools to inherit from BaseTool instead of passing plain functions.

Fix:

Converted PDF reader into:

class FinancialDocumentTool(BaseTool):
### 4️⃣ OpenAI Quota Errors
Problem:
OpenAIException: You exceeded your current quota
Root Cause:

No OpenAI billing enabled.

Fix:

Migrated from OpenAI → Google Gemini API.

### 5️⃣ Gemini + LiteLLM Vertex Routing Issue
Problem:

CrewAI routed Gemini through Vertex AI and required Google Cloud credentials.

DefaultCredentialsError: Your default credentials were not found.
Root Cause:

LiteLLM version bundled with CrewAI defaulted Gemini models to Vertex provider.

Final Fix:

Bypassed LiteLLM routing and used official Gemini SDK directly inside a CrewAI tool.

This eliminated:

Vertex credential requirements

ADC setup

Provider conflicts

### 🏗 Final Architecture
Client → FastAPI → CrewAI Agent → PDF Tool → Gemini SDK → Response

CrewAI handles orchestration

Gemini handles actual LLM reasoning

FastAPI exposes REST endpoint

### 🛠 Setup Instructions
```
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/financial-document-analyzer.git
cd financial-document-analyzer
2️⃣ Install Python

Recommended version:

Python 3.11 (64-bit)
3️⃣ Create Virtual Environment
py -3.11 -m venv venv
venv\Scripts\activate   # Windows
4️⃣ Install Dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
5️⃣ Configure Gemini API Key

Create .env file in project root:

GEMINI_API_KEY=your_api_key_here

Get key from:

https://aistudio.google.com/app/apikey

6️⃣ Run Server
uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs
```
###  📡 API Documentation
```
GET /
Health Check

Response:

{
  "message": "Financial Document Analyzer API is running"
}
POST /analyze

Uploads a financial PDF and returns AI-generated analysis.

Request (multipart/form-data)
Field	Type	Required	Description
file	file	✅	PDF financial document
query	string	❌	Optional analysis instruction
Example Curl
curl -X 'POST' \
  'http://127.0.0.1:8000/analyze' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@TSLA-Q2-2025-Update.pdf;type=application/pdf' \
  -F 'query=Analyze this financial document for investment insights'
Example Response
{
  "status": "success",
  "query": "Analyze this financial document for investment insights",
  "analysis": "Detailed investment insights generated by Gemini...",
  "file_processed": "TSLA-Q2-2025-Update.pdf"
}
```
### 📁 Project Structure
financial-document-analyzer/
│
├── main.py
├── agents.py
├── task.py
├── tools.py
├── requirements.txt
├── README.md
├── .env
├── data/
└── outputs/
### 🔒 Security Notes

.env is excluded via .gitignore

No API keys are committed

Uploaded files are deleted after processing

### 🧠 Key Learnings

Dependency resolution with conflicting ML libraries

CrewAI tool validation under Pydantic v2

LiteLLM provider routing behavior

Difference between Gemini AI Studio vs Vertex AI

FastAPI file upload handling

Agent-based orchestration architecture

### 📌 Future Improvements

Structured JSON output

Async execution support

Better error handling

Persistent analysis storage

Frontend UI integration

### 👨‍💻 Tech Stack

Python 3.11

FastAPI

CrewAI

Google Gemini API

PyPDFLoader

Uvicorn
