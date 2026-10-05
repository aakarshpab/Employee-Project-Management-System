from django.shortcuts import render , get_object_or_404
from .models import Employee, Project


def home(request):
    employee_count = Employee.objects.count()
    active_employee_count = Employee.objects.filter(is_active=True).count()

    project_count = Project.objects.count()
    completed_project_count = Project.objects.filter(status='Completed').count()

    context = {
        'employee_count': employee_count,
        'active_employee_count': active_employee_count,
        'project_count': project_count,
        'completed_project_count': completed_project_count,
    }

    return render(request, 'home.html', context)


def employee_list(request):
    employees = Employee.objects.all()

    department = request.GET.get('department')

    if department:
        employees = employees.filter(department=department)

    departments = Employee.objects.values_list(
        'department', flat=True
    ).distinct()

    context = {
        'employees': employees,
        'departments': departments,
        'selected_department': department,
    }

    return render(request, 'employee_list.html', context)


def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)

    context = {
        'employee': employee,
    }

    return render(request, 'employee_details.html', context)


def project_list(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'project_list.html', context)


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)

    context = {
        'project': project,
    }

    return render(request, 'project_details.html', context)
