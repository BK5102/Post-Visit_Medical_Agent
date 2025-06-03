# OpenAI call to extract structured JSON of tasks
# Explain doctor's notes or test results using glossary + plain english

import openai

def explain_note(note, model="gpt-4", system_prompt=None):
    if system_prompt is None:
        system_prompt = "You are a helpful medical assistant. Explain the following doctor's note to the patient in plain English, keeping it short and kind."

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": note}
        ]
    )
    return response.choices[0].message.content.strip()
