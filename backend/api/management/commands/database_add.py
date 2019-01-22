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
        master = open("programofstudiesfinal.txt", "r", encoding="utf8")
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
            careers = []
            if line[16] == 'x':
                business = Career.objects.get(career_name = 'Business Management and Administration')
                business.suggested_classes.add(a_class)
                careers.append('Business Management and Administration')
            if line[17] =='x':
                finance = Career.objects.get(career_name = 'Finance')
                finance.suggested_classes.add(a_class)
                careers.append('Finance')
            if line[18] =='x':
                it = Career.objects.get(career_name = 'Information Technology')
                it.suggested_classes.add(a_class)
                careers.append('Information Technology')
            if line[19] =='x':
                marketing = Career.objects.get(career_name = 'Marketing')
                marketing.suggested_classes.add(a_class)
                careers.append('Marketing')
            if line[20] =='x':
                health_services = Career.objects.get(career_name = 'Health Services')
                health_services.suggested_classes.add(a_class)
                careers.append('Health Services')
            if line[21] =='x':
                temp = Career.objects.get(career_name = 'Education and Training')
                temp.suggested_classes.add(a_class)
                careers.append('Education and Training')
            if line[22] =='x':
                temp = Career.objects.get(career_name = 'Government and Public Administration')
                temp.suggested_classes.add(a_class)
                careers.append('Government and Public Administration')
            if line[23] =='x':
                temp = Career.objects.get(career_name = 'Hospitality and Tourism')
                temp.suggested_classes.add(a_class)
                careers.append('Hospitality and Tourism')
            if line[24] =='x':
                temp = Career.objects.get(career_name = 'Human Services')
                temp.suggested_classes.add(a_class)
                careers.append('Human Services')
            if line[25] =='x':
                temp = Career.objects.get(career_name = 'Law, Public Safety, Corrections and Security')
                temp.suggested_classes.add(a_class)
                careers.append('Law, Public Safety, Corrections and Security')
            if line[26] =='x':
                temp = Career.objects.get(career_name = 'Agriculture, Food and Natural Services')
                temp.suggested_classes.add(a_class)
                careers.append('Agriculture, Food and Natural Services')
            if line[27] =='x':
                temp = Career.objects.get(career_name = 'Arts, A/V, and Communications')
                temp.suggested_classes.add(a_class)
                careers.append('Arts, A/V, and Communications')
            if line[28] =='x':
                temp = Career.objects.get(career_name = 'Architecture and Construction')
                temp.suggested_classes.add(a_class)
                careers.append('Architecture and Construction')
            if line[29] =='x':
                temp = Career.objects.get(career_name = 'Manufacturing')
                temp.suggested_classes.add(a_class)
                careers.append('Manufacturing')
            if line[30] =='x':
                temp = Career.objects.get(career_name = 'Transportation, Distribution and Logistics')
                temp.suggested_classes.add(a_class)
                careers.append('Transportation, Distribution and Logistics')
            if line[31] =='x':
                temp = Career.objects.get(career_name = 'Science, Technology, and Mathematics')
                temp.suggested_classes.add(a_class)
                careers.append('Science, Technology, and Mathematics')
            a_class.careers = ",".join(careers)
            a_class.save()