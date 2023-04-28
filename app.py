import streamlit as st
import pandas as pd
import pickle
import requests

st.title('Movie Recommender System')

similarity = pickle.load(open('similarity.pkl','rb'))

api_key='277e998c81d1568adc13dac9f303a253'
# url='https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movie_id, api_key)

def fetch_image(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=277e998c81d1568adc13dac9f303a253&language=en-US'.format(movie_id))
    response=response.json()
    return 'https://image.tmdb.org/t/p/w500' + response['poster_path']


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    names=[]
    posters=[]
    movie_similarity=similarity[movie_index]
    movie_similarity=sorted(list(enumerate(movie_similarity)),reverse=True,key=lambda x:x[1])
    for i in movie_similarity[1:6]:
        index=i[0]
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_image(movies.iloc[i[0]].movie_id))
    return names,posters    

movies=pd.DataFrame(pickle.load(open('movie_dict.pkl','rb')))

selected_movie = st.selectbox(
    'Select a Movie',
    movies['title'].values)

if st.button('Recommend'):
    names,posters=recommend(selected_movie)
    # st.write(fetch_image(19995))
    col1, col2, col3 ,col4,col5= st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])  
     
    with col4:
        st.text(names[3])
        st.image(posters[3])   
    
    with col5:
        st.text(names[4])
        st.image(posters[4])    
    # st.write(selected_movie)
    
    
