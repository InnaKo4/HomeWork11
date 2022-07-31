from flask import Flask, render_template
from functions import load_candidates_from_json
from functions import get_candidate
from functions import get_candidates_by_name
from functions import get_candidates_by_skill


app = Flask(__name__)

#создаем главную страницу
@app.route("/")
def main_page():
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)

#создаем страницу для каждого кандидата
@app.route("/candidate/<int:id>")
def candidate_page(id):
    candidate = get_candidate(id)
    return render_template("card.html", candidate=candidate)

#создаем страницу для кандидатов по совпадению имен
@app.route("/search/<candidate_name>")
def search_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    counter = len(candidates)
    return render_template("search.html", candidates=candidates, counter=counter)

#создаем страницу для кандидатов по совпадению скиллов
@app.route("/skill/<skill_name>")
def search_by_skill(skill_name):
    skill_owned = get_candidates_by_skill(skill_name)
    counter = len(skill_owned)
    for candidate in skill_owned:
        return render_template("skill.html", candidate=candidate, candidates=skill_owned, skill_name=skill_name, counter=counter)

app.run()
