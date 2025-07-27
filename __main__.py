import os
import sys
from pathlib import Path
from ytconverter.config import load_local_version as llv

# Allow running as script or module
sys.path.insert(0, str(Path(__file__).parent.parent))

HELP_TEXT = """
  YTConverter - YouTube Downloader CLI Tool

Usage:
  ytconverter -S         Launch the interactive menu and the main script.
  ytconverter -U         Update YTConverter to the latest version via pip.
  ytconverter -v         Show the current installed version.
  ytconverter -h         Show this help message.

Examples:
  ytconverter -S
  ytconverter -U
  ytconverter -v

Upcomig:
  ytconverter <url> -mp3 -b 128, 192,...
  ytconverter <url> -mp4 -r 720, 1080, 4K, ...
  ytconverter <url> -multi_<mp4/mp3>
  ytconverter <url> --playlist
"""

def main():
    if "-U" in sys.argv or "--update" in sys.argv:
        from ytconverter.utils.update import update_self
        update_self()
        sys.exit()

    elif "-v" in sys.argv or "--version" in sys.argv:
        print(f"YTConverter version: {llv()}")
        sys.exit()

    elif "-h" in sys.argv or "--help" in sys.argv:
        print(HELP_TEXT)
        sys.exit()

    elif "-S" in sys.argv or "-s" in sys.argv:
        from ytconverter.cli.menu import main_loop
        main_loop()
    else:
        print(HELP_TEXT)
        sys.exit()
if __name__ == "__main__":
    main()
