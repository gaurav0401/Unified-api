import os, requests

BASE = os.getenv("ATS_BASE_URL")

def fetch_jobs(page=1):
    return requests.get(f"{BASE}/jobs").json()

def create_candidate(data):
    response = requests.post(f"{BASE}/candidates", json=data)

    if response.status_code != 201:
        raise Exception("ATS: Failed to create candidate")

    if not response.text.strip():
        raise Exception("ATS returned empty response")

    return response.json()


def attach_candidate_to_job(cid, jid):
    return requests.post(f"{BASE}/jobs/{jid}/applications", json={"candidate_id": cid}).json()

def fetch_applications(jid):
    response = requests.get(f"{BASE}/jobs/{jid}/applications")

    if response.status_code != 200:
        raise Exception("ATS: Failed to fetch applications")

    # Handle empty response safely
    if not response.text.strip():
        return []

    return response.json()

