from locust import TaskSet, task, HttpUser, between


class UserBehavior(TaskSet):
    wait_time = between(1, 2.5)
    share_data = ['/theme/1', '/theme/2']

    def __init__(self, parent):
        super().__init__(parent)
        self.index = 0

    def on_start(self):
        pass

    def getToken(self):
        req = self.client.get('/index')
        token = req.json()['data']['token']
        return token

    @task
    def test_visit(self):
        url = self.share_data[self.index]
        self.index = (self.index + 1) % len(self.share_data)
        with self.client.get(url, headers={'token': UserBehavior.getToken(self)}, catch_response=True) as response:
            assert response.status_code == 200
            if response.status_code == 200:
                response.success()
            else:
                response.failure("can't")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
