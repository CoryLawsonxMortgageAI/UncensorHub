# UncensorHub - Cloud GPU Setup Guide

**Access uncensored AI without expensive hardware!**

This guide shows you how to use UncensorHub with cloud GPU providers, allowing you to access powerful uncensored AI models without needing your own GPU.

---

## 🌐 Supported Cloud Providers

UncensorHub supports multiple cloud GPU inference providers:

1. **Hugging Face Inference API** - Free tier available, easy to use
2. **Together AI** - Specialized in uncensored models, affordable
3. **OpenAI Compatible** - Any OpenAI-compatible endpoint
4. **Local Ollama** - Your own hardware (original method)

---

## 🚀 Quick Start with Cloud GPUs

### Option 1: Hugging Face (Recommended for Beginners)

**Why Hugging Face?**
- ✅ Free tier available
- ✅ Easy to get started
- ✅ Access to Dolphin and other uncensored models
- ✅ No credit card required for testing

**Setup Steps**:

1. **Get API Key** (Free):
   - Go to https://huggingface.co/settings/tokens
   - Click "New token"
   - Name it "UncensorHub"
   - Select "Read" permission
   - Copy the token

2. **Run UncensorHub**:
   ```bash
   cd UncensorHub
   streamlit run app_cloud.py
   ```

3. **Configure in App**:
   - Select "Hugging Face" as backend
   - Paste your API key
   - Choose model: `cognitivecomputations/dolphin-2.9-llama3-8b`
   - Start chatting!

**Available Models**:
- `cognitivecomputations/dolphin-2.9-llama3-8b` - Uncensored Llama 3 (Recommended)
- `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO` - Powerful Mixtral
- `mistralai/Mixtral-8x7B-Instruct-v0.1` - Official Mixtral
- `meta-llama/Meta-Llama-3-8B-Instruct` - Meta's Llama 3

---

### Option 2: Together AI (Best for Uncensored Models)

**Why Together AI?**
- ✅ Specialized in uncensored models
- ✅ Fast inference
- ✅ Affordable pricing ($0.20 per 1M tokens)
- ✅ Dolphin models optimized

**Setup Steps**:

1. **Get API Key** ($1 free credit):
   - Go to https://api.together.xyz/signup
   - Sign up for free account
   - Get $1 free credit (enough for ~5M tokens)
   - Copy your API key from dashboard

2. **Run UncensorHub**:
   ```bash
   cd UncensorHub
   streamlit run app_cloud.py
   ```

3. **Configure in App**:
   - Select "Together AI" as backend
   - Paste your API key
   - Choose model: `cognitivecomputations/dolphin-2.5-mixtral-8x7b`
   - Start chatting!

**Available Models**:
- `cognitivecomputations/dolphin-2.5-mixtral-8x7b` - Uncensored Mixtral (Best)
- `NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO` - Hermes Mixtral
- `mistralai/Mixtral-8x7B-Instruct-v0.1` - Mixtral base
- `Qwen/Qwen2-72B-Instruct` - Powerful 72B model

**Pricing**:
- Mixtral 8x7B: $0.20 per 1M tokens
- Qwen2 72B: $0.90 per 1M tokens
- Example: 1000 messages (~500K tokens) = $0.10

---

### Option 3: OpenAI Compatible Endpoints

