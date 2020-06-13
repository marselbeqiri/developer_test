import json
import time

import schedule


# ...Centipede
# ..\      /
# ...╚⊙ ⊙╝
# ..╚═(███)═╝
# .╚═(███)═╝
# ..╚═(███)═╝
# .╚═(███)═╝
class Job:
    def __init__(self):
        with open('schedule.json') as file:
            self.data = json.load(file)

    def start_job(self):
        for task in self.data:
            for scheduler in task['schedule']:
                self.scheduler_helper(scheduler)

    def scheduler_helper(self, scheduler):
        if 'at' in scheduler:
            if scheduler['frequency'] == 'day':
                schedule.every().day.at(scheduler['at']).do(self.job, scheduler['title'])

            if scheduler['frequency'] == 'hour':
                schedule.every().hour.at(scheduler['at']).do(self.job, scheduler['title'])

            if scheduler['frequency'] == 'minute':
                schedule.every().minute.at(scheduler['at']).do(self.job, scheduler['title'])

        if 'day' in scheduler:
            if scheduler['frequency'] == 'week':
                self.week_selector(scheduler)
        else:
            self.every_repeater(scheduler)

    def job(self, task):
        print(task)

    def week_selector(self, scheduler):
        if scheduler['day'] == 'monday':
            schedule.every().monday.at("19:15").do(self.job, scheduler['title'])

        if scheduler['day'] == 'tuesday':
            schedule.every().monday.at("19:15").do(self.job, scheduler['title'])

        if scheduler['day'] == 'wednesday':
            schedule.every().wednesday.at("19:15").do(self.job, scheduler['title'])

        if scheduler['day'] == 'thursday':
            schedule.every().thursday.at("19:15").do(self.job, scheduler['title'])

        if scheduler['day'] == 'friday':
            schedule.every().monday.at("19:15").do(self.job, scheduler['title'])

    def every_repeater(self, scheduler):
        if scheduler['frequency'] == 'hour':
            schedule.every(1).hour.do(self.job, scheduler['title'])
        if scheduler['frequency'] == 'minute':
            schedule.every().minute.do(self.job, scheduler['title'])
        if scheduler['frequency'] == 'second':
            schedule.every(2).seconds.do(self.job, scheduler['title'])

    def run_pending(self):
        while True:
            schedule.run_pending()
            time.sleep(1)


job_scheduler = Job()

job_scheduler.start_job()

job_scheduler.run_pending()
