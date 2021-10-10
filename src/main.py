from typing import Optional
from definitions import Job
from fastapi import FastAPI
from memdb import MemDB
from typing import List
import requests, json, os
import urllib.parse

app = FastAPI()
db = MemDB()
EXTERN_URL_PATH = "jobs"

@app.post("/post_job", response_model=Job)
def add_jobs(job: Job):
    return db.create(job)


@app.get("/search_jobs", response_model=List[Job])
def get_jobs(name: Optional[str] = None,
             salary_min: Optional[int] = None,
             salary_max: Optional[int] = None,
             country: Optional[str] = None):

    extern_res = get_jobs_external(name, salary_min, salary_max, country)
    intern_res = db.get_jobs(name, salary_min, salary_max, country)
    return intern_res + extern_res


def get_jobs_external(name: Optional[str] = None,
                      salary_min: Optional[int] = None,
                      salary_max: Optional[int] = None,
                      country: Optional[str] = None):
    external_url = os.getenv("EXTERNAL_JOBS_URL", "localhost")
    external_port = os.getenv("EXTERNAL_JOBS_PORT", "8081")
    url = f"http://{external_url}:{external_port}/{EXTERN_URL_PATH}"
    result = []
    params = {k: v for k, v in
              (("name", name),
               ("salary_min", salary_min),
               ("salary_max", salary_max),
               ("country", country)) if v is not None}
    params_url = f"?{urllib.parse.urlencode(params)}" if params else ""
    try:
        res = requests.get(url + params_url)
        extern_list = json.loads(res.content)
        props = list(Job.schema()["properties"].keys())
        for extern_job in extern_list:
            job = Job.parse_obj(zip(props, extern_job))
            if not db.is_duplicated(job):
                result.append(job)
    except requests.RequestException as _err:
        print(f"Cannot connect to external resources. {_err}")
    return result
