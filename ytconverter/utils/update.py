import subprocess
import sys

def get_version(package_name):
    try:
        from importlib.metadata import version  # Python 3.8+
        return version(package_name)
    except Exception:
        return "Unknown"

def update_self():
    print("🔄 Updating YTConverter using pip...\n")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "--upgrade", "ytconverter"
        ])
        print("✅ YTConverter successfully updated!\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to update YTConverter: {e}")
        return

    print("🔄 Updating yt-dlp...\n")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"
        ])
        print("✅ yt-dlp successfully updated!\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to update yt-dlp: {e}")
        return

    ytconverter_ver = get_version("ytconverter")
    ytdlp_ver = get_version("yt-dlp")

    print("📦 Installed Versions:")
    print(f"   • ytconverter: {ytconverter_ver}")
    print(f"   • yt-dlp     : {ytdlp_ver}")
    print("\n✨ All updates completed!\n")
