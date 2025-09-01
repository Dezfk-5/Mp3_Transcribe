import os
import sys
import tkinter as tk
from tkinter import filedialog
import whisper

# ============================================================
# Function: resource_path
# ------------------------------------------------------------
# Description:
#   Returns the absolute path to a resource, compatible with PyInstaller.
#   Use this for bundled files like models and assets.
#
# Parameters:
#   relative_path (str): Relative path to the resource.
#
# Returns:
#   str: Absolute path to the resource.
# ============================================================
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ============================================================
# Function: add_ffmpeg_temp_path
# ------------------------------------------------------------
# Description:
#   Adds a temporary path for ffmpeg to the environment variable PATH.
#   This allows the script to use a local ffmpeg executable without
#   requiring a system-wide installation.
#
# Parameters:
#   ffmpeg_folder (str): Name of the folder containing ffmpeg.exe.
#
# Returns:
#   None
# ============================================================
def add_ffmpeg_temp_path(ffmpeg_folder="ffmpeg_bin"):
    ffmpeg_dir = resource_path(ffmpeg_folder)
    if os.path.isdir(ffmpeg_dir):
        # Add ffmpeg directory to PATH for this process only
        os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ.get("PATH", "")
        print(f"Temporarily added ffmpeg path: {ffmpeg_dir}")
    else:
        print(f"ffmpeg folder '{ffmpeg_dir}' not found. ffmpeg may not work.")

# ============================================================
# Function: select_directory
# ------------------------------------------------------------
# Description:
#   Opens a dialog for the user to select a directory containing MP3 files.
#
# Returns:
#   directory (str): Path to the selected directory.
# ============================================================
def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    directory = filedialog.askdirectory(title="Select Directory with MP3 Files")
    return directory

# ============================================================
# Function: transcribe_mp3_files
# ------------------------------------------------------------
# Description:
#   Transcribes all MP3 files in the specified directory using Whisper.
#   Saves each transcript as a .txt file in an 'Output' subfolder.
#   Uses bundled model and asset files for PyInstaller compatibility.
#
# Parameters:
#   directory (str): Path to the directory containing MP3 files.
#
# Returns:
#   None
# ============================================================
def transcribe_mp3_files(directory):
    output_dir = os.path.join(directory, "Output")
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

    # Set up paths for model and assets
    model_path = resource_path(os.path.join("models", "base.en.pt"))

    # Load Whisper model (base.en) from bundled model file
    model = whisper.load_model(model_path)

  

    # Iterate through all files in the directory
    for entry in os.scandir(directory):
        # Check if the file is an MP3
        if entry.is_file() and entry.name.lower().endswith(".mp3"):
            mp3_path = entry.path
            print(f"Checking file: {mp3_path}")
            print(f"Transcribing: {entry.name}")
            try:
                # Transcribe the MP3 file
                result = model.transcribe(mp3_path)
                # Format transcript with timestamps
                segments = result.get("segments", [])
                if segments:
                    transcript_lines = []
                    for seg in segments:
                        start = seg["start"]
                        end = seg["end"]
                        text = seg["text"].strip()
                        # Format: [HH:MM:SS - HH:MM:SS] text
                        start_str = f"{int(start//3600):02}:{int((start%3600)//60):02}:{int(start%60):02}"
                        end_str = f"{int(end//3600):02}:{int((end%3600)//60):02}:{int(end%60):02}"
                        transcript_lines.append(f"[{start_str} - {end_str}] {text}")
                    transcript = "\n".join(transcript_lines)
                else:
                    transcript = result["text"]

                # Save transcript to a .txt file in the Output directory
                txt_filename = os.path.splitext(entry.name)[0] + ".txt"
                txt_path = os.path.join(output_dir, txt_filename)
                with open(txt_path, "w", encoding="utf-8") as f:
                    f.write(transcript)
                print(f"Saved transcript to: {txt_path}")
            except Exception as e:
                print(f"Error processing {mp3_path}: {e}")

# ============================================================
# Main Script Execution
# ------------------------------------------------------------
# Description:
#   Adds ffmpeg to PATH, prompts user for directory, and transcribes MP3 files.
#   Uses resource_path for PyInstaller compatibility.
# ============================================================
if __name__ == "__main__":
    add_ffmpeg_temp_path()  # Add ffmpeg_bin to PATH temporarily
    selected_dir = select_directory()
    if selected_dir:
        transcribe_mp3_files(selected_dir)
    else:
        print("No directory selected.")