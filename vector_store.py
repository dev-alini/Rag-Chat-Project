import faiss
import numpy as np

class FaissStore:
    def __init__(self, dim:int):
        self.dim = dim
        self.index = faiss.IndexFlatIP(dim)
        self.meta = []

    def add(self, vectors:np.ndarray, metas:list):
        faiss.normalize_L2(vectors)
        self.index.add(vectors)
        self.meta.extend(metas)

    def search(self, query_vec:np.ndarray, k=5):
        faiss.normalize_L2(query_vec)
        D, I = self.index.search(query_vec, k)
        results = []
        for scores, idxs in zip(D, I):
            hits = []
            for score, idx in zip(scores, idxs):
                if idx == -1:
                    continue
                hits.append({
                    "score": float(score),
                    "meta": self.meta[idx]
                })
            results.append(hits)
        return results
