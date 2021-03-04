from locust import TaskSet, task, HttpUser, between


class UserBehavior(TaskSet):
    wait_time = between(1, 2.5)

    def getToken(self):
        reqIndex = self.client.get("/index")
        token = reqIndex.json()['data']['token']
        return token

    @task
    def list_name(self):
        req = self.client.post("/itemsList/name/0/10", headers={"token": UserBehavior.getToken(self)},
                               data={"itemListName": "查询", "pageSize": "10", "pageNo": "0"})

    @task
    def list_example(self):
        req = self.client.post("/itemsList/example/0/10", headers={"token": UserBehavior.getToken(self)},
                               data={"departmentId": "0", "pageSize": "10", "pageNo": "0", "themeType": "1"})
        id = req.json()['data']['resultList'][0]['itemsListId']
        return id

    @task
    def department(self):
        req = self.client.post("/department/tree", headers={"token": UserBehavior.getToken(self)})

    @task
    def info(self):
        req = self.client.get(f"/itemsList/info/{UserBehavior.list_example(self)}",
                              headers={"token": UserBehavior.getToken(self)})

    @task
    def info(self):
        req = self.client.get(f"/handleItemFlow/{UserBehavior.list_example(self)}",
                              headers={"token": UserBehavior.getToken(self)})

    @task
    def info(self):
        req = self.client.get(f"/legal/{UserBehavior.list_example(self)}",
                              headers={"token": UserBehavior.getToken(self)})


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
