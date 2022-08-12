import streamlit as st
from PIL import Image
import pyperclip
image = Image.open('image.png')

st.image(image, caption='none')


txt = st.text_area('Text to analyze', '''
     The Walrus or := operator is one of the latest additions 
     to python 3.8. It is an assignment operator that lets you 
     assign value to a variable within an expression like 
     conditional statements, loops, etc
     ''')
st.write('1. Walrus operator', txt)


import pyperclip
text_to_be_copied = 'The text to be copied to the clipboard.'
pyperclip.copy(text_to_be_copied)

