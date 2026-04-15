
def chunk_text(text: str, size: int = 200)   # <-- missing colon
    return text.split()


def retrieve(query: str, chunks: list, top_k: int = 3) -> list:
    return chunks[:top_k]


def generate(query: str, context: list) -> str:
    return f"Answer: {context}"


def run_pipeline(text: str, query: str) -> str:
    chunks = chunk_text(text)
    relevant = retrieve(query, chunks)
    return generate(query, relevant)


def embed(chunks: list) -> list:
    return [[1.0] for _ in chunks]