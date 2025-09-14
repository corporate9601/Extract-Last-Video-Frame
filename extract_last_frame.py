import cv2
import os
import sys

# Supported video extensions
SUPPORTED_EXTENSIONS = ('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm')

def extract_last_frame(video_path):
    # Check if file exists
    if not os.path.isfile(video_path):
        print(f"Error: File '{video_path}' not found.")
        return False
    
    # Open video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return False
    
    # Get total frames and last frame position
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if total_frames == 0:
        print("Error: Video has no frames.")
        cap.release()
        return False
    
    # Set position to last frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 1)
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read last frame.")
        cap.release()
        return False
    
    # Create output directory if it doesn't exist
    os.makedirs('output', exist_ok=True)
    
    # Generate output filename
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    output_path = os.path.join('output', base_name + '.png')
    
    # Save frame as PNG
    success = cv2.imwrite(output_path, frame)
    
    if success:
        print(f"Successfully saved last frame to: {output_path}")
    else:
        print("Error: Failed to save image.")
    
    cap.release()
    return success

def main():
    while True:
        # Get input from user
        video_input = input("\nEnter video filename or path (or 'quit' to exit): ").strip()
        
        if video_input.lower() == 'quit':
            break
        
        if not video_input:
            continue
        
        # Process the input
        extract_last_frame(video_input)

if __name__ == "__main__":
    main()
