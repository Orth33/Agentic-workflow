from prompts.templates import report_prompt

def generate_report(llm, summary, decision):
    try:
        print("🧾 Generating report...")
        return llm.invoke(report_prompt.format_prompt(summary=summary, decision=decision).to_string())
    except Exception as e:
        print(f"❌ Report generation failed: {e}")
        return None
