# Study Helper Chatbot
# Created by: [Your Name] and [Partner's Name]
# Group Project - Basic Chatbot Creation

def study_helper_bot():
    print("=" * 50)
    print("    📚 STUDY HELPER BOT 📚")
    print("=" * 50)
    print("I can help with study techniques, time management & exam prep!")
    print("Type 'quit' to end the study session")
    print("-" * 50)
    
    while True:
        user_input = input("\nWhat study help do you need? ").lower().strip()
        
        # Exit condition
        if user_input == 'quit':
            print("Happy studying! You've got this! 💪")
            break
            
        # 1. Time management
        elif 'time management' in user_input or 'schedule' in user_input:
            print("Try the Pomodoro technique: 25 min study, 5 min break. Use a planner and prioritize tasks.")
            
        # 2. Focus problems
        elif 'focus' in user_input or 'concentrate' in user_input:
            print("Eliminate distractions: Phone on silent, clean workspace, use website blockers. Try the 5-second rule to start.")
            
        # 3. Memorization
        elif 'memorize' in user_input or 'remember' in user_input:
            print("Use active recall: Flashcards, self-testing, spaced repetition. Teach the material to someone else.")
            
        # 4. Math help
        elif 'math' in user_input or 'calculus' in user_input:
            print("Practice daily, understand concepts not just formulas, check work step-by-step, use Khan Academy for help.")
            
        # 5. Essay writing
        elif 'essay' in user_input or 'writing' in user_input:
            print("Outline first, write then edit, use thesis statements, proofread aloud, check grammar and flow.")
            
        # 6. Exam preparation
        elif 'exam' in user_input or 'test' in user_input:
            print("Start early, review regularly, practice past papers, get enough sleep, eat well before the exam.")
            
        # 7. Note taking
        elif 'notes' in user_input or 'note taking' in user_input:
            print("Try Cornell method, mind maps, or outline format. Use abbreviations and review notes within 24 hours.")
            
        # 8. Reading comprehension
        elif 'reading' in user_input or 'comprehension' in user_input:
            print("SQ3R method: Survey, Question, Read, Recite, Review. Take notes and summarize each section.")
            
        # 9. Group study
        elif 'group study' in user_input or 'study group' in user_input:
            print("Set clear goals, assign topics, teach each other, stay on task, and quiz one another.")
            
        # 10. Motivation
        elif 'motivation' in user_input or 'procrastinate' in user_input:
            print("Set small goals, reward yourself, remember your 'why', start with easiest task first.")
            
        # 11. Science subjects
        elif 'science' in user_input or 'biology' in user_input or 'chemistry' in user_input:
            print("Draw diagrams, understand processes, do practice problems, connect concepts to real-world examples.")
            
        # 12. Default response
        else:
            print("I can help with study techniques, time management, specific subjects, or exam prep. What's challenging you?")

# Start the chatbot
if __name__ == "__main__":
    study_helper_bot()