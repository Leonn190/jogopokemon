from moviepy.editor import VideoFileClip

# Caminho do vídeo original (coloque o nome do seu arquivo aqui)
video = VideoFileClip("meuvideo.mp4")

# Corta do segundo 10 ao 25
video_cortado = video.subclip(10, 25)

# Salva como novo arquivo
video_cortado.write_videofile("video_cortado.mp4", codec="libx264")