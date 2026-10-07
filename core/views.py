from django.shortcuts import render , get_object_or_404
from .models import Employee, Project
from django.db.models import Q
from django.core.paginator import Paginator


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

    # Get filter and search parameters from the URL
    department = request.GET.get('department')
    search_query = request.GET.get('q', '')  # Grab what the user typed in the search bar

    # 2. Filter by Name or Employee ID if a search query exists
    if search_query:
        employees = employees.filter(
            Q(employee_id__icontains=search_query) | 
            Q(name__icontains=search_query)
        )

    # 3. Filter by department if selected
    if department:
        employees = employees.filter(department=department)

    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    departments = Employee.objects.values_list(
        'department', flat=True
    ).distinct()

    context = {
        'employees': page_obj,  # page_obj replaces the standard queryset
        'page_obj': page_obj,
        'departments': departments,
        'selected_department': department,
        'search_query': search_query,  # Pass this back so the input keeps its text
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


