# ccna-Speech-Speed-Analyzer
## Description

ccna-Speech-Speed-Analyzer est un projet qui analyse la vitesse de parole de différents intervenants à partir d'un fichier de transcription. Le code compte le nombre de mots prononcés par chaque locuteur, calcule le temps total de parole de chaque locuteur et détermine la vitesse de parole en mots par minute.

Package permettant d'analyser le débit dans un fichier .txt, ce code est à utiliser en collaboration avec celui ci : https://github.com/lingualab/ccna-automatic-transcription 

## Comment utiliser

Clonez le dépôt sur votre machine locale.

Placez le fichier de transcription dont vous voulez analyser la vitesse de parole dans le dossier input/. Le fichier de transcription doit être au format texte (.txt) et suivre un format spécifique où chaque ligne commence par "SPEAKER" suivi du numéro de l'intervenant et du timestamp, puis du texte prononcé par l'intervenant. Par exemple :

```
SPEAKER 1 0:00:02  
Bonjour, comment ça va ?
SPEAKER 2 0:00:05  
Très bien, merci.
...
END 0:02:00
```
Exécutez le script main.py. Le script lira le fichier de transcription, calculera le nombre de mots, le temps de parole et la vitesse de parole pour chaque intervenant.

Les résultats seront affichés dans la console et également enregistrés dans un fichier CSV dans le dossier result/. Le fichier CSV contiendra les informations suivantes pour chaque intervenant : nombre de mots, temps de parole en secondes et mots par minute.

Contenu du dépôt
fonctions/Speech_Speed_Analyzer.py : Ce fichier contient les fonctions qui calculent le nombre de mots, le temps de parole et la vitesse de parole pour chaque intervenant.

main.py : C'est le script principal qui utilise les fonctions de Speech_Speed_Analyzer.py pour lire le fichier de transcription, calculer les résultats et les enregistrer dans un fichier CSV.

input/ : C'est le dossier où le fichier de transcription à analyser doit être placé.

result/ : C'est le dossier où le fichier CSV avec les résultats de l'analyse est enregistré.

### venv
```
python3 -m venv venv/ccna-Speech-Speed-Analyzer
source venv/ccna-Speech-Speed-Analyzer/bin/activate
```

