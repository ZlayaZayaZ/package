from datetime import datetime
from application import salary1
import application
from application.db import people

if __name__ == '__main__':
    print(datetime.now())
    print(salary1.calculate_salary())
    print(application.db.people.get_employees())