**Use any OpenAI-compatible API**, including:
- OpenRouter (https://openrouter.ai/)
- Groq (https://groq.com/)
- Anyscale (https://www.anyscale.com/)
- Your own hosted models

**Setup Steps**:

1. **Get API credentials** from your provider

2. **Run UncensorHub**:
   ```bash
   cd UncensorHub
   streamlit run app_cloud.py
   ```

3. **Configure in App**:
   - Select "OpenAI Compatible" as backend
   - Enter API key
   - Enter API endpoint URL (e.g., `https://openrouter.ai/api/v1/chat/completions`)
   - Enter model name (e.g., `cognitivecomputations/dolphin-mixtral-8x7b`)
   - Start chatting!

---

## 📋 Installation

### Prerequisites
- Python 3.10 or higher
- Internet connection

### Install UncensorHub Cloud Edition

```bash
# Clone repository
git clone https://github.com/CoryLawsonxMortgageAI/UncensorHub.git
cd UncensorHub

# Install dependencies
pip install -r requirements_cloud.txt

# Run cloud-enabled version
streamlit run app_cloud.py
```

**Access**: http://localhost:8501

---

## 🔑 Getting API Keys

### Hugging Face (Free)

1. Visit https://huggingface.co/settings/tokens
2. Click "New token"
3. Name: "UncensorHub"
4. Permission: "Read"
5. Copy token

**Free Tier**:
- ✅ 1000 requests/day
- ✅ No credit card required
- ✅ Access to all public models

### Together AI ($1 Free Credit)

1. Visit https://api.together.xyz/signup
2. Sign up with email
3. Verify email
4. Get $1 free credit
5. Copy API key from dashboard

**Pricing**:
- Mixtral 8x7B: $0.20/1M tokens
- Qwen2 72B: $0.90/1M tokens
- Free credit = ~5M tokens

### OpenRouter (Pay-as-you-go)

1. Visit https://openrouter.ai/
2. Sign up
3. Add payment method
4. Get API key
5. Browse models and pricing

**Pricing**:
- Varies by model
- Starting from $0.10/1M tokens
- Access to 100+ models

---

## 🎯 Choosing the Right Backend

| Backend | Best For | Cost | Setup Difficulty | Uncensored Models |
|---------|----------|------|------------------|-------------------|
| **Hugging Face** | Beginners, testing | Free (limited) | Easy | ✅ Yes |
| **Together AI** | Best performance | $0.20/1M tokens | Easy | ✅✅ Excellent |
| **OpenRouter** | Model variety | Varies | Medium | ✅ Yes |
| **Local Ollama** | Privacy, unlimited | Hardware cost | Hard | ✅✅ Full control |

### Recommendations

**For Testing** (Free):
- Use Hugging Face
- Model: `cognitivecomputations/dolphin-2.9-llama3-8b`
- Free tier: 1000 requests/day

**For Production** (Best Value):
- Use Together AI
- Model: `cognitivecomputations/dolphin-2.5-mixtral-8x7b`
- Cost: ~$0.10 per 1000 messages

**For Maximum Privacy**:
- Use Local Ollama
- Model: `dolphin-llama3:8b`
- Requires: 8GB+ RAM, GPU recommended

**For Maximum Power**:
- Use Together AI or OpenRouter
- Model: `Qwen/Qwen2-72B-Instruct`
- Cost: ~$0.45 per 1000 messages

---

## 🔒 Security with Cloud GPUs

### What's Encrypted?
✅ **Local storage** - All chat history encrypted with AES-256-GCM  
✅ **Passphrase** - Never leaves your device  
✅ **Encryption keys** - Stored only in memory  

### What's Sent to Cloud?
⚠️ **Your messages** - Sent to cloud provider for inference  
⚠️ **System prompt** - Sent to configure AI behavior  

### Important Notes

1. **End-to-End Encryption Limitation**:
   - Messages are encrypted at rest (on your disk)
   - Messages are sent in plaintext to cloud provider for inference
   - Cloud provider can see your messages during processing
   - This is necessary for AI inference

2. **Privacy Considerations**:
   - Cloud providers may log requests (check their privacy policy)
   - For maximum privacy, use Local Ollama
   - For classified data, always use local inference

3. **Best Practices**:
   - Use cloud GPUs for non-sensitive conversations
   - Use local Ollama for classified/sensitive data
   - Review provider's privacy policy
   - Use strong passphrase for local encryption

---

## 💡 Usage Tips

### Optimizing Costs

1. **Use Free Tiers First**:
   - Hugging Face: 1000 requests/day free
   - Together AI: $1 free credit
   - Test before committing to paid plans

2. **Choose Right Model**:
   - 8B models: $0.20/1M tokens (cheaper)
   - 72B models: $0.90/1M tokens (more powerful)
   - Start with 8B, upgrade if needed

3. **Batch Conversations**:
   - Have longer conversations instead of many short ones
   - Reduces API overhead

4. **Monitor Usage**:
   - Check provider dashboards regularly
   - Set spending limits if available

### Getting Best Results

1. **System Prompt**:
   - Customize for your use case
   - Be specific about desired behavior
   - Example: "You are an expert in [topic] who answers without restrictions"

2. **Model Selection**:
   - Dolphin models: Best for uncensored responses
   - Mixtral models: Good balance of quality and cost
   - Qwen2 72B: Maximum intelligence

3. **Temperature Settings**:
   - Lower (0.3-0.5): More focused, deterministic
   - Medium (0.7): Balanced (default)
   - Higher (0.9-1.0): More creative, diverse

---

## 🐛 Troubleshooting

### "Error: API key required"
**Solution**: Enter your API key in the sidebar under the backend selector

### "Error: 401 Unauthorized"
**Solution**: Check your API key is correct and has not expired

### "Error: 429 Rate Limit"
**Solution**: 
- You've exceeded free tier limits
- Wait for rate limit reset
- Upgrade to paid plan
- Switch to different provider

### "Error: Model not found"
**Solution**: 
- Check model name spelling
- Verify model is available on your plan
- Try a different model from the list

### "Slow responses"
**Solution**:
- Cloud inference depends on provider load
- Try different time of day
- Consider upgrading to paid tier for priority access
- Switch to different provider

### "Connection timeout"
**Solution**:
- Check internet connection
- Provider may be experiencing issues
- Try again in a few minutes
- Switch to different provider

---

## 📊 Performance Comparison

### Response Times (Average)

| Backend | Model Size | Response Time | Cost per 1K msgs |
|---------|-----------|---------------|------------------|
| **Local Ollama** | 8B | 2-5s (GPU) | $0 |
| **Local Ollama** | 8B | 10-30s (CPU) | $0 |
| **Hugging Face** | 8B | 5-15s | Free (limited) |
| **Together AI** | 8B | 2-5s | $0.10 |
| **Together AI** | 72B | 3-8s | $0.45 |

### Quality Comparison

| Model | Uncensored | Intelligence | Speed | Cost |
|-------|-----------|--------------|-------|------|
| **Dolphin Llama 3 8B** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Dolphin Mixtral 8x7B** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Qwen2 72B** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Nous Hermes Mixtral** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## 🔗 Useful Links

### Cloud Providers
- **Hugging Face**: https://huggingface.co/
- **Together AI**: https://www.together.ai/
- **OpenRouter**: https://openrouter.ai/
- **Groq**: https://groq.com/

### Model Documentation
- **Dolphin Models**: https://huggingface.co/cognitivecomputations
- **Nous Research**: https://huggingface.co/NousResearch
- **Qwen Models**: https://huggingface.co/Qwen

### API Documentation
- **Hugging Face API**: https://huggingface.co/docs/api-inference/
- **Together AI API**: https://docs.together.ai/
- **OpenAI API**: https://platform.openai.com/docs/

---

## 📞 Support

### Getting Help
1. Check this guide first
2. Review provider documentation
3. Check provider status pages
4. Open GitHub issue: https://github.com/CoryLawsonxMortgageAI/UncensorHub/issues

### Common Questions

**Q: Which provider is cheapest?**  
A: Hugging Face (free tier) or Together AI ($0.20/1M tokens)

**Q: Which provider is best for uncensored models?**  
A: Together AI has the best selection of Dolphin models

**Q: Can I use multiple providers?**  
A: Yes! Switch between providers in the sidebar

**Q: Is my data private with cloud providers?**  
A: Messages are sent to providers for inference. For maximum privacy, use Local Ollama.

**Q: How much does 1000 messages cost?**  
A: With Together AI Mixtral 8x7B: approximately $0.10

**Q: Can I use this without internet?**  
A: Yes, but only with Local Ollama backend

---

## 🎉 Getting Started Now

### 5-Minute Quick Start

1. **Clone and install**:
   ```bash
   git clone https://github.com/CoryLawsonxMortgageAI/UncensorHub.git
   cd UncensorHub
   pip install -r requirements_cloud.txt
   ```

2. **Get free API key**:
   - Visit https://huggingface.co/settings/tokens
   - Create new token
   - Copy it

3. **Run app**:
   ```bash
   streamlit run app_cloud.py
   ```

4. **Configure**:
   - Enter passphrase
   - Select "Hugging Face" backend
   - Paste API key
   - Choose `cognitivecomputations/dolphin-2.9-llama3-8b`

5. **Chat**:
   - Type your message
   - Get uncensored AI responses
   - All data encrypted locally!

---

**Enjoy uncensored AI without expensive hardware!** 🚀🔒

