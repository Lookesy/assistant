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

if result_command == "привет включи музыку" or result_command == "включи музыку" or result_command == "привет включил музыку":
	vk_session = vk_api.VkApi(login='89833903557',password='arbuzikiz002')
	vk_session.auth()
	vk = vk_audio.VkAudio(vk=vk_session)
	owner = None
	data = vk.load(owner)
	second_audio = data.Audios[1]
	format_string = "{title} - {artist} ({owner_id}_{id}) -> {url}"
	print("2.",format_string.format(
		title=second_audio.title,
		artist=second_audio.artist,
		owner_id = second_audio.owner_id,
		id=second_audio.id,
		url=second_audio.url
		))
	print("1.",format_string.format(**data.Audios[0].toArray()))