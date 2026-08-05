import os
import sys
from yt_dlp import YoutubeDL

def try_download(url: str, output_dir: str = "downloads"):
    os.makedirs(output_dir, exist_ok=True)

    common_opts = {
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
        "format": "bestvideo*+bestaudio/best",
        "noplaylist": True,
        "retries": 10,
        "js_runtimes": {
            "node": {
                "path": r"C:\Program Files\nodejs\node.exe"
            }
        },
        "fragment_retries": 10,
        "quiet": False,
        "no_warnings": False,
        "progress_with_newline": True,
        "verbose": True,

        # УКАЖИ СВОЙ РЕАЛЬНЫЙ ПУТЬ:
         "ffmpeg_location": r"B:\ffmpeg-8.1-essentials_build\ffmpeg-8.1-essentials_build\bin\ffmpeg.exe",
    }

    format_variants = [
        "bv*+ba/b",
        "bestvideo*+bestaudio/best",
        "best",
    ]

    last_error = None

    for fmt in format_variants:
        print(f"\nПробую формат: {fmt}\n")
        opts = {**common_opts, "format": fmt}

        try:
            with YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
                print(f"\nГотово: {ydl.prepare_filename(info)}")
                return
        except Exception as e:
            last_error = e
            print(f"\nНе удалось скачать с format='{fmt}': {e}\n")

    raise Exception(f"Все попытки скачивания завершились ошибкой: {last_error}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование:")
        print("python dowloader.py <ссылка>")
        sys.exit(1)

    try_download(sys.argv[1])