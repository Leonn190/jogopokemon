from PIL import Image
import os

# def extrair_todos_gifs(pasta_gifs, pasta_saida_base):
#     # Cria a pasta de saída principal se não existir
#     os.makedirs(pasta_saida_base, exist_ok=True)

#     # Lista todos os arquivos .gif na pasta de GIFs
#     arquivos = [f for f in os.listdir(pasta_gifs) if f.lower().endswith(".gif")]

#     for arquivo in arquivos:
#         caminho_gif = os.path.join(pasta_gifs, arquivo)
#         nome_base = os.path.splitext(arquivo)[0]
        
#         # Cria a pasta de saída com o nome do GIF seguido de _frames
#         pasta_saida = os.path.join(pasta_saida_base, nome_base + "_frames")
#         os.makedirs(pasta_saida, exist_ok=True)

#         try:
#             # Abre o arquivo GIF
#             gif = Image.open(caminho_gif)
#             frame = 0

#             while True:
#                 # Tenta acessar cada frame do GIF
#                 gif.seek(frame)
#                 gif_frame = gif.convert("RGBA")
                
#                 # Salva cada frame como um arquivo PNG
#                 gif_frame.save(os.path.join(pasta_saida, f"frame_{frame}.png"))
#                 frame += 1

#         except EOFError:
#             # Fim dos frames
#             print(f"✔️ {arquivo} convertido em {frame} frame(s).")
#         except Exception as e:
#             # Se ocorrer algum erro durante a extração
#             print(f"❌ Erro ao processar {arquivo}: {e}")

# # Exemplo de uso
# pasta_com_gifs = "imagens/gifs/roger"            # Caminho da pasta com os gifs
# pasta_dos_frames = "imagens/gifs/FRA"  # Caminho onde os frames serão salvos
# extrair_todos_gifs(pasta_com_gifs, pasta_dos_frames)

def redimensionar_frames(pasta_frames_base, fator_redimensionamento=1.54166666667):
    for pasta_gif in os.listdir(pasta_frames_base):
        pasta_gif_path = os.path.join(pasta_frames_base, pasta_gif)
        
        if os.path.isdir(pasta_gif_path):
            for arquivo in os.listdir(pasta_gif_path):
                if arquivo.lower().endswith(".png"):
                    caminho_frame = os.path.join(pasta_gif_path, arquivo)
                    
                    try:
                        imagem = Image.open(caminho_frame)
                        largura, altura = imagem.size
                        novo_largura = int(largura * fator_redimensionamento)
                        novo_altura = int(altura * fator_redimensionamento)

                        # Usa o novo método para redimensionar
                        imagem_redimensionada = imagem.resize(
                            (novo_largura, novo_altura), 
                            resample=Image.Resampling.LANCZOS
                        )

                        imagem_redimensionada.save(caminho_frame)
                        print(f"✔️ {arquivo} redimensionado para {novo_largura}x{novo_altura}.")
                    except Exception as e:
                        print(f"❌ Erro ao redimensionar {arquivo}: {e}")

# Exemplo de uso
pasta_dos_frames = "frames_extraidos"
redimensionar_frames(pasta_dos_frames)
