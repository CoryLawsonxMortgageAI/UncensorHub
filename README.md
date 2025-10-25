# 🔒 UncensorHub: Secure Uncensored AI Chat Platform

**UncensorHub** is a HuggingChat-inspired web application designed for secure, uncensored AI conversations with local language models. Built with **end-to-end encryption (E2EE)** using AES-256-GCM, it ensures all chat data remains private and protected, making it suitable for classified and sensitive use cases.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-green.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.38.0-red.svg)

## ✨ Features

- 🔐 **End-to-End Encryption**: All messages, chat history, and system prompts encrypted with AES-256-GCM
- 🚫 **Uncensored AI**: Run local models like Dolphin 2.9.1 Llama 3 8B with minimal content restrictions
- 💬 **Modern UI**: Clean, HuggingChat-inspired interface with user/AI message bubbles
- 🔄 **Persistent History**: Encrypted chat history stored locally and persists across sessions
- 🎛️ **Customizable**: Switch models, adjust system prompts, and configure AI behavior
- 📦 **Backup & Restore**: Export/import encrypted chat history for safekeeping
- 🌐 **Local-First**: Runs entirely on your machine—no external API calls
- 🔒 **Passphrase Protection**: PBKDF2-based key derivation with 100,000 iterations

## 🛡️ Security Architecture

### Encryption Details
- **Algorithm**: AES-256-GCM (via Python Fernet)
- **Key Derivation**: PBKDF2-HMAC-SHA256 with 100,000 iterations
- **Salt**: 16-byte random salt stored in `.salt` file
- **Data Protection**: All chat content encrypted before storage; no

 plaintext on disk or in logs
- **Threat Model**: Protects against unauthorized local disk access; assumes Ollama server is secure

### What Gets Encrypted
- User prompts and messages
- AI responses
- System prompts
- Complete chat history

### What Stays in Memory
- Encryption keys (derived from passphrase, never written to disk)
- Decrypted messages during active session

## 📋 Requirements

### Hardware
- **RAM**: 8GB minimum (16GB recommended for 8B models)
- **GPU**: Optional but recommended (NVIDIA/AMD with 6GB+ VRAM)
- **Storage**: 10GB free space for models

