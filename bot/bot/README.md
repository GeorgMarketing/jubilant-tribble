## ZapTeam Telegram Bot (Python, aiogram 3)

Бот реализует сценарии из ТЗ: главное меню, FAQ, выбор деятельности (бизнес/физлицо/нерезидент), воронки для импорта/экспорта и селлеров, покупка/конвертация USDT, связь с менеджером. Данные пользователей сохраняются в SQLite.

### Быстрый старт (Windows PowerShell)

1. Установите Python 3.11+
2. В корне репозитория:

```
py -m venv .venv
./.venv/Scripts/Activate.ps1
pip install -r bot/requirements.txt --only-binary=:all: --prefer-binary
copy bot/env.example bot/.env
```

3. Отредактируйте `bot/.env`:

- `BOT_TOKEN` — токен Telegram-бота
- `MANAGER_URL` — ссылка на профиль/чат менеджера
- `CHAT_LINK_DEFAULT` — общий чат поддержки
- `CHAT_LINK_USDT` — чат по USDT (если отличается)
- `CORE_REG_URL` — ссылка на регистрацию на платформе CORE (например, `https://otc.bankingcore.cloud/i/6890e0ececb2d97053e5cd31/098825be005c6f5c`)

4. Запуск:

```
py -m bot
```

### Вебхук (для VPS)
- В `.env` укажите:
```
WEBHOOK_URL=https://your.domain.tld
WEBHOOK_PATH=/telegram
WEBHOOK_SECRET=replace_me
WEBAPP_HOST=0.0.0.0
WEBAPP_PORT=8080
```
- Настройте обратный прокси (пример Nginx):
```
server {
  listen 443 ssl;
  server_name your.domain.tld;
  # ssl_certificate /etc/letsencrypt/live/your.domain.tld/fullchain.pem;
  # ssl_certificate_key /etc/letsencrypt/live/your.domain.tld/privkey.pem;

  location /telegram {
    proxy_pass http://127.0.0.1:8080/telegram;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
  }
}
```
- Если `WEBHOOK_URL` задан — бот стартует в режиме webhook, иначе — polling.

Если используете Python 3.13 и возникнут ошибки сборки `aiohttp`, используйте ключи `--only-binary=:all:` как выше, чтобы брать готовые колёса.

### Стек
- Python 3.11+
- aiogram 3.x (long polling)
- SQLite (aiosqlite)
- pydantic-settings

### Структура
- `bot/__main__.py` — входная точка
- `bot/config.py` — загрузка настроек из `.env`
- `bot/db.py` — инициализация БД и операции (users)
- `bot/texts.py` — все тексты бота
- `bot/keyboards.py` — инлайн/реплай клавиатуры
- `bot/handlers/` — обработчики сценариев

### Миграция/БД
При первом запуске автоматически создастся файл БД `bot/storage.db` и таблица `users`.

### Деплой на VPS (кратко)
- Скопируйте проект на сервер
- Создайте venv, установите зависимости, создайте `.env`
- Запускайте как сервис (например, systemd) командой `python -m bot`


