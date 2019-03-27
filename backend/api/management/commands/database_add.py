from api.models import Class,Career
import os
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    help = "Help"

    def handle(self, **options):
        classes = Class.objects.all()
        careers = Career.objects.all()
        if classes.count() != 0:
            classes.delete()
        if careers.count() != 0:
            careers.delete()
        clusters = open("careerclusters.txt","r",encoding = "utf8")
        for line in clusters:
            line = line.split(',')
            a_career = Career()
            a_career.career_name = line[0].replace(";",",")
            a_career.description = line[1].replace(";",",")
            a_career.career_pathways = line[2]
            a_career.save()
        master = open("POS3.txt", "r", encoding="utf8")
        for line in master:
            line = line.split(',')
            a_class = Class()
            a_class.code = line[0]
            a_class.class_name = line[1]
            a_class.credits = line[6]
            a_class.length = line[4]
            a_class.mods = line[5]
            if line[7] == "Y":
                a_class.weighted = True
            if line[7] != "Y":
                a_class.weighted = False
            a_class.subject = line[2]
            if line[3] == "":
                a_class.grade == "9,10,11,12"
            else:
                a_class.grade = line[3].replace(";", ",")
            a_class.prerequisite = line[11].replace(";",",")
            qual = []
            if line[8] == "X":
                qual.append("AP")
            if line[9] == "X":
                qual.append("Honors")
            if line[10] == "X":
                qual.append("IB Diploma")
            qual = ','.join(qual)
            a_class.qualification = qual
            a_class.description = line[12].replace(";", ",")
            a_class.link = line[13]
            a_class.save()
            if line[15] == 'X':
                business = Career.objects.get(career_name = 'Business Management and Administration')
                business.suggested_classes.add(a_class)
                a_class.careers.add(business)
            if line[16] =='X':
                finance = Career.objects.get(career_name = 'Finance')
                finance.suggested_classes.add(a_class)
                a_class.careers.add(finance)
            if line[17] =='X':
                it = Career.objects.get(career_name = 'Information Technology')
                it.suggested_classes.add(a_class)
                a_class.careers.add(it)
            if line[18] =='X':
                marketing = Career.objects.get(career_name = 'Marketing')
                marketing.suggested_classes.add(a_class)
                a_class.careers.add(marketing)
            if line[28] =='X':
                health_services = Career.objects.get(career_name = 'Health Services')
                health_services.suggested_classes.add(a_class)
                a_class.careers.add(health_services)
            if line[23] =='X':
                temp = Career.objects.get(career_name = 'Education and Training')
                temp.suggested_classes.add(a_class)
                a_class.careers.add(temp)
            if line[24] =='X':
                temp = Career.objects.get(career_name = 'Government and Public Administration')
                temp.suggested_classes.add(a_class)
                a_class.careers.add(temp)
            if line[25] =='X':
                temp = Career.objects.get(career_name = 'Hospitality and Tourism')
                temp.suggested_classes.add(a_class)
                a_class.careers.add(temp)
            if line[26] =='X':
                temp = Career.objects.get(career_name = 'Human Services')
                temp.suggested_classes.add(a_class)
                a_class.careers.add(temp)
            if line[27] =='X':
                temp = Career.objects.get(career_name = 'Law, Public Safety, Corrections and Security')
                temp.suggested_classes.add(a_class)
                a_class.careers.add(temp)
            if line[29] =='X':
                temp = Career.objects.get(career_name = 'Agriculture, Food and Natural Services')
                temp.suggested_classes.add(a_class)
                a_class.careers.add(temp)
            if line[14] =='X':
                temp = Career.objects.get(career_name = 'Arts, A/V, and Communications')
                temp.suggested_classes.add(a_class)
                a_class.careers.add(temp)
            if line[19] =='X':
                temp = Career.objects.get(career_name = 'Architecture and Construction')
                temp.suggested_classes.add(a_class)
                a_class.careers.add(temp)
            if line[20] =='X':
                temp = Career.objects.get(career_name = 'Manufacturing')
                temp.suggested_classes.add(a_class)
                a_class.careers.add(temp)
            if line[21] =='X':
                temp = Career.objects.get(career_name = 'Transportation, Distribution and Logistics')
                temp.suggested_classes.add(a_class)
                a_class.careers.add(temp)
            if line[22] =='X':
                temp = Career.objects.get(career_name = 'Science, Technology, and Mathematics')
                temp.suggested_classes.add(a_class)
                a_class.careers.add(temp)
            a_class.save()