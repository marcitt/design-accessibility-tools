# Creative Visual Design Accessibility Tools
This is the go to location for everything related to digital prototyping for my master's project.

# Main Prototype:
https://github.com/marcitt/figma-voice
Moved to a separate repo to more easily facilitate distribution

# Project Overview

**Goal:** Improve the accessibility of existing 2D Vector-Based design software (e.g. Figma, Adobe Illustrator, Inkscape) using voice (for users with mobility disabilities).

**Focused Specific Goal:** Build a plugin that integrates with Figma to enable voice interaction using ASR for transcription and LLMs for command management.

## Repo Structure

This repo now holds the research/data-collection side of the project. The prototype itself has moved to its own repository: [figma-voice](https://github.com/marcitt/figma-voice).

### 1-Experimentation

Early exploration and dead ends that shaped the pivot toward the Figma Plugin API. See [Prototype README](https://github.com/marcitt/figma-voice) for the tool that resulted from this exploration.

- **Accessibility** — macOS AX API exploration, accessibility overlays, screenshot utility benchmarking
- **Audio** — audio sampling & transcription methods, polling vs threading vs streaming
- **Agents** — LLM-based command interpretation experiments (LangChain, tool calling)
- **VLMs** — multimodal LLM/VLM reasoning over design canvas screenshots
- **Figma** — Figma API exploration, FigPy wrapper, early plugin experiments
- **Networking** — boilerplate networking reference materials

### 2-Interviews

Interviews with experts and assistive technology users - primarily hidden for privacy

### 3-Workflow-Analysis

Analysis of existing design workflows 

### 4-Benchmarking

Benchmarking of different voice tools and interaction modalities against specific design tasks

### 5-Evaluation

Usability study data and analysis — task completion time, SUS, and RTLX across the three evaluated conditions (standard Figma, Apple Voice Control, and the custom plugin). Includes quantitative analysis notebooks.











