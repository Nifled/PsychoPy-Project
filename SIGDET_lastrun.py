#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on October 31, 2016, at 22:50
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'SIGDET'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\Erick\\Desktop\\expPY\\SIGDET.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instructions1"
Instructions1Clock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='Welcome to the computer portion of this experiment.\n\nPlease position your index fingers on the "v" and "m" keys as you will only be using these buttons for this experiment.\n\n\nThe computer portion of this experiment lasts approximately 15 minutes and is composed of 3 blocks separated by brief breaks.\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
Cont = visual.TextStim(win=win, name='Cont',
    text='Please press a button  to continue.',
    font='Arial',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Instructions2"
Instructions2Clock = core.Clock()
Instrucciones = visual.TextStim(win=win, name='Instrucciones',
    text="In this experiment you will be presented with either a face with a BIG mouth, or a face with a LITTLE mouth.  You will see them one at a time. \n\nYour task will be to decide whether a BIG or LITTLE mouth was presented by pushing the correct button as quickly and accurately as possible.\n\n The 'v' key will be used to identify the [VStimType] mouth and the 'm' key will be used to identify the [MStimType] mouth.  Examples of what the mouth sizes look like are below:\n",
    font='Arial',
    pos=(0,0), height=0.080, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
LongMouth = visual.ImageStim(
    win=win, name='LongMouth',
    image='caras\\long_mouth.bmp', mask=None,
    ori=0, pos=(-.5,-.6), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
SmallMouth = visual.ImageStim(
    win=win, name='SmallMouth',
    image='caras\\short_mouth.bmp', mask=None,
    ori=0, pos=(.5,-.6), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
BigM = visual.TextStim(win=win, name='BigM',
    text="Big Mouth 'v'",
    font='Arial',
    units='cm', pos=(-10,-9), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
LittleM = visual.TextStim(win=win, name='LittleM',
    text="Little Mouth 'm'",
    font='Arial',
    pos=(.5,-.8), height=.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
Continue = visual.TextStim(win=win, name='Continue',
    text='Please press a button  to continue.',
    font='Arial',
    pos=(0, -.9), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);

# Initialize components for Routine "Instructions_3"
Instructions_3Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Now, let\'s take a practice run. You will see a fixation cross, "+", on the screen.  You should always focus your attention on the fixation cross as this will help you identify the mouth as quickly and accurately as possible.  The fixation cross will be followed by a face with a BIG or a LITTLE mouth. Remember, if you think the mouth is [VStimType], press the \'v\' key.  If you think the mouth is [MStimType], press the \'m\' key.  \n\n\n\nIf you understand these directions and are ready to proceed to the practice round, please press a button.\n',
    font='Arial',
    pos=(0, 0), height=0.080, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
crosshair = visual.TextStim(win=win, name='crosshair',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
Eyes_nose_only = visual.ImageStim(
    win=win, name='Eyes_nose_only',
    image=u'caras\\eyes_nose_only.bmp', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Stimulis = visual.ImageStim(
    win=win, name='Stimulis',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Eyes_nose_only2 = visual.ImageStim(
    win=win, name='Eyes_nose_only2',
    image=u'caras\\eyes_nose_only.bmp', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)


# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
expClock = core.Clock()
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions1"-------
t = 0
Instructions1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
End = event.BuilderKeyResponse()
# keep track of which components have finished
Instructions1Components = [Instructions, End, Cont]
for thisComponent in Instructions1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions1"-------
while continueRoutine:
    # get current time
    t = Instructions1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if t >= 0.0 and Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions.tStart = t
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.setAutoDraw(True)
    
    # *End* updates
    if t >= 0.0 and End.status == NOT_STARTED:
        # keep track of start time/frame for later
        End.tStart = t
        End.frameNStart = frameN  # exact frame index
        End.status = STARTED
        # keyboard checking is just starting
        End.clock.reset()  # now t=0
    if End.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            End.keys = theseKeys[-1]  # just the last key pressed
            End.rt = End.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *Cont* updates
    if t >= 0.0 and Cont.status == NOT_STARTED:
        # keep track of start time/frame for later
        Cont.tStart = t
        Cont.frameNStart = frameN  # exact frame index
        Cont.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions1"-------
for thisComponent in Instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if End.keys in ['', [], None]:  # No response was made
    End.keys=None
thisExp.addData('End.keys',End.keys)
if End.keys != None:  # we had a response
    thisExp.addData('End.rt', End.rt)
thisExp.nextEntry()
# the Routine "Instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions2"-------
t = 0
Instructions2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
Instructions2Components = [Instrucciones, key_resp_2, LongMouth, SmallMouth, BigM, LittleM, Continue]
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions2"-------
while continueRoutine:
    # get current time
    t = Instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instrucciones* updates
    if t >= 0.0 and Instrucciones.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instrucciones.tStart = t
        Instrucciones.frameNStart = frameN  # exact frame index
        Instrucciones.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *LongMouth* updates
    if t >= 0.0 and LongMouth.status == NOT_STARTED:
        # keep track of start time/frame for later
        LongMouth.tStart = t
        LongMouth.frameNStart = frameN  # exact frame index
        LongMouth.setAutoDraw(True)
    
    # *SmallMouth* updates
    if t >= 0.0 and SmallMouth.status == NOT_STARTED:
        # keep track of start time/frame for later
        SmallMouth.tStart = t
        SmallMouth.frameNStart = frameN  # exact frame index
        SmallMouth.setAutoDraw(True)
    
    # *BigM* updates
    if t >= 0.0 and BigM.status == NOT_STARTED:
        # keep track of start time/frame for later
        BigM.tStart = t
        BigM.frameNStart = frameN  # exact frame index
        BigM.setAutoDraw(True)
    
    # *LittleM* updates
    if t >= 0.0 and LittleM.status == NOT_STARTED:
        # keep track of start time/frame for later
        LittleM.tStart = t
        LittleM.frameNStart = frameN  # exact frame index
        LittleM.setAutoDraw(True)
    
    # *Continue* updates
    if t >= 0.0 and Continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        Continue.tStart = t
        Continue.frameNStart = frameN  # exact frame index
        Continue.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions2"-------
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions_3"-------
t = 0
Instructions_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
Instructions_3Components = [text_2, key_resp_3]
for thisComponent in Instructions_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions_3"-------
while continueRoutine:
    # get current time
    t = Instructions_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_3"-------
for thisComponent in Instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "Instructions_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SIGDETExample.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "Practice"-------
    t = 0
    PracticeClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.400000)
    # update component parameters for each repeat
    Stimulis.setImage(Stim)
    res = event.BuilderKeyResponse()
    #if resp.corr: 
    #    msg="Correct! You won 5 cents!" 
    #else: 
    #    msg="Incorrect! You won nothing!" 
    # keep track of which components have finished
    PracticeComponents = [crosshair, Eyes_nose_only, Stimulis, res, Eyes_nose_only2]
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PracticeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crosshair* updates
        if t >= 0.0 and crosshair.status == NOT_STARTED:
            # keep track of start time/frame for later
            crosshair.tStart = t
            crosshair.frameNStart = frameN  # exact frame index
            crosshair.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if crosshair.status == STARTED and t >= frameRemains:
            crosshair.setAutoDraw(False)
        
        # *Eyes_nose_only* updates
        if t >= 1 and Eyes_nose_only.status == NOT_STARTED:
            # keep track of start time/frame for later
            Eyes_nose_only.tStart = t
            Eyes_nose_only.frameNStart = frameN  # exact frame index
            Eyes_nose_only.setAutoDraw(True)
        frameRemains = 1 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Eyes_nose_only.status == STARTED and t >= frameRemains:
            Eyes_nose_only.setAutoDraw(False)
        
        # *Stimulis* updates
        if t >= 1.5 and Stimulis.status == NOT_STARTED:
            # keep track of start time/frame for later
            Stimulis.tStart = t
            Stimulis.frameNStart = frameN  # exact frame index
            Stimulis.setAutoDraw(True)
        frameRemains = 1.5 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Stimulis.status == STARTED and t >= frameRemains:
            Stimulis.setAutoDraw(False)
        
        # *res* updates
        if t >= 1.6 and res.status == NOT_STARTED:
            # keep track of start time/frame for later
            res.tStart = t
            res.frameNStart = frameN  # exact frame index
            res.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(res.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 1.6 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if res.status == STARTED and t >= frameRemains:
            res.status = STOPPED
        if res.status == STARTED:
            theseKeys = event.getKeys(keyList=['m', 'v'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                res.keys = theseKeys[-1]  # just the last key pressed
                res.rt = res.clock.getTime()
                # was this 'correct'?
                if (res.keys == str(corAns)) or (res.keys == corAns):
                    res.corr = 1
                else:
                    res.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Eyes_nose_only2* updates
        if t >= 2.4 and Eyes_nose_only2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Eyes_nose_only2.tStart = t
            Eyes_nose_only2.frameNStart = frameN  # exact frame index
            Eyes_nose_only2.setAutoDraw(True)
        frameRemains = 2.4 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Eyes_nose_only2.status == STARTED and t >= frameRemains:
            Eyes_nose_only2.setAutoDraw(False)
        
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice"-------
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if res.keys in ['', [], None]:  # No response was made
        res.keys=None
        # was no response the correct answer?!
        if str(corAns).lower() == 'none':
           res.corr = 1  # correct non-response
        else:
           res.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('res.keys',res.keys)
    trials.addData('res.corr', res.corr)
    if res.keys != None:  # we had a response
        trials.addData('res.rt', res.rt)
    
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials'


# ------Prepare to start Routine "feedback"-------
t = 0
feedbackClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
msg = "Thanks for participating - that took %.2f minutes in total" %(expClock.getTime()/60.0)
feedback_text.setText(msg)
# keep track of which components have finished
feedbackComponents = [feedback_text]
for thisComponent in feedbackComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "feedback"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = feedbackClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *feedback_text* updates
    if t >= 0.0 and feedback_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        feedback_text.tStart = t
        feedback_text.frameNStart = frameN  # exact frame index
        feedback_text.setAutoDraw(True)
    frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if feedback_text.status == STARTED and t >= frameRemains:
        feedback_text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback"-------
for thisComponent in feedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
