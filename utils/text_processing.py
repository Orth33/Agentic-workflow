from typing import List


def split_into_chunks(text: str, min_tokens: int = 1000, max_tokens: int = 2000, overlap: int = 200) -> List[str]:
    if not text:
        return []

    words = text.split()
    n = len(words)
    if n <= max_tokens:
        return [" ".join(words)]
    chunks: List[str] = []
    start = 0
    while start < n:
        end = min(start + max_tokens, n)
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        if end == n:
            break
        start = max(end - overlap, start + 1)
    return chunks


def summarize_chunks(llm, chunks: List[str], prompt_template) -> List[str]:
    summaries: List[str] = []
    for i, ch in enumerate(chunks, start=1):
        try:
            print(f"  ➤ Summarizing chunk {i}/{len(chunks)}...")
            prompt = prompt_template.format_prompt(document=ch).to_string()
            res = llm.invoke(prompt)
            if res:
                summaries.append(res)
        except Exception as e:
            print(f"  ❌ Chunk {i} summarization failed: {e}")
            continue
    return summaries
