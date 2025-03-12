import cv2
import os


# extract the video frames
def extract_frames(video_path, output_dir):
    # open the video for reading
    video = cv2.VideoCapture(video_path)

    # Check if the video opened correctly
    if not video.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    # Creates the output directory if it does not already exist
    os.makedirs(output_dir, exist_ok=True)

    # Counter to number the frames
    frame_count = 0

    while True:
        # Read the next frame of the video
        ret, frame = video.read()

        #Checks if the frame was read correctly
        if not ret:
            break

        # Sets the file name to save the frame
        frame_filename = f"{frame_count}.jpg"

        # Sets the full path to save the frame
        frame_path = os.path.join(output_dir, frame_filename)

        # Saves the frame to the output directory
        cv2.imwrite(frame_path, frame)

        #Increments the frame counter
        frame_count += 1

    # Releases used resources
    video.release()
    cv2.destroyAllWindows()


# Path to input video
video_path = "FACE2.mp4"

# Output directory for frames
output_dir = "FRAMES"

# Call the function to extract the frames from the video
extract_frames(video_path, output_dir)
