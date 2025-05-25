import os
import cv2
import psutil
import time

def ram_disponivel_gb():
    ram_bytes = psutil.virtual_memory().available
    ram_gb = ram_bytes / (1024 ** 3)  # Converte bytes para gigabytes
    return round(ram_gb, 2)

def extrair_frames_video(caminho_video, multiplicador=1, qualidade_jpg=85):
    if not os.path.exists(caminho_video):
        print(f"Vídeo '{caminho_video}' não encontrado.")
        return

    nome_video = os.path.splitext(os.path.basename(caminho_video))[0]
    pasta_destino = os.path.join(os.path.dirname(caminho_video), f"{nome_video}_frames")
    os.makedirs(pasta_destino, exist_ok=True)

    cap = cv2.VideoCapture(caminho_video)
    frame = 1  # Começa em 1 agora

    while True:
        ret, img = cap.read()
        if not ret:
            break

        if multiplicador != 1:
            nova_largura = int(img.shape[1] * multiplicador)
            nova_altura = int(img.shape[0] * multiplicador)
            img = cv2.resize(img, (nova_largura, nova_altura), interpolation=cv2.INTER_LANCZOS4)

        if isinstance(qualidade_jpg, str) and qualidade_jpg.lower() == "png":
            caminho_frame = os.path.join(pasta_destino, f"{frame}.png")
            cv2.imwrite(caminho_frame, img)  # PNG salva sem parâmetros extras
        else:
            caminho_frame = os.path.join(pasta_destino, f"{frame}.jpg")
            cv2.imwrite(caminho_frame, img, [int(cv2.IMWRITE_JPEG_QUALITY), qualidade_jpg])

        frame += 1

    cap.release()
    print(f"{frame - 1} frame(s) extraído(s) de '{caminho_video}' para a pasta '{pasta_destino}'.")

ram = ram_disponivel_gb()

if ram > 8:
    qualidade = 95
else:
    qualidade = 80

extrair_frames_video("imagens/FundosAnimados/VID.mp4", 1, 100)
