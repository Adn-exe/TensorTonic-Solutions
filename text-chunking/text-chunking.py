def text_chunking(tokens, chunk_size, overlap):
    step = chunk_size - overlap
    ch_text = []

    for i in range(0, len(tokens), step):
        chunk = tokens[i : chunk_size + i]
        ch_text.append(chunk)

        if chunk_size + i >= len(tokens):
            break
    
    return ch_text