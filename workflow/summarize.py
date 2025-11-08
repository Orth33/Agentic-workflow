from prompts.templates import summarize_prompt
from utils.text_processing import split_into_chunks, summarize_chunks


def summarize(llm, document, min_tokens: int = 1000, max_tokens: int = 2000):
    try:
        print("📝 Running chunked summarization...")
        chunks = split_into_chunks(document, min_tokens=min_tokens, max_tokens=max_tokens)
        if not chunks:
            print("❌ No content to summarize.")
            return None

        # If the whole document fits in one chunk, do a single summarization.
        if len(chunks) == 1:
            try:
                return llm.invoke(summarize_prompt.format_prompt(document=document).to_string())
            except Exception as e:
                print(f"❌ Summarization failed: {e}")
                return None

        # Summarize chunks individually
        chunk_summaries = summarize_chunks(llm, chunks, summarize_prompt)
        if not chunk_summaries:
            print("❌ Failed to summarize any chunks.")
            return None

        # Combine chunk summaries and re-summarize into a final concise summary
        combined = "\n\n".join(chunk_summaries)
        print("🔁 Combining chunk summaries and re-summarizing...")
        final_summary = llm.invoke(summarize_prompt.format_prompt(document=combined).to_string())
        return final_summary
    except Exception as e:
        print(f"❌ Summarization failed: {e}")
        return None
