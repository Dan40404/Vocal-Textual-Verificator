import speech_recognition as sr


# Créer un objet `Recognizer`
r = sr.Recognizer()
temps = int(input("Combien de temps pour l'écoute -> "))
fichierTxt = input("Nom du fichier du bon texte -> ")

# Utiliser le microphone du casque pour obtenir l'entrée son
with sr.Microphone() as source:
    print("Prêt à écouter ...")
    audio = r.listen(source,phrase_time_limit=temps) # Limiter le temps d'écoute à 5 secondes

# Utiliser le service de reconnaissance vocale de Google pour transcrire le texte
try:
    text = r.recognize_google(audio, language='fr-FR')
    print(f"Vous avez dit : {text}")

    textToVerify = open(fichierTxt+".txt","r",encoding="utf-8").read().replace("\n"," ")
    while "  " in textToVerify:
        textToVerify = textToVerify.replace("  "," ")
    for i in range(len(textToVerify.split(' '))):
        wordToVerify = textToVerify.split(' ')[i].lower()
        try:
            word = text.split(' ')[i].lower()
        except:
            word = "..."

        if word == wordToVerify:
            print("\033[32m" + wordToVerify,end=" ")
        else:
            print("\033[31m" + word + " [" + wordToVerify + "]" ,end=" ")

except StopIteration:
    print("erreur")
