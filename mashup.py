import sys
import os
from yt_funcs import video_voice_only, get_urls
from merge_audio import cut_and_merge


def run_mashup(artist, num_videos, audio_duration, output_file):
    search_keyword = artist
    num_videos = num_videos
    audio_len = audio_duration * 1000
    output_file = output_file

    assert(num_videos > 0), "Number of videos should be greater than 0"
    assert(audio_duration >=20), "Audio duration should be greater than 20 seconds"
    
    urls = get_urls(search_keyword, num_videos)
    audio_files = []
    for url in urls:
        audio_files += video_voice_only(url)
    cut_and_merge(audio_files, output_file, audio_len)
    print(f'Mashup operation completed. Results saved to {output_file}')



if __name__ == "__main__":
    search_keyword = sys.argv[1]
    num_videos = int(sys.argv[2])
    audio_len = int(sys.argv[3])
    output_file = sys.argv[4]
    run_mashup(search_keyword, num_videos, audio_len, output_file)
    
