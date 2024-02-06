# import the necessary modules
import os
import yt_dlp
from datetime import datetime





# creating a folder for the videos
if os.path.isdir('videos') == True:
     os.chdir('videos')
else:
     os.mkdir('videos')
     os.chdir('videos')


cwd = os.getcwd()  # retrieves the current directory (useful for finding out which folder you are operating in)


# asks for video url to be downloaded
url = input('Enter a youtube video link: ')


# select video quality and fps
video_height = input('Enter your prefered resolution. Available are (360 / 480 / 720 / 1080): ')
flickers = input('Enter your prefered fps. Available are (24 / 30 / 60 / 120): ')


# Use options to download
opts = {"trim_file_name": 200, "restrictfilenames":"ASCII","windowsfilenames": "","format": f"((bv*[fps>={flickers}]/bv*)[height<={video_height}]/(wv*[fps>={flickers}]/wv*)) + ba / (b[fps>{flickers}]/b)[height<={video_height}]/(w[fps>={flickers}]/w)"
}



# Start the download with the yt_dlp engine
with yt_dlp.YoutubeDL(opts) as ydl:
    info_dict = ydl.extract_info(url, download=True)
    video_title: str = info_dict.get('title', str)
    extension = info_dict.get('ext', str)
    dur: str = info_dict.get('duration_string', str)
    res: str = info_dict.get('resolution', str)
    upload = info_dict.get('upload_date')
    id = info_dict.get('id')



# function to print out resolution of downloaded video
def resolution(res)-> str:
     try:
          return res.split('x')[-1]
     except:
          AttributeError
          return video_height




# Print success message when download is done
print(f'''
Download complete!
Video name: {video_title +'.'+ extension}
Video location 👉 : {cwd}/{video_title}.{extension}
Video duration: {dur}
Video resolution: {resolution(res)}p ''')


# check the site the video was downloaded from
def source(url):
    site: str = url.lower()
    if 'instagram' in site:
         return 'Source: Instagram'
    elif "youtu" in site:
         return 'Source: Youtube'
    elif 'tiktok' in site:
         return 'Source: Tiktok'
    elif 'facebook'  in site:
         return 'Source: Facebook'
    elif 'likee' in site:
         return 'Source: Likee'
    return 'Source: Other...'


# Print the site as Source
print(f'''
{source(url)}

<---------------------END--------------------->
''')



# log all the links to a text file for debugging
with open('log.txt', 'a', encoding="utf-8") as f:
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write(f"""Video name: {video_title}.{extension}
Video Duration: {dur}
Video Resolution: {resolution(res)}p
Video Location: {cwd}
Video Link: {url}
Date & Time: {date} \n\n""")




