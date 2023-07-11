from audioSegmentation import speaker_diarization
import argparse
from pydub import AudioSegment
import os

def speakerDiarizationWrapper(inputFile, numSpeakers, useLDA):
    """Returns the list of classes, purity cluster and purity speaker"""
    if useLDA:
        cls, purity_cluster_m, purity_speaker_m, n_speakers = speaker_diarization(inputFile, numSpeakers, lda_dim=5, plot_res=True)
    else:
        cls, purity_cluster_m, purity_speaker_m, n_speakers = speaker_diarization(inputFile, numSpeakers, lda_dim=0, plot_res=True)
    return cls, purity_cluster_m, purity_speaker_m, n_speakers

def sliceAudioSegments(inputFile, numSpeakers, useLDA, save_to):
    """Slices the inputfile into numSpeakers"""
    cls_list, purity_cluster_m, purity_speaker_m, n_speakers = speakerDiarizationWrapper(inputFile, numSpeakers, useLDA)
    input_audio = AudioSegment.from_wav(inputFile)
    min_window = len(input_audio) // len(cls_list)
    
    # Create an empty dictionary
    sliced_audio_dict = {}
    
    # Choose the optimal numSpeakers in case it is not defined
    if numSpeakers <= 0:
        numSpeakers = n_speakers
        print('Optimal number of speakers is ', numSpeakers)
        cls_list, purity_cluster_m, purity_speaker_m, n_speakers = speakerDiarizationWrapper(inputFile, numSpeakers, useLDA)
        
    
    # Iterate over the number of speakers and initialize the slices
    for i in range(numSpeakers):
        sliced_audio_dict[i] = AudioSegment.empty()
        
    input_audio = AudioSegment.from_wav(inputFile)
    # Iterate through the cls and put the audio segments into their classes
    for i in range(len(cls_list)):
        tmp_cls = cls_list[i]
        tmp_slice = input_audio[i * min_window : (i + 1) * min_window - 1]
        for tmp in tmp_slice:
            sliced_audio_dict[tmp_cls] += tmp
            
    # Iterate through sliced_audio_dict and save the result
    os.makedirs(save_to)
    for i in range(numSpeakers):
        sliced_audio_dict[i].export(save_to + '/' + str(i) + '.wav', format='wav')

if __name__ == '__main__':
    # Initialize the argparser    
    parser = argparse.ArgumentParser()
    
    # Add arguments
    parser.add_argument('-f', '--file', help='Path to the input audio file')
    parser.add_argument('-n', '--num', help='number of speakers in the audio file')
    parser.add_argument('-l', '--lda', help='True or false of LDA')
    parser.add_argument('-s', '--saveto', help='Folder to save the segmented files')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Read the input parameters
    inputFile = args.file
    numSpeakers = int(args.num)
    useLDA = args.lda
    save_to = args.saveto
    
    print(inputFile, numSpeakers, useLDA)
    print(type(inputFile), type(numSpeakers), type(useLDA))
    
    # Slice the audio into speaker segments
    sliceAudioSegments(inputFile, numSpeakers, useLDA, save_to)