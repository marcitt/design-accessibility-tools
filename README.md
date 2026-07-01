# Creative Visual Design Accessibility Tools
This is the go to location for everything related to digital prototyping for my master's project.

# Main Prototype:
https://github.com/marcitt/figma-voice
Moved to a separate repo to more easily facilitate distribution

## Project Overview

**Goal:** Improve the accessibility of existing 2D Vector-Based design software (e.g. Figma, Adobe Illustrator, Inkscape) using voice (for users with mobility disabilities).

**Focused Specific Goal:** Build a plugin that integrates with Figma to enable voice interaction using ASR for transcription and LLMs for command management.

## Repo Structure



Most up to date prototype ^

### Research
Anything related to empirical studies collecting data -> includes analysing existing design workflows and benchmarking different voice tools for specific tasks


### Early Experimentation 
Initial experimentation primarily involved working with local models run via ollama (these are more privacy-preserving in comparison to running through APIs), computer vision methods for reasoning with design software.

1. [Accessibility Experiments](https://github.com/marcitt/Creative-Visual-Design-Accessibility-Tools/tree/main/Experimentation/Accessibility) 
    - These experiments focused on understanding how to get access to data crucial for accessibility tools
    - Exploring MacOS AX API which enables extraction of GUI elements 
    - Exploration of how to create accessibility overlays 
    - Evaluating the speed of utility tools important to some of the prototyping process (e.g. screenshots for visual reasoning)

2. [Audio Experiments](https://github.com/marcitt/Creative-Visual-Design-Accessibility-Tools/tree/main/Experimentation/Audio)
    - Testing different audio sampling & transcription methods 
    - exploring polling vs threading vs streaming etc.
    - Looking at how you can integrate commands / tool-calling with transcription

3. [Agent Experiments](https://github.com/marcitt/Creative-Visual-Design-Accessibility-Tools/tree/main/Experimentation/Agents)
    - Testing LLM methods due to their potential to act a command interpretter for accessibility interactions

4. [VLM Experiments](https://github.com/marcitt/Creative-Visual-Design-Accessibility-Tools/tree/main/Experimentation/VLMs)
    - Tested multimodal LLMs / VLMs and their reasoning capacity with screenshots of design canvases and the wider ecosystem e.g. GUI screenshots

5. [GUI Analysis / Computer Vision Experiments](https://github.com/marcitt/DVS-Project)
    - Completed as an external project for my Visual Systems Coursework - thoroughly investigated the potential of cv methods to create generalisable tooling for interacting with design software across any OS/application when accessibility data is not provided via an API or other means. 
    - It was found these approaches are quite unreliable and difficult to scale - this contributed towards a pivot towards working more with more structured design data through standard APIs in order to improve user interaction and scalability for this project

5. [Figma Experiments](https://github.com/marcitt/Creative-Visual-Design-Accessibility-Tools/tree/main/Experimentation/Figma)
    - This experimentation is more linked to phase 2 where the project shifted away from trying to build more generalisable tools to work across different design softwares to focus more specifically on figma as a case study
    - Looking at Figma API; FigPy Wrapper; Figma Plugins

6. [Networking Reference Materials](https://github.com/marcitt/Creative-Visual-Design-Accessibility-Tools/tree/main/Experimentation/Networking)
    - Some boilerplate for setting up basic networking 





