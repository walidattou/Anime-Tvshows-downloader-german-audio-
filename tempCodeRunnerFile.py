import pysubs2

# Specify the path to the directory containing your video file
video_path = 'D:/animes/Violet-Evergarden/Violet-Evergarden-episode-5.mp4'

# Load the video subtitle using pysubs2 with 'latin1' encoding and specifying format as 'srt'
subs = pysubs2.load(video_path, encoding='latin1', format_='srt')

# Save the subtitles
subs.save('Violet-Evergarden-episode-99.srt')