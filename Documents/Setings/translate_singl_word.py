#!/usr/bin/env python3
from googletrans import Translator

def translate_text(text, dest):
    translator = Translator()
    translation = translator.translate(text, dest=dest)
    return translation.text

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: python translator.py <text> <destination_language>")
        sys.exit(1)

    text = sys.argv[1]
    dest = sys.argv[2]
    translated_text = translate_text(text, dest)
    print(f"Translated text: {translated_text}")