# EduSpark Agent Core - Capstone Project
# Applies: Agent Skills, MCP Server integration, and Human-in-the-loop security.

def connect_mcp_server(grade, topic):
    """Simulates connecting to a Google Sheets MCP Server to fetch approved vocabulary."""
    print(f"[MCP SERVER] Fetching approved vocabulary for Grade {grade}, Topic: {topic}...")
    return ["cow", "pig", "horse", "sheep", "duck", "chicken"]

def run_agent_skill(skill_name, context):
    """Simulates loading an Agent Skill progressively."""
    print(f"[AGENT SKILL] Loading {skill_name}.md to generate materials...")
    if skill_name == "game_skill":
        return f"Bingo Game created using words: {', '.join(context)}."
    return f"Flashcards created using words: {', '.join(context)}."

def human_in_the_loop_review(generated_content):
    """Security Feature: Halts execution to wait for teacher's explicit approval."""
    print("\n🚨 [SECURITY] HUMAN-IN-THE-LOOP REVIEW PAUSE 🚨")
    print("Agent has generated the following materials:")
    print(f"-> {generated_content}")
    
    approval = input("\nTeacher, do you approve this content for students? (yes/no): ")
    if approval.lower() == 'yes':
        print("[SUCCESS] Content approved. Exporting PDF...")
    else:
        print("[BLOCKED] Content rejected. Aborting export to protect students.")

# Main Execution
if __name__ == "__main__":
    print("Welcome to EduSpark Agent!")
    vocab = connect_mcp_server(grade=3, topic="Farm Animals")
    draft_materials = run_agent_skill("game_skill", vocab)
    
    # Halt and review before finalizing
    human_in_the_loop_review(draft_materials)