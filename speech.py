from gtts import gTTS
import win32com.client as wincl
import streamlit as st

def main():
    st.title('音声読み上げアプリ')
    selected = st.radio('Audio type',
                        ['Microsoft','Google'])
    text = st.text_input(label='Message',value='Hello,tokyo!')
    if st.button('Speak'):
        audio = 'speech.mp3'
        if selected == 'Google':
            tts = gTTS(text=text, lang='ja')
            tts.save(audio)
        elif selected == 'Microsoft':
            sapi = wincl.Dispatch('SAPI.SpVoice')
            fs = wincl.Dispatch('SAPI.SpFileStream')
            fs.Open(audio,3)
            sapi.AudioOutputStream =fs
            sapi.Speak(text)
            fs.close()
        st.audio(audio)
if __name__=='__main__':
   main()
