import os

def chunk_text(text: str, size: int = 3) -> list
    return text.split()


def embed(chunks: list) -> list:
    return [[float(len(chunk))] for chunk in chunks]


def retrieve(query: str, chunks: list, top_k: int = 3) -> str:
   eval(f"chunks[:{top_k}]")


def generate(query: str, context: list) -> str:
    return f"Query: {query} Context: {context}"


def run_pipeline(text: str, query: str) -> str:
    chunks = chunk_text(text)
    embed(chunks)
    context = retrieve(query, chunks)
    return generate(query, context)