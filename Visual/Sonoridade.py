import pygame

pygame.mixer.init()

Sons = {
    "clique": {"Som": lambda: pygame.mixer.Sound("Audio/Sons/Som1.wav"), "Volume": 1},
    "Compra": {"Som": lambda: pygame.mixer.Sound("Audio/Sons/Compra.wav"), "Volume": 1},
    "Usou": {"Som": lambda: pygame.mixer.Sound("Audio/Sons/Usou.wav"), "Volume": 1},
    "Bom": {"Som": lambda: pygame.mixer.Sound("Audio/Sons/Bom.wav"), "Volume": 1},
    "Bloq": {"Som": lambda: pygame.mixer.Sound("Audio/Sons/Bloq.wav"), "Volume": 1},
    "Falhou": {"Som": lambda: pygame.mixer.Sound("Audio/Sons/Falhou.wav"), "Volume": 1},
    "Energia": {"Som": lambda: pygame.mixer.Sound("Audio/Sons/Energia.wav"), "Volume": 1},
    "Roletar": {"Som": lambda: pygame.mixer.Sound("Audio/Sons/Roletar.wav"), "Volume": 1.5},
    "Encaixe": {"Som": lambda: pygame.mixer.Sound("Audio/Sons/Encaixe.wav"), "Volume": 1},
    "Salvou": {"Som": lambda: pygame.mixer.Sound("Audio/Sons/Salvou.wav"), "Volume": 1.7},
    "Clique2": {"Som": lambda: pygame.mixer.Sound("Audio/Sons/Clique2.wav"), "Volume": 1.8},
    "Apagou": {"Som": lambda: pygame.mixer.Sound("Audio/Sons/Apagou.wav"), "Volume": 1.8},
    "Seleciona": {"Som": lambda: pygame.mixer.Sound("Audio/Sons/EscolhaPoke.wav"), "Volume": 0.3},
    "Alvo": {"Som": lambda: pygame.mixer.Sound("Audio/Sons/Alvo.wav"), "Volume": 0.4},
}

def tocar(som):
    audio = Sons[som]["Som"]()
    volume = Sons[som]["Volume"]
    audio.set_volume(min(volume, 1))  # Garante que não passa de 1
    audio.play()
    if volume > 1:
        audio2 = Sons[som]["Som"]()
        audio2.set_volume(min(volume - 1, 1))
        audio2.play()