def chunk(text: str, size: int, overlap: int) -> list[str]:
    chunk_result = []
    i = 0
    while i < len(text):
        chunk_result.append(text[i:i+size])
        i += size - overlap
    return chunk_result