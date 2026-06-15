# Maestro 🎹

> *Practice smarter.*

An AI practice coach that listens to you play, finds your weaknesses, and plans your next session.

---

## How It Works

1. Upload a target MIDI file (the song you're learning)
2. Play along on your MIDI keyboard — Maestro captures every key press in real time
3. When you're done, Maestro sends both your performance and the original to an LLM


4. Get back a coaching report: what you nailed, what to fix, and what to practice tomorrow

---

## MIDI Input

Maestro reads your piano through its MIDI port, capturing each event as:

| Field | Description |
|---|---|
| `status` | `144` = Note On (pressed), `128` = Note Off (released) |
| `note` | MIDI note number (0–127) representing the key pressed |
| `velocity` | How hard the key was pressed (0–127) |

**MVP (v1):** Uses `note` and `status` only — focuses on what you played and when.


**v2:** Adds `velocity` analysis for deeper insight into dynamics and expression.

---

## Stack

- `pygame.midi` — real-time MIDI capture
- `mido` — MIDI file parsing
- `anthropic` — AI coaching feedback

---

## Status

🚧 Under active development