# AI German Tutor – Project Notes

## Goal
Build a Python program that helps learners practice German grammar through exercises.  
The tool should support different CEFR levels and eventually include AI features for generating exercises and providing explanations.

---

## Current State
- Loads exercises from JSON
- Displays questions and answer options
- Validates user input
- Checks answers and shows feedback
- Practice loop for multiple exercises

---

## Next Features
- Save unknown vocabulary during exercises
- Vocabulary trainer using saved words
- Input validation cleanup
- Session statistics (correct / incorrect answers)
- Filter exercises by CEFR level (A1, B1, etc.)

---

## Exercise Improvements
- Add more exercise types:
  - fill-in-the-blank
  - connector selection
  - sentence ordering
  - error correction

---

## Interface
- Add a simple GUI later (likely Tkinter)
- Cleaner exercise layout
- Button for showing grammar explanations

---

## AI Integration (Later Phase)
- AI-generated exercises
- AI grammar explanations
- AI conversation practice

---

## Architecture Goal
Structure the program so it **does not become one large `main.py` file**.

Possible future modules:

- exercise engine
- input validation
- vocabulary manager
- AI generation
- UI module

---

## Long-Term Ideas
- spaced repetition for vocabulary
- progress tracking
- difficulty levels
- additional exercise categories