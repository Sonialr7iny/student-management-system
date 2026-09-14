# Roles

1. No direct pushes to main

2. Every feature starts with an Issue.

3. Every Issue gets an assigned developer.

4. Every feature is implemented in its own branch.

5. Every branch must have a clear name.

6. Every PR must describe:
   - What was the problem?
   - What was changed?
   - How was it tested?

7. Every PR must have a reviewer.

8. Reviewer must actually review the code.

9. Changes requested by the reviewer must be addressed
   before merging.

10. Tests must pass before merging.

11. Merge to main only after approval.

12. Prefer Squash and Merge.

13. Delete the feature branch after merge.

14. No secrets, credentials, .env files, or unnecessary data
    in the repository.

15. Every member participates in code review.

## Features

- Student management
- Course management
- Enrollment management
- User authentication
- Role-based access
- Data persistence
- Input validation

## Architecture

The project follows a layered architecture:

CLI
↓
Service
↓
Repository
↓
Data Storage

### Layers

- Model: Domain entities
- Repository: Data access
- Service: Business logic
- CLI: User interaction
- Core: Shared application components
- Utils: Reusable utilities

## Project Structure

`text
app/
├── cli/
├── core/
├── model/
├── repo/
├── service/
└── utils/

data/
tests/

main.py
README.md
requirements.txt
.gitignore

### Domain Models

User
Student
Course
Enrollement
Role

### Team Workflow

We use short-lived feature branches and Pull Requests

### Branch Naming

feature/
fix/
test/
docs/
chore/

### Commit Convention

feat:
fix:
test:
docs:
chore:

### Coding Conventions

Follow consistent Python naming conventions
Use type hints
Keep business logic inside services
Keep data access inside repositories
Keep CLI responsible for user interaction
Avoid duplicated logic .
