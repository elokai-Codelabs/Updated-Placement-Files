from django.shortcuts import render,redirect
# models
from .models import *

# import pandas
import pandas as pd
# 
from django.contrib import messages

 

def read_course_excel(request):
    if request.method == 'POST':
        file = request.FILES.get("file")
        excel_file = pd.read_excel(file)
        df = pd.DataFrame(excel_file)

        for index, row in df.iterrows():
            try:
                # Check if course with the given course code already exists
                existing_course = Course.objects.filter(course_code=row['COURSE_CODE']).first()
                if existing_course:
                    # If the course with the course code already exists, show a message
                    messages.warning(request, f"Course with course code '{row['COURSE_CODE']}' already exists.")
                else:
                    # Create a new course
                    course, created = Course.objects.get_or_create(
                        course_code=row['COURSE_CODE'],
                        defaults={
                            'course_name': row['COURSE_NAME'],
                        }
                    )
                    if not created:
                        # If the record already exists, skip it and show a message
                        messages.warning(request, f"The course with course code '{row['COURSE_CODE']}' already exists and was skipped.")
            except Exception as e:
                # If any error occurs during the creation of the record, show an error message
                messages.error(request, f"Error occurred for course with course code '{row['COURSE_CODE']}': {str(e)}")

        messages.success(request, 'Courses uploaded successfully')
        return redirect('courses')
    

    
def read_program_excel(request):
    if request.method == 'POST':
        file = request.FILES.get("file")
        excel_file = pd.read_excel(file)
        df = pd.DataFrame(excel_file)

        for index, row in df.iterrows():
            try:
                # Check if program with the given program code already exists
                existing_program = Program.objects.filter(name=row['NAME_OF_PROGRAM']).first()
                if existing_program:
                    # If the program with the program code already exists, show a message
                    messages.warning(request, f"program with name '{row['NAME_OF_PROGRAM']}' already exists.")
                else:
                    # Create a new program
                    program, created = Program.objects.get_or_create(
                        name=row['NAME_OF_PROGRAM'],
                        
                    )
                    if not created:
                        # If the record already exists, skip it and show a message
                        messages.warning(request, f"The program with name '{row['NAME_OF_PROGRAM']}' already exists and was skipped.")
            except Exception as e:
                # If any error occurs during the creation of the record, show an error message
                messages.error(request, f"Error occurred for program with program code '{row['NAME_OF_PROGRAM']}': {str(e)}")

        messages.success(request, 'programs uploaded successfully')
        return redirect('programs')
