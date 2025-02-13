# def split_text(text, chunk_size=3000):
#     chunks = []
#     while len(text) > chunk_size:
#         split_point = text.rfind('.', 0, chunk_size) or chunk_size
#         chunks.append(text[:split_point+1])
#         text = text[split_point+1:]
#     if text:
#         chunks.append(text)
#     return chunks

def split_text(text, chunk_size=3000):
    chunks = []
    while len(text) > chunk_size:
        split_point = text.rfind('.', 0, chunk_size + 1)
        if split_point == -1:
            split_point = chunk_size
        
        chunks.append(text[:split_point + 1] if split_point != chunk_size else text[:chunk_size])
        text = text[split_point + 1:] if split_point != chunk_size else text[chunk_size:]
    
    if text:
        chunks.append(text.strip())
    
    return chunks