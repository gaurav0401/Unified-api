# ATS Integration Microservice (Serverless + Python)

This project implements a **Serverless ATS integration microservice** that exposes a unified REST API for jobs, candidates, and applications.  
It integrates with a **mock ATS (built using Flask)** that simulates real-world ATS platforms like Greenhouse or Lever.

The goal of this project is to demonstrate:
- Service-to-service REST integration
- Serverless API design
- ATS-agnostic architecture
- Proper error handling and input validation

---

## 🧠 Architecture Overview

There are **two services**:

1. **Mock ATS (Flask)**
   - Acts as the ATS provider
   - Exposes ATS APIs (`/jobs`, `/candidates`, `/applications`)
   - Provides a simple UI to visualize data

2. **Serverless Integration Microservice**
   - Exposes unified APIs required by the assignment
   - Internally calls the ATS APIs over HTTP
   - Can be adapted to real ATS providers by changing environment variables


---

## 1️⃣  Flask based ATS app  for testing 

### Mock ATS Features
- Job listing
- Candidate creation
- Job applications
- Simple UI for visualization
---
### Start the ATS

```bash
pip install -r requirements.txt
cd mock-ats
python app.py
``` 

### ATS will run at:
    http://localhost:4000

### UI endpoints:

    - Jobs: http://localhost:4000/ui/jobs
    
    - Candidates: http://localhost:4000/ui/candidates
    
    - Applications: http://localhost:4000/ui/applications

---

## 2️⃣How to Run the Service Locally
### Prerequisites

    - Python 3.12
  
    - Node.js 18+
  
    - Serverless Framework


### Step 1: Run the Mock ATS
```bash
cd mock-ats
python app.py
```


#### Verify: http://localhost:4000/jobs

### Step 2: Setup Serverless Microservice
``` bash
cd ats-service
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
npm install -g serverless
serverless --version

```

### Step 3: Start Serverless Offline
```bash

serverless offline
```


Serverless API will be available at: http://localhost:3000/dev

---

## 3️⃣ Available API Endpoints
    ✅ GET /jobs
    
      Returns a list of open jobs in a standard format.
      
      GET http://localhost:3000/dev/jobs
    
    ✅ POST /candidates
    
        Creates a candidate and attaches them to a job (application).
        
        POST http://localhost:3000/dev/candidates

    ✅ GET /applications

        Returns applications for a given job.
        
        GET http://localhost:3000/dev/applications?job_id=1
---

## 4️⃣ Testing on  Postman Setup (for creating candidates)

      Create Candidate
      
      Method: POST
      
      URL:
      
      http://localhost:3000/dev/candidates
      
      
      Headers:
      
      Content-Type: application/json
      
      
      Body (raw JSON):
      
      {
        "name": "Gaurav Bhatt",
        "email": "demo@test.com",
        "job_id": "1"
      }
---
## 5️⃣ Design Considerations

    - The integration service is ATS-agnostic
    
    - Flask ATS can be replaced with real ATS providers
    
    - UI is intended for admin/testing purposes only
    
    - All APIs include input validation and proper error handling
---
## 6️⃣ Summary

    This project demonstrates:
    
    - Clean REST API design
    
      - Serverless integration architecture
      
      - Proper separation of concerns
      
      - Realistic ATS interaction flow
      
      - It fulfills all requirements defined in the assignment specification.
