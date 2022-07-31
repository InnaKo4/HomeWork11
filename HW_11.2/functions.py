import json
def load_candidates_from_json():
    """Загружает данные из Json в Python"""
    with open("candidates.json", "r") as file:
        file_json = file.read()
        all_candidates = json.loads(file_json)
        return all_candidates

def get_candidate(candidate_id):
    """Выводит данные кандидата по id"""
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate_id == candidate['id']:
            return candidate

def get_candidates_by_name(candidate_name):
    """Выводит данные кандидата по имени"""
    candidates = load_candidates_from_json()
    candidates_by_name = []
    for candidate in candidates:
        if candidate_name in candidate['name']:
            candidates_by_name.append(candidate)
    return candidates_by_name

def get_candidates_by_skill(skill_name):
    """Выводит кандидатов по скиллу"""
    skill_owned = []
    candidates = load_candidates_from_json()
    for candidate in candidates:
        candidate_skills = candidate['skills'].lower()
        if skill_name.lower() in candidate_skills.split(', '):
            skill_owned.append(candidate)
    return skill_owned

