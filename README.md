# 🎤 Voice to Text Tool

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange?style=for-the-badge)

**A modern desktop application for converting audio files to text using Speech Recognition technology**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing) • [License](#-license)

[![GitHub stars](https://img.shields.io/github/stars/MrPatchara/voice-to-text-tool?style=social)](https://github.com/MrPatchara/voice-to-text-tool/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/MrPatchara/voice-to-text-tool?style=social)](https://github.com/MrPatchara/voice-to-text-tool/network/members)
[![GitHub issues](https://img.shields.io/github/issues/MrPatchara/voice-to-text-tool)](https://github.com/MrPatchara/voice-to-text-tool/issues)

</div>

---

## 📋 About

**Voice to Text Tool** is a powerful desktop application built with Python and Tkinter that converts audio files to text using Google Speech Recognition API. It supports multiple audio formats (WAV, MP3) and features a beautiful dark mode interface.

Perfect for:
- ✍️ **Writers** - Convert interviews and conversations to text
- 📝 **Students** - Transcribe lectures and study materials
- 🎯 **Content Creators** - Create transcripts from audio content
- 💼 **Professionals** - Batch process multiple audio files

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **Thai Language Support** | Accurate Thai speech-to-text conversion |
| 📁 **Multi-file Processing** | Process multiple audio files simultaneously |
| 🎨 **Dark Mode UI** | Beautiful, eye-friendly dark theme interface |
| ⚡ **Auto Chunking** | Automatically splits large files into manageable chunks |
| 💾 **Export Results** | Save transcriptions as `.txt` files |
| 🔄 **Real-time Progress** | Live progress indicator during processing |
| 🎵 **Multiple Formats** | Supports WAV and MP3 audio files |
| 🌐 **Internet-based** | Uses Google Speech Recognition API for accuracy |

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)
![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-3.10+-blue)
![pydub](https://img.shields.io/badge/pydub-0.25+-green)

</div>

- **Python 3.7+** - Core programming language
- **Tkinter** - GUI framework (built-in)
- **SpeechRecognition** - Speech-to-text library
- **pydub** - Audio processing library
- **Google Speech Recognition API** - Recognition engine

---

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- Internet connection (required for Google Speech Recognition API)
- Operating System: Windows, Linux, or macOS

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MrPatchara/voice-to-text-tool.git
   cd voice-to-text-tool
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install SpeechRecognition pydub
   ```

3. **Install FFmpeg (Linux/macOS only)**
   
   For Ubuntu/Debian:
   ```bash
   sudo apt-get install ffmpeg
   ```
   
   For macOS:
   ```bash
   brew install ffmpeg
   ```
   
   For Windows, FFmpeg is usually handled automatically by pydub.

---

## 🚀 Usage

### Quick Start

Run the application:
```bash
python app.py
```

### Step-by-Step Guide

1. **Select Audio Files**
   - Click the **"Browse"** button to select audio files (.wav or .mp3)
   - You can select multiple files at once

2. **Convert to Text**
   - Click the **"Convert Audio to Text"** button
   - Wait for processing (progress bar will be displayed)

3. **View Results**
   - Transcribed text will appear in the results panel
   - Each file's results are displayed separately

4. **Save Results**
   - Click **"Save Text"** to export as a `.txt` file
   - Choose your desired location and filename

5. **Clear Results**
   - Click **"Clear Text"** to reset the results panel

### Menu Options

**File Menu:**
- Select Files
- Save Text
- Clear Text
- Exit

**Help Menu:**
- Developer Information

---

## 📸 Screenshots

> *Screenshots coming soon!*

---

## ⚙️ Configuration & Limitations

### Limitations

- ⚠️ Requires **Internet Connection** for Google Speech Recognition API
- ⚠️ Large audio files may take longer to process
- ⚠️ Google Speech Recognition API has rate limits

### Tips for Best Results

- ✅ Use high-quality audio files for better accuracy
- ✅ Ensure clear audio without background noise
- ✅ For long files, consider splitting them into smaller chunks
- ✅ Check your internet connection before processing

---

## 🐛 Troubleshooting

### Common Issues

<details>
<summary><b>Q: Application cannot convert audio</b></summary>

**A:** Check your internet connection and ensure the audio file format is supported (.wav or .mp3)
</details>

<details>
<summary><b>Q: Transcribed text is inaccurate</b></summary>

**A:** Verify the audio quality and clarity of speech in your file
</details>

<details>
<summary><b>Q: Application runs slowly</b></summary>

**A:** Large audio files take time to process. Try splitting files into smaller chunks
</details>

<details>
<summary><b>Q: Cannot install pydub</b></summary>

**A:** For Linux/macOS, you may need to install FFmpeg first (see Installation section)
</details>

<details>
<summary><b>Q: Import errors when running</b></summary>

**A:** Make sure all dependencies are installed: `pip install -r requirements.txt`
</details>

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔄 Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex code
- Update documentation as needed
- Test your changes before submitting

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Developer

**Patchara Alumaree**

<div align="center">

[![Email](https://img.shields.io/badge/Email-Patcharaalumaree@gmail.com-red?style=flat-square&logo=gmail)](mailto:Patcharaalumaree@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-MrPatchara-black?style=flat-square&logo=github)](https://github.com/MrPatchara)

</div>

---

## ⭐ Acknowledgments

- Thanks to [Google Speech Recognition API](https://cloud.google.com/speech-to-text) for the recognition engine
- Built with [SpeechRecognition](https://github.com/Uberi/speech_recognition) library
- Audio processing powered by [pydub](https://github.com/jiaaro/pydub)

---

## 📊 Project Status

![GitHub last commit](https://img.shields.io/github/last-commit/MrPatchara/voice-to-text-tool)
![GitHub repo size](https://img.shields.io/github/repo-size/MrPatchara/voice-to-text-tool)
![GitHub language count](https://img.shields.io/github/languages/count/MrPatchara/voice-to-text-tool)

---

<div align="center">

### ⭐ If you like this project, give it a star! ⭐

**Made with ❤️ by [MrPatchara](https://github.com/MrPatchara)**

[⬆ Back to Top](#-voice-to-text-tool)

</div>
