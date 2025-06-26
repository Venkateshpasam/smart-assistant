from transformers import pipeline

qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_question(question, context):
    result = qa_model(question=question, context=context)
    answer = result['answer']
    snippet = context[result['start']:result['end'] + 200].split(". ")[0]
    justification = f"This is supported by the text: '{snippet.strip()}'"
    return answer, justification
