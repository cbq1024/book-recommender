import streamlit as st

st.set_page_config(
    page_title="Book Recommend",
    page_icon="👋",
)

st.write("# Book Recommend 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    > a recommend system for homework in jzxy university
    """
)

st.write("# dev tools info ")
st.markdown(
    """
    - PyCharm 2024.3 (Professional Edition)
    - Windows11 with 24h2
    - anaconda 24.9.2
    - python 3.9.20
    - pip 24.3.1
    """
)

st.write("# ref ")
st.markdown(
    """
    - https://recommenders-team.github.io/recommenders/intro.html
    - http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2023-0-1-1
    """
)

st.title("波兰球 —— 高山下的花环")
st.image("./data/image/poland_ball.jpg")

# st.title("data frame load test")
#
#
# @st.cache_data
# def load_data():
#     return pd.read_csv("./data/uncleaned/books-kaggle-mohamadreza-momeni.csv", on_bad_lines='skip')
#
#
# df = load_data()
# st.dataframe(df.head(10))
