# wings-of-fire

## Структура проекта

- `server.py` — локальный сервер (запуск: `python server.py`, затем открыть http://localhost:8000)
- `src/js/` — модули JavaScript (namespace `window.WOF`):
  - `helpers.js`   — утилиты DOM, случайные числа, шум, цвета
  - `canvas.js`    — игровой холст и контекст 2D
  - `terrain.js`   — генерация рельефа мира
  - `camera.js`    — виртуальная камера и проекция
  - `math3d.js`    — матрицы поворота 3x3
  - `emitQueue.js` — очередь объектов рендера
  - `colors.js`    — палитра мира
  - `save.js`      — профиль игрока (localStorage), апгрейды
- `scripts/` — служебные скрипты сборки/извлечения
- `Qwen_html_20261010_w6p7ub4fi.html` — исходный единый HTML-файл

## Запуск локального сервера

```bash
python server.py                 # порт 8000 по умолчанию
python server.py --port 3000     # другой порт
python server.py --no-browser    # не открывать браузер автоматически
```

Сервер раздаёт файлы из корня проекта; страница доступна по адресу http://localhost:8000.
