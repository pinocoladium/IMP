from datetime import datetime

from telebot import telebot
from vk_api import vk_api

from application.salary import calculate_salary
from application.db.people import get_employees
from dirty.dirty_main import dirty_main

if __name__ == '__main__':
    print(datetime.now())
    print(calculate_salary())
    print(get_employees())
    print(dirty_main())
    