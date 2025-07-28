import random

def intro():
    print("🌟 Welcome to EnglishGuru! Your English homework helper.")
    print("Type 'exit' to quit anytime.")

def grammar_correction(user_input):
    corrections = {
        "i am go to school": "I am going to school.",
        "he eat apple": "He eats an apple.",
        "they is happy": "They are happy.",
        "my friend are playing": "My friend is playing."
    }
    corrected = corrections.get(user_input.lower(), None)
    if corrected:
        return f"✅ Corrected: '{corrected}'\n📝 Explanation: Subject-verb agreement or tense was incorrect."
    else:
        return "✅ Your sentence seems fine, or I don't have a correction for it right now."

def vocabulary_meaning(word):
    meanings = {
        "benevolent": "kind and generous (Telugu: దయతో కూడిన)",
        "honest": "truthful and sincere (Telugu: నిజాయితీ గలవాడు)",
        "beautiful": "pleasant to look at (Telugu: అందమైన)"
    }
    return meanings.get(word.lower(), "Sorry, I don't know the meaning of that word yet.")

def essay_topic(topic):
    topics = {
        "my best friend": "My best friend is Ravi. He is kind, helpful, and studies well. We play together every evening.",
        "my school": "My school is big and beautiful. There are many trees. My teachers are friendly and helpful.",
        "my country": "My country is India. It is known for its culture and unity. I love my country very much."
    }
    return topics.get(topic.lower(), "Sorry, I don’t have an essay on that topic yet.")

def translate_telugu(roman_input):
    translations = {
        "nenu school ki vellanu": "I went to school.",
        "mee peru emiti": "What is your name?",
        "naku english raledu": "I don't know English."
    }
    return translations.get(roman_input.lower(), "Sorry, I couldn't understand the Telugu sentence.")

def main():
    intro()
    while True:
        user_input = input("👦 You: ")
        if user_input.lower() == "exit":
            print("👋 Goodbye! Keep practicing English.")
            break

        if "correct" in user_input.lower() or "grammar" in user_input.lower():
            sentence = input("📌 Enter a sentence to check grammar: ")
            print(grammar_correction(sentence))

        elif "meaning" in user_input.lower() or "word" in user_input.lower():
            word = input("📚 Enter the word: ")
            print("📖 Meaning:", vocabulary_meaning(word))

        elif "essay" in user_input.lower() or "paragraph" in user_input.lower():
            topic = input("✏️ Enter essay topic (e.g., my best friend): ")
            print("📝", essay_topic(topic))

        elif "translate" in user_input.lower() or "telugu" in user_input.lower():
            telugu_input = input("🗣️ Enter Telugu sentence in English letters: ")
            print("🔁 English Translation:", translate_telugu(telugu_input))

        else:
            print("🤖 I can help with grammar correction, word meanings, essays, or Telugu to English translation.")

if __name__ == "__main__":
    main()
