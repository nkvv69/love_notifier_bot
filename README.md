# 💌 Love Notifier Bot

Личный Telegram-бот для уведомлений и сигналов 💫  

---

## 🚀 Возможности

✅ Проверяет, кто нажимает **Start**  
✅ Если это нужный человек — отправляет "обращение зарегистрировано"  
✅ Автор получает тревожное уведомление:  
> 🚨 *"Она написала! Езжай за цветами 🌹"*  
✅ Работает 24/7 на Raspberry Pi или любом Linux-сервере  
✅ Управление через `systemd`

---

## 🧩 Технологии

- 🐍 **Python 3.11+**
- 🤖 **Aiogram 3**
- ⚙️ **Systemd**
- 🍓 **Raspberry Pi 5**

---

## ⚙️ Установка

```bash
# Клонируй репозиторий
git clone https://github.com/<твое_имя>/love_notifier_bot.git
cd love_notifier_bot

# Создай виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# Установи зависимости
pip install -r requirements.txt
```

---

## 🔧 Настройка бота

1. Создай бота через [@BotFather](https://t.me/BotFather)  
2. Получи токен и вставь его в `bot.py`:
   ```python
   API_TOKEN = "ТОКЕН_БОТА"
   ```
3. Укажи ID пользователей:
   ```python
   ALLOWED_USER_IDS = [11111111, 22222222]  # подруга
   ALERT_USER_ID = 33333333                  # ты
   ```

---

## 🖥️ Автозапуск через systemd

1. Скопируй сервис:
   ```bash
   sudo cp love_notifier_bot.service /etc/systemd/system/
   ```

2. Перечитай конфигурацию:
   ```bash
   sudo systemctl daemon-reload
   ```

3. Включи автозапуск:
   ```bash
   sudo systemctl enable love_notifier_bot
   ```

4. Запусти:
   ```bash
   sudo systemctl start love_notifier_bot
   ```

5. Проверить статус:
   ```bash
   sudo systemctl status love_notifier_bot
   ```

---

## 🧰 Полезные команды

| Действие | Команда |
|----------|----------|
| 🔄 Перезапустить | `sudo systemctl restart love_notifier_bot` |
| ⏹ Остановить | `sudo systemctl stop love_notifier_bot` |
| 📜 Логи | `sudo journalctl -u love_notifier_bot -n 50 --no-pager` |
| ⚙️ Перечитать демоны | `sudo systemctl daemon-reload` |

---

## 🧠 Структура проекта

```
love_notifier_bot/
├── bot.py
├── requirements.txt
├── README.md
└── love_notifier_bot.service
```

---

## ❤️ NK

Создан с помощью Python 🐍 и Raspberry Pi 🍓  
**Love Notifier Bot © 2025**
