#!/usr/bin/env python3
"""
Локальный сервер для проекта "Wings of Fire".

Просто поднимает статический HTTP-сервер в корневой папке проекта,
чтобы можно было открыть index.html (и src/js/*) в браузере по адресу:

    http://localhost:8000

Использование:
    python server.py            # порт 8000 по умолчанию
    python server.py --port 3000
    python server.py --host 127.0.0.1 --port 5000
"""

import argparse
import http.server
import os
import socketserver
import sys
import webbrowser

# Корень проекта — папка, где лежит этот файл
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


class QuietHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Обработчик с понятным логом запросов."""

    def log_message(self, format, *args):
        sys.stdout.write(f"[server] {self.address_string()} - {format % args}\n")
        sys.stdout.flush()


def main():
    parser = argparse.ArgumentParser(description="Локальный сервер проекта Wings of Fire")
    parser.add_argument("--host", default="localhost", help="Хост (по умолчанию: localhost)")
    parser.add_argument("--port", type=int, default=8000, help="Порт (по умолчанию: 8000)")
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Не открывать браузер автоматически",
    )
    args = parser.parse_args()

    # Сервер отдаёт файлы из корня проекта
    os.chdir(PROJECT_ROOT)

    handler = QuietHTTPRequestHandler

    class ThreadingServer(socketserver.ThreadingTCPServer):
        allow_reuse_address = True
        daemon_threads = True

    try:
        with ThreadingServer((args.host, args.port), handler) as httpd:
            url = f"http://{args.host}:{args.port}/"
            print(f"Сервер запущен: {url}")
            print(f"Корень: {PROJECT_ROOT}")
            print("Нажмите Ctrl+C, чтобы остановить сервер.")

            if not args.no_browser:
                try:
                    webbrowser.open(url)
                except Exception:
                    pass  # если браузер не открылся — не критично

            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
    except OSError as e:
        print(f"Не удалось запустить сервер на {args.host}:{args.port}: {e}")
        print("Попробуйте другой порт, например: python server.py --port 8080")
        sys.exit(1)


if __name__ == "__main__":
    main()
