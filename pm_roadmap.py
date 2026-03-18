import json
import os

def load_data(filepath):
    """Imports the JSON data from the specified path."""
    with open(filepath, 'r') as file:
        return json.load(file)

def save_to_markdown(output_text, filename="PM_Status_Report.md"):
    """Ensures the Reports directory exists and saves the Markdown file."""
    # Define the directory and full path
    report_dir = "Reports"
    
    # Check if directory exists; if not, create it
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
        print(f"📁 Created directory: {report_dir}")

    full_path = os.path.join(report_dir, filename)

    # Write the file to the new path
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(output_text)
        
    print(f"\n✅ Success! Report saved to: {full_path}")

# def save_to_markdown(output_text, filename="PM_Status_Report.md"):
#     """Writes the generated roadmap to a Markdown file."""
#     with open(filename, "w", encoding="utf-8") as f:
#         f.write(output_text)
#     print(f"\n✅ Success! Report saved to: {filename}")

def get_progress_bar_string(completed, total):
    """Generates the visual progress bar as a string."""
    if total == 0: return "|░░░░░░░░░░| 0.0%"
    percentage = (completed / total) * 100
    blocks = int(percentage // 10)
    bar = "█" * blocks + "░" * (10 - blocks)
    return f"|{bar}| {percentage:.1f}%"

def generate_roadmap_string(roadmap):
    """Generates the roadmap and returns it as a formatted string."""
    output = []
    total_tasks = 0
    completed_tasks = 0
    
    output.append(f"--- 🎯 PROFESSIONAL GOAL: {roadmap['achievement_goal']} ---\n")
    
    for phase in roadmap["phases"]:
        output.append(f"🚀 {phase['title'].upper()}")
        output.append(f"🚩 MILESTONE: {phase['milestone']}\n")
        
        for task in phase["tasks"]:
            total_tasks += 1
            status = "✅" if task["done"] else "⬜" 
            if task["done"]: completed_tasks += 1
            output.append(f"{status} {task['name']}")
        output.append("\n" + ("-" * 30) + "\n")

    # Progress Calculation & Visual Bar
    bar_str = get_progress_bar_string(completed_tasks, total_tasks)
    output.append(f"Overall Progress:\n {bar_str} ")
    
    return "\n".join(output)

# --- EXECUTION ---
data_path = os.path.join("Data", "roadmap_data.json")

try:
    # 1. Load the JSON
    my_pm_data = load_data(data_path)
    
    # 2. Generate the content
    final_report = generate_roadmap_string(my_pm_data)
    
    # 3. Print to console for immediate view
    print(final_report)
    
    # 4. Export to Markdown
    save_to_markdown(final_report)

except FileNotFoundError:
    print(f"Error: Could not find the JSON file at {data_path}. Please check your Data folder.")