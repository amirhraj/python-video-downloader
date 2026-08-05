# Python Video Downloader

A simple Python-based video downloader built with `yt-dlp` and `ffmpeg`.

The project supports downloading media from YouTube and other websites supported by `yt-dlp`, including HLS (`.m3u8`) streams.

---

## Features

- Download videos from YouTube.
- Download HLS (`.m3u8`) streams.
- Merge video and audio streams automatically.
- Retry failed downloads.
- Support for `ffmpeg`.
- Support for JavaScript challenges through Node.js.
- Support for browser cookies.
- Detailed logging output.

---

## Requirements

Before using the script, install the following software:

- Python 3.12+
- FFmpeg
- Node.js 22+
- yt-dlp
- yt-dlp-ejs

---

## Installation

Clone the repository:

```bash
git clone git@github.com:amirhraj/python-video-downloader.git
cd python-video-downloader
```

Install Python dependencies:

```bash
pip install -U yt-dlp yt-dlp-ejs
```

---

## Install FFmpeg

Download FFmpeg and extract it somewhere on your machine.

Example:

```text
B:\ffmpeg\bin\ffmpeg.exe
```

Update the path inside the script:

```python
"ffmpeg_location": r"B:\ffmpeg\bin\ffmpeg.exe"
```

---

## Install Node.js

Download and install the latest LTS version of Node.js.

Verify the installation:

```bash
node --version
```

---

## Usage

Download a YouTube video:

```bash
python downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Download a YouTube Shorts video:

```bash
python downloader.py "https://www.youtube.com/shorts/VIDEO_ID"
```

Download an HLS stream:

```bash
python downloader.py "https://example.com/master.m3u8"
```

---

## Project structure

```text
python-video-downloader/
│
├── downloads/
├── downloader.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Example

```bash
python downloader.py "https://www.youtube.com/watch?v=5ltsySR5h9I"
```

---

## Disclaimer

This project is intended for educational purposes only.

Users are responsible for complying with the terms of service and copyright regulations of the websites they use.

---

## License

MIT License