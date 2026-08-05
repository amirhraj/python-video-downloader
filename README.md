# Python Video Downloader

A simple command-line video downloader built with Python, `yt-dlp`, FFmpeg, Node.js, and Docker Compose.

The project can download:

* YouTube videos
* YouTube Shorts
* HLS streams using `.m3u8` links
* Media from other websites supported by `yt-dlp`

Downloaded files are saved to the local `downloads` directory.

---

## Features

* Downloads video and audio in the best available quality
* Automatically merges separate video and audio streams
* Supports YouTube and other websites supported by `yt-dlp`
* Supports HLS `.m3u8` streams
* Uses FFmpeg for media processing
* Uses Node.js for YouTube JavaScript challenges
* Retries failed downloads
* Runs inside Docker
* Does not require local Python, FFmpeg, Node.js, or `yt-dlp` installation

---

## Requirements

You only need to install:

* Git
* Docker Desktop

Docker Desktop must be running before you build or run the project.

Check that Docker is installed:

```bash
docker --version
docker compose version
```

---

## Installation

Clone the repository:

```bash
git clone git@github.com:amirhraj/Python-Video-Downloader.git
```

Open the project directory:

```bash
cd Python-Video-Downloader
```

Create the downloads directory if it does not exist:

```bash
mkdir downloads
```

On Windows PowerShell, you can use:

```powershell
New-Item -ItemType Directory -Force downloads
```

---

## Build the Docker Image

Run:

```bash
docker compose build
```

Docker will install all required dependencies inside the image:

* Python
* FFmpeg
* Node.js
* yt-dlp
* yt-dlp-ejs

The first build may take longer because Docker needs to download and install the required packages.

---

## Usage

### Download a YouTube video

```bash
docker compose run --rm downloader "https://www.youtube.com/watch?v=VIDEO_ID"
```

Example:

```bash
docker compose run --rm downloader "https://www.youtube.com/watch?v=5ltsySR5h9I"
```

---

### Download a YouTube Shorts video

```bash
docker compose run --rm downloader "https://www.youtube.com/shorts/VIDEO_ID"
```

---

### Download an HLS stream

Use the direct `.m3u8` URL:

```bash
docker compose run --rm downloader "https://example.com/video/master.m3u8"
```

---

## Windows PowerShell

You can run the command on one line:

```powershell
docker compose run --rm downloader "https://www.youtube.com/watch?v=VIDEO_ID"
```

Or split it into multiple lines:

```powershell
docker compose run --rm downloader `
  "https://www.youtube.com/watch?v=VIDEO_ID"
```

---

## Downloaded Files

Downloaded files are saved to:

```text
./downloads
```

On Windows, the full path may look like:

```text
C:\Users\YourName\Desktop\Python-Video-Downloader\downloads
```

The `downloads` directory is mounted from your computer into the Docker container, so downloaded files remain available after the container stops.

---

## Stop and Clean Up

Remove stopped project containers:

```bash
docker compose down
```

Remove the project image:

```bash
docker image rm python-video-downloader:latest
```

Rebuild the image without using Docker cache:

```bash
docker compose build --no-cache
```

---

## Troubleshooting

### Docker is not running

If you see an error related to the Docker daemon or Docker engine, start Docker Desktop and run the command again.

---

### The video is unavailable

If the downloader reports:

```text
This video is not available
```

check that:

* The video opens in your browser
* The video was not deleted
* The video is not private
* The video is available in your region
* The video does not require account authorization


---

### Rebuild the image

If dependencies are outdated or the container behaves incorrectly:

```bash
docker compose build --no-cache
```

Then run the downloader again:

```bash
docker compose run --rm downloader "VIDEO_URL"
```

---

## Updating yt-dlp

The Docker image contains the `yt-dlp` version installed during the build.

To install the latest available version, rebuild without cache:

```bash
docker compose build --no-cache
```

---

## Legal Notice

This project is intended for educational and personal use.

Only download media that you are legally allowed to access and save. Users are responsible for following copyright laws and the terms of service of the websites they use.

This project does not bypass DRM protection.

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.


# Описание

Этот проект представляет собой универсальный загрузчик видео, построенный на основе `yt-dlp`, `FFmpeg`, `Node.js` и `Docker`.
Этот проект предназначен для образовательного и личного использования.
Загружайте только те медиафайлы, к которым вам разрешен доступ и сохранение по закону. Пользователи несут ответственность за соблюдение законов об авторском праве и условий обслуживания веб-сайтов, которые они используют.
Этот проект не обходит защиту DRM.

С его помощью можно скачивать:

* видео с ЮТУБ;
* ЮТУБ Shorts;
* HLS-потоки (`.m3u8`);
* контент с других сайтов, поддерживаемых `yt-dlp`.

Главная особенность проекта заключается в том, что пользователю не нужно отдельно устанавливать Python, FFmpeg, Node.js, `yt-dlp` и другие зависимости. Всё необходимое уже находится внутри Docker-контейнера.

Для работы понадобятся только:

* Docker Desktop;
* Docker Compose;
* Git.

### Установка Docker

Проверьте, установлен ли Docker:

```bash
docker --version
docker compose version
```

Если команды успешно выполнились, значит, всё готово к работе.

### Клонирование репозитория

```bash
git clone git@github.com:amirhraj/Python-Video-Downloader.git
cd Python-Video-Downloader
```

### Сборка проекта

```bash
docker compose build
```

### Скачивание видео

```bash
docker compose run --rm downloader "VIDEO_URL"
```

Пример:

```bash
docker compose run --rm downloader "https://www.youtube.com/watch?v=5ltsySR5h9I"
```

### Скачивание HLS-потока

```bash
docker compose run --rm downloader "https://example.com/video/master.m3u8"
```

Все загруженные файлы автоматически сохраняются в каталог `downloads`.
