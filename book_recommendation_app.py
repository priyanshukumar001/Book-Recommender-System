import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

st.title("Book Recommendation App")

books_dict = pickle.load(open('pickle_files/books.pkl', 'rb'))
books_pivot = pd.DataFrame(books_dict)

selected_book_name = st.selectbox("Type or select a book from the dropdown", books_pivot.index)
recommender = pickle.load(open('pickle_files/recommender.pkl', 'rb'))
book_number = st.selectbox("Select Number of books", [2,3,4,5])

def recommend_book(selected_book_name):
    book_id = np.where(books_pivot.index == selected_book_name)[0][0]
    distances, index = recommender.kneighbors(books_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=book_number+1)
    suggestions = []
    for i in index:
        suggestions.append(books_pivot.index[i])
    return suggestions


if st.button("Show Recommendation"):
    st.write("The suggestions for **{}** are".format(selected_book_name))
    recommendations = recommend_book(selected_book_name)[0][1:]
    for i,name in enumerate(recommendations):
        st.write("{} - {}".format(i+1,name))
