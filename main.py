import streamlit as st
import re

st.title("Аналіз текстового файлу")

uploaded_file = st.file_uploader("Завантажте текстовий файл (.txt)", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")

    st.subheader("Вміст файлу:")
    st.text_area("Текст", text, height=300)

    words = re.findall(r"\b[\w\-']+\b", text, re.UNICODE)
    
    word_count = len(words)
    char_count = len(text)

    st.subheader("Статистика:")
    st.write(f"**Кількість слів (без розділових знаків):** {word_count}")
    st.write(f"**Кількість символів (включно з пробілами):** {char_count}")
else:
    st.info("Будь ласка, завантажте .txt файл для аналізу.")
