import streamlit as st

st.title("はじめてのStreamlitアプリ")
st.write("こんにちは!Streamlitの世界へようこそ!")
name = st.text_input("あなたの名前は?")
if name:
    st.write(f"こんにちは、{name}さん!")
st.subheader("Streamlitでできること")
st.write("- データの可視化")
st.write("- インタラクティブなWebアプリ")