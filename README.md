<p align="center">
  <img src="https://github.com/Cron-Routine-Orchestrator-Webapp/.github/blob/main/assets/icon.png?raw=true" alt="Logo" width=200px />
</p>

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/Cron-Routine-Orchestrator-Webapp/CROW-Client)
[![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/Cron-Routine-Orchestrator-Webapp/CROW-Client?style=flat&link=https%3A%2F%2Fgithub.com%2FCron-Routine-Orchestrator-Webapp%2FCROW-ClientC%2Fissues)](https://github.com/Cron-Routine-Orchestrator-Webapp/CROW-Client/issues)
[![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr/Cron-Routine-Orchestrator-Webapp/CROW-Client?style=flat&color=%230000ff&link=https%3A%2F%2Fgithub.com%2FCron-Routine-Orchestrator-Webapp%2FCROW-Client%2Fpulls)](https://github.com/Cron-Routine-Orchestrator-Webapp/CROW-Client/pulls)
[![GitHub License](https://img.shields.io/github/license/Cron-Routine-Orchestrator-Webapp/CROW-Client?style=flat&color=%237f3403)](https://github.com/Cron-Routine-Orchestrator-Webapp/CROW-Client?tab=Apache-2.0-1-ov-file#readme)
[![GitHub Release](https://img.shields.io/github/v/release/Cron-Routine-Orchestrator-Webapp/CROW-Client?display_name=tag&style=flat&label=GitHub%20Release&color=%233e85e0)](https://github.com/Cron-Routine-Orchestrator-Webapp/CROW-Client/releases/latest)

# CROW-Client

**CROW** (Cron-Routine-Orchestrator-Webapp) is a distributed task execution and orchestration system. This repository contains the **CROW-Client**, a lightweight WebSocket-based agent that runs on client machines to execute tasks dispatched by the CROW-Server.

## 🎯 Overview

CROW-Client is a Python-based task execution agent that:

- Runs as a WebSocket server on the client machine
- Receives task execution requests from the CROW-Server
- Executes tasks with proper error handling and status reporting
- Provides real-time bidirectional communication via WebSockets
- Handles concurrent task requests asynchronously

## ✨ Features

- **Async WebSocket Communication**: Non-blocking WebSocket server for reliable task delivery
- **Task Execution**: Flexible task parsing and execution framework
- **Error Handling**: Comprehensive error handling with detailed status codes and messages
- **Lightweight**: Minimal dependencies - only requires `asyncio`, `pydantic`, and `websockets`
- **Production-Ready**: Type-safe request/response validation using Pydantic
- **Easy Integration**: Simple CLI startup and configuration

## 🚀 Installation (Linux, macOS, Windows)

CROW Client can be installed with a single command on all major operating systems. The installer scripts are fetched directly from this repository and executed locally.

### ⚠️ Security Note

This executes a remote script from this repository. Only run it if you trust the source.

---

## Linux / macOS (bash)

### Linux

```bash
curl -fsSL https://raw.githubusercontent.com/Cron-Routine-Orchestrator-Webapp/CROW-Client/main/installer/install_linux.sh | bash
```

### macOS:

```bash
curl -fsSL https://raw.githubusercontent.com/Cron-Routine-Orchestrator-Webapp/CROW-Client/main/installer/install_macos.sh | bash
```

---

## Windows (PowerShell)

Run in PowerShell:

```powershell
iwr https://raw.githubusercontent.com/Cron-Routine-Orchestrator-Webapp/CROW-Client/main/installer/install_windows.ps1 -UseBasicParsing | iex
```

---

## What this does

Each installer will:

- Fetch the latest release from GitHub
- Download the correct platform ZIP asset
- Extract the `crow-client` executable
- Install it into a user-local directory
- Register it for auto-start:
  - Linux: `systemd --user`
  - macOS: `launchd`
  - Windows: Startup folder shortcut
- The client will start and listen on `0.0.0.0:1237` for incoming task requests from the CROW-Server.

---

## File locations after install

- Linux: `~/.local/share/crow-client`
- macOS: `~/Library/Application Support/crow-client`
- Windows: `%APPDATA%\crow-client`

---

## Updating

Re-run the same command to update to the latest version. The installer will replace the existing installation with the newest release automatically.

## 🏗️ Architecture

```
CROW-Client Architecture:
┌─────────────────────────────────────┐
│      WebSocket Server (Port 5000)   │
│       Listens for task requests     │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│      Request Parser & Validator     │
│    (Using Pydantic Models)          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│      Task Executor                  │
│   Parses and executes commands      │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Response Builder & Sender         │
│   Returns status + execution output │
└─────────────────────────────────────┘
```

## 📋 Requirements

- **Python**: 3.10 or higher
- **Dependencies**:
  - `asyncio` >= 4.0.0 - Asynchronous I/O support
  - `pydantic` >= 2.13.4 - Data validation and serialization
  - `websockets` >= 16.0 - WebSocket protocol implementation

## 📂 Project Structure

```
src/client/
├── __init__.py              # Package initialization
├── __main__.py              # Entry point - starts WebSocket server
├── communication/
│   ├── __init__.py
│   └── web_sockets.py       # WebSocket server implementation
├── exec_handling/
│   ├── __init__.py
│   └── executor.py          # Task execution logic
└── helper/
    ├── __init__.py
    └── types.py             # Pydantic models (Request, Response)
```

## 🔌 Communication Protocol

### Request Format

The client expects requests in JSON format matching the `Request` model:

- `PID`: Process ID for tracking
- `ACTION_TYPE`: Type of action to execute
- `[other fields]`: Action-specific parameters

### Response Format

Responses are sent back in JSON format with:

- `STATUS`: "success" or "error"
- `CODE`: HTTP-style status code (200, 500, etc.)
- `PID`: Process ID from the request
- `ACTION_TYPE`: The action that was executed
- `OUTPUT`: Execution result or error message

## 📚 Documentation

For detailed documentation and API reference, visit:

- **[Documentation (DeepWiki)](https://deepwiki.com/Cron-Routine-Orchestrator-Webapp/CROW-Client)**
- **[CROW-Server Documentation](https://deepwiki.com/Cron-Routine-Orchestrator-Webapp/CROW-Server)**

## 🔗 Related Projects

- **[CROW-Server](https://github.com/Cron-Routine-Orchestrator-Webapp/CROW-Server)** - The orchestration server that dispatches tasks to clients
- **[CROW Organization](https://github.com/Cron-Routine-Orchestrator-Webapp)** - Main organization repository

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:

- How to submit issues
- How to create pull requests
- Code standards and best practices

## 📜 Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 📞 Support

If you encounter any issues or have questions:

- Open an [issue](https://github.com/Cron-Routine-Orchestrator-Webapp/CROW-Client/issues) on GitHub
- Check the [documentation](https://deepwiki.com/Cron-Routine-Orchestrator-Webapp/CROW-Client)
- Review existing discussions in the repository
