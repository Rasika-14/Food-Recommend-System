import streamlit as st
import pickle
import pandas as pd


def recommend(food):
    food_index = foods[foods['dish'] == food].index[0]
    distances = similarity[food_index]
    food_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_food = []
    for i in food_list:
        recommended_food.append(foods.iloc[i[0]].dish)
    return recommended_food


food_dict = pickle.load(open('food_dict.pkl', 'rb'))
foods = pd.DataFrame(food_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Food Recommender System')

selected_food_name = st.selectbox(
    'Select Favourite Dish',
    foods['dish'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_food_name)
    for i in recommendations:
        st.write(i)
