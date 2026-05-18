# ai-customer-complaint-analyzer

## Project Overview
This application accepts customer complaint text and returns structured JSON with:
* problem
* root_cause
* recommended_action

## Example Input and Output

**Input:**
"My product arrived completely smashed and the box was torn open."

**Output:**
```json
{
  "problem": "Product arrived damaged",
  "root_cause": "Packaging issue",
  "recommended_action": "Send replacement and improve packaging"
}
```

## Features
- Extracts structured data from unstructured customer complaints.
- Uses LLM APIs to intelligently parse and categorize problems.
- Ready to be integrated into automated customer support workflows.

## Tech Stack
- Python
- OpenAI API
- FastAPI (planned)
- Pydantic

## Folder Structure
```text
ai-customer-complaint-analyzer/
├── README.md
├── TRACKER.md
├── .gitignore
├── requirements.txt
├── app.py
├── prompts/
│   └── complaint_extraction_prompt.txt
├── data/
│   └── sample_complaints.txt
├── outputs/
│   └── .gitkeep
└── docs/
    └── architecture.md
```

## 60-Day Roadmap Summary
### Month 1
* Week 1: Prompt engineering and environment setup
* Week 2: First LLM API project
* Week 3: Web UI with context injection
* Week 4: Basic RAG prototype

### Month 2
* Week 5: Production-quality RAG web app
* Week 6: Agentic workflow project
* Week 7: Testing and documentation
* Week 8: Resume, LinkedIn, and applications

## Setup Instructions
1. Clone the repository.
2. Create a Python virtual environment: `python -m venv venv`
3. Activate the virtual environment.
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file and add your OpenAI API Key: `OPENAI_API_KEY=your_key_here`

## How to Run
Run the main application script:
```bash
python app.py
```

## Future Improvements
- Add FastAPI endpoints for web integration.
- Build a user-friendly frontend to interact with the analyzer.
- Implement RAG (Retrieval-Augmented Generation) for historical complaint matching.

## Author
Kris
Transitioning from BPO to AI Application Developer
