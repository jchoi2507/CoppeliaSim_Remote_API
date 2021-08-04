# 🤖 Preface

- Please consider this repository a progression of my journey in robotic simulations, starting with messing around with the p3dx, to IK tip & target tracing with the UR10, and finally a more in-depth pick and place simulation of the UR5 in an industry setting
   - [UR5 Deep Fry Simulation Video v1](https://www.youtube.com/watch?v=A1o8x-pBRHQ)
      - Features:
         - Performs moving, shaking, and returning of up to 2 baskets through inverse kinematics implementation
         - Allows user to select which action to perform
         - Gripper control
   - [UR5 Deep Fry Simulation Video v2](https://www.youtube.com/watch?v=x2EhPGrvZ0g)
      - Improvements:
         - Handles up to 4 baskets
         - Faster simulation runtime, less lag
         - Backend scheduling (via threading) to determine shake time and total number of shakes
         - Improved menu UI and new timer UI that displays type of chicken and status
         - General improvements and additions in the CoppeliaSim scene
   - [UR5 Deep Fry Simulation Video v3](https://www.youtube.com/watch?v=B6eoovQDeW8)
      - Improvements:
         - Speed control of robotic arm (range: 100 mm/s to 100,000 mm/s)
         - Improved menu UI, less clutter
         - Reduced # of unnecessary waypoints
* Legacy remote API (not to be confused with b0 remote API) commands were used
* Simulations in CoppeliaSim must already be running for remote API connection to work
* sim.py, simConst.py, rempoteApi.dll must all be in workspace directory
* Sphere object is there purely for the purpose of having simRemoteApi.start(19999) in its child script; without that command somewhere in the scene, remote API connection is not possible—the command is not included in the child script of the actual robotic arm for the sake of disabling the object's entire child script

# 👨🏻‍💻 Simulated Robots

### PIONEER p3dx 
  * The code for the Pioneer p3dx is able to control the speed of the left and right motors, utilize the ultrasonic sensors, and capture images (given that a vision
sensor has been set up in Coppelia)

### UR10 robotic arm (angular & linear)
 * The angular version of the script allows joint control based on user input (in degrees that is later converted to radians); the .py script is executable in any terminal program

* The linear version of the script essentially allows the user to enter a set of coordinates (x, y, z) that the robotic arm will follow. Inverse kinematics with tip and target tracing was used; the .py script is executable in any terminal program

- A few notes about the linear version:
   - Use Coppelia 4.1--the current 4.2 version doesn't support tip-target inverse kinematics, so an older version was used (older versions of CoppeliaSim can be installed online)
   - For the alpha, beta, gamma inputs in the linear version, set all of them equal to zero

### UR5 robotic arm (pick and place cuboids & pick and place deep fry baskets)
- There are three industry simulations of the UR5 performing pick and place actions
   - External libraries used: tkinter (button interface), threading (multiprocessing), colorama (optional, for terminal output colors)
* All joints are set to inverse kinematics + hybrid enabled mode
* The gripper is the child object of the UR5_connection object. Contrary to online tutorials, the gripper can remain dynamically ENABLED as long as it's connected to the correct object. See: https://www.coppeliarobotics.com/helpFiles/en/designingDynamicSimulations.htm

# ❓ For any confusion on...

### [Function parameters](https://www.coppeliarobotics.com/helpFiles/en/remoteApiFunctionsPython.htm)
- Most, if not all, functions that involve manipulating an object in CoppeliaSim in any way (changing position, velocity, etc, etc.) require obtaining that object's 'handle' with: returnCode, handle = sim.simxGetObjectHandle(clientID, objectName, operationMode)
   - The variable 'handle' is now usable for future function calls from the sim library that require an object's handle
- All parameters for functions in the 'sim' (in earlier versions, this was 'vrep') library can be found at the official documentation link above
- Pretty self-explanatory, only possible confusing parts involve the sim.simx_opmode_blocking/oneshot_wait/streaming
   - Follow documentation recommendations for operation mode parameter, but from personal experience, it is best to try all the suggestions and play around with it to see which one works best

### [Understanding dynamic simulations](https://www.coppeliarobotics.com/helpFiles/en/designingDynamicSimulations.htm)
- Inverse kinematics was used in the 4.1 .py files, which allows for two dummies to be linked as 'tip' and 'target'
   - Moreover, the 'tip' (attached at the flange of the robotic arm) will follow the 'target' by performing IK calculations
   - The method in which the linear positioning programs work is through repositioning the 'target' dummy, thus achieving the effect of the robotic arm moving to a desired coordinate

### [Remote API connection](https://youtu.be/SQont-mTnfM?t=982)
- Why?
   - Remote API connection doesn't require the user to learn/program Lua, but rather in C++, Python, Java, or MATLAB (more commonly known languages)
   - Understanding and establishing remote API connection can not only help understand but also facilitate real-life robot control through these external programs
- Remote API connection allows control of the CoppeliaSim software without actually interacting with the application's interface
   - In this case, Python was used to communicate between CoppeliaSim and a user interface
   - There are online guides for CoppeliaSim remote API connection in MATLAB, C++, and Java
- Certain conditions must be met for remote API connection to work, including:
   - Correct files in workplace directory
   - Correct command in the child script of any object in the scene
   - Simulation already running before executing a Python program
- A newer and more flexible method to utilize remote API was released, the BlueZero interface
   - The b0-based remote API connection utilizes a similar but different library and also requires a resolver to be running
   - Attempting to run the programs in this repository with b0-based software will not work !!

### [The move_L function](https://youtu.be/CVoV08T0Aqo?t=948)
- Credits to Mechatronics Ninja on YT for providing the code for the move_L function in MATLAB which I then translated to Python

### CoppeliaSim Lag
- The CoppeliaSim software is CPU-intensive, so if you're operating on a low/medium-end computer, you can do the following to increase simulation FPS:
   - Decrease the actual window size as small as possible
   - Zoom in to the scene itself as much as possible
   - Refrain from adding any external textures (My Deep Fry v1 video showcases how much lag it can produce...)
   - Remove unnecessary objects/disable unnecessary child scripts

### General questions
- I highly recommend posting a question on the [CoppeliaSim Forums](https://forum.coppeliarobotics.com/) with any Coppelia software-related questions
- It is also suggested to refer to all the hyperlinks above with any general questions about CoppeliaSim/API connection/inverse kinematics/robotic arm movements
