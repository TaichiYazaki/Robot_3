import csv
import os
import termcolor

DEFAULT_ROBOT_NAME = 'Roboko'


class Roboter(object):

    def __init__(self, robot_name=DEFAULT_ROBOT_NAME, user_name=''):
        self.robot_name = robot_name
        self.user_name = user_name

    def hello(self):
        f = open('roboter/templates/hello.txt',  'r')
        template = f.read()
        user_name = input(termcolor.colored(
            template.replace('$robot_name', self.robot_name), 'green'))
        self.user_name = user_name

    def greeting(self):
        path = 'ranking.csv'
        is_file = os.path.isfile(path)
        if is_file:
            with open('ranking.csv', 'r+') as ranking_csv:
                ranking_lists = ranking_csv.read().splitlines()
                count = {}
                for ranking_list in ranking_lists:
                    count.setdefault(ranking_list, 0)
                    count[ranking_list] += 1
                lists = sorted(count.items(), key=lambda x: x[1], reverse=True)
                for key, value in lists:
                    with open('roboter/templates/greeting.txt',
                              'r') as greeting_file:
                        template = greeting_file.read()
                    is_yes = input(termcolor.colored(
                        template.replace(
                            '$restaurant', key), 'red'))
                    if is_yes.lower() == 'y' or is_yes.lower() == 'yes':
                        writer = csv.writer(ranking_csv)
                        writer.writerow([key])
                        break
        else:
            pass

    def which_restaurant(self):
        with open('roboter/templates/which_restaurant.txt', 'r') as f:
            template = f.read()
        favorite_restaurant = input(termcolor.colored(
            template.replace('$user_name', self.user_name), 'red'))
        count = 1
        with open('ranking.csv', 'w', newline='') as f:
            header = ['NAME', 'COUNT']
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerow({'NAME': favorite_restaurant, 'COUNT': count})

    def good_bye(self):
        with open('roboter/templates/good_bye.txt', 'r') as f:
            template = f.read()
        print(termcolor.colored(
            template.replace('$user_name', self.user_name), 'green'))
