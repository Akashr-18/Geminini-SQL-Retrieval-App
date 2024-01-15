import streamlit as st
import os
import sqlite3
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## Function To Load Google Gemini Model and provide queries as response
def gemini_response(system_message, input):
    model = genai.GenerativeModel(model_name= 'gemini-pro')  
    response = model.generate_content([system_message[0], input])
    return response.text

## Fucntion To retrieve query from the database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## System message
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("SQL Data Retrieval App")

input = st.text_input("Enter your query", key='input')

button = st.button("Get Response")

if button:
    response = gemini_response(prompt, input)
    print("Response: ", response)
    response_sql = read_sql_query(response,"student.db")
    st.subheader("Response: ")
    for row in response_sql:
        st.write(row)
    st.subheader("SQL Query used: ")
    st.write(response)