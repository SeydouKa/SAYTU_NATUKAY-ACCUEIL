import streamlit as st

import tkinter as tk

import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import numpy as np
import tkinter as tk
import ffmpeg

import numpy as np

import pygame
from pydub import AudioSegment
from pydub.playback import play

############## --------- -----------------      PAGE D'ACCEUIL 2 BOUTONS              ------------------------------------------


# Créer une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.geometry("300x300")
fenetre.title("SAYTU NATUKAY")

#Ajouter un son en wolof et francais

# Initialiser Pygame
pygame.init()

# Initialiser Pygame mixer
pygame.mixer.init()

# Charger les fichiers audio
audio = pygame.mixer.Sound("Intro.wav")    
audio.play()


# Ajouter les boutons à la fenêtre
bouton_lecon = tk.Button(fenetre, text="Leçon", bg="white")
bouton_lecon.pack(side="left", padx=10, pady=10, fill="both", expand=True)

bouton_quiz = tk.Button(fenetre, text="Quiz", bg="yellow")
bouton_quiz.pack(side="left", padx=10, pady=10, fill="both", expand=True)

# Démarrer la boucle principale Tkinter
fenetre.mainloop()

