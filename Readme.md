# Speaker Segmentation using pyAudioAnalysis
## Installation
### Install ffmpeg
### Install required Python libraries
Use pip to install requirements.txt
```bash
pip install -r requirements.txt
```

## Run the code for new audio file (python command)
Use the following command to run the Python code.
```bash
python main.py -f Alrajhi_call.wav -n 3 -l False -s saved
```
-f: Input file name (e.g. -f Alrajhi_call.wav)<br>
-n: Number of Speakers (e.g. -n 5)<br>
-l: The parameter to use LDA or not (e.g. -l True (-l False))<br>
-s: Folder to save the segmented audio files (e.g. -s saved)<br>
Note: If -n is 0, then the python module automatically finds the optimal number of speakers and segments audio for that number.

## Run the code for new audio file (jupyter notebook)
Run the main.ipynb file.