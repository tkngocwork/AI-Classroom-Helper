# EduSpark Agent 🍎🤖
**Kaggle AI Agents Capstone Project - Track: Agents for Good**

## 🌟 Problem Statement
Primary school English teachers face extreme burnout spending hours preparing curriculum-aligned lesson materials. Generic AI tools fail because they hallucinate advanced vocabulary that is not approved for young learners. 

## 💡 Solution
EduSpark is an AI Agent that automates the creation of safe, age-appropriate educational materials. It connects to an official Vocabulary Database to prevent hallucination and uses strict security checkpoints before any material is finalized.

## 🏗️ Architecture & Key Concepts Applied
This project demonstrates three core concepts from the Kaggle AI Agents course:
1. **MCP Server:** Instead of relying on LLM memory, the agent fetches grade-specific words dynamically from an external Model Context Protocol server.
2. **Agent Skills:** Uses progressive disclosure via `flashcard_skill.md` and `game_skill.md` to prevent context rot.
3. **Security (Human-in-the-Loop):** Implements a mandatory execution halt. The agent generates the lesson but requires explicit human teacher approval before exporting, ensuring student safety.

## 🚀 Setup Instructions
1. Clone this repository: `git clone https://github.com/tkngocwork/AI-Classroom-Helper`
2. Navigate to the folder: `cd eduspark-agent`
3. Run the agent simulation: `python src_agent_core.py`
*(Note: No API keys are required to run this local simulation as per security best practices).*

## 🎥 Video Demo
https://youtu.be/sTtLPVbIkiQ?si=FepwM5Bef8zFi92K
