"""
author : QY
"""
from faker import Faker


class GetData:
    def __init__(self):
        self.faker = Faker(locale='zh-CN')

    def get_name(self):
        return self.faker.name()

    def get_phone(self):
        return self.faker.phone_number()

