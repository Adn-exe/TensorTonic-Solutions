def remove_stopwords(tokens, stopwords):
    stopwords = set(stopwords)
    rm_stopwords = [word for word in tokens if word not in stopwords]

    return rm_stopwords