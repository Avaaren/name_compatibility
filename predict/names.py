import csv

from .models import Relationship


def create():
    objs = []
    with open('predict/relationships.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:

            objs.append(Relationship(female_name=row[0],
                                     male_name=row[1],
                                     slug=row[2],
                                     percent_in_love=row[3],
                                     percent_in_married=row[4],
                                     header=row[5],
                                     description=row[6]))

    Relationship.objects.bulk_create(objs)
