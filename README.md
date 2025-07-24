# 🚀 Automated Instagram Poster

This project enables you to automatically post on Instagram using a Flask-based Python server, **ngrok** for public URL access, and **n8n** for workflow automation.

## 🛠️ Setup Instructions (All-in-One)

### 1. Install Python
Download and install Python from the official website:  
🔗 https://www.python.org/downloads

Verify the installation:
```bash
python --version
# or
python3 --version
```

---

### 2. Install Virtual Environment
```bash
pip install virtualenv
```

---

### 3. Create & Activate Virtual Environment

**On Windows:**
```bash
virtualenv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
virtualenv venv
source venv/bin/activate
```

---

### 4. Install Project Dependencies
```bash
pip install -r requirements.txt
```

---

### 5. Start the Flask Server
```bash
python Server.py
```

---

### 6. Make the Server Public Using ngrok

Open a new terminal window and run:
```bash
ngrok http 5000
```

Copy the generated public URL (e.g., `https://xyz.ngrok.io`) — you’ll need it for your n8n workflow.

---

### 7. Use n8n to Automate Instagram Posts

- Import the provided **n8n workflow JSON** into your n8n instance.
- Replace any placeholder URLs in the workflow with your actual ngrok URL.
- Trigger the workflow manually or on a schedule.

---

### 8. Shut Down Services Safely

To stop everything:
```bash
# In both terminals:
CTRL + C

# Then deactivate your environment:
deactivate
```

✅ Done! Your automation setup is complete.
