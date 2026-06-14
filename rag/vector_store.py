import faiss
import numpy as np
import pickle
import os

INDEX_FILE = "data/report_index.faiss"
TEXT_FILE = "data/report_chunks.pkl"


def save_chunks(chunks, embeddings):  

    dimension = len(embeddings[0])

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        np.array(embeddings).astype(
            "float32"
        )
    )

    faiss.write_index(
        index,
        INDEX_FILE
    )

    with open(
        TEXT_FILE,
        "wb"
    ) as f:

        pickle.dump(
            chunks,
            f
        )


def load_index():

    if not os.path.exists(
        INDEX_FILE
    ):
        return None, []

    index = faiss.read_index(
        INDEX_FILE
    )

    with open(
        TEXT_FILE,
        "rb"
    ) as f:

        chunks = pickle.load(f)

    return index, chunks