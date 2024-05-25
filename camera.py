import cv2
import os
import time
def capture_images(camera_index=0, save_folder="captured_images"):
  """
  Captures images from the specified camera and saves them to a folder.

  Args:
      camera_index (int, optional): The index of the camera to use. Defaults to 0 (internal camera).
      save_folder (str, optional): The folder to save the captured images. Defaults to "captured_images".

  Returns:
      None
  """

  # Create the folder if it doesn't exist
  if not os.path.exists(save_folder):
    os.makedirs(save_folder)
    print(f"Created directory: {save_folder}")  # Debug message

  # Open the video capture object
  cap = cv2.VideoCapture(camera_index)

  # Check if camera opened successfully
  if not cap.isOpened():
    print("Error opening camera!")
    return

  # Set image width and height (optional, adjust as needed)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

  frame_count = 0
  while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    time.sleep(1)
    if not ret:
      print("Failed to capture frame!")
      break

    # Display the resulting frame
    cv2.imshow('Camera', frame)


    filename = os.path.join(save_folder, f"image_{frame_count}.jpg")
    print(f"Saving image to: {filename}")  # Debug message
    success = cv2.imwrite(filename, frame)
    if success:
        print("Image captured and saved successfully!")
    else:
        print("Error saving image!")
    frame_count += 1

    # Press 'q' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
      break

  # When everything is done, release the capture and close all windows
  cap.release()
  cv2.destroyAllWindows()

# Try opening internal camera first
capture_images()

# If internal camera fails, try external camera (assuming index 1)
if not cv2.VideoCapture(0).isOpened():
  print("Internal camera not found. Trying external camera...")
  capture_images(camera_index=1)
