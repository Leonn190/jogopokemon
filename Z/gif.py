import os
from PIL import Image

def extrair_gifs_para_frames(pasta_gifs, multiplicador=1.488):
    from PIL import Image
    import os

    # Garante que a pasta existe
    if not os.path.exists(pasta_gifs):
        print(f"Pasta '{pasta_gifs}' não encontrada.")
        return

    for arquivo in os.listdir(pasta_gifs):
        if arquivo.lower().endswith(".gif"):
            caminho_gif = os.path.join(pasta_gifs, arquivo)
            nome_base = os.path.splitext(arquivo)[0]
            pasta_destino = os.path.join(pasta_gifs, f"{nome_base}_frames")

            os.makedirs(pasta_destino, exist_ok=True)

            try:
                img = Image.open(caminho_gif)
                frame = 0
                while True:
                    img.seek(frame)
                    frame_atual = img.convert("RGBA")

                    # Calcula novo tamanho com base no multiplicador
                    largura_original, altura_original = frame_atual.size
                    nova_largura = int(largura_original * multiplicador)
                    nova_altura = int(altura_original * multiplicador)

                    redimensionada = frame_atual.resize((nova_largura, nova_altura), Image.LANCZOS)

                    # Salva o frame
                    caminho_frame = os.path.join(pasta_destino, f"frame_{frame:03}.png")
                    redimensionada.save(caminho_frame)
                    frame += 1
            except EOFError:
                print(f"{arquivo}: {frame} frame(s) extraído(s).")
            except Exception as e:
                print(f"Erro ao processar {arquivo}: {e}")
                
extrair_gifs_para_frames("imagens/Gen 2")
