# Test

**LEGACY REMOTE API (not to be confused with b0 Remote API) commands were used**
**SIMULATIONS IN COPPELIA MUST ALREADY BE RUNNING FOR REMOTE API CONNECTION TO WORK**
**sim.py, simConst.py, rempoteApi.dll must all be in workspace directory**
 
 ## PIONEER p3dx ##
The code for the Pioneer p3dx is able to control the speed of the left and right motors, utilize the ultrasonic sensors, and capture images (given that a vision
sensor has been set up in Coppelia).

  ## UR10 robotic arm ##
The code for the UR10 robotic arm is able to control each joint of the robotic arm, based on user input (in degrees that is later converted to radians). The .py script is executable
in any terminal program.

The linear version of the script essentially allows the user to enter a set of coordinates (x, y, z) that the robotic arm will follow. 
Inverse kinematics with tip and target tracing was used. The .py script is executable in any terminal program.

A few notes about the linear version:
- Use Coppelia 4.1--the current 4.2 version doesn't support tip-target inverse kinematics, so an older version was used (older versions of CoppeliaSim can be installed online)
- The scene file (version 4.1) that I used is attached in the repository as a .ttt file--trying to run the angular version will likely cause an error as that code is for 4.2
- For the alpha, beta, gamma inputs in the linear version, set all of them equal to zero

## UR5 robotic arm ##
There are two pick and place scripts: one is for dynamic, respondable cuboids (UR5_Pick_And_Place_4_1.py). The second is for static, non-respondable deep fry baskets (UR5_Deep_Fry_Simulation_4_1.py). In both cases, 'gripping' was emulated
and not actually performed. The UR5_Pick_And_Place_4_1.py has an associated scene, UR5_Cuboids.ttt. The UR5_Deep_Fry_Simulation_4_1.py has an associated scene, UR5_Deep_Fry_Simulation.ttt
