function sysCall_threadmain()
    -- Put some initialization code here


    -- Put your main loop here, e.g.:
    --
    -- while sim.getSimulationState()~=sim.simulation_advancing_abouttostop do
    --     local p=sim.getObjectPosition(objHandle,-1)
    --     p[1]=p[1]+0.001
    --     sim.setObjectPosition(objHandle,-1,p)
    --     sim.switchThread() -- resume in next simulation step
    -- end
end

function sysCall_cleanup()
    -- Put some clean-up code here
end

local VISIBLE_EDGES = 2
local RESPONDABLE_SHAPE = 8
local tblSize = {0.019, 0.019, 0.019}

while true do
    local hndShape = sim.createPureShape(0, VISIBLE_EDGES + RESPONDABLE_SHAPE, tblSize, 0.1, NULL) -- Creates the pure shape
    sim.setObjectInt32Parameter(hndShape, 10, 0) -- Sets the pure shape as invisible from cameras ONLY, still visible from vision sensor
    sim.setObjectPosition(hndShape, -1, {-1.97, -0.7028, 0.5548}) -- Sets spawn point of shape
    sim.setObjectSpecialProperty(hndShape, sim.objectspecialproperty_detectable_all) -- Makes the object detectable to vision sensor
    sim.wait(10) -- Increase wait time if the cube + basket attachments are spawning too quickly
    
end
