# Important Notes

* Legacy remote API (not to be confused with b0 remote API) commands were used
* Simulations in CoppeliaSim must already be running for remote API connection to work
* sim.py, simConst.py, rempoteApi.dll must all be in workspace directory
* Sphere object is there purely for the purpose of having simRemoteApi.start(19999) in its child script; without that command somewhere in the scene, remote API connection is not possible. The command is not included in the child script of the actual robotic arm for the sake of disabling the object's entire child script.

# For any confusion on:

* [Function parameters](https://www.coppeliarobotics.com/helpFiles/en/remoteApiFunctionsPython.htm)
* [Understanding dynamic simulations](https://www.coppeliarobotics.com/helpFiles/en/designingDynamicSimulations.htm)
* [Remote API connection](https://youtu.be/SQont-mTnfM?t=982)
* [The move_L function](https://youtu.be/CVoV08T0Aqo?t=948)

# Simulated Robots

1. PIONEER p3dx 
  * The code for the Pioneer p3dx is able to control the speed of the left and right motors, utilize the ultrasonic sensors, and capture images (given that a vision
sensor has been set up in Coppelia).

2. UR10 robotic arm 
 * The angular version of the script allows joint control based on user input (in degrees that is later converted to radians). The .py script is executable in any terminal program.

* The linear version of the script essentially allows the user to enter a set of coordinates (x, y, z) that the robotic arm will follow. Inverse kinematics with tip and target tracing was used. The .py script is executable in any terminal program.

* A few notes about the linear version:
- Use Coppelia 4.1--the current 4.2 version doesn't support tip-target inverse kinematics, so an older version was used (older versions of CoppeliaSim can be installed online)
- For the alpha, beta, gamma inputs in the linear version, set all of them equal to zero

3. UR5 robotic arm
* There are two pick and place scripts: one is for dynamic, respondable cuboids (UR5_Pick_And_Place_4_1.py). The second is for static, non-respondable deep fry baskets (UR5_Deep_Fry_Simulation_4_1.py). In both cases, 'gripping' was emulated and not actually performed
* All joints are set to inverse kinematics + hybrid enabled mode
* The gripper is the child object of the UR5_connection object. Contrary to online tutorials, the gripper can remain dynamically ENABLED as long as it's connected to the correct object. See: https://www.coppeliarobotics.com/helpFiles/en/designingDynamicSimulations.htm
* The UR5_Pick_And_Place_4_1.py has an associated scene, UR5_Cuboids.ttt. The UR5_Deep_Fry_Simulation_4_1.py has an associated scene, UR5_Deep_Fry_Simulation.ttt
* The deep fry simulation versions are all controlled through buttons
