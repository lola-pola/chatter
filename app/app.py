from streamlit_chat import message
import streamlit as st
import openai
import os
#gnhfBKzFnC9uQEgE321w
# Define Streamlit app
## simple dic
import streamlit as st
import pandas as pd
import numpy as np



def chatterbot(question, context,max_tokens=2000,temperature=1,engine="gpt3"):
        print(question,context,max_tokens,temperature,engine)
        response = openai.ChatCompletion.create(
            engine=engine,
            messages=[{"role":"system","content":context},
              {"role":"user","content":question}
              ],
        
            max_tokens=max_tokens,
            stop=None,
            temperature=temperature
            )
        return  str(response['choices'][0]['message']['content'])
        


# Define Streamlit app
def app():
    st.set_page_config(page_title="OpenAI Simple Chatbot", page_icon=":robot:")
    st.title("OpenAI Simple Chatbot")
    
    with st.expander("Settings"):
            context = st.text_area("Context", height=200, key="you are a bot very nice of a israeli startup",value="you are a bot very nice of a israeli startup")
            max_tokens = st.number_input("Max tokens", value=2000, key="max_tokens")
            temperature = st.number_input("Temperature", value=1, key="temperature")
            engine = st.text_input("Engine", "gpt3", key="gpt3")
            

            # Set up OpenAI API key
            openai.api_type = "azure"
            openai.api_base = st.text_input("API base", value="https://aks-production.openai.azure.com/", key="api_base")
            openai.api_version = st.text_input("api version",value="2023-03-15-preview")
            openai.api_key = st.text_input('azure openai key', key="KEY_AZURE_AI", value=os.getenv("KEY_AZURE_AI"), type="password") 
            if st.checkbox("Submit", key="submit"):
                st.success("Submitted!")

        
        

    st.session_state['generated'] = []
    st.session_state['past'] = []


    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []
        
        

    user_input=st.text_input("You:",key='input')

    if user_input:
        output=chatterbot(user_input,context,max_tokens,temperature,engine)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])-1, -1, -1):
                message(st.session_state["generated"][i], key=str(i))
                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user') 
                st.session_state.generated = ''



def main():
    app()


if __name__ == '__main__':
    main()
