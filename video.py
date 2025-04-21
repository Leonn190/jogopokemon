import os
import cv2

def extrair_frames_video(caminho_video, multiplicador=1):
    if not os.path.exists(caminho_video):
        print(f"Vídeo '{caminho_video}' não encontrado.")
        return

    nome_video = os.path.splitext(os.path.basename(caminho_video))[0]
    pasta_destino = os.path.join(os.path.dirname(caminho_video), f"{nome_video}_frames")
    os.makedirs(pasta_destino, exist_ok=True)

    cap = cv2.VideoCapture(caminho_video)
    frame = 0

    while True:
        ret, img = cap.read()
        if not ret:
            break

        if multiplicador != 1:
            nova_largura = int(img.shape[1] * multiplicador)
            nova_altura = int(img.shape[0] * multiplicador)
            img = cv2.resize(img, (nova_largura, nova_altura), interpolation=cv2.INTER_LANCZOS4)

        caminho_frame = os.path.join(pasta_destino, f"frame_{frame:03}.png")
        cv2.imwrite(caminho_frame, img)
        frame += 1

    cap.release()
    print(f"{frame} frame(s) extraído(s) de '{caminho_video}' para a pasta '{pasta_destino}'.")

# Exemplo de uso:
extrair_frames_video("imagens/FundosAnimados/test2.mp4", multiplicador=1)
