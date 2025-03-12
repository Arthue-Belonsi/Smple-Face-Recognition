import cv2
import os


# Função para extrair e salvar os frames do vídeo
def extract_frames(video_path, output_dir):
    # Abre o vídeo para leitura
    video = cv2.VideoCapture(video_path)

    # Verifica se o vídeo foi aberto corretamente
    if not video.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    # Cria o diretório de saída, se ainda não existir
    os.makedirs(output_dir, exist_ok=True)

    # Contador para numerar os frames
    frame_count = 0

    while True:
        # Lê o próximo frame do vídeo
        ret, frame = video.read()

        # Verifica se o frame foi lido corretamente
        if not ret:
            break

        # Define o nome do arquivo para salvar o frame
        frame_filename = f"{frame_count}.jpg"

        # Define o caminho completo para salvar o frame
        frame_path = os.path.join(output_dir, frame_filename)

        # Salva o frame no diretório de saída
        cv2.imwrite(frame_path, frame)

        # Incrementa o contador de frames
        frame_count += 1

    # Libera os recursos utilizados
    video.release()
    cv2.destroyAllWindows()


# Caminho para o vídeo de entrada
video_path = "FACE2.mp4"

# Diretório de saída para os frames
output_dir = "FRAMES"

# Chama a função para extrair os frames do vídeo
extract_frames(video_path, output_dir)
