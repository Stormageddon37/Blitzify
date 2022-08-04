import re

import openai
from decouple import config

openai.api_key = config('OPENAI_API_KEY')


def tldr(content):
	response = openai.Completion.create(
		model="text-davinci-002",
		prompt=content + '\n\nTl;dr',
		temperature=0.7,
		max_tokens=60,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0
	)
	return response.choices[0].text


def remove_emojis(content):
	regrex_pattern = re.compile(
		pattern="["u"\U0001F600-\U0001F64F" u"\U0001F300-\U0001F5FF" u"\U0001F680-\U0001F6FF" u"\U0001F1E0-\U0001F1FF" "]+",
		flags=re.UNICODE)
	return regrex_pattern.sub(r'', content)


def add_footer(message):
	return message + '\n💚🖤💚🖤'
