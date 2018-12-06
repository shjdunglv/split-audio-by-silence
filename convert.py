from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import split_on_silence

def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)

song = AudioSegment.from_file("saki.mp4", "mp4")


#split track where silence is 2 seconds or more and get chunks

chunks = split_on_silence(song)
#Process each chunk per requirements
for i, chunk in enumerate(chunks):
    #Create 0.5 seconds silence chunk
    silence_chunk = AudioSegment.silent(duration=0)

    #Add  0.5 sec silence to beginning and end of audio chunk
    audio_chunk = silence_chunk + chunk + silence_chunk

    #Normalize each audio chunk
    normalized_chunk = match_target_amplitude(audio_chunk, -20.0)

    #Export audio chunk with new bitrate
    print("exporting chunk{0}.mp3".format(i) )
    normalized_chunk.export(".//converted/chunk{0}.mp3".format(i), bitrate='192k', format="mp3")