from locust import TaskSet, task, HttpUser, between, LoadTestShape
from locust.contrib.fasthttp import FastHttpUser
import time

class UserBehavior(TaskSet):
    wait_time=between(1,2.5)

    @task(1)
    def baidu_index(self):
        self.client.get("/")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 3000
    max_wait = 6000
#
# class MyUser(FastHttpUser):
#     wait_time = between(2,5)
#
#     @task
#     def index(self):
#         response = self.client.get("/")

# class MyCustomShape(LoadTestShape):
#     time_limit = 600
#     spawn_rate = 20
#
#     def tick(self):
#         run_time = self.get_run_time()
#
#         if run_time < self.time_limit:
#             user_count = round(run_time,-2)
#             return (user_count, self.spawn_rate)
#
#         return None