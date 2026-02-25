## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()
from crewai.tools import BaseTool
from langchain_community.document_loaders import PyPDFLoader


#from crewai_tools.tools.serper_dev_tool import SerperDevTool
from langchain_community.document_loaders import PyPDFLoader


# ---------------------------------------------------------
# Search Tool
# ---------------------------------------------------------

#search_tool = SerperDevTool()


# ---------------------------------------------------------
# Custom PDF Reader Tool
# ---------------------------------------------------------

class FinancialDocumentTool(BaseTool):
    name: str = "financial_document_reader"
    description: str = "Reads and returns the content of a financial PDF document."

    def _run(self, path: str = "data/sample.pdf") -> str:
        if not os.path.exists(path):
            return f"Error: File not found at {path}"

        docs = PyPDFLoader(path).load()

        full_report = ""

        for data in docs:
            content = data.page_content
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"

        return full_report


# ---------------------------------------------------------
# Investment Analysis Tool
# ---------------------------------------------------------

class InvestmentTool:

    @staticmethod
    async def analyze_investment_tool(financial_document_data):

        processed_data = financial_document_data

        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1

        return "Investment analysis functionality to be implemented"


# ---------------------------------------------------------
# Risk Assessment Tool
# ---------------------------------------------------------

class RiskTool:

    @staticmethod
    async def create_risk_assessment_tool(financial_document_data):
        return "Risk assessment functionality to be implemented"