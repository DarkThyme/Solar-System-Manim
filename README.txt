# Solar System Animation using Manim

This project generates a 3D animation of the solar system using [Manim](https://www.manim.community/), a powerful mathematical animation engine. It also includes an example video that demonstrates the solar system's orbit.

# Solar System Animation using Manim

This project generates a 3D animation of the solar system using [Manim](https://www.manim.community/), a powerful mathematical animation engine. It also includes an example video that demonstrates the solar system's orbit.

## Requirements

- [Chocolatey](https://chocolatey.org/) (for package management on Windows)
- [FFmpeg](https://ffmpeg.org/) (for video rendering)
- [Manim](https://docs.manim.community/en/stable/) (for creating animations)

## Installation Instructions

### 1. Install Chocolatey

Open **Command Prompt as Administrator** and run the following command to install Chocolatey:

```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; 
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; 
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))


# Once installed, restart your terminal.

### 2. Install Manim and FFmpeg

With Chocolatey installed, run the following commands to install Manim and FFmpeg:

choco install manim
choco install ffmpeg

# Ensure that the packages are properly installed by running:

manim --version

### 3. Running the code
- Once you've installed Manim, you can run the provided Solar_System.py script.

- Open Command Prompt and navigate to the directory where Solar_System.py is located:

cd path\to\your\project

- Run the script with the following command:

manim -pql Solar_System.py SolarSystem

#####(-pql: This flag indicates to render the video in high quality with preview. l is lower, h is higher.) (SolarSystem: The name of the class in the script that contains the scene.)

### 4. Example Video
- You can find the example video generated from this script in the repository: SolarSystem.mp4.




