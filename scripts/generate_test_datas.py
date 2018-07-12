import os
import json
from random import randrange, choice
#import random.randrange
from faker import Faker
from simplejob.models import db, User, Company, Job
#import random

faker = Faker('zh-CN')  # 创建 faker 工厂对象，生成一个用于测试数据的库

user = User(
    username='Shiyanlou',
    password='shiyanlou',
    phone='12012134999',
    email='shiyanlou@qq.com',
    role=30,
)

with open(os.path.join(os.getcwd(), 'datas', 'job.json')) as f:
    jobs = json.load(f)

def iter_companys():
    #for i in jobs:
    #for i, job in enumerate(jobs):
    for company in jobs:

        yield Company(
            #logo = company['logo'],
            #company_name = company['company_name'],
            #offical_websit = company['offical_websit'],
            #industry = company['industry'],
            #stage = company['stage'],
            #city = company['city']
            
            #name = i['company'],OK
            name = company['company'],
            email = faker.email(),
            website = faker.uri(),
            #password = '123456',
            user = user,
            address = faker.address()
        )
companys = list(iter_companys())
print(companys)
print(randrange(1000,8000,500))
def iter_jobs():
    #with open(os.path.join(os.getcwd(), 'datas', 'jobs.json')) as f:
     #   jobs = json.load(f)
    for i, job in enumerate(jobs):
        yield Job(
            #job_name = job['jobname'],
            #wage_area = job['wage_area'],
            #working_address = job['working_address'],
            #experience_required = job['experience'],
            #edu_required = job['education'],
            #release_date = job['release_date']
            #release_date = faker.date(),
            name = job['name'],
            #salary = job['salary'],
            salary_low = randrange(3000,8000,1000),
            salary_high = randrange(8000,20000,1000),
            exp = choice(['全部','应届毕业生','3年及以下','3-5年','5-10年','10年以上','不限']),
            degree = choice(['全部','本科','研究生','专科','不限']),
            #address = job['address'],
            location = job['address'],
            company = user
            )
#print(next(iter_jobs()))
def run():
    #for company in companys:OK
    for company in iter_companys():
        db.session.add(company)

    for job in iter_jobs():
        db.session.add(job)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
                
