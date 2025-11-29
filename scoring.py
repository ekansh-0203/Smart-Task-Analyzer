import datetime
def calculate_task_score(task, all_tasks, strategy="smart"):
    score = 0
    
    if task["due_date"]:
        due_date = datetime.datetime.strptime(task["due_date"], "%Y-%m-%d").date()
        days_left = (due_date - datetime.date.today()).days

        if day_left < 0 :
            urgency_score = 20
        else:
            urgency_score = max(0, 10 - days_left)
    else:
        urgency_score = 0


    importance_score = task.get("importance",5)
    
    effort_score = max(0, 10 - task.get("estimated_hours", 1))

    dependency_score = len(task.get("dependencies", []))*3

    if strategy == "fast":
        score = effort_score * 2
    elif strategy == "impact":
        score = importance_score * 2
    elif strategy == "deadline":
        score = urgency_score * 2
    else:
        score = urgency_score + importance_score + effort_score + dependency_score

    return round(score, 2)
        
    
    
