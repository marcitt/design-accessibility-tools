# Figma Plugin to Support Controlled Benchmarking

This plugin was specifically designed for my benchmarking/test tasks in Figma. Links to a specific set of design task and enables the viewport to snap to a precise position to ensure any user testing is controlled. This is important as the viewport will effect the relative sizes of objects which can either indirectly or directly influence interaction patterns. 

This can be adapted to any other tasks by adapting the task list in `code.js`


## Setup

- Benchmark frames are named benchmark-1, benchmark-2, etc. in Figma
- Each frame must have the same aspect ratio as your Figma window (1470 × 880px recommended)
- Load the plugin via Plugins -> Development -> Import plugin from manifest

The plugin counts frames matching the benchmark-n format automatically 


## Usage
- On open, the plugin automatically snaps to benchmark-1
- Tasks can be navigated between using `Back` or `Next Task` or the current frame can be 're-snapped\ using `Re-snap` which is useful if we want to reset a task


## Notes and References
Claude Sonnet 4.6 was used to generate and iterate on the plugin code, including the viewport snap logic, frame detection, and UI. The plugin was designed to ensure benchmarking tasks are presented consistently across participants, with a controlled starting viewport for each task.