
# Milestone 4 — Manual Testing Checklist

| # | Test Scenario | Steps | Expected Result | Status |
|---|---|---|---|---|
| 1 | Launch application | Run `docker compose up --build` and open localhost:5173 | Dashboard loads successfully | Pass |
| 2 | Create a task | Enter a title, course, and due date; click Add Task | New task appears on dashboard | Pass |
| 3 | Database persistence | Create a task and refresh the page | Saved task remains visible | Pass |
| 4 | Invalid task title | Enter only spaces for the title and submit | Error message appears; task is not added | Pass |
| 5 | Missing required field | Leave the course field empty and submit | Browser rejects submission | Pass |
| 6 | Backend availability | Open localhost:8000/docs | FastAPI documentation loads | Pass |
