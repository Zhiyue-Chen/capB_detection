from jetson.inference import detectNet
from jetson.utils import videoSource, videoOutput
import jetson.inference
import jetson.utils

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource("./dev/2.jpg") # '/dev/video0' for V4L2
display = videoOutput("display://0") # 'my_video.mp4' for file
while display.IsStreaming(): # main loop will go here
    img = camera.Capture() 

    if img is None: # capture timeout
        continue
    else:
        detections = net.Detect(img)

        #
        print(1)                
        print(detections)
        for i in range(len(detections)):
            print(detections[i])
        display.Render(img)
        display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
        break