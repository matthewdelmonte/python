def print_progress_bar(completed, total):
    """Calculates and prints a visual progress bar."""
    if total == 0: return
    percentage = (completed / total) * 100
    bar = "█" * int(percentage // 10) + "░" * (10 - int(percentage // 10))
    print(f"Overall Progress: |{bar}| {percentage:.1f}%")

def generate_interactive_roadmap(roadmap):
    total_tasks = 0
    completed_tasks = 0
    
    print(f"--- 🎯 PROFESSIONAL GOAL: {roadmap['achievement_goal']} ---\n")
    
    for phase in roadmap["phases"]:
        print(f"🚀 {phase['title'].upper()}")
        print(f"🚩 MILESTONE: {phase['milestone']}")
        
        for task in phase["tasks"]:
            total_tasks += 1
            status = "✅" if task["done"] else "⬜"
            if task["done"]: completed_tasks += 1
            print(f"  {status} {task['name']}")
        print("-" * 30)

    print_progress_bar(completed_tasks, total_tasks)

# Updated Data Structure with Progress Tracking
my_pm_data = {
    "achievement_goal": "Establish a data-driven feedback loop between Marketing and Engineering by Day 90.",
    "phases": [
        {
            "title": "Days 1-30: Discovery",
            "milestone": "Complete Stakeholder Map & Tech Audit",
            "tasks": [
                {"name": "1-on-1s with Eng leads", "done": True},
                {"name": "Audit SaaS onboarding funnel", "done": False},
                {"name": "Review Q1/Q2 churn data", "done": False}
            ]
        },
        {
            "title": "Days 31-60: Integration",
            "milestone": "First Feature/Fix Shipped",
            "tasks": [
                {"name": "Align Jira workflow with Marketing needs", "done": False},
                {"name": "Present 'Quick Win' feature spec", "done": False}
            ]
        }
    ]
}

generate_interactive_roadmap(my_pm_data)