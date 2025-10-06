from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Chatbot logic (from your existing code)
def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == 'quit':
        return "Happy studying! You've got this! 💪"

    elif 'time management' in user_input or 'schedule' in user_input:
        return "Try the Pomodoro technique: 25 min study, 5 min break. Use a planner and prioritize tasks."

    elif 'focus' in user_input or 'concentrate' in user_input:
        return "Eliminate distractions: Phone on silent, clean workspace, use website blockers. Try the 5-second rule to start."

    elif 'memorize' in user_input or 'remember' in user_input:
        return "Use active recall: Flashcards, self-testing, spaced repetition. Teach the material to someone else."

    elif 'math' in user_input or 'calculus' in user_input:
        return "Practice daily, understand concepts not just formulas, check work step-by-step, use Khan Academy for help."

    elif 'essay' in user_input or 'writing' in user_input:
        return "Outline first, write then edit, use thesis statements, proofread aloud, check grammar and flow."

    elif 'exam' in user_input or 'test' in user_input:
        return "Start early, review regularly, practice past papers, get enough sleep, eat well before the exam."

    elif 'notes' in user_input or 'note taking' in user_input:
        return "Try Cornell method, mind maps, or outline format. Use abbreviations and review notes within 24 hours."

    elif 'reading' in user_input or 'comprehension' in user_input:
        return "SQ3R method: Survey, Question, Read, Recite, Review. Take notes and summarize each section."

    elif 'group study' in user_input or 'study group' in user_input:
        return "Set clear goals, assign topics, teach each other, stay on task, and quiz one another."

    elif 'motivation' in user_input or 'procrastinate' in user_input:
        return "Set small goals, reward yourself, remember your 'why', start with easiest task first."

    elif 'science' in user_input or 'biology' in user_input or 'chemistry' in user_input:
        return "Draw diagrams, understand processes, do practice problems, connect concepts to real-world examples."

    else:
        return "I can help with study techniques, time management, specific subjects, or exam prep. What's challenging you?"

# HTML Template
html_template = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>📚 Study Helper Chatbot</title>
  <style>
    body { font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #f1f5f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .chat-container { background: #1e293b; border-radius: 12px; padding: 20px; width: 400px; max-width: 90%; box-shadow: 0 0 20px rgba(0,0,0,0.3); }
    h2 { text-align: center; color: #38bdf8; }
    #chat-box { height: 300px; overflow-y: auto; background: #0f172a; padding: 10px; border-radius: 8px; margin-bottom: 10px; }
    .msg { padding: 8px 12px; border-radius: 10px; margin: 6px 0; }
    .user { background: #2563eb; text-align: right; }
    .bot { background: #334155; text-align: left; }
    input { width: 78%; padding: 8px; border-radius: 8px; border: none; outline: none; }
    button { padding: 8px 12px; border: none; border-radius: 8px; background: #38bdf8; color: #0f172a; cursor: pointer; font-weight: 600; }
  </style>
</head>
<body>
  <div class="chat-container">
    <h2>📚 Study Helper Bot</h2>
    <div id="chat-box">
      <div class="msg bot">Hi! I'm your Study Helper Bot. Ask me about study techniques, time management, or exam prep.</div>
    </div>
    <div>
      <input type="text" id="user-input" placeholder="Type your question..." onkeydown="if(event.key==='Enter') sendMessage()">
      <button onclick="sendMessage()">Send</button>
    </div>
  </div>

  <script>
    async function sendMessage() {
      const input = document.getElementById('user-input');
      const message = input.value.trim();
      if (!message) return;

      const chatBox = document.getElementById('chat-box');
      chatBox.innerHTML += `<div class='msg user'>${message}</div>`;
      input.value = '';

      const res = await fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message})
      });
      const data = await res.json();

      chatBox.innerHTML += `<div class='msg bot'>${data.reply}</div>`;
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    response = get_bot_response(user_input)
    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=True)
