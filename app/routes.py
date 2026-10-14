
from flask import Blueprint, render_template

from app.projects import PROJECTS
from app.skills import SKILLS, SKILL_LEVELS

main = Blueprint("main", __name__)


@main.route("/")
def home():
    skills = {
        category: [
            {
                **skill,
                **SKILL_LEVELS[skill["level"]],
            }
            for skill in items
        ]
        for category, items in SKILLS.items()
    }

    return render_template(
        "index.html",
        skills=skills,
        projects=PROJECTS,
    )
