# Workflow Analysis Details

## Introduction
The aim of this study is to model vector-based design workflows in order to gain an understanding for what would be required for a voice-based control system specifically for design tasks. 

This study will help with:
- Understanding low-level actions involved in digital design workflows (incl. density, frequency and avg. action times).
- Identifying which low-level actions are most frequently performed and which high-level groupings most frequently appear.

It was found that the process of coding itself helped with building an intuition of what kinds of commands may be required in a voice-based command grammar, as notes and encoded actions may reflect potential voice interactions. 

This exercise aims to subtly highlight how quick all of these actions are when its easy to work with the mouse and keyboard but how time consuming they would be if that was not possible


## Methodology 

The selected methodology involves collecting publicly available YouTube videos which capture live digital desk tasks, using these videos to create a timestamped codebook of actions taken by the designer and then applying this data to derive key statistics.

[Coding Scheme Link](https://github.com/marcitt/Creative-Visual-Design-Accessibility-Tools/blob/main/Research/Workflow%20Analysis/Workflow%20Analysis%20Coding%20Scheme.md)


 For videos
with commentary a purposive sampling approach was used to select video segments
with significantly reduced commentary, but for videos without commentary a random
sampling approach was applied. A thorough explanation of the sampling procedure and
coding process is available through the See the project’s central GitHub Repository.




## Data Collection: Video Sampling Approach

### Search Strategy

A keyword search was performed using YouTube with these search prompts:
```
figma livestream no speaking
figma livestream asmr
figma livestream design asmr
figma real time work livestream design asmr
figma real time 
figma real time livestream
figma vod stream
figma coworking
figma UI challenge
figma lofi work session
figma speed design live
figma speed design livestream
design with me live
Design With Me Live Long Session
```

Key identified creators:
```
DesignCode - 345k Subscribers - Large Quanity of Livestreams
CharliMarieTV - 237k Subscribers - Large Quanity of "Design with me Livestreams" Livestreams 
NAM Design - 33.4k Subscribers- does silent UI design challenges - super useful
Charli Cheung - 31.5k Subscribers
DSCode - 22.9k Subscribers
ASMR Design - 342 Subscribers - but very useful as has no talking 
```

#### Inclusion and Exclusion Criteria

**Criteria**

|Criterion|Rationale|
|---|---|
|The video is not a tutorial demonstration of a specific feature|Aims to capture naturalistic design workflows|
|No cuts or speed-ups within the coded segment|Allows for collecting realistic time-frames|
|No/minimal commentary within the coded segment|This often impacts natural timings|

---

## General Findings / Results / Thoughts

```
Sampled from total footage:
36:17 + 17:28 + 44:43 + 92:07 + (60 + 55:27) + (120 + 57:50) + 25:16 + (60 + 40:56) + (60 + 17:53) + (60 + 19:44)

~ 36 + 17.5 + 44.75 + 92 + 60 + 55.5 + 120 + 58 + 25.25 + 60 + 41 + 60 + 18 + 60 + 19.75
= ~767.75 minutes of footage

Assume around 10% was not workflow footage ~77

Assume total footage ~ 767.76-77 = ~691 minutes = ~ 11.5 hours of footage
```

So around 10 minutes of footage was sampled from 11.5 hours of videos
There were a total of ~400 coded interaction (397 total) and 61 unique actions - saturation of actions began after around 330 actions. Saturation of tags began earlier.


Findings are mostly included in the notes below: 

---
## Notes on Specific Video Samples

This section includes some notes on specific samples including how timeframes/videos were selected but also ==qualitative findings / thoughts that inform design implications and objectives.==

For the first two video samples I began collecting data from the start of the videos - whereas in the other videos data is collected from random positions in the timeline. I thought it was important to have some data on the start of the design process as this can often be a little different from mid sections, which is why I actively included some starting segments in my analysis. For the rest of the data random timeframes were selected as this was important to ensure diverse workflows were sampled.

---

### Sample Workflow 1
Sampled from NAM Design - random sample from UI Speed Design Weekly Challenge (had 38 videos at the time):

```run-python
import random
print(random.randint(1,38))
```
Selected video 6: https://www.youtube.com/watch?v=JkC4o1U5zgM&list=PLfrBp-7QhDqtmJ8oAjYhP6PLQqwDI0z1S&index=6

Skipped to 0:21 for the start of the design interaction. 

**Findings:**
- ==Making mistakes is cheap with mouse and keyboard (often < 1 second for clicking the wrong object).==
- ==In comparision making mistakes with voice is frustrating and significantly slows down the design process and interrupts the design flow (known from prior experience).==
- The longest tasks with mouse and keyboard are often associated with typing text - selecting, dragging and clicking things is usually super quick
- Simultaneous clicking + keyboard shortcut is probably hard with voice - need to check 

---

### Sample Workflow 2
Sampled from ASMR Design - random sample from UI Speed Design Weekly Challenge (had 8 videos at the time):

```run-python
import random
print(random.randint(1,8))
```
Selected video 7: https://www.youtube.com/watch?v=OLb7Rqo1KVQ

---

### Sample Workflow 3
Unit flows - two videos other 15 minutes long
https://www.youtube.com/@unitflows

```run-python
import random
print(random.randint(1,2))
```
Selected video: https://www.youtube.com/watch?v=GfVA26-Z-SE

I started using randomly sampling to select the start time for data collection:
```run-python
import random

def random_timestamp(end="67.02", start="0.00"):
    def to_seconds(t):
        m, s = str(t).split(".")
        return int(m) * 60 + int(s.ljust(2, "0"))
    
    t = random.randint(to_seconds(start), to_seconds(end))
    return f"{t // 60}.{t % 60:02d}"

print(random_timestamp(start="0.54", end="40.00"))
```

Start time = 10.38 - sample from here - moved to 10.36 for first clear action

**Findings:**
- ==Being able to maintain an internal state history may be relevant e.g. if the user wants to say something like "zoom back to the original position" -> this later directly informed design objectives==
- Desired positions will be hard to verbally dictate without some kind of visual support e.g. a grid interface or similar ==-> also informed design objectives==
- Repeated sequences are common which would be time-consuming to replicate with voice - but these can potentially be encoded as a 'macro' or 'function' defined by the user e.g. repeat sequence on object x; or if the software can identify repeated sequences and map them to new objects - e.g. you've already performed this sequence would you like to repeat it?
- hovering is difficult to achieve via voice but is required for some information revealing/wayfinding purposes e.g. finding where a layer is; revealing tooltips etc. 
- clicking on GUI values / updating these values is important - in theory all of these values could be rewritten as voice inputs but that could potentially be quite time consuming -> a more intuitive method would try to take what already exists and make it easier to navigate -> rewriting everything as plaintext.
- lots of actions may not actually be required for a voice tool as they are mistakes/misclicks.
- ==deep select is probably **HARD** for voice since it requires explicit hierarchy knowledge that a mouse user gets visually for free.==

==For users without disabilities many actions can be 'comfort' actions e.g. zooming in and out briefly or deselecting an object and reselecting an object when necessary. These actions are redundancies and not crucial to actual tangible design updates but can help the user with wayfinding. In comparison these actions are extremely costly for users with disabilities - although that does not eliminate the fact that they might actually be desirable - it is hard to know== 

---
### Sample Workflow 4
Selected video 4: https://www.youtube.com/watch?v=k0fbFIAUwfA&t=1052s


Total video length: 1:32:07 ~ 92 minutes (remove 5 minutes ~ 87)
Start time sample: 10:00

```run-python
import random

def random_timestamp(end="87", start="10.00"):
    def to_seconds(t):
        m, s = str(t).split(".")
        return int(m) * 60 + int(s.ljust(2, "0"))
    
    t = random.randint(to_seconds(start), to_seconds(end))
    return f"{t // 60}.{t % 60:02d}"

print(random_timestamp())
```

Start time = 61.28- sample from here

**Findings:**
- ==Need a way to delete objects using voice==

---

### Sample Workflow 5
Selected video 5: https://www.youtube.com/watch?v=ajwuqQDeeG4
The video has 4 seperate work sessions - sample from: 
```
import random
print(random.randint(1,4))
```
Session 1 selected

This video has its own internal timer which is likely to be more accurate e.g. in the case of the video being slightly sped up so that timer will be used instead. These are 25 minute pomodoro timers which are counting down instead of up so the worksheet code had to be adapted for this.

Started from 24:30
Has an interesting segment different to the previous samples

**Findings:**
-	==Moving something to an open space or just kind of relative to a cluster of objects doesn’t require a lot of precision - it's a different kind of action==
-	==Some actions require a lot of alignment grid things==
-	==Some actions would require pixel level precision - but most fit the above==

---

### Sample Workflow 6
https://www.youtube.com/watch?v=Yf00MKUfcIY
Actions start from ~2:23 and end at ~2:53:07
Sample between 2:30-2:50:00 

```run-python
import random

def random_timestamp(end="170.00", start="2.30"):
    def to_seconds(t):
        m, s = str(t).split(".")
        return int(m) * 60 + int(s.ljust(2, "0"))
    
    t = random.randint(to_seconds(start), to_seconds(end))
    return f"{t // 60}.{t % 60:02d}"

print(random_timestamp())
```

94.02 = 134.02

---

### Sample Workflow 7
[Figma Website Design | Yoga & Meditation Instructor Section - YouTube](https://www.youtube.com/watch?v=MR-dH-E5Ais)

Start time: 0:43; end time: 25:16 (remove 3 minutes = 22.16)

```run-python
import random

def random_timestamp(end="22.16", start="0.43"):
    def to_seconds(t):
        m, s = str(t).split(".")
        return int(m) * 60 + int(s.ljust(2, "0"))
    
    t = random.randint(to_seconds(start), to_seconds(end))
    return f"{t // 60}.{t % 60:02d}"

print(random_timestamp())
```
Sample start time: 14.57

---

### Sample Workflow 8
https://www.youtube.com/watch?v=YNxU9YPZRSM&list=PLuCVsS_EScKHdEgqHps_rFxCFX8IpUF8g&index=2
Design UI with me LIVE! UI Design #14 - picked this one beacuse it has some more drawing elements involved which haven't been covered by previous samples (more of a purposive approach)

start time: ~4:00; end time: ~135:00

```run-python
import random

def random_timestamp(end="95.00", start="4.00"):
    def to_seconds(t):
        m, s = str(t).split(".")
        return int(m) * 60 + int(s.ljust(2, "0"))
    
    t = random.randint(to_seconds(start), to_seconds(end))
    return f"{t // 60}.{t % 60:02d}"

print(random_timestamp())
```
Sample start time: 86.56

60 + 26.56 - 1:26:56 - checked its not too much of a speaking section ✅

**Findings**
- This video was more interesting as it had some spline drawing components which was new -> these are probably a bit outside of the project scope at this current time though

---

https://www.youtube.com/watch?v=1m1IqcBaNGg


## Sample Workflow 9
https://www.youtube.com/watch?v=1m1IqcBaNGg

START: 5:15 - 1:10:00 (70 MINS)

```run-python
import random

def random_timestamp(end="70.00", start="5.15"):
    def to_seconds(t):
        m, s = str(t).split(".")
        return int(m) * 60 + int(s.ljust(2, "0"))
    
    t = random.randint(to_seconds(start), to_seconds(end))
    return f"{t // 60}.{t % 60:02d}"

print(random_timestamp())
```

START SAMPLING AT: 29.20 Nope this doesn't have enough meaningful actions try again
TRY THIS START TIME: 55.53 - yep that works fine

**Findings**
- The pace of this design workflow is quite a bit slower than previous ones with less action density. 


## Sample Workflow 10 - incomplete
https://www.youtube.com/watch?v=uz9tPsak9pM&list=PLrJQSKQvgHS73G9sOhMhmWk-JoJZsyPiX


Around 25 mins in starts getting into design properly 
Begins to slow down around 62 mins

```run-python
import random

def random_timestamp(end="62.00", start="25.00"):
    def to_seconds(t):
        m, s = str(t).split(".")
        return int(m) * 60 + int(s.ljust(2, "0"))
    
    t = random.randint(to_seconds(start), to_seconds(end))
    return f"{t // 60}.{t % 60:02d}"

print(random_timestamp())
```

START SAMPLE TIME = 56.32 - started a bit later 57.00 when there is less talking interupting the workflow