import streamlit as st

def main():
    st.title("Study Material Website")

    # Sidebar options
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Home", "Subjects", "About"])

    if page == "Home":
        display_home_page()
    elif page == "Subjects":
        display_subjects_page()
    elif page == "About":
        display_about_page()

def display_home_page():
    st.header("Welcome to our Study Material Website")
    st.write("This website provides study material for various subjects.")

def display_subjects_page():
    st.header("Subjects")
    subjects = ["Mathematics", "Physics", "Chemistry", "Biology"]

    selected_subject = st.selectbox("Select a subject", subjects)

    if selected_subject == "Mathematics":
        display_mathematics_material()
    elif selected_subject == "Physics":
        display_physics_material()
    elif selected_subject == "Chemistry":
        display_chemistry_material()
    elif selected_subject == "Biology":
        display_biology_material()

def display_mathematics_material():
    st.subheader("Mathematics Study Material")
    st.write("Insert mathematics study material here.")

def display_physics_material():
    st.subheader("Physics Study Material")
    st.write("Insert physics study material here.")

def display_chemistry_material():
    st.subheader("Chemistry Study Material")
    st.write("Insert chemistry study material here.")

def display_biology_material():
    st.subheader("Biology Study Material")
    st.write("Insert biology study material here.")

def display_about_page():
    st.header("About")
    st.write("This website is created using Streamlit, a popular Python library for building web apps.")

if __name__ == "__main__":
    main()
