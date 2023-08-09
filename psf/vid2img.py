#%% 
# Download image from Youtube
from pytube import YouTube
url = 'https://www.youtube.com/watch?v=JDCvOQo9kBI' # paste your YouTube video url here
youtube = YouTube(url)
stream = youtube.streams.get_highest_resolution()  # gets the highest resolution stream
stream.download(filename='download_vid/raining_man.mp4')

#%%
# Convert video to images
import cv2

# Open the video file
video_file = "download_vid/raining_man.mp4"
cap = cv2.VideoCapture(video_file)

# Get the frames per second (fps) of the video
fps = cap.get(cv2.CAP_PROP_FPS)

timestamps = []
cnt=0
while True:
    cnt=cnt+1
    ret, frame = cap.read()
    if not ret:
        break
    
    # Get the current frame's timestamp in seconds
    current_timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)/1000.0
    timestamps.append(current_timestamp)
    cv2.imwrite("images/images/frame%d.jpg" % cnt, frame)
    if (cnt==200):
        break
    # Display the frame if needed
    # cv2.imshow('Frame', frame)
    
    # Press 'q' to exit the loop
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release the video capture object and close windows
cap.release()
# cv2.destroyAllWindows()
timestamps_file = "images/timestamps.txt"

with open(timestamps_file, "w") as file:
    for timestamp in timestamps:
        file.write(str(timestamp) + "\n")

# %%
