# Agentic Workflow

A modular Python workflow for document processing using LLMs.  
This project can summarize documents, make decisions based on the summaries, and generate professional reports automatically.

---

## Features

- Modular design for easy maintenance and extension
- Summarization of text documents into concise bullet points
- Decision-making with justification and next steps
- Executive report generation for stakeholders
- Reads documents from a folder and saves results in organized batches
- Compatible with Ollama LLMs (currently using Mistral)

---

## Folder Structure

agentic_workflow/
│
├── agentic_workflow.py # Entry point
├── config/
│ └── settings.py # Project configuration
├── llm/
│ └── ollama_client.py # LLM initialization
├── workflow/
│ ├── summarize.py # Summarization logic
│ ├── decision.py # Decision-making logic
│ ├── report.py # Report generation logic
│ └── runner.py # Workflow orchestration
├── prompts/
│ └── templates.py # Prompt templates
├── utils/
│ └── file_io.py # File reading/writing utilities
└── results/ # Auto-created output folder


---

## Installation

1. Clone the repository:

```
git clone https://github.com/<your-username>/agentic-workflow.git
cd agentic-workflow
```
2. Create a virtual environment
```
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
3. Install dependencies:
```
pip install -r requirements.txt
```
## Usage
1. Place your text documents in the documents/ folder.
2. Run the workflow:

```
python main.py
```
3. Results (summary, decision, and report) will be saved in the results/ folder in a timestamped batch.
