from translate import Translator

translator = Translator(to_lang="it")

try:
    with open('english.txt', mode='r') as my_file:
        text = (my_file.read())
        translation = translator.translate(text)
        with open('italian.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print('Check your file path!!!')
