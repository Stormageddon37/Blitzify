import emojis
import openai
from decouple import config

from translate import text_to_english

openai.api_key = config('OPENAI_API_KEY')


def smart_emojify_text(text: str) -> str:
	response = openai.Completion.create(
		model="text-davinci-002",
		prompt=f"Convert text into emojis. {text}:",
		temperature=1.0,
		max_tokens=50,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0.85,
		stop=["\n"]
	)
	return ''.join(emojis.get(response.choices[0].get('text')))


def slow_smart_emojify_text(text: str) -> str:
	response = ''
	words = text.split()
	for item in words:
		response += item + ' ' + smart_emojify_text(item) + ' '
	return response.replace('  ', ' ')


# message = open(file='input.txt', mode='r', encoding='utf-8').read()
# message = text_to_english(message)
# print('original english msg:\n\n' + message)
# message = slow_smart_emojify_text(message)
# print('end result:\n\n' + message)
