import streamlit as st
from logic.document_processor import extract_text_from_file
from logic.summarizer import generate_summary
from logic.qa_engine import answer_question
from logic.logic_questioner import generate_questions, evaluate_answer

st.set_page_config(page_title="Smart Research Assistant", layout="wide")
st.title("📄 Smart Assistant for Research Summarization")

if 'document_text' not in st.session_state:
    st.session_state.document_text = ""
    st.session_state.questions = []
    st.session_state.answers = []

uploaded_file = st.file_uploader("Upload a research document (PDF or TXT)", type=['pdf', 'txt'])

if uploaded_file:
    st.session_state.document_text = extract_text_from_file(uploaded_file)
    summary = generate_summary(st.session_state.document_text)
    st.subheader("📝 Auto Summary")
    st.write(summary)

    mode = st.radio("Choose Interaction Mode:", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        question = st.text_input("Ask a question based on the document:")
        if question:
            answer, justification = answer_question(question, st.session_state.document_text)
            st.markdown(f"**Answer:** {answer}")
            st.markdown(f"_Justification:_ {justification}")

    elif mode == "Challenge Me":
        if not st.session_state.questions:
            st.session_state.questions = generate_questions(st.session_state.document_text)
        st.subheader("🧠 Attempt the questions below:")
        for i, q in enumerate(st.session_state.questions):
            user_ans = st.text_input(f"Q{i+1}: {q['question']}", key=f"ans_{i}")
            if user_ans:
                feedback = evaluate_answer(user_ans, q['answer'], q['justification'])
                st.markdown(f"**Feedback:** {feedback}")
