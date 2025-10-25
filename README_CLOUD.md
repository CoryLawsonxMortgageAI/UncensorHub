# 🔒 UncensorHub - Cloud GPU Edition

**Secure, End-to-End Encrypted AI Chat with Cloud GPU Support**

Access powerful uncensored AI models without expensive hardware! UncensorHub now supports cloud GPU inference from multiple providers while maintaining end-to-end encryption for your local chat history.

---

## 🌟 What's New in Cloud Edition?

### ✅ Cloud GPU Support
- **Hugging Face Inference API** - Free tier available
- **Together AI** - Specialized uncensored models ($0.20/1M tokens)
- **OpenAI Compatible** - Any OpenAI-compatible endpoint
- **Local Ollama** - Original local inference (still supported)

### ✅ No Expensive Hardware Needed
- Access Dolphin 8B models without 8GB+ RAM
- Use 72B models without high-end GPU
- Pay only for what you use
- Free tiers available for testing

### ✅ Same Security
- AES-256-GCM encryption for local storage
- PBKDF2 key derivation (100,000 iterations)
- Passphrase protection
- No plaintext on disk

---

## 🚀 Quick Start

### Option 1: Cloud GPU (Recommended for Most Users)

**No GPU or powerful hardware needed!**

```bash
# Clone repository
git clone https://github.com/CoryLawsonxMortgageAI/UncensorHub.git
cd UncensorHub

# Install dependencies
pip install -r requirements_cloud.txt

# Run cloud-enabled version
streamlit run app_cloud.py
```

**Get Free API Key**:
1. Visit https://huggingface.co/settings/tokens
2. Create new token (Read permission)
3. Copy token

**Configure in App**:
1. Enter passphrase (min 8 characters)
2. Select "Hugging Face" backend
3. Paste API key
4. Choose model: `cognitivecomputations/dolphin-2.9-llama3-8b`
5. Start chatting!

**Access**: http://localhost:8501

---

### Option 2: Local Ollama (Maximum Privacy)

**Requires 8GB+ RAM and GPU recommended**

```bash
# Clone repository
git clone https://github.com/CoryLawsonxMortgageAI/UncensorHub.git
cd UncensorHub

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull model
ollama pull dolphin-llama3:8b

# Install dependencies
pip install -r requirements.txt

# Start Ollama (separate terminal)
ollama serve

# Run app
streamlit run app.py
```

**Access**: http://localhost:8501

---

## 🌐 Supported Cloud Providers

| Provider | Cost | Free Tier | Best For | Setup Difficulty |
|----------|------|-----------|----------|------------------|
| **Hugging Face** | Free (limited) | ✅ 1000 req/day | Testing, beginners | Easy |
| **Together AI** | $0.20/1M tokens | ✅ $1 credit | Production, best models | Easy |
| **OpenRouter** | Varies | ❌ Pay-as-you-go | Model variety | Medium |
| **Local Ollama** | Hardware cost | ✅ Unlimited | Privacy, control | Hard |

### Recommended Setup

**For Testing** (Free):
- Provider: Hugging Face
- Model: `cognitivecomputations/dolphin-2.9-llama3-8b`
- Cost: Free (1000 requests/day)

**For Production** (Best Value):
- Provider: Together AI
- Model: `cognitivecomputations/dolphin-2.5-mixtral-8x7b`
- Cost: ~$0.10 per 1000 messages

**For Maximum Privacy**:
- Provider: Local Ollama
- Model: `dolphin-llama3:8b`
- Cost: Hardware only

---

## 📊 Available Models

### Hugging Face
- `cognitivecomputations/dolphin-2.9-llama3-8b` ⭐ Recommended
- `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO`
- `mistralai/Mixtral-8x7B-Instruct-v0.1`
- `meta-llama/Meta-Llama-3-8B-Instruct`

### Together AI
- `cognitivecomputations/dolphin-2.5-mixtral-8x7b` ⭐ Best Quality
- `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO`
- `mistralai/Mixtral-8x7B-Instruct-v0.1`
- `Qwen/Qwen2-72B-Instruct` ⭐ Most Powerful

