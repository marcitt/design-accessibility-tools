### Early Experimentation 
Initial experimentation primarily involved working with local models run via ollama (these are more privacy-preserving in comparison to running through APIs), computer vision methods for reasoning with design software.

1. Accessibility Experiments
    - These experiments focused on understanding how to get access to data crucial for accessibility tools
    - Exploring MacOS AX API which enables extraction of GUI elements 
    - Exploration of how to create accessibility overlays 
    - Evaluating the speed of utility tools important to some of the prototyping process (e.g. screenshots for visual reasoning)

2. Audio Experiments
    - Testing different audio sampling & transcription methods 
    - exploring polling vs threading vs streaming etc.
    - Looking at how you can integrate commands / tool-calling with transcription

3. Agent Experiments
    - Testing LLM methods due to their potential to act a command interpretter for accessibility interactions

4. VLM Experiments
    - Tested multimodal LLMs / VLMs and their reasoning capacity with screenshots of design canvases and the wider ecosystem e.g. GUI screenshots

5. GUI Analysis / Computer Vision Experiments
    - Completed as an external project for my Visual Systems Coursework - thoroughly investigated the potential of cv methods to create generalisable tooling for interacting with design software across any OS/application when accessibility data is not provided via an API or other means. 
    - It was found these approaches are quite unreliable and difficult to scale - this contributed towards a pivot towards working more with more structured design data through standard APIs in order to improve user interaction and scalability for this project

5. Figma Experiments
    - This experimentation is more linked to phase 2 where the project shifted away from trying to build more generalisable tools to work across different design softwares to focus more specifically on figma as a case study
    - Looking at Figma API; FigPy Wrapper; Figma Plugins

6. Networking Reference Materials
    - Some boilerplate for setting up basic networking 