from flask import Flask, render_template, jsonify

app = Flask(__name__)

Projects = [
    {
        "id": 1,
        "title": "Three-Day Planner App",
        "description": "A web app to help users plan and manage their tasks over a three-day period.",
        "technologies": ["HTML", "CSS", "JavaScript", "Flask"],
        "githublink": "https://github.com/username/three-day-planner"
    },
    {
        "id": 2,
        "title": "WebSocket Demo Game",
        "description": "A real-time multiplayer game that demonstrates the use of WebSockets for communication.",
        "technologies": ["HTML", "CSS", "JavaScript", "WebSocket", "Node.js"],
        "githublink": "https://github.com/username/websocket-demo-game"
    },
    {
        "id": 3,
        "title": "Insurance Advisor Website",
        "description": "A website to help an insurance advisor organize and run their business more efficiently.",
        "technologies": ["HTML", "CSS", "JavaScript", "Flask", "Bootstrap"],
        "githublink": "https://github.com/username/insurance-advisor-website"
    },
    {
        "id": 4,
        "title": "Client Relationship Management System",
        "description": "A CRM system to enhance follow-ups and provide personalized service for a lawyer's clients.",
        "technologies": ["HTML", "CSS", "JavaScript", "Django", "PostgreSQL"],
        "githublink": "https://github.com/username/client-relationship-management"
    },
    {
        "id": 5,
        "title": "Soccer Management System",
        "description": "A system to manage soccer teams, track player stats, and organize matches.",
        "technologies": ["Python", "Django", "SQLite"],
        "githublink": "https://github.com/username/soccer-management-system"
    }
]




@app.route("/")
def Home():
    return render_template("home.html",projects = Projects)

@app.route("/Resume")
def Resume():
    return render_template("resume.html")


@app.route("/Blog")
def Blog():
    return render_template("blog.html")


@app.route("/api/projects")
def list_projects():
    return jsonify(Projects)
    


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)  