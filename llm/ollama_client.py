from langchain_ollama import OllamaLLM

def get_llm(MODEL_TYPE):
    try:
        llm = OllamaLLM(model=MODEL_TYPE)
        print(f"✅ Ollama model '{MODEL_TYPE}' initialized.")
        return llm
    except Exception as e:
        print(f"❌ Failed to initialize Ollama model: {e}")
        raise
