from api.models import Class
import os
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    help = "Help"

    def handle(self, **options):
        classes = Class.objects.all()
        if classes.count() != 0:
            classes.delete()
        master = open("programofstudies.txt", "r", encoding="utf8")
        for line in master:
            line = line.split(',')
            a_class = Class()
            a_class.code = line[0]
            a_class.class_name = line[1]
            a_class.credits = line[2]
            a_class.length = line[3]
            if line[4] == "1":
                a_class.weighted = True
            if line[4] != "1":
                a_class.weighted = False
            a_class.subject = line[5]
            a_class.grade = line[6].replace(";", ",")
            qual = []
            if line[7] == "x":
                qual.append("AP")
            if line[8] == "x":
                qual.append("Honors")
            if line[9] == "x":
                qual.append("MYP")
            if line[10] == "x":
                qual.append("MYP Elective")
            if line[11] == "x":
                qual.append("IB Diploma")
            if line[12] == "x":
                qual.append("NCAA")
            if line[13] == "x":
                qual.append("Global Fluency")
            qual = ','.join(qual)
            a_class.qualification = qual
            a_class.description = line[14].replace(";", ",")
            a_class.link = line[15]

            a_class.save()
