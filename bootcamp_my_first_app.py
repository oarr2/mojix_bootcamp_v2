import streamlit as st
from PIL import Image

image = Image.open('image.png')

st.image(image, caption='none')

st.title('1. Walrus operator')


txt = st.text_area('Text to analyze', '''
     The Walrus or := operator is one of the latest additions 
     to python 3.8. It is an assignment operator that lets you 
     assign value to a variable within an expression like 
     conditional statements, loops, etc
     ''')

st.header('Example')

code = '''Mylist = [1,2,3]
if(l := len(mylist) > 2)
print(l)'''
st.code(code, language='python')

st.header('output')

st.code('3', language='python')