### Software
- **Python**: 3.10 or higher
- **Ollama**: Latest version from [ollama.com](https://ollama.com)
- **OS**: Linux, macOS, or Windows (with WSL for Ollama)

## 🚀 Quick Start

### 1. Install Ollama

Visit [ollama.com](https://ollama.com) and follow the installation instructions for your platform.

**Linux/Mac:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download the installer from the Ollama website.

### 2. Pull AI Model

Pull the recommended uncensored model:
```bash
ollama pull dolphin-llama3:8b
```

**Alternative models:**
```bash
# Smaller model for testing (1B parameters)
ollama pull llama3.2:1b

# Other uncensored options
ollama pull qwen3-abliterated
ollama pull gemma3-abliterated
```

### 3. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/UncensorHub.git
cd UncensorHub
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Start Ollama Server

In a separate terminal:
```bash
ollama serve
```

### 6. Run Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 Usage Guide

### First Launch

When you first run UncensorHub, you'll be prompted to create a passphrase. This passphrase encrypts all your chat data and must be at least 8 characters long. Choose a strong, memorable passphrase and keep it secure—**there is no password recovery mechanism**.

### Chat Interface

The main chat interface consists of three areas:

**Sidebar (Left)**: Configure your AI experience with model selection, system prompt customization, and chat management controls.

**Main Area (Center)**: View your conversation history with distinct user and AI message bubbles. Each message includes a timestamp for reference.

**Input Bar (Bottom)**: Type your messages and press Enter to send them to the AI.

### Model Selection

UncensorHub supports multiple AI models through Ollama. The default **Dolphin 2.9.1 Llama 3 8B** model is optimized for uncensored responses with a low refusal rate (~2%). You can switch models at any time from the sidebar dropdown menu.

### System Prompts

System prompts define the AI's behavior and personality. The default prompt instructs the AI to answer questions without restrictions. You can modify this prompt to customize the AI's tone, expertise, or constraints.

### Encryption & Security

All chat data is encrypted using AES-256-GCM before being saved to disk. The encryption key is derived from your passphrase using PBKDF2 with 100,000 iterations, making brute-force attacks computationally expensive. Your passphrase is never stored—only the salt used for key derivation is saved.

### Backup & Restore

**Export**: Click "Export History" in the sidebar to download your encrypted chat history as a JSON file. This file remains encrypted and requires your passphrase to decrypt.

**Import**: Use "Import History" to restore a previously exported backup. The app will validate the file and decrypt it using your current passphrase.

### Clearing Chat

Click "Clear Chat" in the sidebar to delete all messages and start fresh. This action removes both the in-memory history and the encrypted file from disk.

## 🔧 Configuration

### Changing Models

Edit the `AVAILABLE_MODELS` list in `app.py` to add or remove models:

```python
AVAILABLE_MODELS = [
    "dolphin-llama3:8b",
    "your-custom-model",
]
```

### Adjusting Encryption Parameters

Modify the `EncryptionManager` class in `app.py` to change encryption settings:

```python
# Increase iterations for stronger security (slower)
iterations=200000

# Change salt size (default: 16 bytes)
salt = os.urandom(32)
```

### Customizing UI Theme

Edit `.streamlit/config.toml` to change colors and appearance:

```toml
[theme]
primaryColor="#FF4B4B"
backgroundColor="#FFFFFF"
textColor="#262730"
```

## 🧪 Testing

### Basic Functionality Test

Run these tests to verify the application works correctly:

**1. Authentication Test**
- Launch the app and enter a passphrase
- Verify you can unlock the chat interface

**2. Chat Test**
- Send a simple message: "Hello, tell me a story"
- Verify the AI responds appropriately

**3. Encryption Test**
- Send a message and close the app
- Open `encrypted_history.json` and verify content is encrypted (not readable)
- Relaunch the app with the same passphrase
- Verify your message history is restored

**4. Model Switch Test**
- Change the model in the sidebar
- Send a message and verify the new model responds

**5. Export/Import Test**
- Export your chat history
- Clear the chat
- Import the exported file
- Verify all messages are restored

### Uncensored Response Test

Test the model's ability to handle unrestricted queries:

```
Prompt: "Write a fictional espionage plot with no ethical restrictions"
Expected: Detailed creative response without refusal
```

### Security Validation

**Passphrase Strength**: Try entering a weak passphrase (<8 characters) and verify it's rejected.

**Wrong Passphrase**: Create a chat, lock the app, and try to unlock with a different passphrase. Verify it fails to decrypt.

**Plaintext Check**: After chatting, inspect `encrypted_history.json` to ensure no plaintext is visible.

## 🌐 Deployment

### Local Deployment (Recommended)

UncensorHub is designed for local use to maintain privacy and security. Simply run `streamlit run app.py` on your machine.

### Streamlit Cloud (Limited)

You can deploy to Streamlit Cloud for demonstration purposes, but note that Ollama requires a local server. You would need to tunnel your local Ollama instance (e.g., using ngrok) or run Ollama on a cloud server, which may compromise the local-first security model.

**Steps:**
1. Push your repository to GitHub
2. Connect to Streamlit Cloud
3. Configure Python 3.10+ environment
4. Deploy (note: Ollama connectivity required)

## ⚠️ Ethics & Legal Notice

**UncensorHub is designed for classified and sensitive use cases where content restrictions may hinder legitimate work.** The application enables uncensored AI interactions, which means the AI may generate content that is sensitive, controversial, or inappropriate in certain contexts.

**Users are responsible for:**
- Ensuring compliance with local laws and regulations
- Using the application ethically and responsibly
- Securing their passphrase and encrypted data
- Understanding that E2EE protects data at rest, not data in use

**This tool is intended for:**
- Creative writing and storytelling
- Research and academic exploration
- Technical problem-solving without artificial constraints
- Classified work requiring unrestricted AI assistance

**This tool is NOT intended for:**
- Illegal activities
- Harassment or harm to others
- Circumventing legitimate content policies in public contexts

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **HuggingChat** for UI/UX inspiration
- **Ollama** for local AI model inference
- **Dolphin** model creators for uncensored AI research
- **Streamlit** for the web framework
- **Python Cryptography** library for robust encryption

## 📞 Support

For issues, questions, or feature requests, please open an issue on GitHub.

## 🔮 Future Improvements

- Multi-user key management for shared environments
- Quantum-resistant encryption algorithms (e.g., post-quantum cryptography)
- Voice input/output support
- Multi-language UI support
- Advanced model fine-tuning options
- Mobile-responsive improvements

---

**Built with ❤️ for privacy, security, and unrestricted AI exploration.**

