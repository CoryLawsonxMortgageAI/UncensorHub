# UncensorHub Screenshots

## Main Interface

The UncensorHub interface features a clean, modern design inspired by HuggingChat:

### Login Screen
- Passphrase entry with security validation
- First-time setup instructions
- Security warning banner

### Chat Interface
- **Left Sidebar**: 
  - Model selection dropdown (Dolphin, Llama, Qwen, Gemma)
  - System prompt customization
  - Clear chat button
  - Export/Import history
  - Lock & Exit button
  
- **Center Area**:
  - User messages with 👤 avatar (light blue background)
  - AI messages with 🤖 avatar (gray background)
  - Timestamps for each message
  - Smooth scrolling chat history

- **Bottom Input**:
  - Text input bar for new messages
  - Send on Enter key

### Features Visible in UI
- 🔒 Encryption indicator in title
- ⚠️ Security warning banner
- 💬 Message count in sidebar
- 🔐 Encryption status indicator

## To Add Screenshots

After running the application:

1. Start the app: `streamlit run app.py`
2. Take screenshots of:
   - Login/passphrase screen
   - Main chat interface with sample conversation
   - Sidebar settings panel
   - Export/import functionality
3. Save as:
   - `screenshots/login.png`
   - `screenshots/chat_interface.png`
   - `screenshots/sidebar.png`
4. Update README.md with image links

## Live Demo

For a live demonstration, run locally:
```bash
streamlit run app.py
```

Then navigate to `http://localhost:8501`
