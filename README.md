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
This software module monitors and analyzes the store's entrance/exit point. It counts the number of people entering and leaving the building and the total number of people present in the building at any instance and provides realtime analysis in the form of a GUI. It also sends an email alert if the number of people present in the building at that moment exceeds a given threshold. An excel sheet also gets created at the end of the session which contains some quite useful data that can be used by the administrator for footfall analysis. The administrator can also setup the timer (session's max time limit) and scheduler (automatically starts the session at the scheduled date and time). Output video gets generated and stored permanently on local disk and can be viewed by the admin anytime.

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
> Specify the --input arguement leading to the corresponding path of the prerecorded input video (or) if you wan't to enable webcam specify url=0 in the config file.
> ![EE_terminal](https://user-images.githubusercontent.com/55687431/116130450-dfa9c200-a6e8-11eb-8536-c882f061d043.JPG)
> ___Note:___ Arguements can be manipulated in Main.py as per your convinience

> * ### Config file:
> ![EE_config](https://user-images.githubusercontent.com/55687431/116130607-0f58ca00-a6e9-11eb-9b49-e2c50af74e17.JPG)
> 
> ___Note:___ The config values can be manipulated manually as per your requirements.

> * ### Mailer functionality:
> This functionality can be enabled by specifying the mail id on which you wan't to receive the mail in the config file, setting up the maximum threshold and specifying ___ALERT=True___
> ![entry_exit](https://user-images.githubusercontent.com/55687431/116131272-cf461700-a6e9-11eb-9619-73cc03d3aad7.JPG)
> 
> __As soon as the maximum threshold you specified gets exceeded, you receive the corresponding mail.__
> 
> ![EE_alert](https://user-images.githubusercontent.com/55687431/116131338-e553d780-a6e9-11eb-9d98-181dedef3dce.JPG)

> * ### Log file functionality:
> Set ___Log=True___ in the config file
> ![log_](https://user-images.githubusercontent.com/55687431/116131835-7fb41b00-a6ea-11eb-848b-42bf68c25c2d.JPG)

> * ### Timer functionality:
> Set ___Timer=True___ in config file and change the time limit as per your requirement in Main.py as shown below,
> ![EE_timer](https://user-images.githubusercontent.com/55687431/116132075-bee26c00-a6ea-11eb-9909-b0736a350b89.JPG)

> * ### Scheduler functionality:
> Set ___Schedule=True___ in the config file and then specify the schedule time and date in Main.py as shown below,
> ![EE_schedule](https://user-images.githubusercontent.com/55687431/116132749-868f5d80-a6eb-11eb-9a6b-73672466a05d.JPG)

> * ### Realtime analysis in GUI:
> ![EE_op](https://user-images.githubusercontent.com/55687431/116133087-f0a80280-a6eb-11eb-9a08-3d9595cfee73.JPG)
> 
> ___The above image is just a screenshot of the video being displayed as a GUI in realtime.___

----

# (2) Instore Crowd Analysis:
This software module monitors the crowd inside the store. The admin can specify the ROI limit which indicates the area needed to be monitored for analysis. It detects the movement of people inside those the store, calculates the distances between them, analyzes the people violating social distancing and provides the reults in the form of a GUI to the adminstrator in realtime. The admin also gets an email alert if the total number of people violating social distancing exceeds a given threshold. As in Store Entry/Exit analysis module the admin can set the timer & scheduler and can also access the output video anytime later from the local storage.

> ### Environment used:
* Anaconda
* Jupyter

> ### Packages and dependencies:
* numpy
* pandas
* scipy
* datetime
* schedule
* opencv-python
* jupyter notebook
* ipykernel

> ### Implementation steps:
* Virtual environment setup in anaconda
* Obtaining input video (prerecorded video or webcam)
* Frame differencing and image preprocessing
* Training the YOLO neural network
* Construction of centroid tracking algorithm
* Creating a trackable object
* Implementation of social distance detection algorithm
* Writing output frames to a video file on disk
* Implementing mail alert, timer and scheduler setup and max threshold functionalities

> ## Output of Crowd Analysis module:

> * ### Basic run-time anaconda terminal:
> ![C_terminal](https://user-images.githubusercontent.com/55687431/116143684-1091f300-a6f9-11eb-90f8-d7def372af74.JPG)
> ___Note___: Arguements can be manipulated in ___Main.py___ file inside Instore_Crowd_Analysis folder as per your convinience

> * ### Config file:
> ![C_config](https://user-images.githubusercontent.com/55687431/116144954-471c3d80-a6fa-11eb-9f84-a303d4cb1d09.JPG)
> 
> Note: The config values can be manipulated manually as per your requirements.

> * ### Mailer functionality:
> This functionality can be enabled by specifying the mail id on which you wan't to receive the mail in the config file, setting up the maximum threshold and specifying ___ALERT=True___
> ![C_alert](https://user-images.githubusercontent.com/55687431/116212923-f55bcd80-a762-11eb-9c60-2f44c501af69.JPG)

> * ### GPU available:
> You can enable the GPU in the config file. This will speed up the frames' analysis and subsequently reduces the processing time. (This can only be done if you have CUDA NVIDIA GPU)

> * ### Time and Scheduler:
> Set ___Timer=True___ and/or ___Schedule=True___ in the config file.

> * ### Realtime analysis in GUI:
> ![C_op](https://user-images.githubusercontent.com/55687431/116213984-e32e5f00-a763-11eb-8f5d-717e2c4c0f62.JPG)
> 
> ___The above image is just a screenshot of the video being displayed as a GUI in realtime.___

----

## System Architecture of the software:
![sysArc](https://user-images.githubusercontent.com/55687431/116218425-225eaf00-a768-11eb-8f0d-a09ff347cd35.JPG)

----
