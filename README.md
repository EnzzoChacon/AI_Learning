# 🤖 Gemini Vision Chatbot (Python)

An interactive terminal chatbot integrated with Google Gemini API. Built as part of my AI development learning journey, this application supports conversation history and multimodal input (local image analysis).

---

## 🛠️ Tech Stack

- **Python 3.14+**
- **Google GenAI SDK** (`google-genai`)
- **Pillow (`PIL`)** for image processing
- **python-dotenv** for secure environment variable management

---

## 🧠 Key Learnings

- Secure API authentication using environment variables (`.env`).
- Session management with active chat history.
- Multimodal processing (analyzing local image inputs alongside prompt texts).
- Git best practices using `.gitignore` to protect sensitive credentials.

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/EnzzoChacon/AI_Learning.git
   cd AI_Learning

Install dependencies:

    ```bash
pip install -r requirements.txt

2. **Set up environment variables:**

Create a .env file in the root directory following .env.example:

GEMINI_API_KEY=your_api_key_here

3. **Run the script:**

python chatbot.py