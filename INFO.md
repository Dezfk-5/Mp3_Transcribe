# MP3 Transcribe - Developer Info

This project provides a script (`transcript.py`) for transcribing MP3 files using OpenAI's Whisper model. It is designed to work both in development and as a bundled executable (e.g., with PyInstaller).

## Overview
- **Language:** Python
- **Main Script:** `transcript.py`
- **Dependencies:**
  - [whisper](https://github.com/openai/whisper)
  - [tkinter](https://docs.python.org/3/library/tkinter.html) (for GUI directory selection)
## How It Works
1. **FFmpeg Setup:**
   - Adds the local `ffmpeg_bin` folder to the process PATH so the script can use `ffmpeg.exe` without requiring a system-wide installation.
2. **Directory Selection:**
   - Uses a Tkinter dialog to prompt the user to select a folder containing MP3 files.
3. **Transcription:**
   - Loads the Whisper model from the `models` folder using a PyInstaller-compatible path resolver.
   - Iterates through all MP3 files in the selected directory.
   - Transcribes each file and saves the transcript (with timestamps) as a `.txt` file in an `Output` subfolder.

## Key Functions

- `resource_path(relative_path)`: Resolves paths for bundled resources (important for PyInstaller compatibility).

- `add_ffmpeg_temp_path(ffmpeg_folder)`: Temporarily adds the local ffmpeg folder to PATH.
Download the Windows executable from the official site:
- [FFmpeg Download Page](https://ffmpeg.org/download.html)
- Direct link for Windows builds: [gyan.dev FFmpeg builds](https://www.gyan.dev/ffmpeg/builds/)
After downloading, place `ffmpeg.exe` in the `ffmpeg_bin` folder.

- `select_directory()`: Opens a GUI dialog for directory selection.
Download the model file from OpenAI's Whisper repository:
- [Whisper Model Files](https://github.com/openai/whisper)
- Direct link for base English model: [base.en.pt on Hugging Face](https://huggingface.co/openai/whisper-base.en/resolve/main/model.pt)
Rename the downloaded file to `base.en.pt` and place it in the `models` folder.
- `transcribe_mp3_files(directory)`: Transcribes all MP3 files in the given directory and saves results.

## Output
- Transcripts are saved in an `Output` folder inside the selected directory.
- Each transcript is a `.txt` file named after the original MP3 file.
- Timestamps are included for each segment if available.

## Usage
1. Run `transcript.py`.
2. Select the directory containing MP3 files when prompted.
3. Wait for transcription to complete. Check the `Output` folder for results.

## Notes
- The script is compatible with PyInstaller for creating standalone executables.
- Ensure `ffmpeg.exe` and the Whisper model file are present in their respective folders.
- Error messages are printed to the console if files cannot be processed.

## File Structure
```
Mp3_Transcribe/
├── transcript.py
├── ffmpeg_bin/
│   └── ffmpeg.exe
├── models/
│   └── base.en.pt
└── ...
```


