import os
import difflib
import vk_api
import vk_audio
from pocketsphinx import LiveSpeech, get_model_path

#Список возможных команд
#List of possible commands

command_list = ["привет", "включи", "музыку", "включи музыку", "привет включи музыку", "привет включил музыку"]
result = False

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

print("Say something!")

for phrase in speech:
    print(phrase)
    if result == True:
    	result = False
    	break
    elif phrase != None:
    	for commanda in command_list:
    		if commanda == str(phrase):
    			result_command = str(phrase)
    			result = True
    			break
    	if result != True:
    		print('Повторите запрос, пожалуйста!')
    	elif result == True:
    		result = False
    		break

#Ниже просто набросок для будущего кода. Он ни на что не годен, оставил просто для заметки.