### Local Ollama
- `dolphin-llama3:8b` ⭐ Recommended
- `llama3.2:1b` (lightweight)
- `qwen3-abliterated`
- `gemma3-abliterated`

---

## 💰 Pricing Comparison

### Cost per 1000 Messages (~500K tokens)

| Provider | Model | Cost | Quality | Speed |
|----------|-------|------|---------|-------|
| **Hugging Face** | Dolphin 8B | Free* | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Together AI** | Dolphin Mixtral | $0.10 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Together AI** | Qwen2 72B | $0.45 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Local Ollama** | Dolphin 8B | $0** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

\* Free tier: 1000 requests/day  
\*\* One-time hardware cost

**Example**: 10,000 messages per month with Together AI Mixtral = $1.00

---

## 🔒 Security & Privacy

### What's Encrypted?
✅ **Local chat history** - AES-256-GCM encryption  
✅ **Passphrase** - Never leaves your device  
✅ **Encryption keys** - Stored only in memory  
✅ **Exported backups** - Fully encrypted  

### What's Sent to Cloud?
⚠️ **Your messages** - Sent to cloud provider for AI inference  
⚠️ **System prompt** - Sent to configure AI behavior  

### Important Privacy Notes

**Cloud Inference**:
- Messages are encrypted at rest (on your disk)
- Messages are sent in plaintext to cloud provider for inference
- This is necessary for AI to process your requests
- Cloud providers may log requests (check their privacy policy)

**For Maximum Privacy**:
- Use Local Ollama for sensitive/classified data
- Use cloud GPUs for non-sensitive conversations
- Review provider privacy policies
- Choose providers with strong privacy commitments

**Comparison**:

| Aspect | Local Ollama | Cloud GPU |
|--------|--------------|-----------|
| **Local Storage** | ✅ Encrypted | ✅ Encrypted |
| **In Transit** | ✅ Never leaves device | ⚠️ Sent to provider |
| **Provider Access** | ✅ None | ⚠️ Can see messages |
| **Privacy Level** | ✅✅✅ Maximum | ⚠️ Depends on provider |

---

## 📋 Features

### Core Features
- ✅ End-to-end encryption (AES-256-GCM)
- ✅ Passphrase protection (PBKDF2, 100K iterations)
- ✅ Multiple inference backends
- ✅ Cloud GPU support
- ✅ Local Ollama support
- ✅ Model switching
- ✅ Custom system prompts
- ✅ Chat history export/import
- ✅ Encrypted backups
- ✅ HuggingChat-inspired UI

### Cloud Features
- ✅ Hugging Face Inference API
- ✅ Together AI integration
- ✅ OpenAI-compatible endpoints
- ✅ Automatic API key management
- ✅ Backend switching
- ✅ Cost-effective inference

---

## 🎯 Use Cases

### Personal Use
- **Research**: Explore topics without censorship
- **Creative Writing**: Generate uncensored content
- **Learning**: Ask any questions freely
- **Brainstorming**: Unrestricted ideation

### Professional Use
- **Security Research**: Discuss vulnerabilities openly
- **Content Moderation**: Test filtering systems
- **AI Safety**: Research alignment issues
- **Education**: Teach about AI limitations

### Development
- **API Testing**: Test uncensored model APIs
- **Prompt Engineering**: Develop effective prompts
- **Model Comparison**: Compare different models
- **Integration**: Build on top of UncensorHub

---

## 📖 Documentation

### Quick Links
- **[Cloud GPU Setup Guide](CLOUD_GPU_GUIDE.md)** - Detailed cloud setup
- **[Deployment Guide](DEPLOYMENT.md)** - Deployment options
- **[Test Results](TEST_RESULTS.md)** - Unit test results
- **[Live Test Report](LIVE_TEST_REPORT.md)** - Live testing
- **[Project Summary](PROJECT_SUMMARY.md)** - Technical details

