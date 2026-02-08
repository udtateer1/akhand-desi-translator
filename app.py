import streamlit as st
import fitz
from googletrans import Translator
import json

st.set_page_config(page_title="Desi Katha Vachak")
st.title("📜 Akhand Desi Anuvad")

translator = Translator()

if 'memory' not in st.session_state:
    st.session_state.memory = {"System": "Kaal-Chakra"}

def translate_desi(text):
    try:
        t = translator.translate(text, src='en', dest='hi').text
        for eng, desi in st.session_state.memory.items():
            t = t.replace(eng, desi)
        return t.replace("क्या कर रहे हो", "का कर रओ").replace("बेवकूफ", "ससुरो")
    except:
        return text

up = st.file_uploader("PDF Upload Karo", type="pdf")
if up:
    doc = fitz.open(stream=up.read(), filetype="pdf")
    if st.button("Anuvad Shuru"):
        res = ""
        for i in range(len(doc)):
            res += f"\n\n--- Page {i+1} ---\n\n" + translate_desi(doc[i].get_text())
        st.text_area("Desi Novel", res, height=300)
        st.download_button("Download", res, "Desi_Novel.txt")
