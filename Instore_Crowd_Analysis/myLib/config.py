#=================================================================
#                     MANUAL USER CONFIG SETUP
#=================================================================

# base path to YOLO directory
MODEL_PATH = "model"

# initialize minimum probability to filter weak detections along with the threshold when applying non-maxima suppression
MIN_CONF = 0.3
NMS_THRESH = 0.3

# boolean indicating if NVIDIA CUDA GPU should be used
USE_GPU = False

# define the minimum safe distance (in pixels) that two people can be from each other
MIN_DISTANCE = 70


#Email alert
MAIL = ''       #Enter the mail id on which u wan't to receive the alert, inside the single quotes
ALERT = True
Threshold = 17

# Auto run/Schedule the software to run at your desired time
Scheduler = False

# Auto stop the software after certain a time/hours
Timer = True
