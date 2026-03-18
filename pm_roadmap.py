def generate_roadmap(plan, level=0):
    """
    Recursively prints the onboarding roadmap.
    """
    for stage, tasks in plan.items():
        indent = "  " * level
        print(f"{indent}🚀 {stage.upper()}")
        
        if isinstance(tasks, dict):
            generate_roadmap(tasks, level + 1)
        else:
            for task in tasks:
                print(f"{indent}  - [ ] {task}")
        print()

# Your personalized PM onboarding data
pm_roadmap = {
    "Days 1-30: Information Synthesis": {
        "People": [
            "1-on-1s with Engineering leads to understand tech debt",
            "Sync with Marketing on current campaign attribution models",
            "Identify key stakeholders for the SaaS product lifecycle"
        ],
        "Product": [
            "Audit the current user onboarding funnel",
            "Review the last 3 months of churn data",
            "Deep dive into the API documentation"
        ]
    },
    "Days 31-60: Strategic Alignment": {
        "Process": [
            "Audit the current Sprint cadence and Jira workflow",
            "Identify bottlenecks between Marketing requests and Dev capacity"
        ],
        "Quick Wins": [
            "Ship one small feature or bug fix to build 'Product Trust'",
            "Update the internal Wiki for the latest SaaS feature release"
        ]
    },
    "Days 61-90: Execution & Ownership": {
        "Growth": [
            "Present a data-backed proposal for a new SaaS feature",
            "Establish a 6-month product vision roadmap"
        ]
    }
}

print("--- MATTHEW'S SAAS PM ONBOARDING ROADMAP --- \n")
generate_roadmap(pm_roadmap)