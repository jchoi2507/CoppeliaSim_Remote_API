function sysCall_init() 
    forwarder=sim.getObjectHandle('conveyorBeltForwarder')
    proximitySensor = sim.getObjectHandle('Proximity_sensor')
end

function sysCall_cleanup() 
 
end 

function sysCall_actuation() 
    beltVelocity=sim.getScriptSimulationParameter(sim.handle_self,"conveyorBeltVelocity")
    PSensor_distance = sim.readProximitySensor(proximitySensor)
    if (PSensor_distance > 0) then
        beltVelocity = 0

    end
    -- Here we "fake" the transportation pads with a single static rectangle that we dynamically reset
    -- at each simulation pass (while not forgetting to set its initial velocity vector) :
    
    relativeLinearVelocity={beltVelocity,0,0}
    -- Reset the dynamic rectangle from the simulation (it will be removed and added again)
    sim.resetDynamicObject(forwarder)
    -- Compute the absolute velocity vector:
    m=sim.getObjectMatrix(forwarder,-1)
    m[4]=0 -- Make sure the translation component is discarded
    m[8]=0 -- Make sure the translation component is discarded
    m[12]=0 -- Make sure the translation component is discarded
    absoluteLinearVelocity=sim.multiplyVector(m,relativeLinearVelocity)
    -- Now set the initial velocity of the dynamic rectangle:
    sim.setObjectFloatParameter(forwarder,sim.shapefloatparam_init_velocity_x,absoluteLinearVelocity[1])
    sim.setObjectFloatParameter(forwarder,sim.shapefloatparam_init_velocity_y,absoluteLinearVelocity[2])
    sim.setObjectFloatParameter(forwarder,sim.shapefloatparam_init_velocity_z,absoluteLinearVelocity[3])
end 
