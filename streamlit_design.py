import streamlit as st
def main():
    st.set_page_config("Chat with Multiple PDFs", page_icon=":books:")
    st.header("Chat with Multiple PDFs :books:")
    with st.sidebar:
        st.header("Chat with PDF 💬")
        st.title("LLM Chatpdf LangChain")
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload the PDF Files here", accept_multiple_files=True)
        st.button("Process")

        st.markdown('''
        - [Streamlit](https://streamlit.io/)
        - [LangChain](https://python.langchain.com/)
        - [OpenAI](https://platform.openai.com/docs/models) LLM Model
        ''')
if __name__ == "__main__":
    main()