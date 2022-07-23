from googletrans import Translator

translator = Translator()


def text_to_english(text):
	return translator.translate(text, dest='en').text


def text_to_hebrew(text):
	return translator.translate(text, dest='he').text


with open(file='input.txt', mode='rt', encoding='utf-8') as text_file:
	content = text_file.read()
