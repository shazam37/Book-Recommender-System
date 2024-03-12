import pickle
import streamlit as st
import numpy as np
from sklearn.neighbors import NearestNeighbors

st.header("Books Recommender System")

model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

def fetch_poster(suggestion):
    books_name = []
    ids_index = []
    poster_url = []
    authors = []

    for book_id in suggestion:
        books_name.append(book_pivot.index[book_id])

    for i in books_name[0]:
        ids = np.where(final_rating['title'] == i)[0][0]
        ids_index.append(ids)
    
    for idx in ids_index:
        url = final_rating.iloc[idx]['img_url']
        poster_url.append(url)

    for idx in ids_index:
        author = final_rating.iloc[idx]['Author']
        authors.append(author)

    return poster_url, authors
    

def recommend_books(book_name):
    book_list = []

    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)

    poster_url, authors = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)
    
    return book_list, poster_url, authors

selected_books = st.selectbox(
    "Type or select the name of book",
    books_name
)

if st.button('Show recommendation'):
    recommendation_books, poster_url, authors = recommend_books(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1])
        st.text(f'Author: {authors[1]}')

    with col1:
        st.text(recommendation_books[2])
        st.image(poster_url[2])
        st.text(f'Author: {authors[2]}')

    with col1:
        st.text(recommendation_books[3])
        st.image(poster_url[3])
        st.text(f'Author: {authors[3]}')

    with col1:
        st.text(recommendation_books[4])
        st.image(poster_url[4])
        st.text(f'Author: {authors[4]}')

    with col1:
        st.text(recommendation_books[5])
        st.image(poster_url[5])
        st.text(f'Author: {authors[5]}')