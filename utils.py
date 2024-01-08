import pickle
import numpy as np
import pandas as pd

books_dict = pickle.load(open('pickle_files/books.pkl', 'rb'))
recommender = pickle.load(open('pickle_files/recommender.pkl', 'rb'))
books_pivot = pd.DataFrame(books_dict)

def recommend(title: str, count: int):
    book_id = np.where(books_pivot.index == title)[0][0]
    distances, index = recommender.kneighbors(books_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=count+1)
    suggestions = []

    for book_id in index:
        suggestions.append(books_pivot.index[book_id])
    return suggestions