### Getting API Keys
- **Hugging Face**: https://huggingface.co/settings/tokens
- **Together AI**: https://api.together.xyz/signup
- **OpenRouter**: https://openrouter.ai/

---

## 🛠️ Installation

### System Requirements

**For Cloud GPU Edition**:
- Python 3.10 or higher
- 2GB RAM (minimal)
- Internet connection
- No GPU required!

**For Local Ollama**:
- Python 3.10 or higher
- 8GB+ RAM (16GB recommended)
- GPU with 6GB+ VRAM (recommended)
- 10GB disk space

### Install Steps

```bash
# Clone repository
git clone https://github.com/CoryLawsonxMortgageAI/UncensorHub.git
cd UncensorHub

# Install dependencies
pip install -r requirements_cloud.txt

# Run cloud-enabled version
streamlit run app_cloud.py

# OR run local-only version
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎨 User Interface

### Features
- **Clean Design**: HuggingChat-inspired interface
- **Sidebar Controls**: Easy access to settings
- **Backend Selector**: Switch between providers
- **Model Selector**: Choose from available models
- **API Key Input**: Secure key management
- **System Prompt Editor**: Customize AI behavior
- **Chat History**: Persistent encrypted storage
- **Export/Import**: Backup functionality
- **Security Indicators**: Encryption status visible

### Screenshots
See `screenshots/` directory for live application images.

---

## 🐛 Troubleshooting

### Common Issues

**"Error: API key required"**
- Solution: Enter API key in sidebar

**"Error: 401 Unauthorized"**
- Solution: Check API key is valid

**"Error: 429 Rate Limit"**
- Solution: Exceeded free tier, wait or upgrade

**"Slow responses"**
- Solution: Try different provider or time of day

**"Model not found"**
- Solution: Check model name spelling

See [Cloud GPU Guide](CLOUD_GPU_GUIDE.md) for detailed troubleshooting.

---

## 📊 Performance

### Response Times (Average)

| Backend | Model | Response Time |
|---------|-------|---------------|
| Local Ollama (GPU) | 8B | 2-5 seconds |
| Local Ollama (CPU) | 8B | 10-30 seconds |
| Hugging Face | 8B | 5-15 seconds |
| Together AI | 8B | 2-5 seconds |
| Together AI | 72B | 3-8 seconds |

### Quality Comparison

| Model | Uncensored | Intelligence | Speed |
|-------|-----------|--------------|-------|
| Dolphin Llama 3 8B | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Dolphin Mixtral 8x7B | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Qwen2 72B | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file

---

## ⚠️ Disclaimer

**Legal & Ethical Use**:
- This tool is for legitimate research, education, and personal use
- Users are responsible for compliance with local laws
- Do not use for illegal activities
- Respect provider terms of service
- Use ethically and responsibly

**Privacy**:
- Cloud providers may log requests
- Review provider privacy policies
- Use local inference for sensitive data
- Encryption protects local storage only

**No Warranty**:
- Provided "as is" without warranty
- Use at your own risk
- Not responsible for misuse

---

## 🔗 Links

- **Repository**: https://github.com/CoryLawsonxMortgageAI/UncensorHub
- **Issues**: https://github.com/CoryLawsonxMortgageAI/UncensorHub/issues
- **Live Demo**: See repository for demo link

---

## 🎉 Get Started Now!

### 3-Step Quick Start

1. **Clone & Install**:
   ```bash
   git clone https://github.com/CoryLawsonxMortgageAI/UncensorHub.git
   cd UncensorHub
   pip install -r requirements_cloud.txt
   ```

2. **Get Free API Key**:
   - Visit https://huggingface.co/settings/tokens
   - Create token, copy it

3. **Run & Chat**:
   ```bash
   streamlit run app_cloud.py
   ```
   - Enter passphrase
   - Select "Hugging Face"
   - Paste API key
   - Start chatting!

**Enjoy uncensored AI without expensive hardware!** 🚀🔒

---

**Made with ❤️ by the UncensorHub community**

