from prompts.templates import summarize_prompt

def summarize(llm, document):
    try:
        print("📝 Running summarization...")
        return llm.invoke(summarize_prompt.format_prompt(document=document).to_string())
    except Exception as e:
        print(f"❌ Summarization failed: {e}")
        return None
