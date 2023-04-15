from controller import Supervisor
import os
import sys

try:
    includePath = os.environ.get("WEBOTS_HOME") + "/projects/samples/robotbenchmark/include"
    includePath.replace('/', os.sep)
    sys.path.append(includePath)
    from robotbenchmark import robotbenchmarkRecord
except ImportError:
    sys.stderr.write("Warning: 'robotbenchmark' module not found.\n")
    sys.exit(0)

robot = Supervisor()

timestep = int(robot.getBasicTimeStep())

l1r2 = robot.getFromDef("L1R2")

translation = l1r2.getField("translation")

running = True
stopMessageSent = False
while robot.step(timestep) != -1:
    t = translation.getSFVec3f()
    if running:
        time = robot.getTime()        
        if ((t[2] > 1.60 and t[2] < 1.75) and (t[0] > 1.26 and t[0] < 1.75)):
            message = "stop"
            running = False
        
        robot.wwiSendText("time:%-24.3f" % time)
    else:  
        if not stopMessageSent:
            robot.wwiSendText("stop")
            stopMessageSent = True
        else:
            message = robot.wwiReceiveText()
            if message:
                if message.startswith("record:"):
                    record = robotbenchmarkRecord(message, "line_following", time)
                    robot.wwiSendText(record)
                    break
                elif message == "exit":
                    break

robot.simulationSetMode(Supervisor.SIMULATION_MODE_PAUSE)
