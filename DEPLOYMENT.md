# UncensorHub Deployment Guide

## Deployment Status

✅ **Successfully Deployed**

- **Repository**: https://github.com/CoryLawsonxMortgageAI/UncensorHub
- **License**: MIT
- **Status**: Public, ready for cloning
- **Last Updated**: October 24, 2025

## Quick Clone & Deploy

```bash
# Clone the repository
git clone https://github.com/CoryLawsonxMortgageAI/UncensorHub.git
cd UncensorHub

# Install Ollama (if not already installed)
curl -fsSL https://ollama.com/install.sh | sh

# Pull the AI model
ollama pull dolphin-llama3:8b

# Install Python dependencies
pip install -r requirements.txt

# Start Ollama server (in separate terminal)
ollama serve

# Run the application
streamlit run app.py
```

Access at: `http://localhost:8501`

## Deployment Options

### Option 1: Local Deployment (Recommended)

**Best for**: Privacy, security, classified use cases

**Requirements**:
- Python 3.10+
- Ollama installed locally
- 8GB+ RAM (16GB recommended)
- Optional: GPU with 6GB+ VRAM

**Steps**: See Quick Clone & Deploy above

**Advantages**:
- Complete privacy (no external API calls)
- Full E2EE protection
- Uncensored AI responses
- No internet dependency after setup

### Option 2: Self-Hosted Server

**Best for**: Team use, always-on access

**Requirements**:
- Linux server (Ubuntu 22.04 recommended)
- 16GB+ RAM
- GPU recommended
- Static IP or domain name

**Steps**:
1. Set up server with SSH access
2. Install Ollama and Python dependencies
3. Configure firewall (allow port 8501)
4. Run with systemd service

### Option 3: Docker Deployment

**Best for**: Containerized environments, easy scaling

Create a Dockerfile in the project root and build the container image for consistent deployment across environments.

## Security Considerations

### Production Deployment Checklist

- Use strong passphrase (12+ characters)
- Backup `.salt` file securely
- Regular encrypted history exports
- Keep Ollama updated
- Monitor system resources
- Configure firewall rules
- Use HTTPS for remote access
- Implement rate limiting (if public)
- Regular security audits

### Network Security

For remote access, use SSH tunneling, VPN, or reverse proxy with SSL/TLS to ensure encrypted communication channels.

## Troubleshooting

### Issue: Ollama connection failed

Check if Ollama is running and restart the service if necessary. Verify the connection at `http://localhost:11434`.

### Issue: Model requires more memory

Use a smaller model like `llama3.2:1b`, add swap space, or upgrade system RAM/GPU.

### Issue: Streamlit port already in use

Find and terminate the process using port 8501, or specify a different port when starting Streamlit.

### Issue: Encryption key mismatch

Verify the correct passphrase is being used and that the `.salt` file exists. Restore from backup if needed.

## Performance Optimization

### For Better Response Times

Enable GPU acceleration by installing CUDA drivers. Ollama automatically detects and utilizes available GPUs for faster inference.

### For Lower Memory Usage

Use quantized models (e.g., `dolphin-llama3:8b-q4_0`) and limit the context length by keeping only recent messages in the conversation history.

## Monitoring

### Check Application Health

Monitor Streamlit logs, check Ollama status via API, and track system resources using standard monitoring tools.

### Backup Strategy

Implement automated backups of `encrypted_history.json` and `.salt` files. Schedule regular backups using cron jobs and maintain retention policies.

## Scaling

### Multi-User Setup

For multiple users, consider running separate instances per user, sharing a single Ollama server across multiple Streamlit apps, or implementing user authentication.

### Load Balancing

For high traffic scenarios, run multiple Streamlit instances on different ports and use a reverse proxy like Nginx for load distribution.

## Updates & Maintenance

### Updating the Application

Pull the latest changes from GitHub, upgrade dependencies, and clear the Streamlit cache to ensure all updates are applied.

### Updating Models

Regularly update Ollama models to benefit from improvements and bug fixes. Remove unused models to free up disk space.

## Support & Community

- **Issues**: https://github.com/CoryLawsonxMortgageAI/UncensorHub/issues
- **Discussions**: GitHub Discussions tab
- **Documentation**: README.md and wiki

## License

MIT License - See LICENSE file for details

---

**Deployment complete! Enjoy secure, uncensored AI conversations with UncensorHub.**

