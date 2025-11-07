import sys
from llm.ollama_client import get_llm
from workflow.runner import run_workflow
from utils.file_io import get_documents, save_results

def main(folder_path="documents"):
    llm = get_llm()
    documents = get_documents(folder_path)
    if not documents:
        print("❌ No documents found.")
        return
    
    results = []
    for filename, text in documents:
        print(f"\n📄 Processing {filename}")
        summary, decision, report = run_workflow(llm, text)
        results.append({
            "filename": filename,
            "summary": summary,
            "decision": decision,
            "report": report
        })
    save_results(results)

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "documents"
    main(folder)
