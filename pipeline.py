def chunk_text(text: str, size: int = 200) -> list:
       words = text.split()
       return [" ".join(words[i : i + size]) for i in range(0, len(words), size)]

def embed(chunks: list) -> list:
    return [[float(ord(c)) for c in chunk[:8]] for chunk in chunks]

def retrieve(query: str, chunks: list, top_k: int = 3) -> list:
    return chunks[:top_k]

def generate(query: str, context: list) -> str:
    return f"[Answer to '{query}'] Context: {' '.join(context)[:100]}"

def run_pipeline(text: str, query: str) -> str:
    chunks = chunk_text(text)
    embed(chunks)
    relevant = retrieve(query, chunks)
    return generate(query, relevant)