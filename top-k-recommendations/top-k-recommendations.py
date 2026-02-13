def top_k_recommendations(scores, rated_indices, k):
    rated_indices = set(rated_indices)

    candidate_scores_idx = [i for i in range(len(scores)) if i not in rated_indices]
    candidate_scores_idx.sort(key= lambda i: scores[i], reverse = True)

    return candidate_scores_idx[:k]