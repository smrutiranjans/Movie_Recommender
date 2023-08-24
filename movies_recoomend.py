import streamlit as st 
import pickle
def recommend(movie):
    index=movies[movies['title']==movie].index[0] 
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommended_list=[]
    for i in distances[1:6]:
        recommended_list.append(movies.iloc[i[0]].title)
    return recommended_list

st.title("Movie Recommendation")
movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies_list=movies['title'].values
selected_movie=st.selectbox("Select from below movies",movies_list)
if st.button('Show recommendation'):
    movie_names=recommend(selected_movie)
    for i in movie_names:
        st.header(i)