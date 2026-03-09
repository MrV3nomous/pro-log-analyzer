def read_in_chunks(file, chunk_size=10000):

    chunk = []

    for line in file:

        chunk.append(line)

        if len(chunk) >= chunk_size:
            yield chunk
            chunk = []

    if chunk:
        yield chunk
