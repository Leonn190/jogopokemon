import pygame

pygame.mixer.init()

Sons = {
    "clique": lambda: pygame.mixer.Sound("Audio/Sons/Som1.wav"),
    "Compra": lambda: pygame.mixer.Sound("Audio/Sons/Compra.wav"),
    "Usou": lambda: pygame.mixer.Sound("Audio/Sons/Usou.wav"),
    "Bom": lambda: pygame.mixer.Sound("Audio/Sons/Bom.wav"),
    "Bloq": lambda: pygame.mixer.Sound("Audio/Sons/Bloq.wav"),
    "Falhou": lambda: pygame.mixer.Sound("Audio/Sons/Falhou.wav"),
    "Energia": lambda: pygame.mixer.Sound("Audio/Sons/Energia.wav"),
    "Roletar": lambda: pygame.mixer.Sound("Audio/Sons/Roletar.wav")
}

def tocar(som):
    audio = Sons[som]()
    audio.play()