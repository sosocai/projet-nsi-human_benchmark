import random
import time

#Les règles du jeu
print("Game's rules: Type the given text correctly within a certain time. If the time's up, you lost!")

#choix de langues
language= input("Choose a language (FR/EN): ")

print("Level information: EASY: 1 minute, NORMAL: 45 seconds,HARD: 30 seconds ")
niveau = input("Choose a level (HARD/NORMAL/EASY):")

if niveau == "HARD":
    temps_maxi = 30
elif niveau == "NORMAL":
    temps_maxi = 45
elif niveau == "EASY":
    temps_maxi = 60
else:
    print("Choose an existing level.")

if language == "FR" :
    #Liste de textes généré par ChatGPT
    mots = ["Les étoiles scintillaient dans le ciel nocturne, créant un spectacle enchanteur pour les observateurs émerveillés.",
            "Le parfum des fleurs printanières emplissait l'air, annonçant l'arrivée imminente de la belle saison.",
            "Les vagues de l'océan se brisaient doucement contre le rivage, apaisant les âmes en quête de sérénité.",
            "Au sommet de la montagne, le vent soufflait avec une force impressionnante, rappelant la puissance de la nature.",
            "Les rires des enfants résonnaient dans le parc, témoignant de leur joie contagieuse.",
            "Les pages du livre tournaient rapidement, captivant le lecteur jusqu'à la dernière ligne.",
            "Le crépuscule enveloppait la ville dans des teintes de rose et d'orange, créant une toile de fond magnifique pour la soirée à venir.",
            "L'odeur alléchante du pain frais sortant du four remplissait la boulangerie, attirant les gourmands.",
            "Les éclats de rire et les conversations animées emplissaient le café, créant une atmosphère chaleureuse et accueillante."]
    
    #Choix du texte à taper
    texte = ""
    for i in range(10):
        texte = random.choice(mots)
    mots_texte = texte.split()
    
    # Afficher le texte à taper
    print(texte)
    
    #démarrer le chrono
    start_time = time.time()
    
    #input
    saisie = input("Tapez le texte : ")
    
    #Liste des erreurs
    erreurs = []
    for mot in saisie.split() :
        if mot not in mots_texte:
            erreurs.append(mot)
    
    # Afficher les erreurs
    if erreurs:
        print("Les erreurs sont :")
        for erreur in erreurs:
            print(erreur)

    
    #Vérifier le timing ou afficher le score
    if time.time() - start_time >= temps_maxi:
        print("Le temps s'est écoulé, vous avez perdu...")
    else:
        score = 10 - len(erreurs)
        if score <=0:
            print("Perdu : vous avez fait trop d'erreurs...")
        elif score ==10:
            print("Bien joué ! 10 / 10")
            
        else:
            print("Votre score est :", score, "/ 10,", "avec", len(erreurs), "erreurs.")
    
elif language == "EN":
    #Liste de textes généré par ChatGPT
    words = ["The stars were twinkling in the night sky, creating an enchanting spectacle for the awe-struck onlookers.",
            "The scent of spring flowers filled the air, heralding the imminent arrival of the beautiful season.",
            "Ocean waves gently broke against the shore, soothing souls in search of serenity.",
            "At the mountain's summit, the wind blew with impressive force, reminding us of nature's power.",
            "Children's laughter echoed in the park, bearing witness to their contagious joy.",
            "The pages of the book turned quickly, captivating the reader until the very last line.",
            "Twilight draped the city in shades of pink and orange, creating a beautiful backdrop for the evening ahead.",
            "The tempting aroma of freshly baked bread wafted from the bakery, drawing in the food enthusiasts.",
            "Peals of laughter and lively conversations filled the cafe, creating a warm and welcoming atmosphere."]
    
    #Choix du texte à taper
    text = ""
    for i in range(10):
        text = random.choice(words)
    words_text = text.split()
    
    # Afficher le texte à taper
    print(text)
    
    #démarrer le chrono
    start_time = time.time()
    
    #input
    input_ = input("Type the text: ")
    
    #Liste des erreurs
    errors = []
    for word in input_.split() :
        if word not in words_text:
            errors.append(word)
    
    # Afficher les erreurs
    if errors:
        print("Les erreurs sont :")
        for error in errors:
            print(error)
    
    #Vérifier le timing ou afficher le score
    if time.time() - start_time >= temps_maxi:
        print("Game over : Time is up.")
    else:
        score = 10 - len(errors)
        if score <=0:
            print("Too much mistakes, Game over...")
        elif score ==10:
            print("GG ! 10/10")
            
        else:
            print("Your final score is:", score, "/ 10,", "with", len(errors), "errors.")
    
else:
    print("Choose a correct language.")