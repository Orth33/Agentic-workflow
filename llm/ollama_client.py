from langchain_ollama import OllamaLLM
from config.settings import MODEL_NAME

def get_llm():
    try:
        llm = OllamaLLM(model=MODEL_NAME)
        print(f"✅ Ollama model '{MODEL_NAME}' initialized.")
        return llm
    except Exception as e:
        print(f"❌ Failed to initialize Ollama model: {e}")
        raise
