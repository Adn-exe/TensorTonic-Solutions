import numpy as np

def cosine_similarity(a, b):
    a = np.asarray(a, dtype = 'float')
    b = np.asarray(b, dtype = 'float')

    ab_dot = np.dot(a, b)
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)

    if a_norm == 0 or b_norm == 0:
        return 0

    cos_sim = ab_dot / (a_norm * b_norm)
    return cos_sim
