import random

import blitz_dictionary

dictionary = blitz_dictionary.Dictioanry.blitz_dictionary


def dumb_emojify_text(content: str) -> str:
	content = content.replace(',', '').replace('!', '❗').replace('?', '❓')
	# if '💚🖤' not in content[-4:]:
	# 	content = f'{content}\n💚🖤💚🖤'
	last_emoji = ''
	for word in content.split():
		if word in dictionary:
			replacement = random.choice(dictionary[word])
			# print(f'chose {replacement} to replace {word}')
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
