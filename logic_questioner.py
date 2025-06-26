from transformers import pipeline

qg_model = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")

def generate_questions(text):
    chunks = text.split(". ")[:5]
    questions = []
    for chunk in chunks:
        q_input = f"generate question: {chunk}"
        q_output = qg_model(q_input, max_length=64)[0]['generated_text']
        questions.append({
            'question': q_output,
            'answer': chunk.strip(),
            'justification': f"Based on: '{chunk.strip()}'"
        })
    return questions

def evaluate_answer(user_response, correct_answer, justification):
    if user_response.lower() in correct_answer.lower():
        return f"✅ Correct! {justification}"
    return f"❌ Not quite. {justification}"
