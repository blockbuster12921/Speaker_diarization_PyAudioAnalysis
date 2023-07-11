from pydub import AudioSegment

audio = AudioSegment.from_wav("sample.wav")

start_time = 0.1
end_time = 1.1
frame_rate = 1000

sliced_audio = audio[start_time * frame_rate : end_time * frame_rate]

print(len(sliced_audio), len(audio), audio.sample_width, audio.frame_rate)

# sliced_audio.export('test.wav', format='wav')