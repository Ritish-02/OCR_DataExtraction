import re
def extract_fields(text):
    data = {}
    name_match = re.search(r"Patient Name\s*:\s*(.+)",text)
    dob_match = re.search(r"DOB\s*:\s*(\d{2}/\d{2}/\d{4})",text)
    data["patient_name"] = name_match.group(1).strip() if name_match else "Unknown"
    data["dob"] = dob_match.group(1) if dob_match else "Unknown"
    data["injection"] = "Yes" if "INJECTION : YES" in text else "No"
    data["exercise_therapy"] = "Yes" if "Exercise Therapy : Yes" in text else "No"
    ratings = {}
    for activity in ["Bending","Putting on shoes","Sleeping"]:
        match = re.search(rf"{activity}:\s*(\d)",text)
        ratings[activity.lower().replace(" ","_")] = int(match.group(1)) if match else 0
    data["difficulty_ratings"] = ratings
    symptoms = ["Pain","Numbness","Tingling","Burning","Tightness"]
    pain_data = {}
    for symptom in symptoms:
        match = re.search(rf"{symptoms}:\s*(\d+)",text)
        pain_data[symptom.lower()] = int(match.group(1)) if match else 0
    data["pain_symptoms"] = pain_data
    return data