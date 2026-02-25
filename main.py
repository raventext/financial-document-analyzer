from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document as financial_task  # renamed to avoid conflict

app = FastAPI(title="Financial Document Analyzer")


# ---------------------------------------------------------
# Run Crew Function
# ---------------------------------------------------------

def run_crew(query: str, file_path: str = "data/sample.pdf"):
    """Run CrewAI financial analysis"""

    financial_crew = Crew(
        agents=[financial_analyst],
        tasks=[financial_task],
        process=Process.sequential,
    )

    result = financial_crew.kickoff({
        "query": query,
        "file_path": file_path
    })

    return result


# ---------------------------------------------------------
# Health Check Endpoint
# ---------------------------------------------------------

@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}


# ---------------------------------------------------------
# Analyze Endpoint
# ---------------------------------------------------------

@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):

    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)
        os.makedirs("outputs", exist_ok=True)

        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        if not query or query.strip() == "":
            query = "Analyze this financial document for investment insights"

        # Run Crew
        response = run_crew(query=query.strip(), file_path=file_path)

        # Save output file
        output_path = f"outputs/result_{file_id}.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(str(response))

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename,
            "output_saved_to": output_path
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing financial document: {str(e)}")

    finally:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass


# ---------------------------------------------------------
# Run Server
# ---------------------------------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)