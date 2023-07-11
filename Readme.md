# Speaker Segmentation using pyAudioAnalysis
## Installation
### Install ffmpeg
### Install required Python libraries
Use pip to install requirements.txt
```bash
pip install -r requirements.txt
```

## Run the code for new audio file
Use the following command to run the Python code.
```bash
python main.py -f Alrajhi_call.wav -n 3 -l False -s saved
```
-f: Input file name (e.g. -f Alrajhi_call.wav)
-n: Number of Speakers (e.g. -n 5)
-l: The parameter to use LDA or not (e.g. -l True (-l False))
-s: Folder to save the segmented audio files (e.g. -s saved)