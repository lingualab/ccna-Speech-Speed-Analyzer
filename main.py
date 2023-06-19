import csv
import re
from collections import defaultdict
from datetime import datetime


def count_words_per_speaker(file_path):
    word_count = {}
    speaker = None

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('SPEAKER'):
                speaker = line.split()[1]
                if speaker not in word_count:
                    word_count[speaker] = 0
            else:
                if speaker is not None:  # Vérification de la variable 'speaker'
                    words = line.split()
                    word_count[speaker] += len(words)

    return word_count


def calculate_speaker_times(file_path):
    # Ouvrez le fichier et lisez le contenu
    with open(file_path, 'r') as file:
        text = file.read()

    # Créez un dictionnaire pour stocker les temps de parole de chaque locuteur
    speaker_times = defaultdict(int)

    # Extrayez toutes les lignes commençant par 'SPEAKER' ou 'END'
    speaker_lines = re.findall(r'SPEAKER (\d+)\s+(\d{1,2}:\d{2}:\d{2})', text)

    for i in range(len(speaker_lines) - 1):
        speaker, start_time = speaker_lines[i]
        _, next_start_time = speaker_lines[i + 1]

        # Convertir les temps en objets datetime pour le calcul
        start = datetime.strptime(start_time, '%H:%M:%S')
        next_start = datetime.strptime(next_start_time, '%H:%M:%S')

        # Calculer la durée de parole pour ce segment
        duration = (next_start - start).total_seconds()

        # Ajouter la durée au temps total pour ce locuteur
        speaker_times[speaker] += duration

    # Traiter le dernier locuteur
    if speaker_lines:
        last_speaker, last_start_time = speaker_lines[-1]
        end_time = re.search(r'END (\d{1,2}:\d{2}:\d{2})', text)
        if end_time:
            end = datetime.strptime(end_time.group(1), '%H:%M:%S')
            last_start = datetime.strptime(last_start_time, '%H:%M:%S')
            duration = (end - last_start).total_seconds()
            speaker_times[last_speaker] += duration

    # Retourner les temps de parole pour chaque locuteur
    return speaker_times


file_path = 'input/transcript.txt'
word_count = count_words_per_speaker(file_path)

# Affichage des résultats
for speaker, count in word_count.items():
    print(f"Locuteur {speaker}: {count} mots")

result = calculate_speaker_times(file_path)

# Afficher les temps de parole pour chaque locuteur
for speaker, time in result.items():
    print(f"{speaker} a parlé pendant {time} secondes.")

# Enregistrer les informations dans un fichier CSV
csv_file = 'result/speaker_info.csv'
fieldnames = ['Locuteur', 'Nombre de mots', 'Temps de parole (secondes)']

with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for speaker, count in word_count.items():
        time = round(result[speaker])
        writer.writerow({'Locuteur': speaker, 'Nombre de mots': count, 'Temps de parole (secondes)': time})

print(f"Les informations ont été enregistrées dans {csv_file}.")








