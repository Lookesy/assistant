import os
import difflib
import pyglet
import webbrowser 
import re
from pocketsphinx import LiveSpeech, get_model_path

#Список возможных команд
#List of possible commands

command_list = ["привет", "включи", "музыку", "включи музыку", "привет включи музыку", "привет включил музыку", "поиск", "писк"]
end_comm = None
find_str = ['поиск', "найти", "найди"]

#Распознавание речи
#Speech recognition
model_path = get_model_path()

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'zero_ru.cd_cont_4000'),
    lm=os.path.join(model_path, 'ru.lm'),
    dic=os.path.join(model_path, 'ru.dic')
)

print("Скажите что-нибудь!")

for phrase in speech:
    print(phrase)
    text_phrase = phrase
    if phrase != None:
        for command in command_list:
            if command == str(phrase):
                end_comm = str(phrase)
        if end_comm == "включи" or end_comm == "музыку" or end_comm == "включи музыку" or end_comm == "включил музыку" or end_comm == "привет включи музыку" or end_comm == "привет включил музыку":
            sound = pyglet.media.load('nggyu.mp3', streaming=False)
            sound.play()
            pyglet.app.run()
        for findstr in find_str:
            index = text_phrase.find(findstr)
            if index != -1:
                query = phrase.replace(findstr, '')
                webbrowser.open_new_tab('https://yandex.ru/search/?text=' % query)




        print("Повторите запрос!")



