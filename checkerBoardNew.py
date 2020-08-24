from __future__ import division
from psychopy import visual, event, core
import numpy as np
import time
# the target frequencies
# we made it align to monitor refreshing rate
freq1 = 8.423
freq2 = 9.374
freq3 = 9.961
freq4 = 10.84
freq5 = 11.79
freq6 = 13.4
freq7 = 14.87

#the position of stimuli, the center of the screen will be [0,0]
pos1 = [64, 128]
pos2 = [-64, 128]
pos3 = [128, 0]
pos4 = [0, 0]
pos5 = [-128, 0]
pos6 = [64, -128]
pos7 = [-64, -128]
posc = [pos1, pos2, pos3, pos4, pos5, pos6, pos7]
posl = [1, 2, 3, 4, 5, 6, 7]


playtime = 20
pausetime = 2
cuetime = 2
sizecheckerboard = (128, 128)
windowsize = [1024, 512]

def getFrame(n, freq):
    phiAngle = ((np.pi/2)+(np.pi/2)*np.sin((2*np.pi*n*(freq/(2*60)))-(np.pi/2)))/np.pi*0.5
    return phiAngle


win = visual.Window(windowsize)

# the generation of stimuli
wedge1 = visual.RadialStim(win, tex='sqrXsqr', color=-1, size=128, pos = pos1, units = 'pix',
    visibleWedge=[0, 360], radialCycles=5, angularCycles=12, interpolate=False,
    autoLog=False)  # this stim changes too much for autologging to be useful
wedge2 = visual.RadialStim(win, tex='sqrXsqr', color=-1, size=128, pos = pos2, units = 'pix',
    visibleWedge=[0, 360], radialCycles=5, angularCycles=12, interpolate=False,
    autoLog=False)  # this stim changes too much for autologging to be useful
wedge3 = visual.RadialStim(win, tex='sqrXsqr', color=-1, size=128, pos = pos3, units = 'pix',
    visibleWedge=[0, 360], radialCycles=5, angularCycles=12, interpolate=False,
    autoLog=False)  # this stim changes too much for autologging to be useful
wedge4 = visual.RadialStim(win, tex='sqrXsqr', color=-1, size=128, pos = pos4, units = 'pix',
    visibleWedge=[0, 360], radialCycles=5, angularCycles=12, interpolate=False,
    autoLog=False)  # this stim changes too much for autologging to be useful
wedge5 = visual.RadialStim(win, tex='sqrXsqr', color=-1, size=128, pos = pos5, units = 'pix',
    visibleWedge=[0, 360], radialCycles=5, angularCycles=12, interpolate=False,
    autoLog=False)  # this stim changes too much for autologging to be useful
wedge6 = visual.RadialStim(win, tex='sqrXsqr', color=-1, size=128, pos = pos6, units = 'pix',
    visibleWedge=[0, 360], radialCycles=5, angularCycles=12, interpolate=False,
    autoLog=False)  # this stim changes too much for autologging to be useful
wedge7 = visual.RadialStim(win, tex='sqrXsqr', color=-1, size=128, pos = pos7, units = 'pix',
    visibleWedge=[0, 360], radialCycles=5, angularCycles=12, interpolate=False,
    autoLog=False)  # this stim changes too much for autologging to be useful

# cover the center of the stimuli to avoid flickering effects
cover1 = visual.Circle(win, color=(0,0,0), size=10, pos = pos1, units = 'pix')  
cover2 = visual.Circle(win, color=(0,0,0), size=10, pos = pos2, units = 'pix')  
cover3 = visual.Circle(win, color=(0,0,0), size=10, pos = pos3, units = 'pix')  
cover4 = visual.Circle(win, color=(0,0,0), size=10, pos = pos4, units = 'pix')  
cover5 = visual.Circle(win, color=(0,0,0), size=10, pos = pos5, units = 'pix')  
cover6 = visual.Circle(win, color=(0,0,0), size=10, pos = pos6, units = 'pix')  
cover7 = visual.Circle(win, color=(0,0,0), size=10, pos = pos7, units = 'pix')  

stimList = [cover1,cover2,cover3,cover4,cover5,cover6,cover7]
screenshot = visual.BufferImageStim(win, stim=stimList)
message = visual.TextStim(win, text='1', height=0.2, color=(0, 1, 0))
# message.setAutoDraw(True)

#press any key to exit this
t0 = time.time()
for j in range(100):

    idx = posl[j]-1
    message.setAutoDraw(True)
    p1 = posc[idx][0]/windowsize[0]*2
    p2 = posc[idx][1]/windowsize[1]*2
    message.pos = (p1, p2)
    win.flip()
    time.sleep(cuetime)
    for i in range(1, playtime*60):
        if not event.getKeys():
            wedge1.radialPhase = getFrame(i, freq1)  
            wedge2.radialPhase = getFrame(i, freq2)  
            wedge3.radialPhase = getFrame(i, freq3)  
            wedge4.radialPhase = getFrame(i, freq4)  
            wedge5.radialPhase = getFrame(i, freq5)
            wedge6.radialPhase = getFrame(i, freq6)
            wedge7.radialPhase = getFrame(i, freq7)
            wedge1.draw()
            wedge2.draw()
            wedge3.draw()
            wedge4.draw()
            wedge5.draw()
            wedge6.draw()
            wedge7.draw()
            cover1.draw()
            cover2.draw()
            cover3.draw()
            cover4.draw()
            cover5.draw()
            cover6.draw()
            cover7.draw()

            win.flip()
        else:
            win.close()
            core.quit()
    message.setAutoDraw(False)
    win.flip()
    time.sleep(pausetime)
# The contents of this file are in the public domain.