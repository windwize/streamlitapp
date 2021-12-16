import streamlit as st
import requests
import json

st.set_page_config(layout="wide", page_title="Translate app")

st.header("Translate app")

danci = st.text_input("中国語若しくは英語を入力してください")
fanhui = requests.get("http://dict.iciba.com/dictionary/word/suggestion?word="+danci)
data1 = fanhui.text
data2 = json.loads(data1)
for i in range(len(data2["message"])):
    st.write(data2["message"][i]["key"],data2["message"][i]["paraphrase"])

#隐藏按钮及底部链接
sysmenu = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
'''
st.markdown(sysmenu,unsafe_allow_html=True)