from gtts import gTTS
import os

myText = 'Hello aiyhaam'

language='ml'

output = gTTS(text=myText, lang=language, slow=False)

output.save('output2.mp3')

os.system('start output2.mp3')
