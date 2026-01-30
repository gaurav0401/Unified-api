def job_schema(j):
    return {
        "id": j["id"],
        "title": j["title"],
        "location": j["location"],
        "status": j["status"],
        "external_url": j["external_url"]
    }

def application_schema(a):
    return {
        "id": a["id"],
        "candidate_name": a["candidate"]["name"],
        "email": a["candidate"]["email"],
        "status": a["status"]
    }
