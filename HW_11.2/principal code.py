from flask import Flask, render_template
from functions import load_candidates_from_json
from functions import get_candidate
from functions import get_candidates_by_name
from functions import get_candidates_by_skill
from functions import count_candidates_by_name

app = Flask(__name__)

#создаем главную страницу
@app.route("/")
def main_page():
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:id>")
def candidate_page(id):
    candidate = get_candidate(id)
    return render_template("card.html", candidate=candidate)

@app.route("/search/<candidate_name>")
def search_by_name(candidate_name):
    candidate = get_candidates_by_name(candidate_name)
    counter = count_candidates_by_name(candidate_name)
    return render_template("search.html", candidate=candidate, counter=counter)

@app.route("/skill/<skill_name>")
def search_by_skill(skill_name):
    skill_owned = get_candidates_by_skill(skill_name)
    for candidate in skill_owned:
        return render_template("skill.html", candidate=candidate, skill_name=skill_name)
app.run()
