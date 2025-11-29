function analyze(){
    let tasks = JSON.parse(document.getElementById("taskInput").value);
    let strategy = doucument.getelementBYId("strategy").value;
    fetch("http://127.0.0.1:8000/api/tasks/analyze/",{
        method: "POST",
        headers: {
            "Content-Type": "application/json"
    },
        body: JSON.stringify({tasks, strategy})
})
.then(res => res.json())
.then(data => {
    let out = "";
    data.sorted_tasks.forEach(t => {
        let cls = t.score > 20 ? "high" : t.score > 10 ? "medium" : "low";
        out += `
        <div class="task ${cls}">
            <strong>${t.title}</strong><br>
            Score: ${t.score}<br>
            Due: ${t.due_date}<br>
            Hours: ${t.estimated_hours}<br>
            Importance: ${t.importance}
            </div>
           `;
    });
    document.getElementById("output").innerHTML = out;
});

}