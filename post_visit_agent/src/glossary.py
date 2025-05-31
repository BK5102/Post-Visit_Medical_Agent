# Term replacement logic

#Maps med terms → layperson explanations

"""
    Replaces/appends explanations for glossary terms in text.
    
    Parameters:
    - text: string, sentence from samples_labeled
    - glossary: dictionary {term: description}
    
    Returns:
    - explained_text: modified sentence with term explanations
    """

import re

def explain_terms(text, glossary):
    
    explained_text = text
    for term, desc in glossary.items():
        pattern = r'\b' + re.escape(term) + r'\b'
        if re.search(pattern, explained_text, flags=re.IGNORECASE):
            explained_text = re.sub(
                pattern,
                f"{term} ({desc})",
                explained_text,
                flags=re.IGNORECASE
            )
    return explained_text


