from definitions import Job

class MemDB():
    def __init__(self):
        self._models = {}

    def create(self, model: Job):
        id = model.get_id_hash()
        if id in self._models:
            return self._models[id]
        self._models[id] = model
        return model

    def get_jobs(self, name=None, salary_min=None, salary_max=None, country=None):
        result = [
            job for job in self._models.values() if
            (name is None or name.lower() in job.name.lower()) and
            (salary_min is None or job.salary >= salary_min) and
            (salary_max is None or job.salary <= salary_max) and
            (country is None or job.country.lower() == country.lower())
        ]
        print(self._models)
        return result

    def is_duplicated(self, model: Job):
        return True if model.get_id_hash() in self._models else False
