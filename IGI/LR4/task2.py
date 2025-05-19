# Lab Work 4: Task 2
# Version: 1.0
# Developer: Belavusau Anton
# Date: May 10, 2025

import re
import zipfile
from statistics import mean

def analyze_text(input_file: str, output_file: str):
    """Analyze text from input file and save results to output file."""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        words = re.findall(r'\b\w+\b', text)

        modified_text = re.sub(r'([a-z])([A-Z])', r'_?_\1\2_?_', text)

        short_words = [w for w in words if len(w) < 7]
        num_short_words = len(short_words)

        words_ending_a = [w for w in words if w.endswith('a')]
        shortest_a = min(words_ending_a, key=len) if words_ending_a else "None"

        sorted_words = sorted(words, key=len, reverse=True)

        print(text)

        narrative = len(re.findall(r'[\.]+', text))
        interrogative = len(re.findall(r'[\?]+', text))
        imperative = len(re.findall(r'[\!]+', text))

        sentences = re.split(r'[\.\!\?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        num_sentences = len(sentences)

        avg_sentence_length = mean(len(re.findall(r'\b\w+\b', s)) for s in sentences)
        avg_word_length = mean(len(w) for w in words)

        emoticon_pattern = r'[:;]-*([\(\)\[\]])\1*'
        num_emoticons = len(list(re.finditer(emoticon_pattern, text)))

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Modified Text:\n{modified_text}\n\n")
            f.write(f"Words < 7 chars: {num_short_words}\n")
            f.write(f"Shortest word ending with 'a': {shortest_a}\n")
            f.write(f"Sorted words:\n{', '.join(sorted_words)}\n\n")
            f.write(f"Total sentences: {num_sentences}\n")
            f.write(f"Narrative: {narrative}, Interrogative: {interrogative}, Imperative: {imperative}\n")
            f.write(f"Avg sentence length: {avg_sentence_length:.2f} words\n")
            f.write(f"Avg word length: {avg_word_length:.2f} chars\n")
            f.write(f"Emoticons: {num_emoticons}\n")

        with zipfile.ZipFile('output.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(output_file)

        with zipfile.ZipFile('output.zip', 'r') as zipf:
            info = zipf.getinfo(output_file)
            print(f"Archived file: {info.filename}, Size: {info.file_size}, Compressed: {info.compress_size}")

    except FileNotFoundError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"Error during text analysis: {e}")