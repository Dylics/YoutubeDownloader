import os
import yt_dlp

def download_youtube_video():
    # Настройки для пользователя
    url = input("Введите ссылку на YouTube видео: ")
    save_folder = os.path.join(os.getcwd(), "video")
    os.makedirs(save_folder, exist_ok=True)

    # Конфигурация yt-dlp
    ydl_opts = {
        'outtmpl': os.path.join(save_folder, '%(title)s [%(id)s].%(ext)s'),
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'merge_output_format': 'mp4',
        'cookiefile': 'cookies.txt',
        'noplaylist': False,               # Скачивать только видео, не плейлист
        'socket_timeout': 30,             # Таймаут соединения (секунды)
        'retries': 10,                    # Число попыток при ошибках
        'fragment_retries': 10,
        'ignoreerrors': True,             # Пропускать ошибки в плейлистах
        'no_warnings': True,             # Показывать предупреждения
        'writethumbnail': False,          # Скачивать превью
        'postprocessors': [{
            'key': 'EmbedThumbnail',     # Встраивать превью в файл
            'already_have_thumbnail': False
        }],
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'geo-bypass': True,               # Обход географических ограничений
        'verbose': False
    }

    try:
        print("\nНачинаем загрузку...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✔ Видео успешно скачано в папку video!")

    except Exception as e:
        print(f"\n❌ Критическая ошибка: {str(e)}")
    finally:
        input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    download_youtube_video()