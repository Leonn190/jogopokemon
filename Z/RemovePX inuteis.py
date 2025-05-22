from PIL import Image, ImageOps
import os

def cortar_transparencia(imagem):
    """Remove as áreas totalmente transparentes e ajusta para quadrado."""
    if imagem.mode != 'RGBA':
        imagem = imagem.convert('RGBA')

    bbox = imagem.getbbox()
    if not bbox:
        return imagem  # imagem totalmente transparente

    imagem_cortada = imagem.crop(bbox)
    largura, altura = imagem_cortada.size
    lado = max(largura, altura)

    # Criar novo fundo quadrado transparente
    nova_imagem = Image.new('RGBA', (lado, lado), (0, 0, 0, 0))

    # Centraliza a imagem cortada no quadrado
    pos_x = (lado - largura) // 2
    pos_y = (lado - altura) // 2
    nova_imagem.paste(imagem_cortada, (pos_x, pos_y))

    return nova_imagem

def processar_pasta(caminho_entrada, caminho_saida):
    if not os.path.exists(caminho_saida):
        os.makedirs(caminho_saida)

    for nome_arquivo in os.listdir(caminho_entrada):
        if nome_arquivo.lower().endswith(('.png', '.webp')):
            caminho_img = os.path.join(caminho_entrada, nome_arquivo)
            imagem = Image.open(caminho_img)
            imagem_quadrada = cortar_transparencia(imagem)

            caminho_saida_img = os.path.join(caminho_saida, nome_arquivo)
            imagem_quadrada.save(caminho_saida_img)
            print(f"Processado: {nome_arquivo}")

# Exemplo de uso
entrada = "imagens/pokeicons"
saida = "imagens/pokeiconsrecortados"
processar_pasta(entrada, saida)