from PIL import Image
import numpy as np
import os

def similaridade_pixels_iguais(pasta, limiar=5):
    arquivos = sorted([f for f in os.listdir(pasta) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    if len(arquivos) == 0:
        print("Pasta vazia ou sem arquivos de imagem.")
        return

    # Carrega o frame 0
    path_frame0 = os.path.join(pasta, arquivos[0])
    img0 = np.array(Image.open(path_frame0)).astype(np.int16)

    print(f"Comparando todos os frames com {arquivos[0]}:")

    total_pixels = img0.shape[0] * img0.shape[1]

    for arquivo in arquivos:
        path_atual = os.path.join(pasta, arquivo)
        img = np.array(Image.open(path_atual)).astype(np.int16)

        if img.shape != img0.shape:
            print(f"{arquivo}: tamanho diferente, pulando...")
            continue

        # Calcula a diferença absoluta por canal
        diff = np.abs(img0 - img)

        # Verifica pixels onde todas as diferenças dos canais estão abaixo do limiar
        pixels_similares = np.all(diff <= limiar, axis=2)

        # Conta pixels semelhantes
        count_similares = np.sum(pixels_similares)

        # % pixels semelhantes
        porcentagem_similaridade = (count_similares / total_pixels) * 100

        print(f"{arquivo}: {porcentagem_similaridade:.2f}% pixels praticamente iguais ao frame 0")

# Uso:
similaridade_pixels_iguais("imagens/FundosAnimados/fundovid_frames")