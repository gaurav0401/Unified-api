from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

jobs = [
    {
        "id": "1",
        "title": "Backend Engineer",
        "location": "Remote",
        "status": "OPEN",
        "external_url": "https://example.com/job/1"
    },
    {
  "id": "2",
  "title": "Frontend Engineer",
  "location": "Bangalore, India",
  "status": "OPEN",
  "external_url": "https://example.com/job/2"
},
{
  "id": "3",
  "title": "Full Stack Developer",
  "location": "Remote",
  "status": "OPEN",
  "external_url": "https://example.com/job/3"
},
{
  "id": "4",
  "title": "DevOps Engineer",
  "location": "Hyderabad, India",
  "status": "OPEN",
  "external_url": "https://example.com/job/4"
},
{
  "id": "5",
  "title": "Data Engineer",
  "location": "Pune, India",
  "status": "CLOSED",
  "external_url": "https://example.com/job/5"
},
{
  "id": "6",
  "title": "Machine Learning Engineer",
  "location": "Remote",
  "status": "OPEN",
  "external_url": "https://example.com/job/6"
},
{
  "id": "7",
  "title": "QA Automation Engineer",
  "location": "Noida, India",
  "status": "OPEN",
  "external_url": "https://example.com/job/7"
},
{
  "id": "8",
  "title": "Cloud Solutions Architect",
  "location": "Gurgaon, India",
  "status": "DRAFT",
  "external_url": "https://example.com/job/8"
},
{
  "id": "9",
  "title": "Product Manager",
  "location": "Mumbai, India",
  "status": "OPEN",
  "external_url": "https://example.com/job/9"
},
{
  "id": "10",
  "title": "UI/UX Designer",
  "location": "Remote",
  "status": "OPEN",
  "external_url": "https://example.com/job/10"
},
{
  "id": "11",
  "title": "Mobile App Developer (Android)",
  "location": "Chennai, India",
  "status": "OPEN",
  "external_url": "https://example.com/job/11"
},
{
  "id": "12",
  "title": "Mobile App Developer (iOS)",
  "location": "Remote",
  "status": "CLOSED",
  "external_url": "https://example.com/job/12"
},
{
  "id": "13",
  "title": "Cyber Security Analyst",
  "location": "Bangalore, India",
  "status": "OPEN",
  "external_url": "https://example.com/job/13"
},
{
  "id": "14",
  "title": "Technical Support Engineer",
  "location": "Jaipur, India",
  "status": "OPEN",
  "external_url": "https://example.com/job/14"
},
{
  "id": "15",
  "title": "Site Reliability Engineer",
  "location": "Remote",
  "status": "DRAFT",
  "external_url": "https://example.com/job/15"
},
{
  "id": "16",
  "title": "Business Analyst",
  "location": "Kolkata, India",
  "status": "OPEN",
  "external_url": "https://example.com/job/16"
}

]

candidates = []
applications = []

# ---------- UI ----------

@app.route("/")
def home():
    return redirect("/ui/jobs")

@app.route("/ui/jobs")
@app.route("/ui/jobs")
def ui_jobs():
    return render_template(
        "jobs.html",
        jobs=jobs,
        candidates=candidates
    )

@app.route("/ui/candidates")
def ui_candidates():
    return render_template("candidates.html", candidates=candidates)

@app.route("/ui/applications")
def ui_apps():
    return render_template("applications.html", applications=applications)

@app.route("/ui/candidates/create", methods=["POST"])
def ui_create_candidate():
    data = request.form
    candidate = {
        "id": str(len(candidates) + 1),
        "name": data["name"],
        "email": data["email"],
        "phone": data.get("phone"),
        "resume_url": data.get("resume_url")
    }
    candidates.append(candidate)
    return redirect("/ui/candidates")

# ---------- ATS API ----------

@app.route("/jobs", methods=["GET"])
def get_jobs():
    return jsonify(jobs)

@app.route("/candidates", methods=["POST"])
def create_candidate():
    data = request.json
    candidate = {
        "id": str(len(candidates) + 1),
        "name": data["name"],
        "email": data["email"],
        "phone": data.get("phone"),
        "resume_url": data.get("resume_url")
    }
    candidates.append(candidate)
    return jsonify(candidate), 201

@app.route("/jobs/<job_id>/applications", methods=["POST"])
def apply(job_id):
    data = request.json
    app_entry = {
        "id": str(len(applications) + 1),
        "job_id": job_id,
        "candidate_id": data["candidate_id"],
        "status": "APPLIED"
    }
    applications.append(app_entry)
    return jsonify(app_entry), 201

@app.route("/jobs/<job_id>/applications", methods=["GET"])

def get_apps(job_id):
    result = []

    for a in applications:
        if a["job_id"] == job_id:
            candidate = next(
                (c for c in candidates if c["id"] == a["candidate_id"]),
                None
            )
            result.append({
                "id": a["id"],
                "candidate": candidate,
                "status": a["status"]
            })

    return jsonify(result)
            

@app.route("/ui/apply", methods=["POST"])
def ui_apply():
    job_id = request.form["job_id"]
    candidate_id = request.form["candidate_id"]

    application = {
        "id": str(len(applications) + 1),
        "job_id": job_id,
        "candidate_id": candidate_id,
        "status": "APPLIED"
    }

    applications.append(application)

    return redirect("/ui/applications")

if __name__ == "__main__":
    app.run(port=4000, debug=True)
