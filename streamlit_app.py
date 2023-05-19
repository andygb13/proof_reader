import streamlit as st
import openai

key = "sk-YgrnmIBaIxKn0AGflchBT3BlbkFJm1ZaEcZauwD172cI3b"
st.title("Proof-Reader")
code = st.text_input("Enter code:", "")
#if len(code)>0:
openai.api_key = "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"

gen = st.button('Generate')
if gen and code:
    completions = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = code,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    st.write(message)