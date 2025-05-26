# Welcome to the ACP/A2A/MCP Multi-Protocol Agentic Chat Client 🤖💬

Effortlessly interact with multiple protocols using a lightweight, intuitive command-line chat interface. Whether you're managing ACP, A2A, or MCP agents, this tool has you covered!

[![Python](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue)](LICENSE)

## ✨ Features

- 🔄 Command history support
- 📝 Support for multiline inputs
- 🚀 Lightweight and fast
- 🔌 Easy integration with multiple protocols (ACP, A2A, MCP)
- 💬 Friendly and intuitive chat UI for the command-line interface

## ⚙️ Setup

### Create/Update `.env`

```env
## ACP Agent Configuration
CNOE_AGENT_ARGOCD_API_KEY=
CNOE_AGENT_ARGOCD_ID=
CNOE_AGENT_ARGOCD_PORT=10000

## A2A Agent Configuration
A2A_AGENT_HOST=localhost
A2A_AGENT_PORT=8000

## MCP Server Configuration
MCP_HOST=localhost
MCP_PORT=9000
```

## 🚀 Usage

### Running with UV

```bash
```bash
uv run github.com/cnoe-io/agent-chat-cli <acp|a2a|mcp>
```

## Quick Demos

### AGNTCY ACP Demo

![acp_docker_terminal_demo](https://github.com/user-attachments/assets/9f090ce4-87f3-4bc7-8857-2ea4647187d5)

### Google A2A Demo

![a2a_docker_terminal_demo](https://github.com/user-attachments/assets/2a84fd6b-102f-425b-8312-501b47c11e81)

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.