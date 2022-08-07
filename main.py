import time

from dumb_emojify import dumb_emojify_text
from smart_emojify import slow_smart_emojify_text
from utils import remove_emojis, add_footer


def full_emojify(content):
	content = remove_emojis(content)
	content = dumb_emojify_text(content)
	content = slow_smart_emojify_text(content, 100)
	content = add_footer(content)
	return content.replace('  ', ' ')


if __name__ == '__main__':
	try:
		start = time.time()
		message = open(file='input.txt', mode='r', encoding='utf-8').read()
		output_file = open(file='output.txt', mode='wt', encoding='utf-8')
		output_file.write(full_emojify(message).strip())
		elapsed = time.time() - start
		print(f'Task finished. Message Blitzified ⚡ in {round(elapsed, 3)} s')
	except (Exception, UnicodeError) as e:
		print(f'Oh no! Someone has done an oopsy: \n{e}')
