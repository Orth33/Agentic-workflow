from langchain_core.prompts import PromptTemplate

summarize_prompt = PromptTemplate.from_template(
    "Summarize the following text in 3 concise bullet points:\n\n{document}\n\nBullets:"
)

decision_prompt = PromptTemplate.from_template(
    "Given this summary:\n{summary}\n\nDecide whether any action is required (Yes/No). "
    "Provide a short justification and two next steps."
)

report_prompt = PromptTemplate.from_template(
    "Combine the following information into a concise professional report for a stakeholder. "
    "Limit to 150 words.\n\nSummary:\n{summary}\n\nDecision & Steps:\n{decision}"
)
