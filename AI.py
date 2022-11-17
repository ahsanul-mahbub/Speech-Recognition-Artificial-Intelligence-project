import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
from PIL import Image

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()
print()
print('Digital Udhbahboni Mela 2022')
talk('Digital Udhbahboni Mela 2022')
print()
print('PRAN-RFL Public School Sheikh Russel ICT Lab')
talk('PRAN-RFL Public School Sheikh Russel ICT Lab')
print()
im = Image.open(r"C:\Users\DOEL\Downloads\pran.jfif")
im.show()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'sheikh russel' in command and 'wikipedia' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for,4)
        print(info)
        talk(info)
    if  'quiz' in command :
        while True:
            print('Question me I will answer your qustion if I know the question answer')
            talk('Question me I will answer your qustion if I know the question answer')
            qt = command
            qt = qt.lower()
            
            if 'who' in qt:
                if 'sheikh' in qt :
                    if 'russel' in qt:
                        print('Sheikh Russel was the youngest child of Bangabandhu Sheikh Mujibur Rahman')
                        talk('Sheikh Russel was the youngest child of Bangabandhu Sheikh Mujibur Rahman')
                        im = Image.open(r"C:\Users\DOEL\Pictures\pictures\sheikhrussel.jpeg")
                        im.show()
            if 'when' in qt and 'where' in qt:
                if 'born' in qt:
                    print('Sheikh Russel was born on October 18, 1964,at Bangabandhu Bhaban in Dhanmondi, Dhaka, Bangladesh')
                    talk('Sheikh Russel was born on October 18, 1964,at Bangabandhu Bhaban in Dhanmondi, Dhaka, Bangladesh')
                if 'death' in qt:
                    print('Sheikh Russel was death On the morning of August 15, 1975,at No.32 in Dhanmondi,Dhaka,Bangladesh')
                    talk('Sheikh Russel was death On the morning of August 15, 1975,at No.32 in Dhanmondi,Dhaka,Bangladesh')
            if 'what' in qt:
                if 'when' in qt:
                    if 'died' in qt:
                        print('At the time of his death, Sheikh Russel was a student at the University Laboratory School')
                        talk('At the time of his death, Sheikh Russel was a student at the University Laboratory School')
                elif 'at the time of sheikh russel death' in qt:
                    print('At the time of his death, Sheikh Russel was a student at the University Laboratory School')
                    talk('At the time of his death, Sheikh Russel was a student at the University Laboratory School')
            if 'what' in qt:
                if 'relation' in qt:
                    if 'with' in qt:
                        if 'hasina' in qt:
                            print('Prime Minister of Bangladesh Sheikh Hasina was the sister of Sheikh Russel')
                            talk('Prime Minister of Bangladesh Sheikh Hasina was the sister of Sheikh Russel')
                            im = Image.open(r"C:\Users\DOEL\Downloads\sheikhhasina.jfif")
                            im.show()
                        if 'bangabandhu sheikh mujibur rahman' in qt:
                            print('Bangabandhu Sheikh Mujibur Rahman was the father of Sheikh Russel')
                            talk('Bangabandhu Sheikh Mujibur Rahman was the father of Sheikh Russel')
                            im = Image.open(r"C:\Users\DOEL\Downloads\231.jpg")
                            im.show()
                        if 'fazilatunnesa' in qt:
                            print('Sheikh Fazilatunnesa Mujib was the mother of Sheikh Russel')
                            talk('Sheikh Fazilatunnesa Mujib was the mother of Sheikh Russel')
                            im = Image.open(r"C:\Users\DOEL\Downloads\222.jpg")
                            im.show()
                        if 'rehena' in qt:
                            print('Sheikh Rehena was the sister of Sheikh Russel')
                            talk(' Sheikh Rehena was the sister of Sheikh Russel')
                            im = Image.open(r'C:\Users\DOEL\Downloads\2020.jfif')
                            im.show()
                        if 'kamal' in qt:
                            print('Sheikh Kamal was the brother of Sheikh Russel')
                            talk('Sheikh Kamal was the brother of Sheikh Russel')
                        if 'jamal' in qt:
                            print('Sheikh Jamal was the brother of Sheikh Russel')
                            talk('Sheikh Jamal was the brother of Sheikh Russel')
            if 'how' in qt:
                if 'lab' in qt:
                    if'bangladesh' in qt:
                        print('Around 4161 Sheikh Russel Digital Labs(SRDLs) are in Bangladesh')
                        talk('Around 4161 Sheikh Russel Digital Labs(SRDLs) are in Bangladesh')
                    if 'sylhet' in qt:
                        print('Around 273 Sheikh Russel Digital Labs(SRDLs) are in Sylhet')
                        talk('Around 273 Sheikh Russel Digital Labs(SRDLs) are in sylhet')
                    if 'dhaka' in qt:
                        print('Around 850 Sheikh Russel Digital Labs(SRDLs) are in Dhaka')
                        talk('Around 850 Sheikh Russel Digital Labs(SRDLs) are in dhaka')
                    if'khulna' in qt:
                        print('Around 494` Sheikh Russel Digital Labs(SRDLs) are in Khulna')
                        talk('Around 494 Sheikh Russel Digital Labs(SRDLs) are in khulna')
                    if'chittagong' in qt:
                        print('Around 789 Sheikh Russel Digital Labs(SRDLs) are in Chittagong')
                        talk('Around 789 Sheikh Russel Digital Labs(SRDLs) are in chittagong')
                    if'barisal' in qt:
                        print('Around 329 Sheikh Russel Digital Labs(SRDLs) are in Barisal')
                        talk('Around 329 Sheikh Russel Digital Labs(SRDLs) are in Barisal')
                    if'mymensingh' in qt:
                        print('Around 379 Sheikh Russel Digital Labs(SRDLs) are in Mymensingh')
                        talk('Around 379 Sheikh Russel Digital Labs(SRDLs) are in Mymensingh')
                    if'rangpur' in qt:
                        print('Around 444 Sheikh Russel Digital Labs(SRDLs) are in Rangpur')
                        talk('Around 444 Sheikh Russel Digital Labs(SRDLs) are in rangpur')
                    if'`rajshahi' in qt:
                        print('Around 603 Sheikh Russel Digital Labs(SRDLs) are in Rajshahi')
                        talk('Around 603 Sheikh Russel Digital Labs(SRDLs) are in rajshahi')
            if 'what' in qt:
                if 'the' in qt:
                    if 'name' in qt:
                        if 'school and colelge' in qt:
                            print('The name of Sheikh Russel school and colelge is Sheikh Russel Cantonment Public School and Colelge in')
                            talk('The name of Sheikh Russel school and colelge is Sheikh Russel Cantonment Public School and Colelge in')
            if 'where' in qt :
                if 'sheikh russel' in qt:
                    if 'bridge' in qt:
                        print('Sheikh Russel Bridge is in Kushtiya')
                        talk('Sheikh Russel Bridge is in Kushtiya')
                if 'national park' in qt:
                    print('Sheikh Russel National Park is in Nawabganj,Dinajpur')
                    talk('Sheikh Russel National Park is in Nawabganj,Dinajpur')
                if 'government school' in qt:
                    if 'primary' in qt:
                        print('Shiekh Russel Government Primary School is in Noa')

                if'rolelr' in qt:
                    print('3 No Gate, Bangabandhu National Stadium Rd, Dhaka 1000')
                    talk('3 No Gate, Bangabandhu National Stadium Rd, Dhaka 1000')
            if 'what' in qt:
                if 'venue' in qt:
                    print('The venue of Udhbhaboni Mela is in front of Union office Shayestaganj,Habiganj')
                    talk('The venue of Udhbhaboni Mela is in front of Union office Shayestaganj,Habiganj')
            

            if qt == 'exit':
                print('Do you have any more qustion about this topic')
                talk('Do you have any more qustion about this topic')
                yn = input()
                if 'no' in yn or 'NO' in yn or 'No' in yn:
                    break   
while True:
    run_alexa()
