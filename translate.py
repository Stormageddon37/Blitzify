from googletrans import Translator

translator = Translator()


def text_to_lang(text, destination):
	return translator.translate(text, dest=destination).text


def text_to_english(text):
	return text_to_lang(text, 'en')


def text_to_hebrew(text):
	return text_to_lang(text, 'he')
