import os
import sys
from pathlib import Path

from ytconverter.cli.banner import print_banner, des4
from ytconverter.config import load_local_version, save_user_data
from ytconverter.core.bootstrap import ensure_dependencies, setup_termux_storage
from ytconverter.utils.update import update_self
from ytconverter.core.version import check_version
from ytconverter.downloaders import multi_mp3, multi_mp4, single_mp3, single_mp4
from ytconverter.utils.styling import apply_style

ensure_dependencies()
setup_termux_storage()

# Version check
local, remote = check_version()
if remote and local != remote:
    print(
        apply_style("\nA new version for the tool is available!\n", "/cyan/bold")
        + f"Current: v{local}, Latest: v{remote}\n"
    )
    choice = input(
        apply_style("Update automatically? (y/n): ", "/cyan/bold")
    ).lower()
    if choice in {"y", ""}:
        update_self()
        exit()

# First-run data collection
from ytconverter.config import load_user_data as _lud

def user_data_collect(name_lud, num_lud):
 if name_lud is None:
     import getpass

     notice_text = apply_style("IMPORTANT NOTICE", "/red/bold")
     notice = apply_style(
        "We respect your privacy. Any basic info this tool collects "
        "(like usage data, usage statistics) is handled securely and used in "
        "improving error handling, never shared. "
        "\nNo creepy tracking—just good software",
        "/green/bold",
     )
     tname = apply_style("WHAT IS YOUR NAME?", "/yellow/bold")
     tnum = apply_style(
        "ENTER YOUR EMAIL ADDRESS TO STAY UPDATED ABOUT NEW RELEASES "
        "(IF YOU'RE INTERESTED)",
        "/cyan/bold",
     )
     warning = apply_style("(ENTER WISELY YOU CAN'T CHANGE IT LATER)", "/red/bold")

     print("\nTHIS IS COMPULSORY FOR THE FIRST TIME\n")
     print(notice_text.center(100) + "\n")
     print(notice)
     name = input("\n" + tname + warning + " ⚠⚠ : ").strip()
     print()
     num = input(tnum + warning + " ⚠⚠ : ").strip()
     save_user_data(name, num)
     # name, num = _lud()
     # return name, num
 else:
     pass
 # name, num = _lud()

def main_loop():
    while True:
        os.system("clear")
        version, version_type = load_local_version()
        print_banner(version+"_pypi")
        choice = input(des4).strip()
        if choice == "1":
            single_mp3.run()
        elif choice == "2":
            single_mp4.run()
        elif choice == "3":
            multi_mp4.run()
        elif choice == "4":
            multi_mp3.run()
        elif choice == "5":
            print("Have a nice day, Bye!")
            sys.exit()
        else:
            print("Have a nice day, Bye!")
            sys.exit()

        exitc = apply_style(
            "Press [ENTER] to continue downloading another content  ", "/green/bold"
        )
        input(exitc)



name, num =_lud()
if name is None:
  user_data_collect(name, num)
else:
  pass


