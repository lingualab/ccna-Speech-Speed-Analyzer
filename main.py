import csv
import re
from collections import defaultdict
from datetime import datetime
from fonctions.Speech_Speed_Analyzer import count_words_per_speaker, calculate_speaker_times, calculate_words_per_minute


file_path = 'input/transcript.txt'
word_count = count_words_per_speaker(file_path)
result = calculate_speaker_times(file_path)
words_per_minute = calculate_words_per_minute(word_count, result)

# Affichage des résultats
for speaker, count in word_count.items():
    print(f"Locuteur {speaker}: {count} mots")

for speaker, time in result.items():
    print(f"{speaker} a parlé pendant {time} secondes.")

for speaker, wpm in words_per_minute.items():
    print(f"{speaker} a parlé à une vitesse de {wpm:.2f} mots par minute.")

# Enregistrer les informations dans un fichier CSV
csv_file = 'result/speaker_info.csv'
fieldnames = ['Locuteur', 'Nombre de mots', 'Temps de parole (secondes)', 'Mots par minute']

with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for speaker, count in word_count.items():
        time = round(result[speaker])
        wpm = round(words_per_minute[speaker])
        writer.writerow({'Locuteur': speaker, 'Nombre de mots': count, 'Temps de parole (secondes)': time, 'Mots par minute': wpm})

print(f"Les informations ont été enregistrées dans {csv_file}.")
