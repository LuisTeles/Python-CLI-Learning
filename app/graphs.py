### app/graphs.py
from app.models import get_all_tasks
from rich.console import Console
from rich.progress import Progress

console = Console()

def display_progress_chart():
    tasks = get_all_tasks()
    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return

    with Progress() as progress:
        for task in tasks:
            progress.add_task(task.name, total=task.duration, completed=task.days_passed)