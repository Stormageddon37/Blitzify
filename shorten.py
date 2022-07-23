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
