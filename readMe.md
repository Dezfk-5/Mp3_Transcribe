# Audio to Text Transcription Tool

This Python program transcribes all `.mp3` files in a selected directory using [OpenAI Whisper](https://github.com/openai/whisper).  
It is designed for easy distribution (including PyInstaller bundling) and supports local models and assets.

---

## Features

- **Batch transcription** of MP3 files in a folder
- **Readable transcript output** with timestamps for each segment
- **Resource path system** for bundling models and assets with PyInstaller
- **Automatic ffmpeg path setup** for portable audio conversion
- **Error handling** for corrupted or unsupported files

---

## How It Works

1. **Select a directory** containing MP3 files via a dialog.
2. The program loads the Whisper model and required assets from bundled folders.
3. Each MP3 is transcribed and saved as a timestamped `.txt` file in an `Output` subfolder.
4. The program prints progress and errors to the terminal.

---

## Folder Structure

```

Audio2Text/
├── transcript.py
├── models/
│   └── base.en.pt
└── ffmpeg_bin/
    └── ffmpeg.exe

```

---

## Usage

1. **Install dependencies:**
   ```sh
   pip install openai-whisper tkinter
   ```
2. **Download and place model and asset files:**
   - Place `base.en.pt` in `models/`
   - Place `ffmpeg.exe` in `ffmpeg_bin/`

3. **Run the script:**
   ```sh
   python transcript.py
   ```
   - Select your MP3 folder when prompted.
   - Transcripts will be saved in an `Output` folder inside the selected directory.

---

## PyInstaller Bundling

To bundle with PyInstaller, use the following options to include models, assets, and ffmpeg:

```sh
PyInstaller --onefile transcript.py --collect-data whisper --add-data "models/base.en.pt;models" --add-data "ffmpeg_bin/ffmpeg.exe;ffmpeg_bin" --recursive-copy-metadata "openai-whisper"
```




---

## Troubleshooting

- **ffmpeg errors:**  
  Make sure `ffmpeg.exe` is present in `ffmpeg_bin/` and is included in your bundle.

- **Corrupted MP3 files:**  
  The program will skip files that cannot be processed and print an error message.

---

## License

This project is for educational and personal use.  
See [OpenAI Whisper license](https://github.om/openai/whisper/blob/main/LICENSE) for model terms.

---

## Credits

- [OpenAI Whisper](https://github.com/openai/whisper)
- [PyInstaller](https://pyinstaller.org/)
- [ffmpeg](https://ffmpeg.org/)
