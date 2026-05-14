The `environment.yaml` file includes all the dependencies for these experiments

The majority of this experimentation is derived from:
[Speech Recognition in Python: Complete Voice Processing Guide | TechyOwls](https://techyowls.io/blog/speech-recognition-python-guide/)

## Questions to Answer through these experiments

**Q1: Which sampling methodology works best**
What tools are out there for audio processing + transcription especially for python
Whisper & Google Speech Recognition are the most common

**Q2: Which sampling methodology works best**
Potential options include: 
- Polling
- Threading
- Streaming

## Engineering & Design Decisions

Whisper API vs Local Whisper vs Google Speech Recognition

Consider how the user experience is impacted by these decisions
In most cases having better engineering/performance metrics will improve user experience 

Key metrics:
- Speed - slow audio processing + transcription will impact the whole downstream system and user experience
- Accuracy - if the system does not transcribe properly that creates frustration and users may be required to repeat steps
- Interaction modality - can the users continuously speak to the system or do they need to wait until a certain event has occurred, will the system use push to talk?

## Additional Whisper Resources:
- https://medium.com/@eaniyom/recording-audio-with-python-a-simple-guide-25e0635e8eaf
- https://github.com/collabora/WhisperLive
- https://medium.com/@alexrodriguesj/creating-an-audio-transcription-and-summarization-with-openais-whisper-and-python-860b41dfac8c
- https://www.geeksforgeeks.org/python/build-a-voice-recorder-gui-using-python/
- https://medium.com/@jwcsavage/using-openais-whisper-to-transcribe-real-time-audio-c2ea27f6037f
- https://analyzingalpha.com/openai-whisper-python-tutorial
- https://github.com/davabase/whisper_real_time/blob/master/transcribe_demo.py