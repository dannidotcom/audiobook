from gtts import gTTS

# Fonction pour lire un fichier texte et générer un audio
def text_to_speech(file_path, output_audio):
    try:
        # Charger le texte du fichier
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Vérifier que le texte n'est pas vide
        if not text.strip():
            print("Le fichier est vide. Veuillez fournir un fichier texte avec du contenu.")
            return

        # Convertir le texte en audio avec gTTS
        tts = gTTS(text, lang='fr')  # 'fr' pour le français
        tts.save(output_audio)
        print(f"Livre audio créé avec succès : {output_audio}")
    except FileNotFoundError:
        print(f"Fichier introuvable : {file_path}. Vérifiez le chemin.")
    except Exception as e:
        print(f"Erreur lors de la création de l'audio : {e}")

# Chemin du fichier texte
txt_file = 'book.txt'  # Remplacez par le chemin de votre fichier texte
audio_file = 'livre_audio.mp3'  # Nom du fichier audio de sortie

# Appeler la fonction pour créer le livre audio
text_to_speech(txt_file, audio_file)
