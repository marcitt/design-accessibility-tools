## Benchmarking Analysis

### Preprocessing

For testing cropping:
```
ffplay -vf "crop=in_w-240:in_h-45:0:45" preliminary_benchmarking.mp4
```
```
ffmpeg -i raw_preliminary_benchmarking.mp4 -vf "crop=in_w-240:in_h-45:0:45" -c:v libx264 -crf 18 -vsync cfr -c:a copy preliminary_benchmarking.mp4
```
-crf 18 keeps quality high
`-c:a copy` - audio and video stay in synch

if the original Teams recording has any variable frame rate (VFR) this can caues subtle sync drift over a long file.

For final benchmarking use quicktime player instead


## Benchmarking Task Instructions

==Please make sure you understand the task instructions before starting the task.==
_If you are unsure what a task is asking please as the researcher before starting it - this is important as we are not investigating your understanding of the task but instead how you choose to perform it._

Press next to move to the next task. 
For mouse-based tasks your actions will be timed after your cursor leaves the `next` icon. For trackpad based tasks your actions will be timed after your first trackpad instance.
For voice-based tasks your actions will be timed when you begin speaking.


Here are the instructions for each task (they are also available in the task widget):

Some of these tasks may be frustrating by design. Please try your best to complete them - but not all tasks need to be completed. These will be marked as incomplete attempts. 

Thanks!


**Task 1:** Please zoom in 3 times so that after each zoom the coloured box outline aligns with the viewport outline, please briefly pause before each zoom.

**Task 2:** Please pan to the right 3 times to centre the coloured box on screen after each pan, please briefly pause before each pan.

**Task 3:** Please use a combination of panning and zooming to focus in on one coloured box at a time. After focusing on one box press re-snap to reset the canvas and then focus in on the next box.

**Task 4:** Please click on each box one at a time.

**Task 5:** Please click on each box one at a time.

**Task 6:** Please click on each box one at a time.

**Task 7:** Please multiselect these three boxes (e.g. select all of them at the same time).

**Task 8:** Please multiselect these three boxes (e.g. select all of them at the same time). 

**Task 9:** Please type the text in the specified locations.

**Task 10:** Please create three rectangles to the right of the existing rectangle. They can be any shape or size.

**Task 11:** Please create three rectangles in the specified positions.

**Task 12:** Please create three rectangles in the specified positions.

**Task 12:** Please move the three rectangles to the right into the gaps in the pattern on the left, making sure they are aligned correctly.

**Task 13:** Please drag the three rectangles to increase the sizes to the desired positions

## Training Task Checklist

### Mouse+Keyboard
- [ ] Do you know how to navigate e.g. zoom and pan around in Figma?
- [ ] Do you know how to multiselect objects in Figma? e.g. select more than one object at once?
- [ ] Do you know how to create a rectangle and text using a keyboard shortcut in figma?

### Apple Voice Control

Run training exercises with Mouse Grid 

this includes using basic Mouse Grid
Mouse Grid with shift click for multi-select
Mouse Grid with text command + rectangle command

- [ ] Do you know how to navigate e.g. zoom and pan around in Figma?
- [ ] Do you know how to multiselect objects in Figma? e.g. select more than one object at once?


### LLM Control

Ideal if all commands are made clear through the voice interface - but run a few training exercises