import datetime
import os
import random
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rstaller.settings')

import django

django.setup()

from colector.models import Colector

SEED = 0

films = {'Laptop':
                 ['1'
                ,'2'
                ,'3'
                ,'4'
                ,'5'
                ,'6'
                ,'7'
                ,'9'
                ,'10'
                ,'11'
                ,'12'
                ,'13'
                ,'14'
                ,'15'
                ,'16'
                ,'17'
                ,'18'
                ,'19'
                ,'20'],
             'Impresora': ['21'
                ,'22'
                ,'23'
                ,'24'
                ,'25'
                ,'26'
                ,'27'
                ,'28'
                ,'29'
                ,'30'
                ,'31'
                ,'32'
                ,'33'
                ,'34'
                ,'35'
                ,'36'
                ,'37'
                ,'38'
                ,'39'
                ,'40'
             ],
        'Oficina':['41'
                ,'41'
                ,'42'
                ,'43'
                ,'44'
                ,'45'
                ,'46'
                ,'47'
                ,'48'
                ,'49'
                ,'50'
                ,'51'
                ,'52'
                ,'53'
                ,'54'
                ,'55'
                ,'56'
                ,'57'
                ,'58'
                ,'59'
                ,'60'
            ],
        'action': ['61'
                ,'62'
                ,'63'
                ,'64'
                ,'65'
                ,'66'
                ,'67'
                ,'68'
                ,'69'
                ,'70'
                ,'71'
                ,'72'
                ,'73'
                ,'74'
                ,'75'
                ,'76'
                ,'77'
                ,'78'
                ,'79'
                ,'80'
            ]}

class User:
    sessionId = 0
    userId = 0
    likes = {}
    events = {}

    def __init__(self, user_id, action, laptop, impresora ,oficina):
        self.sessionId = random.randint(0, 1000000)
        self.userId = user_id
        self.likes = {'action': action, 'Laptop': laptop, 'Impresora': impresora,'Oficina':oficina}
        self.events = {self.sessionId: []}

    def get_session_id(self):
        if random.randint(0, 100) > 90:
            self.sessionId += 1
            self.events[self.sessionId] = []

        return self.sessionId

    def select_genre(self):
        return sample(self.likes)


def select_film(user):

    genre = user.select_genre()
    interested_films = films[genre]
    film_id = ''
    while film_id == '':
        film_candidate = interested_films[random.randint(0, len(interested_films) - 1)]
        if film_candidate not in user.events[user.sessionId]:
            film_id = film_candidate

    return film_id


def select_action(user):
    actions = {'genreView': 15, 'details': 50, 'moreDetails': 24, 'addToList': 10, 'buy': 1}

    return sample(actions)


def sample(dictionary):
    random_number = random.randint(0, 100)
    index = 0
    for key, value in dictionary.items():
        index += value

        if random_number <= index:
            return key


def main():
    Colector.objects.all().delete()
    random.seed(SEED)

    number_of_events = 50000

    print("Generating Data")
    users = [
        User(5, 20, 30, 50, 40),
        User(6, 50, 20, 40, 50),
        User(7, 20, 30, 50, 40),
        User(8, 100, 0, 0, 0),
        User(9, 0, 100, 0, 0),
        User(10, 0, 0, 100, 0),
        User(11, 0, 0, 0, 100),
    ]
    print("Simulating " + str(len(users)) + " visitors")

    for x in range(0, number_of_events):
        randomuser_id = random.randint(0, len(users) - 1)
        user = users[randomuser_id]
        selected_film = select_film(user)
        action = select_action(user)
        if action == 'buy':
            user.events[user.sessionId].append(selected_film)
        print("user id " + str(user.userId) + " selects film " + str(selected_film) + " and " + action)

        l = Colector(user_id=str(user.userId),
                content_id=selected_film,
                event=action,
                session_id=str(user.get_session_id()),
                created=datetime.datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
                )
        l.save()

    print("users\n")
    for u in users:
        print("user with id {} \n".format(u.userId))
        for key, value in u.events.items():
            if len(value) > 0:
                print(" {}: {}".format(key, value))


if __name__ == '__main__':
    print("Starting MovieGeeks Log Population script...")
    main()
