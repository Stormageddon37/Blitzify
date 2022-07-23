import time

from dumb_emojify import dumb_emojify_text
from smart_emojify import smart_emojify_text, slow_smart_emojify_text
from translate import text_to_english, text_to_hebrew


def full_emojify(content):
	content = text_to_english(content)
	content = smart_emojify_text(dumb_emojify_text(content))
	return content


if __name__ == '__main__':
	try:
		start = time.time()
		message = open(file='input.txt', mode='r', encoding='utf-8').read()
		print(message)
		print(text_to_english(message))
		print(dumb_emojify_text(text_to_english(message)))
		print(slow_smart_emojify_text(dumb_emojify_text(text_to_english(message))))
		print(text_to_hebrew(slow_smart_emojify_text(dumb_emojify_text(text_to_english(message)))))

		exit()
		message = full_emojify(message)
		# output_file = open(file='output.txt', mode='wt', encoding='utf-8')
		# output_file.write(message)
		end = time.time()
		elapsed = 1000 * (end - start)
		print(f'Task finished. Message Blitzified ⚡ in {elapsed} ms')
	except (Exception, UnicodeError) as e:
		print(f'Oh no! Someone has done an oopsy: \n{e}')
