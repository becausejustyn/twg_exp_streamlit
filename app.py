
import streamlit as st
import numpy as np


def triangles(n):
    val = (n*(n + 1) / 2) * 1000
    return f'You would need {val:,.0f} exp.'

stat_options = [
    "Attack Bonus", "Block", "Dodge", "Submission Bonus", 
    "SDI", "Adrenaline", "Bleed Bonus", "DDI", 
    "Escape Submission", "Initiative", "Health Points", 
    "Stamina", "Pin Opp", "Pin Bonus"]

regular_stat_options = [
    "Attack Bonus", "Block", "Dodge", "Submission Bonus", 
    "SDI", "Adrenaline", "Bleed Bonus", "DDI", 
    "Escape Submission", "Initiative", "Pin Opp", "Pin Bonus"]

def stat_triangles(n, value):

    stat = 0

    if value == 'Health Points':
        stat = (n*(n + 1)) * 20
    if value == 'Stamina':
        stat = (n*(n + 1)) * 5
    if value in regular_stat_options:
        stat = (n*(n + 1)) * 1
    return f'You would get {stat:,.0f} stat points.'


def stat_third_triangles(n, stat):

    level = np.sqrt(n * 2).round(0)
    return f'You would need {level:,.0f} levels of {stat}.'

st.write("""## EXP Calculator""")
st.write("""Insert the number of the AT you would like and the require exp will be shown. """)

number = st.number_input('Insert your desired exp level', min_value=1, max_value=None, step=1, format='%d') #%d %e %f %g %i %u

user_val = triangles(number)

st.write(user_val)

st.write("""## Stat Calculator""")
st.write("""Same as above but for stats. This will allow you to select stats that follow different rules.""")

stat_number = st.number_input('Insert your desired stat level', min_value=1, max_value=None, step=1, format='%d')

stat_type = st.selectbox(
     'Select the stat of interest',
     (stat_options))

user_stat_val = stat_triangles(n = stat_number, value = stat_type)
st.write(user_stat_val)

st.write("""## Reverse Stat Calculator""")
st.write("""How much exp you would require for a certain stat value. """)
st.write("""Note: I have not calculated this for stamina or HP yet. """)
st.write("""Additional Note: The calculation for this is an estimation so values might be off by 1 level in certain situations. """)

stat_number_third = st.number_input('Insert your desired stat value', min_value=1, max_value=None, step=1, format='%d')

stat_type_third = st.selectbox(
     'Select the stat of interest',
     (regular_stat_options))

user_stat_val_third = stat_third_triangles(n = stat_number_third, stat = stat_type_third)

st.write(user_stat_val_third)

st.markdown('This is :sparkles: :sparkles: **fabulous** :sparkles: :sparkles: !')