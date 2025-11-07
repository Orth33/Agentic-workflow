from workflow.summarize import summarize
from workflow.decision import make_decision
from workflow.report import generate_report

def run_workflow(llm, document_text):
    summary = summarize(llm, document_text)
    if not summary:
        return None, None, None

    decision = make_decision(llm, summary)
    if not decision:
        return summary, None, None

    report = generate_report(llm, summary, decision)
    return summary, decision, report
