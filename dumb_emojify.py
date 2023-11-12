import random

import blitz_dictionary
from translate import text_to_english

dictionary = blitz_dictionary.Dictionary.blitz_dictionary


def dumb_emojify_text(content: str) -> str:
    content = content.replace('!', '❗').replace('?', '❓')
    last_emoji = ''
    for hebrew_word in content.split():
        english_word = text_to_english(hebrew_word).lower()
        if english_word in dictionary:
            replacement = random.choice(dictionary[english_word])
            if replacement is not last_emoji:
                content = content.replace(hebrew_word, f'{hebrew_word} {replacement}')
                last_emoji = replacement
            else:
                stashed_word = dictionary[english_word].remove(replacement)
                try:
                    replacement = random.choice(dictionary[english_word])
                except IndexError:
                    replacement = stashed_word
                if replacement is not None:
                    content = content.replace(hebrew_word, f'{hebrew_word} {replacement}')
                    last_emoji = replacement

    return content
