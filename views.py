from rest_framework.decorators import api_view
from rest_framework.response import Response
from .scoring import calculate_task_score
from .serializers import TaskSerializer

@api_view(["POST"])
def analyze_tasks(request):
    tasks = request.data.get("tasks", [])
    strategy = request.data.get("strategy", "smart")

    score = []
    for t in tasks:
        t["score"] = calculate_task_score(t, tasks, strategy)
        scored.append(t)

    scored = sorted(scored, key=lambda x: x["score"], reverse=True)

    return Response({"sorted_tasks": scored})
@api_view(["GET"])
def suggest_tasks(request):
    tasks = request.data.get("tasks", [])

    scored = []
    for t in tasks:
        t["score"] = calculate_task_score(t, tasks)
        scored.append(t)

    scored = sorted(scored, key=lambda x: x["score"], reverse=True)

    return Response(scored[:3])

        

