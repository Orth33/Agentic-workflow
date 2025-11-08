import sys
from llm.ollama_client import get_llm
from workflow.summarize import summarize
from workflow.decision import make_decision
from workflow.report import generate_report
from utils.file_io import get_documents, save_results
from config.settings import MODEL_NAME, SUMMARY_MODEL_NAME, DECISION_MODEL_NAME


def main(folder_path="documents"):
    summary_llm = get_llm(SUMMARY_MODEL_NAME)
    decision_llm = get_llm(DECISION_MODEL_NAME)
    other_llm = get_llm(MODEL_NAME)

    documents = get_documents(folder_path)
    if not documents:
        print("❌ No documents found.")
        return
    
    results = []
    for filename, text in documents:
        print(f"\n📄 Processing {filename}")
        # Generate summary once using summary_llm
        summary = summarize(summary_llm, text)
        if not summary:
            print(f"❌ Failed to generate summary for {filename}")
            continue
        
        # Use the summary for decision-making with other_llm
        decision = make_decision(decision_llm, summary)
        if not decision:
            print(f"❌ Failed to generate decision for {filename}")
            continue
        
        # Use the summary and decision for report generation with other_llm
        report = generate_report(other_llm, summary, decision)
        if not report:
            print(f"❌ Failed to generate report for {filename}")
            continue
        
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