from datetime import datetime
from typing import List


class Bug:
    def __init__(
        self,
        description: str,
        severity: int,
        deadline: datetime,
        status: str,
        assignee: str,
    ):
        self.description = description
        self.severity = severity
        self.deadline = deadline
        self.status = status
        self.assignee = assignee

    def __repr__(self):
        return (
            f"Bug(description='{self.description}', severity={self.severity}, "
            f"deadline={self.deadline}, status='{self.status}', assignee='{self.assignee}')"
        )


class Backlog:
    def __init__(self):

        self.bugs: List[Bug] = []

    def add_bug(self, bug: Bug):

        self.bugs.append(bug)

    def get_resolved_bugs_by_assignee(self, assignee: str) -> List[Bug]:

        return [
            bug
            for bug in self.bugs
            if bug.assignee == assignee and bug.status == "RESOLVED"
        ]

    def sort_by_severity(self):

        self.bugs.sort(key=lambda bug: bug.severity, reverse=True)

    def __repr__(self):
        return f"Backlog(bugs={self.bugs})"


backlog = Backlog()


backlog.add_bug(
    Bug("Невірне відображення кнопки", 5, datetime(2023, 12, 1), "RESOLVED", "Іван")
)
backlog.add_bug(
    Bug("Помилка з'єднання з сервером", 9, datetime(2023, 11, 15), "OPEN", "Олексій")
)
backlog.add_bug(
    Bug("Помилка авторизації", 7, datetime(2023, 11, 20), "RESOLVED", "Іван")
)
backlog.add_bug(
    Bug("Помилка бази даних", 10, datetime(2023, 11, 18), "IN_PROGRESS", "Олексій")
)


resolved_bugs_ivan = backlog.get_resolved_bugs_by_assignee("Іван")
print("Баги зі статусом 'RESOLVED' для Івана:", resolved_bugs_ivan)


backlog.sort_by_severity()
print("Беклог, відсортований за важливістю:", backlog)
