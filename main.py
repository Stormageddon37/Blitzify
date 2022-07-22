import random
import time
from math import ceil

import blitz_dictionary

dictionary = blitz_dictionary.Dictioanry.blitz_dictionary


def convert_line(content: str) -> str:
    content = content.replace(',', '').replace('!', '❗').replace('?', '❓')
    # if '💚🖤' not in content[-4:]:
    # 	content = f'{content}\n💚🖤💚🖤'
    last_emoji = ''
    for word in content.split():
        if word in dictionary:
            replacement = random.choice(dictionary[word])
            print(f'chose {replacement} to replace {word}')
            if replacement is not last_emoji:
                content = content.replace(word, f'{word} {replacement}')
                last_emoji = replacement
            else:
                dictionary[word].remove(replacement)
                replacement = random.choice(dictionary[word])
                if replacement is not None:
                    content = content.replace(word, f'{word} {replacement}')
                    last_emoji = replacement

    return content.replace('  ', ' ')


def convert_file() -> float:
    start = time.time()
    input_file = open(file='input.txt', mode='rt', encoding='utf-8')
    if input_file is None:
        print('you need an input')
    output_file = open(file='output.txt', mode='wt', encoding='utf-8')
    for line in input_file:
        output_file.write(convert_line(line))
    time.sleep(0.001)  # this is important for a reason
    input_file.close()
    output_file.close()
    end = time.time()
    return 1000 * (end - start)  # conert to milliseconds


if __name__ == '__main__':
    try:
        elapsed = convert_file()
        print(f'Task finished. Message Blitzified ⚡ in {ceil(elapsed)} ms')
    except (Exception, UnicodeError) as e:
        print(f'Oh no! Someone has done an oopsy: \n{e}')
