import os
import json
from random import randint
from faker import Faker
from simplejob.models import db, User, Company, Job

faker = Faker()  # 创建 faker 工厂对象，生成一个用于测试数据的库

user = User(
    username='Shiyanlou',
    password='shiyanlou',
    phone='12012134999',
    email='shiyanlou@qq.com',
    role=30,
)

def iter_companys():
    #for company in jobs:
    yield Company(
                #logo = company['logo'],
                #company_name = company['company_name'],
                #offical_websit = company['offical_websit'],
                #industry = company['industry'],
                #stage = company['stage'],
                #city = company['city']
                name = 'testcompany',
                email = 'test@test.com',
                website = 'http://www.111.com',
                password = '123456',
                user = user,
                address = 'beijing'
                )
companys = list(iter_companys())
print(companys)
def iter_jobs():
    with open(os.path.join(os.getcwd(), 'datas', 'jobs.json')) as f:
        jobs = json.load(f)
    for job in jobs:
        yield Job(
            #job_name = job['jobname'],
            #wage_area = job['wage_area'],
            #working_address = job['working_address'],
            #experience_required = job['experience'],
            #edu_required = job['education'],
            #release_date = job['release_date']
            name = job['name'],
            #salary = job['salary'],
            #address = job['address'],
            company = companys[0]
            )
print(next(iter_jobs()))
def run():
    for company in companys:
        db.session.add(company)

    for job in iter_jobs():
        db.session.add(job)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
                
