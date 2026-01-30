import json
from src.ats_client import ATSClient

def handler(event, context):
    job_id = event["queryStringParameters"]["job_id"]
    page = 1
    applications = []

    try:
        while True:
            response = ATSClient.get_applications(job_id, page)

            if response.status_code != 200:
                return {
                    "statusCode": response.status_code,
                    "body": json.dumps({"error": "Failed to fetch applications"})
                }

            data = response.json()
            applications.extend(data["results"])

            if not data.get("next_page"):
                break

            page += 1

        normalized = [
            {
                "id": a["id"],
                "candidate_name": a["candidate"]["name"],
                "email": a["candidate"]["email"],
                "status": a["status"]
            }
            for a in applications
        ]

        return {
            "statusCode": 200,
            "body": json.dumps(normalized)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
