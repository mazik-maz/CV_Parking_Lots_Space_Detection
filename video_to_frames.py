import cv2
import os

def video_to_frames(video_file, output_dir):
    """
    Extract frames from a video file and save them as images.

    :param video_file: Path to the input video file.
    :param output_dir: Directory where extracted frames will be saved.
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_file)

    # Check if video opened successfully
    if not cap.isOpened():
        print(f"Error opening video file {video_file}")
        return

    frame_number = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break  # No more frames, exit loop

        # Define the filename for each frame
        frame_filename = os.path.join(output_dir, f'frame_{frame_number:06d}.jpg')

        # Save the current frame as an image file
        cv2.imwrite(frame_filename, frame)

        frame_number += 1

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    print(f"Extracted {frame_number} frames to '{output_dir}'.")

if __name__ == "__main__":
    # Example usage
    input_video = 'input_video.mp4'  # Replace with your video file path
    output_folder = 'extracted_frames'  # Replace with your desired output directory
    video_to_frames(input_video, output_folder)
