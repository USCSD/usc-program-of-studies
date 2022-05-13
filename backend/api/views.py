from rest_framework import generics, filters
from .models import Class, Career, Info
from .serializers import *

class class_list(generics.ListCreateAPIView):
    serializer_class = ClassSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `grade` query parameter in the URL.
        """
        queryset = Class.objects.all()
        grade = self.request.query_params.get('grade', None)
        if grade is not None:
            queryset = queryset.filter(grade__contains=grade)
        subject = self.request.query_params.get('subject', None)
        if subject is not None:
            queryset = queryset.filter(subject__contains=subject)
        qualification = self.request.query_params.get('qualification', None)
        if qualification is not None:
            queryset = queryset.filter(qualification__contains=qualification)
        length = self.request.query_params.get('length', None)
        if length is not None:
            queryset = queryset.filter(length__contains=length)
        credit = self.request.query_params.get('credits', None)
        if credit is not None:
            queryset = queryset.filter(credits__contains=credit)
        viewable = self.request.query_params.get('viewable', None)
        if viewable is not None:
            queryset = queryset.filter(viewable__exact=viewable)
        return queryset

    filter_backends = (filters.SearchFilter,)
    search_fields = ('class_name', 'credits')


class class_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class career_list(generics.ListCreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer


class career_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer


class info_list(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class info_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
