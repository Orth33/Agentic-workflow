from prompts.templates import decision_prompt

def make_decision(llm, summary):
    try:
        print("⚖️ Running decision-making...")
        return llm.invoke(decision_prompt.format_prompt(summary=summary).to_string())
    except Exception as e:
        print(f"❌ Decision-making failed: {e}")
        return None
