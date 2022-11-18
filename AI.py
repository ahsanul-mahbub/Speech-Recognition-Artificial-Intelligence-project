import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
from PIL import Image
import webbrowser
lis = sr.Recognizer()
siri = pyttsx3.init()
voices = siri.getProperty('voices')
siri.setProperty('voice', voices[1].id)


def talk(text):
    siri.say(text)
    siri.runAndWait()
def Wm():
    time = int(datetime.datetime.now().hour)
    if time >= 4 and time <12:
        print('Siri : Good Noon Sir')
        talk(' Good Noon Sir')
    elif time >= 16 and time < 18:
        print('Siri : Good Afternoon Sir')
        talk('Good Afternoon Sir')
    elif time >= 18 and time < 20:
        print('Siri : Good Evening Sir')
        talk('Good Evening Sir')
    else:
        print('Siri : Good Night Sir ')
        talk('Good Night Sir')
Wm()

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
            voice = lis.listen(source)
            command = lis.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                command = command.replace('siri', '')
    except:
        pass
    return command

def run_siri():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 2)
        print(info)
        talk(info)

    elif  'quiz' in command:
        while True:
            talk('Ask a question about sheikh russel')
            qt = input('Ask a question about Sheikh Russel :')
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
    if 'pran' in command:
        while True:
            rfl = input("Ask a question about PRAN-RFL Public School : ")
            rfl = rfl.lower()

            if "founded" in rfl:
                if "pran" in rfl:
                    if "rfl" in rfl:
                            print("Founder : Major Genarel Amjad Khan Chowdhury")
                            talk("Founder : Major Genarel Amjad Khan Chowdhury")
                            im = Image.open(r"C:\Users\DOEL\Downloads\amjad.jpg")
                            im.show()
            elif "ceo" in rfl:
                print("CEO : Ahsan Khan Chowdhury")
                talk("CEO : Ahsan Khan Chowdhury")
                im = Image.open(r'C:\Users\DOEL\Downloads\ahsan.jpg')
            elif "director" in rfl :
                print("Director : Seema Chowdhury")
                talk("Director : Seema Chowdhury")
            elif "advisor" in rfl:
                print("Advisor : Suprita Paul")
                talk("Advisor : Suprita Paul")
            elif "head" in rfl and "hrm" in rfl:
                print("HRM Head is : Faruk hossain")
                talk("HRM Head is : Faruk hossain")
            elif "president" in rfl:
                print("commander M Shamsul alom miah , b an-ob")
                talk("commander M Shamsul alom miah , b an-ob")
            elif "principal" in rfl:
                if "pip" in rfl:
                    print("Shah Muhammad: Jewel Reza")
                    talk("Shah Muhammad: Jewel Reza")
                elif "hip" in rfl:
                    print("Mr.Muhammad Mubinul Hoque Chowdhury")
                    talk("Mr.Muhammad Mubinul Hoque Chowdhury")
                    im = Image.open(r"C:\Users\DOEL\Pictures\Saved Pictures\principalhip.jpg")
                    im.show()
                elif "danga" in rfl:
                    print("Muhammad Shahidur Rahman Khan")
                    talk("Muhammad Shahidur Rahman Khan")

                else:
                    print("There is no PRAN RFL public school principal in this district")
                    talk("There is no PRAN RFL public school principal in this district")
            elif "vice" in rfl and "principal" in rfl:
                if "hip" in rfl:
                    print("Muhammad Samsul Islam")
                    talk("Muhammad Samsul Islam")
                elif "pip" in rfl:
                    print("Muhammad Samsul Islam")
                    talk("Muhammad Samsul Islam")
            elif "club" in rfl:
                if "hip" in rfl:
                    print("Science Club, Soprts Club, Literary Club, Debate Club")
                    talk("Science Club, Soprts Club, Literary Club, Debate Club")
                if "pip" in rfl:
                    print("Science Club,Sports Club")
                    talk("Science Club, Sports Club")
            elif "sports" in rfl and "teacher" in rfl:
                if "hip" in rfl:
                    print("Muhammad Jakir Hossain")
                    talk("Muhammad Jakir Hossain")
                if "pip" in rfl:
                    print("Muhammad Jakir Hossain")
                    talk("Muhammad Jakir Hossain")
            if "science" in rfl :
                if "hip" in rfl :
                    print("1 : Chemistry Teacher : Faruk Hossain")
                    print("2 : Higher Math Teacher : Mr. Tahazul Islam and Mr.Lutur Rahman")
                    print("3 : Physics Teacher : Sarwer Alom")
                    print("4 : Bangladesh and Global studies Teacher : Mr. Sanaullah")
                    print("5 : Biology Teacher : Mr. Mahfuzur Rahman")
                    talk("Chemistry Teacher : Faruk Hossain")
                    talk(" Higher Math Teacher : Mr. Tahazul Islam and Mr.Lutur Rahman")
                    talk("Physics Teacher : Sarwer Alom")
                    talk("Bangladesh and Global studies Teacher : Mr. Sanaullah")
                    talk("Biology Teacher : Mr. Mahfuzur Rahman")
                elif "ghorshal" in rfl:
                    print("1 : Chemistry Teacher : Masuda Sultana")
                    print("2 : Higher Math Teacher : Dipak Chandra Das")
                    print("3 : Physics Teacher : Mohaimeen-Bin-Zaman")
                    print("4 : Bangladesh and Global studies Teacher : Sumitra Rani Bhowmik")
                    print("5 : Biology Teacher : Abu Hanif Sarker")
                    print(" Science Teacher : Muhammad Kafi Uddin and Tanzina Sanjid Sinthi")
                    talk("1 : Chemistry Teacher : Masuda Sultana")
                    talk("2 : Higher Math Teacher : Dipak Chandra Das")
                    talk("3 : Physics Teacher : Mohaimeen-Bin-Zaman")
                    talk("4 : Bangladesh and Global studies Teacher : Sumitra Rani Bhowmik")
                    talk("5 : Biology Teacher : Abu Hanif Sarker")
                    talk(" Science Teacher : Muhammad Kafi Uddin and Tanzina Sanjid Sinthi")
                elif "danga" in rfl:
                    print("Science Teacher : Sheikh Tahmin Akter Jui")
                    talk("Science Teacher : Sheikh Tahmin Akter Jui")
                else:
                    print("There is no PRAN RFL public school Science teacher in this district")
                    talk("There is no PRAN RFL public school science teacher in this district")
            elif "ict" in rfl :
                if "hip" in rfl:
                    print("ICT Teacher : Ms. Shamima Sultana")
                    talk("ICT Teacher : Ms. Shamima Sultana")
                elif "pip" in rfl:
                    print("ICT Teacher: Muhammad Mosharaf Hossain")
                    talk("ICT Teacher : Muhammad Mosharaf Hossain")
                else:
                    print("There is no PRAN RFL public school ict teacher in this district")
                    talk("There is no PRAN RFL public school ict teacher in this district")
            elif "religion" in rfl :
                if "hip" in rfl:
                    print("Islam Teacher : Mr.Abdur Rahman Faruki")
                    print("Hindu Teacher : Sharna Bashak")
                    talk("Islam Teacher : Mr.Abdur Rahman Faruki")
                    talk("Hindu Teacher : Sharna Bashak")
                elif "pip" in rfl:
                    print("Islam Teacher : Muhammad Zulfiker Ali")
                    print("Hindu Teacher : Shishir Chandra Biswas")
                    talk("Islam Teacher : Muhammad Zulfiker Ali")
                    talk("Hindu Teacher : Shishir Chandra Biswas")
                else:
                    print("There is no PRAN RFL public school religion teacher in this district")
                    talk("There is no PRAN RFL public school religion teacher in this district")
            elif "pran" in rfl and "gm" in rfl:
                print("Genarel Manager : Dipak Kumar Dev")
                talk("Genarel Manager : Dipak Kumar Dev")
            elif "incharge" in rfl :
                if "hip" in rfl:
                    print("Senior In-charge : Mr. Tahazul Islam")
                    print("junior In-charge : Ms. Maksuda Akter Bithi")
                    talk("Senior In-charge : Mr. Tahazul Islam")
                    talk("junior In-charge : Ms. Maksuda Akter Bithi")
                    im = Image.open(r"C:\Users\DOEL\Pictures\Saved Pictures\3233.jpeg")
                    im.show()
                    im = Image.open(r"C:\Users\DOEL\Pictures\Saved Pictures\1203.jpeg")
                    im.show()
                elif "pip" in rfl:
                    print("Junior In-cahrge : Muhammad Mosharaf Hossain")
                    talk("Junior In-cahrge : Muhammad Mosharaf Hossain")
                else:
                    print("There is no PRAN RFL public school in-charge in this district")
                    talk("There is no PRAN RFL public school in-charge in this district")
            elif "bangla" in rfl and "teacher" in rfl:
                if "hip" in rfl :
                    print("Bangla Teacher : Mr. Mofakkar Uddin")
                    talk("Bangla Teacher : Mr. Mofakkar Uddin")
                elif "pip" in rfl:
                    print("Bangla Teacher : Muhammad Tuhidul Islam")
                    print(" Bangla Teacher : Muhammad Nur Alam")
                    talk("Bangla Teacher : Muhammad Tuhidul Islam")
                    talk(" Bangla Teacher : Muhammad Nur Alam")
                elif "danga" in rfl:
                    print("Bangla Teacher : Muhammad Shahinur Rahman")
                    talk("Bangla Teacher : Muhammad Shahinur Rahman")
                else:
                    print("There is no PRAN RFL public school bangla teacher in this district")
                    talk("There is no PRAN RFL public school bangla teacher in this district")
            elif "english" in rfl and "teacher" in rfl:
                if "hip" in rfl:
                    print("English Teacher : Mr. Biplop Deb")
                    print("English Teacher : Ms. Fabiha Chowdhury")
                    print("English Teacher : Tahmina Ahsan")
                    talk("English Teacher : Mr. Biplop Deb")
                    talk("English Teacher : Ms. Fabiha Chowdhury")
                    talk("English Teacher : Tahmina Ahsan")
                elif "pip" in rfl:
                    print("English Teacher : Subarna mili")
                    print("English Teacher : Shayla Ahmed")
                    print("English Teacher : Tahmina Sharmin")
                    print("English Teacher : Zubayda Sultana")
                    talk("English Teacher : Subarna mili")
                    talk("English Teacher : Shayla Ahmed")
                    talk("English Teacher : Tahmina Sharmin")
                    talk("English Teacher : Zubayda Sultana")
                else:
                    print("There is no PRAN RFL public school english teacher in this district")
                    talk("There is no PRAN RFL public school english teacher in this district")
            elif "commerce" in rfl and "teacher" in rfl:
                if "hip" in rfl :
                    print("Finance Banking Teacher : Shamima Aktar Asha")
                    print("Accounting Teacher : Dipto Singha ")
                    talk("Finance Banking Teacher : Shamima Aktar Asha")
                    talk("Accounting Teacher : Dipto Singha ")
                if "pip" in rfl:
                    print("Accounting Teacher : Mohammad Kamrul Islam")
                    talk("Accounting Teacher : Mohammad Kamrul Islam")
                else:
                    print("There is no PRAN RFL public school commerce teacher in this district")
                    talk("There is no PRAN RFL public school commerce in this district")
            elif "math" in rfl and "teacher" in rfl:
                if "hip" in rfl :
                    print("Math Teacher : Mr. Tahazul Islam ")
                    print("Math Teacher : Mr.AKM Abul Bashar Farazi")
                    print("Math Teacher : Mr. N.M Ashek Ullah")
                    print("Math Teacher : Mr.Lutfur Rahman ")
                    print("Math Teacher : Ms. Shaiqun Nahar")
                    talk("Math Teacher : Mr. Tahazul Islam ")
                    talk("Math Teacher : Mr.AKM Abul Bashar Farazi")
                    talk("Math Teacher : Mr. N.M Ashek Ullah")
                    talk("Math Teacher : Mr.Lutfur Rahman ")
                    talk("Math Teacher : Ms. Shaiqun Nahar")
                elif "pip" in rfl:
                    print("Math Teacher : Mazharul Huque")
                    print("Math Teacher : Muhammad Aroj Ali")
                    print("Math Teacher : Dipak Chandra Das")
                    talk("Math Teacher : Mazharul Huque")
                    talk("Math Teacher : Muhammad Aroj Ali")
                    talk("Math Teacher : Dipak Chandra Das")
                else:
                    print("There is no PRAN RFL public school math teacher in this district")
                    talk("There is no PRAN RFL public school math teacher in this district")
            elif "junior" in rfl and "teacher" in rfl:
                if "hip" in rfl:
                    print("HIP - Junior Section Teachers ")
                    talk("hip - Junior section teachers ")
                    print("Ms. Apifa Akter")
                    print("Ms. Sultana Begum")
                    print("Ms. Tahmida Haque ")
                    print("Ms. Sirajum Munira tuli")
                    print("Ms. Lutfun Nahar Mukti")
                    print("Suma Sutradhar Sreya")
                    print("Sharna Bashak")
                    talk("Ms. Apifa Akter")
                    talk("Ms. Sultana Begum")
                    talk("Ms. Tahmida Haque ")
                    talk("Ms. Sirajum Munira tuli")
                    talk("Ms. Lutfun Nahar Mukti")
                    talk("Suma Sutradhar Sreya")
                    talk("Sharna Bashak")
                elif "pip" in rfl:
                    print("PIP - Junior Section Teachers")
                    talk("pip - junior section teachers")
                    print("Shalma Siddiqua")
                    print("Tania Akter Rokeya ")
                    print("Ayesha Alieva")
                    print("Naznin Nahar")
                    print("Farhana Akter")
                    print("Shakila Zaman Nipa")
                    print("Selina Begum")
                    print("Umma Kulsum")
                    talk("Shalma Siddiqua")
                    talk("Tania Akter Rokeya ")
                    talk("Ayesha Alieva")
                    talk("Naznin Nahar")
                    talk("Farhana Akter")
                    talk("Shakila Zaman Nipa")
                    talk("Selina Begum")
                    talk("Umma Kulsum")
                elif "danga" in rfl :
                    print("DANGA - Junior Section Teachers")
                    talk("danga - junior section teachers")
                    print("Marufa")
                    print("Chaitaly Paul")
                else:
                    print("There is no PRAN RFL public school junior section teacher in this district")
                    talk("There is no PRAN RFL public school junior section teacher in this district")
            elif "admin" in rfl and "officer" in rfl:  
                if "hip" in rfl:
                    print("Addmin Officer : Mr. Ajoy Krishna")
                    talk("Addmin Officer : Mr. Ajoy Krishna")
                elif "pip" in rfl:
                    print("Addmin Oficer : Muhammad Sharif")
                    talk("Addmin Officer : Muhammad Sharif")
                elif "danga" in rfl:
                    print("Addmin Officer : Tapan Sen")
                    talk("Addmin Officer : Tapan Sen")
                else:
                    print("There is no PRAN RFL public school addmin officer in this district")
                    talk("There is no PRAN RFL public school officer in this district")
            elif "office" in rfl and "assistant" in rfl :
                if "hip" in rfl:
                    print("Office Assistant : Shahin Miah")
                    print("Office Assistant : Laxmi Rani")
                    talk("Office Assistant : Shahin Miah")
                    talk("Office Assistant : Laxmi Rani")
                elif "pip" in rfl :
                    print("Office Assistant : Muhammad Sohel Miah")
                    talk("Office Assistant : Muhammad Sohel miah")
                else:
                    print("There is no PRAN RFL public school Office Assistant in this district")
                    talk("There is no PRAN RFL public school office Assistant in this district")

            elif "service" in rfl and "assistant" in rfl:
                if "hip" in rfl:
                    print("HIP - Service Assistants Name ")
                    talk("HIP - Service Assistants Name")
                    print("Bilkis")
                    print("Fulbashi")
                    print("Luki Rani")
                    print("Joydeb Rishi")
                    talk("Bilkis")
                    talk("Fulbashi")
                    talk("Luki Rani")
                    talk("Joydeb Rishi")
                elif "pip" in rfl:
                    print("PIP - Service Assistants Name")
                    talk("PIP - Service Assistants Name")
                    print("Hajera Begum")
                    print("Kohinur Begum")
                    print("AL-Amin")
                    print("Runa Akter")
                    print("Sabiha Begum")
                    print("Sathi Akter")
                    talk("Hajera Begum")
                    talk("Kohinur Begum")
                    talk("AL-Amin")
                    talk("Runa Akter")
                    talk("Sabiha Begum")
                    talk("Sathi Akter")
                elif "danga" in rfl :
                    print("DANGA - Service Assistants Name")
                    talk("Danga - Service Assistants Name")
                    print("Mitu Akter")
                    print("Sadia")
                    print("Shilpi Akter")
                    talk("Mitu Akter")
                    talk("Sadia")
                    talk("Shilpi Akter")
                else:
                    print("There is no PRAN RFL public school Service Assistant in this district")
                    talk("There is no PRAN RFL public school Service Assistant in this district")
            elif "bus" in rfl :
                if "hip" in rfl:
                    print("HIP - Bus Drivers Name")
                    talk("HIP - Bus Drivers Name")
                    print("Harun Miah")
                    print("Muhammad Shahin")
                    talk("Harun Miah")
                    talk("Muhammad Shahin")
                elif "pip" in rfl:
                    print("PIP - Bus Drivers Name")
                    talk("HIP - Bus Drivers Name")
                    print("Monir Hossain")
                    print("Nur Muhammad")
                    print("Khondokar Iqbal")
                    talk("Monir Hossain")
                    talk("Nur Muhammad")
                    talk("Khondokar Iqbal")
                else:
                    print("There is no PRAN RFL public school Bus Drivers in this district")
                    talk("There is no PRAN RFL public school Bus Drivers in this district")
            elif "bus" in rfl and "helper" in rfl:
                if "hip" in rfl:
                    print("HIP - Bus Helpers Name")
                    talk("HIP - Bus Helpers Name")
                    print("Biswajit Rishi")
                    print("Abu Sayed")
                    talk("Biswajit Rishi")
                    talk("Abu Sayed")
                elif "pip"  in rfl:
                    print("PIP - Bus Helpers Name")
                    talk("PIP - Bus Helpers Name")
                    print("Harun Miah")
                    print("Kamal Hossain")
                    print("Mamun Miah")
                    print("Mithu Miah")
                    talk("Harun Miah")
                    talk("Kamal Hossain")
                    talk("Mamun Miah")
                    talk("Mithu Miah")
                else:
                    print("There is no PRAN RFL public school Bus Helpers in this district")
                    talk("There is no PRAN RFL public school Bus Helpers in the district")
            elif "how" in rfl and "many" in rfl and "students" in rfl:
                if "hip" in rfl:
                    print("Almost 619")
                    talk("Almost 619")
                elif "pip" in rfl:
                    print("Almost 1300")
                    talk("Almost 1300")
                elif "danga" in rfl:
                    print("Almost 185")
                    talk("Almost 185")
                else:
                    print("There is no PRAN RFL public school Students in this district")
                    talk("There is no PRAN RFL public school Students in this district")
            elif "how" in rfl and "many" in rfl and "teachers" in rfl:
                if "hip" in rfl:
                    print("Almost 32")
                    talk("Almost 32")
                elif "pip" in rfl:
                    print("Almost 43")
                    talk("Almost 43")
                elif "danga" in rfl:
                    print("Almost 10")
                    talk("Almost 10")
                else:
                    print("There is no PRAN RFL public school Teachers in this district")
                    talk("There is no PRAN RFL public school Teachers in this district")
            elif "exit" in rfl:
                print('Do you have any more qustion about this topic')
                talk('Do you have any more qustion about this topic')
                yn= input()
                if 'no' in yn or 'No' in yn or 'NO' in yn:
                    break
    elif 'open youtube' in command:
        webbrowser.open('youtube.com')
    elif 'open google' in command:
        webbrowser.open('google.com')
    elif 'how are you' in command:
        print('I am fine . Thank you . I think you are also fine')
        talk('I am fine . Thank you . I think you are also fine')
    elif 'you ' in command and 'beauiful' in command:
        print('WOW,thanks.I think you are beautiful too')
    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)


while True:
    run_siri()
