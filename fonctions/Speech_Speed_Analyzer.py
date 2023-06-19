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


def calculate_words_per_minute(word_count, speaker_times):
    words_per_minute = {}

    for speaker, count in word_count.items():
        if speaker in speaker_times and speaker_times[speaker] > 0:
            time_in_minutes = speaker_times[speaker] / 60
            words_per_minute[speaker] = count / time_in_minutes

    return words_per_minute