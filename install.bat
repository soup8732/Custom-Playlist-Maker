@echo off
setlocal enabledelayedexpansion

:: Define emoji symbols (default)
set "CHECK=✅"
set "CROSS=❌"
set "INFO=ℹ️"
set "STAR=✨"

:: Define ASCII fallback symbols
set "CHECK_ASC=OK"
set "CROSS_ASC=ERR"
set "INFO_ASC=INFO"
set "STAR_ASC=*"

:: Function to check if console font supports emoji
:: We'll assume modern Windows supports them, but provide a fallback if needed.
set "EMOJIS_SUPPORTED=1"

:: If you want to be super safe, uncomment the next lines to ask user
:: echo Are emojis displaying correctly? (y/n)
:: set /p emojians=
:: if /i NOT "%emojians%"=="y" set "EMOJIS_SUPPORTED=0"

:: Choose symbols depending on support
if "%EMOJIS_SUPPORTED%"=="1" (
    set "SYM_CHECK=%CHECK%"
    set "SYM_CROSS=%CROSS%"
    set "SYM_INFO=%INFO%"
    set "SYM_STAR=%STAR%"
) else (
    set "SYM_CHECK=%CHECK_ASC%"
    set "SYM_CROSS=%CROSS_ASC%"
    set "SYM_INFO=%INFO_ASC%"
    set "SYM_STAR=%STAR_ASC%"
)

:: Color support (Windows 10+ supports ANSI codes in cmd with ENABLE_VIRTUAL_TERMINAL_PROCESSING)
:: Try to enable ANSI colors
>nul 2>&1 reg query "HKCU\Console" /v VirtualTerminalLevel && (
    :: Windows 10+ with VT support
    set "GREEN=\033[0;32m"
    set "RED=\033[0;31m"
    set "YELLOW=\033[1;33m"
    set "CYAN=\033[0;36m"
    set "RESET=\033[0m"
) || (
    :: No color support, empty codes
    set "GREEN="
    set "RED="
    set "YELLOW="
    set "CYAN="
    set "RESET="
)

echo %SYM_STAR% %GREEN%Starting YTConverter™ universal installer...%RESET%

:: Function to check if a command exists
:: Usage: call :command_exists <command_name>
:command_exists
    where %1 >nul 2>&1
    exit /b %errorlevel%

:: --- System Package Installation (Windows Equivalent) ---
echo %SYM_INFO% %CYAN%Checking system dependencies...%RESET%

:: Python 3 and Pip
call :command_exists python
if %errorlevel% neq 0 (
    echo %SYM_CROSS% %RED%Python 3 not found. Please install Python 3 from python.org and add it to your PATH.%RESET%
    echo %SYM_INFO% %YELLOW%Download Python from: https://www.python.org/downloads/windows/%RESET%
    pause
    goto :eof
) else (
    echo %SYM_CHECK% %GREEN%Python 3 found.%RESET%
)

call :command_exists pip
if %errorlevel% neq 0 (
    echo %SYM_CROSS% %RED%Pip not found. Please ensure Python 3 was installed with pip.%RESET%
    pause
    goto :eof
) else (
    echo %SYM_CHECK% %GREEN%Pip found.%RESET%
)

:: FFmpeg
call :command_exists ffmpeg
if %errorlevel% neq 0 (
    echo %SYM_CROSS% %RED%FFmpeg not found.%RESET%
    echo %SYM_INFO% %YELLOW%Please download FFmpeg binaries and add its 'bin' directory to your system PATH.%RESET%
    echo %SYM_INFO% %YELLOW%Refer to: https://ffmpeg.org/download.html%RESET%
    :: Optionally, you could try to download with curl/bitsadmin if present, but it's complex for PATH setup.
    pause
) else (
    echo %SYM_CHECK% %GREEN%FFmpeg found.%RESET%
)

:: yt-dlp (system-wide if not via pip)
:: On Windows, yt-dlp is typically installed via pip or downloaded as a standalone exe.
:: We'll prioritize pip installation in the next step. If it's already a command, great.
call :command_exists yt-dlp
if %errorlevel% neq 0 (
    echo %SYM_INFO% %YELLOW%yt-dlp command not found directly. Will attempt pip install.%RESET%
) else (
    echo %SYM_CHECK% %GREEN%yt-dlp command found.%RESET%
)

:: --- Python Package Installation ---
echo.
echo %SYM_INFO% %CYAN%Installing/Upgrading Python packages...%RESET%

:: Upgrade pip
python -m pip install --upgrade pip || (
    echo %SYM_CROSS% %RED%Failed to upgrade pip.%RESET%
    goto :eof
)
echo %SYM_CHECK% %GREEN%Pip upgraded.%RESET%

:: Install Python packages
python -m pip install --upgrade yt-dlp fontstyle colored requests || (
    echo %SYM_CROSS% %RED%Python package installation failed.%RESET%
    goto :eof
)
echo %SYM_CHECK% %GREEN%Python packages installed successfully.%RESET%

echo.
echo %SYM_CHECK% %GREEN%Installation complete! You can now run YTConverter™.%RESET%
echo %SYM_INFO% %CYAN%To start: run 'python ytconverter.py' or use your launcher.%RESET%

pause
endlocal
exit /b 0

