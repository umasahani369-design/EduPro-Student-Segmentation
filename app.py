import streamlit as st
import pandas as pd

st.title("🎓 EduPro Student Segmentation")

users = pd.read_csv("users.csv")
courses = pd.read_csv("courses.csv")
transactions = pd.read_csv("transactions.csv")

df = transactions.merge(users, on="UserID").merge(courses, on="CourseID")

user = st.selectbox("Select User", sorted(df["UserID"].unique()))

st.subheader("Learner Profile")
st.dataframe(df[df["UserID"] == user][["Age","Gender"]].drop_duplicates())

st.subheader("Enrolled Courses")
st.dataframe(df[df["UserID"] == user][["CourseCategory","CourseLevel","CourseRating","Amount"]])
