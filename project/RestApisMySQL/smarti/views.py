from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import xlsxwriter
from . import models
import pandas as pd
import time
from . import serializers
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def employer_list(request):
    # get all employers
    try:
        employers = models.EMPLOYER.objects.all()
        employer_serializer = serializers.EmployerSerializer(employers, many=True)
        return JsonResponse({'Employers list': employer_serializer.data}, safe=False, status=status.HTTP_200_OK)
    except:
        return JsonResponse({'message': 'Problem with DB'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def employer_detail(request, pk):
    # find employer by pk (id)
    try:
        print(pk)
        employerDetails = models.EMPLOYER.objects.get(pk=pk)

        employer_serializer = serializers.EmployerSerializer(employerDetails)
        print(employer_serializer)
        return JsonResponse({'Employer': employer_serializer.data}, safe=False, status=status.HTTP_200_OK)
    except models.EMPLOYER.DoesNotExist:
        return JsonResponse({'message': 'Employer does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def employer_delete(request, pk):
    try:
        employer = models.EMPLOYER.objects.get(pk=pk)
        if request.method == 'DELETE':
            employer.delete()
            return JsonResponse({'message': 'employer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except:
        return JsonResponse({'message': 'employer was not deleted !'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def employer_update(request, pk):
    try:
        employer = models.EMPLOYER.objects.get(pk=pk)

        if request.method == 'PUT':
            employer_data = JSONParser().parse(request)
            employer_serializer = serializers.EmployerSerializer(employer, data=employer_data)
        if employer_serializer.is_valid():
            employer_serializer.save()
            return JsonResponse({'Employer': employer_serializer.data}, safe=False, status=status.HTTP_200_OK)
    except:
        return JsonResponse(employer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def employer_create(request):
    try:
        if request.method == 'POST':
            employer_data = JSONParser().parse(request)
            employer_serializer = serializers.EmployerSerializer(data=employer_data)
            print(employer_serializer.is_valid())
            if employer_serializer.is_valid():
                employer_serializer.save()
                return JsonResponse({'New Employer Created': employer_serializer.data}, safe=False ,status=status.HTTP_201_CREATED)
    except:
        return JsonResponse({'Employer was not created'}, status=status.HTTP_400_BAD_REQUEST)

# .select_related('employerId')
@api_view(['GET'])
def employerWithContact_list(request):
    # get all employers
    try:
        contactWithEmployer = models.Contact.objects.all().select_related('employerId')
        contactWithEmployer_serializer = serializers.ContactSerializer(contactWithEmployer, many=True)
        return JsonResponse({'Employer With Contact': contactWithEmployer_serializer.data}, safe=False,
                            status=status.HTTP_200_OK)
    except models.EMPLOYER.DoesNotExist:
        return JsonResponse({'message': 'The Employers do not exist'}, status=status.HTTP_404_NOT_FOUND)



# Writing to an excel
@api_view(['GET'])
def write_to_excel(request):
    try:
        row = 1
        col = 0
        colHeaders = 0;
        rowHeaders = 0;
        employers = models.EMPLOYER.objects.all()
        res = [(x.id,x.name,x.phone,x.email) for x in employers]
        workbook = xlsxwriter.Workbook('employers.xlsx')
        worksheet = workbook.add_worksheet('Employers')
        headers =['Id', 'Name', 'Phone', 'Email']
        for c in headers:
            worksheet.write(rowHeaders,colHeaders,c)
            colHeaders+=1

        for a,b,c,d in (res):
            worksheet.write(row, col, a)
            worksheet.write(row, col + 1, b)
            worksheet.write(row, col + 2, c)
            worksheet.write(row, col + 3, d)
            row += 1
        workbook.close()
        return JsonResponse({'Result': 'Writed to Excel'}, status=status.HTTP_200_OK)
    except:
        return JsonResponse({'message': 'There is a problem with db/write file'}, status=status.HTTP_404_NOT_FOUND)




