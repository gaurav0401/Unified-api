import json
from dotenv import load_dotenv
load_dotenv()

from src.ats_client import *
from src.schemas import *
from src.utils import *

def get_jobs(event, context):
    jobs = collect(fetch_jobs)
    return {"statusCode": 200, "body": json.dumps([job_schema(j) for j in jobs])}

def create_candidate_handler(event, context):
    try:
        raw_body = event.get("body")

        if not raw_body:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Request body is required"
                })
            }

        body = json.loads(raw_body)

        required_fields = ["name", "email", "job_id"]
        missing = [f for f in required_fields if f not in body]

        if missing:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": f"Missing required fields: {', '.join(missing)}"
                })
            }

        candidate = create_candidate({
            "name": body["name"],
            "email": body["email"],
            "phone": body.get("phone"),
            "resume_url": body.get("resume_url")
        })

        attach_candidate_to_job(candidate["id"], body["job_id"])

        return {
            "statusCode": 201,
            "body": json.dumps({
                "message": "Candidate created and attached",
                "candidate_id": candidate["id"]
            })
        }

    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Invalid JSON body"
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

def get_applications(event, context):
    try:
        params = event.get("queryStringParameters") or {}
        job_id = params.get("job_id")

        if not job_id:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Missing required query parameter: job_id"
                })
            }

        apps = fetch_applications(job_id)

        return {
            "statusCode": 200,
            "body": json.dumps([application_schema(a) for a in apps])
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
