import streamlit as st
from openai import OpenAI
api_key='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'
client=OpenAI(api_key=api_key)
def get_ans(input_text):
    OpenAI.api_key = "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"
    chatOutput = (client.chat.completions.create(model="gpt-3.5-turbo-16k",
                                              messages=[{"role": "system",
                                                         "content": "You are a very intelligent farmer who can understand various languages like English , Tamil. You are here to help with any sort of agricultural doubts asked to you. The user can ask questions in either english or tamil. You can reply in English itself. If they greet you tell them I am vevasa, your personal agricultural assistant"},
                                                        {"role": "user", "content": input_text}
                                                        ],
                                              temperature=0
                                              ))
    r= chatOutput.choices[0].message.content
    return r
st.title("VEVASA ASSISTANT")
input_text=st.text_input(label='Enter Your Question')
if st.button("SUBMIT"):
    answers = get_ans(input_text)
    st.write(answers)