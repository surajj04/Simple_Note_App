from pymongo import MongoClient

MONGO_URI = 'mongodb+srv://suraj04:TmDc6ddSD5WibRqm@note-app.cqnbz8f.mongodb.net/?retryWrites=true&w=majority&appName=note-app'


conn = MongoClient(MONGO_URI)

notes = [
    {
        "id": 1,
        "title": "Grocery List",
        "content": "Buy milk, eggs, bread, and butter from the supermarket.",
        "category": "personal",
        "tags": ["shopping", "food"]
    },
    {
        "id": 2,
        "title": "Project Meeting",
        "content": "Discuss project milestones and deliverables with the team on Monday at 10 AM.",
        "category": "work",
        "tags": ["meeting", "project"]
    },
    {
        "id": 3,
        "title": "Python Study Plan",
        "content": "Complete Python OOP and start learning Django this week.",
        "category": "study",
        "tags": ["python", "django", "learning"]
    },
    {
        "id": 4,
        "title": "Book Ideas",
        "content": "Outline plot for the mystery novel. Research detective character inspiration.",
        "category": "personal",
        "tags": ["writing", "novel", "ideas"]
    },
    {
        "id": 5,
        "title": "Team Feedback",
        "content": "Collect and compile feedback from all team members about Q3 performance.",
        "category": "work",
        "tags": ["feedback", "team", "performance"]
    }
]

db = conn['notesdb']
collection = db['notes']
