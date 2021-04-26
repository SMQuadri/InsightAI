# Realtime-Video-Analytics-in-Retail-stores

> ___Video Analysis___ is the process of automatically analyzing the video using algorithms constructed by training them over deep neural networks to monitor, analyze, manage and detect specific events from large volumes of videos.

> ___Video Analytics in retail stores___ help the retailer to grab useful insights in realtime so that they can enhance customers' shopping experience.
> 
> ![va](https://user-images.githubusercontent.com/55687431/116121850-ab310880-a6de-11eb-9439-6dc4a79cfcc9.jpg)

----

## Project Modules :
* ___Store Entry/Exit Analysis___
* ___Instore Crowd Analysis___

----

# (1) Store Entry/Exit Analysis :

> ### Environment used:
* Anaconda
* Jupyter

> ### Packages and dependencies:
* numpy
* pandas
* scipy
* imutils
* datetime
* schedule
* opencv-python
* dlib (You need to install cmake globally prior to dlib installation)
* jupyter notebook
* ipykernel

> ### Implementation steps:
* Virtual environment setup in anaconda
* Obtaining input video (prerecorded video or webcam)
* Image preprocessing and blob inferencing
* Training the MobileNetSSD neural network
* Construction of centroid tracking algorithm
* Creating a trackable object
* Implementation of people counter
* Writing output frames to a video file on disk
* Implementing people's log file, mail alert, timer and scheduler setup and max threshold functionalities

> ### Features:
* This model is capable of running over both input videos as well as in realtime through webcam or ip-cameras, giving a higher FPS throughput rate than even yolo and r-cnns
* The software user (or) the store administrator can even enable mailer functionality. Doing this, they will receive an email alert if the number of people present in the store exceeds the specified threshold.
* I have also provided a functionality, which on enabling results in the automatic creation of a log file (excel sheet/csv file) at the end of the session, which would be helpful for footfalall analysis.
* The user can also setup the timer upto which the video runs and then stops automatically.
* Keypresses are also captured and are handled correspondingly.
* Video summarization text is displayed on the window.
* Output frames can be written to a video file on local disk for permanent storage(if the user specifies --output arguement during run-time). The output video can be recorded in any supportive format like avi, mkv, mp4v.
* Automatic cleanup work is also done at the end of the session.

> ## Output of Entry/Exit Analysis module:

> * ### Basic run-time anaconda terminal:
> Specify the --input arguement leading to the corresponding path of the prerecorded input video (or) if you wan't to enable webcam Specify url=0 in the config file.
> ![EE_terminal](https://user-images.githubusercontent.com/55687431/116130450-dfa9c200-a6e8-11eb-8536-c882f061d043.JPG)
> Note: Arguements can be manipulated in Main.py as per your convinience

> * ### Config file:
> ![EE_config](https://user-images.githubusercontent.com/55687431/116130607-0f58ca00-a6e9-11eb-9b49-e2c50af74e17.JPG)
> 
> Note: The config values can be manipulated manually as per your requirements.

> * ### Mailer functionality:
> This functionality can be enabled by specifying the mail id on which you wan't to receive the mail in the config file, setting up the maximum threshold and specifying ALERT=True
> ![entry_exit](https://user-images.githubusercontent.com/55687431/116131272-cf461700-a6e9-11eb-9619-73cc03d3aad7.JPG)
> 
> As soon as the maximum threshold you specified gets exceeded, you receive the corresponding mail.
> 
> ![EE_alert](https://user-images.githubusercontent.com/55687431/116131338-e553d780-a6e9-11eb-9d98-181dedef3dce.JPG)

> * ### Log file functionality:
> Set Log=True in the config file
> ![log_](https://user-images.githubusercontent.com/55687431/116131835-7fb41b00-a6ea-11eb-848b-42bf68c25c2d.JPG)

> * ### Timer functionality:
> Set Timer=True in config file and change the time limit as per your requirement in Main.py as shown below,
> ![EE_timer](https://user-images.githubusercontent.com/55687431/116132075-bee26c00-a6ea-11eb-9909-b0736a350b89.JPG)

> * ### Scheduler functionality:
> Set Schedule=True in the config file and then specify the schedule time and date in Main.py as shown below,
> ![EE_schedule](https://user-images.githubusercontent.com/55687431/116132749-868f5d80-a6eb-11eb-9a6b-73672466a05d.JPG)

> * ### Realtime analysis:
> ![EE_op](https://user-images.githubusercontent.com/55687431/116133087-f0a80280-a6eb-11eb-9a08-3d9595cfee73.JPG)
> 
> The above image is just a screenshot of the video being displayed as a GUI in realtime.

----

# (2) Crowd Analysis:

> ### Environment used:
* Anaconda
* Jupyter

> ### Packages and dependencies:
* numpy
* pandas
* scipy
* imutils
* datetime
* schedule
* opencv-python
* dlib (You need to install cmake globally prior to dlib installation)
* jupyter notebook
* ipykernel

> ### Implementation steps:
* Virtual environment setup in anaconda
* Obtaining input video (prerecorded video or webcam)
* Image preprocessing and blob inferencing
* Training the MobileNetSSD neural network
* Construction of centroid tracking algorithm
* Creating a trackable object
* Implementation of people counter
* Writing output frames to a video file on disk
* Implementing people's log file, mail alert, timer and scheduler setup and max threshold functionalities
