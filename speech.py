import speech_recognition as sr
import webbrowser as wb
r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()
with sr.Microphone() as source:
    print('[search edureka: search youtube]')
    print('SPEAK NOW ')
    audio=r3.listen(source)


if 'video' in r2.recognize_google(audio):
    r2=sr.Recognizer()
    url='http://www.edureka.co/'
    with sr.Microphone() as source:
        print('SEARCH YOUR QUERY')
        audio = r2.listen(source)

        try:
            get=r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('ERROR')
        except sr.RequestError as e:
            print('FAILED'.format(e))
