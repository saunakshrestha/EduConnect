from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.http import require_GET

from admin_dashboard.forms import StudentForm, AddressForm, UsersForm

from admin_dashboard.filters import StudentFilter
from admin_dashboard.models import Student
import logging

logger = logging.getLogger('educonnect_logger')


@method_decorator(login_required, name='dispatch')
class HomeView(View):
    def get(self, request, *args, **kwargs):
        logger.info(request.GET)
        try:
            student_filter = StudentFilter(request.GET, queryset=Student.objects.all())
            logger.info(f"User {request.user.username} accessed the student home page.")
            return render(request, 'admin_dashboard/home.html', {'filter': student_filter})
        except Exception as e:
            logger.error(f"Error: {e}")
            return redirect('home')


class AddStudentView(View):
    def get(self, request, *args, **kwargs):
        form = StudentForm()
        users_form = UsersForm()
        perm_addresses = AddressForm(prefix='perm')
        temp_addresses = AddressForm(prefix='temp')

        context = {
            'form': form,
            'perm_addresses': perm_addresses,
            'temp_addresses': temp_addresses,
            'users_form': users_form
        }
        return render(request, 'admin_dashboard/entry_students/entry_student.html', context)

    def post(self, request, *args, **kwargs):
        logger.info(request.POST)

        users_form = UsersForm(request.POST)
        perm_address_form = AddressForm(request.POST, prefix='perm')
        temp_address_form = AddressForm(request.POST, prefix='temp')
        student_form = StudentForm(request.POST)
        if users_form.is_valid():
            logger.info(f"User form is valid: {users_form.cleaned_data}")
        if perm_address_form.is_valid():
            logger.info(f"Perm Address form is valid: {perm_address_form.cleaned_data}")
        if temp_address_form.is_valid():
            logger.info(f"Temp Address form is valid: {temp_address_form.cleaned_data}")
        if student_form.is_valid():
            logger.info(f"Student form is valid: {student_form.cleaned_data}")
        else:
            logger.info(f"Student form is invalid: {student_form.errors}")

        if (users_form.is_valid() and perm_address_form.is_valid() and temp_address_form.is_valid()
                and student_form.is_valid()):
            try:
                with transaction.atomic():
                    # Create User
                    user = users_form.save()

                    # Create Permanent Address
                    perm_address = perm_address_form.save()

                    # Create Temporary Address
                    temp_address = temp_address_form.save()

                    # Create Student
                    student = student_form.save(commit=False)
                    student.user = user
                    student.permanent_address = perm_address
                    student.temporary_address = temp_address
                    student.save()

                return redirect('home')
            except Exception as e:
                logger.error(f"Error saving student data: {e}")

        else:
            logger.error(f"Form errors: {users_form.errors}, {perm_address_form.errors}, {temp_address_form.errors}, ")
        context = {
            'form': student_form,
            'perm_addresses': perm_address_form,
            'temp_addresses': temp_address_form,
            'users_form': users_form
        }
        return render(request, 'admin_dashboard/entry_students/entry_student.html', context)


@require_GET
def get_districts(request):
    province = request.GET.get('province')
    logger.info(f"Province selected: {province}")

    # Mapping of districts to their respective provinces
    province_district_mapping = {
        'Province 1': ['Bhojpur', 'Dhankuta', 'Ilam', 'Jhapa', 'Khotang', 'Morang', 'Okhaldhunga', 'Panchthar',
                       'Sankhuwasabha', 'Solukhumbu', 'Sunsari', 'Taplejung', 'Terhathum', 'Udayapur'],
        'Madhesh Pradesh': ['Bara', 'Dhanusha', 'Mahottari', 'Parsa', 'Rautahat', 'Saptari', 'Sarlahi', 'Siraha'],
        'Bagmati Pradesh': ['Bhaktapur', 'Chitwan', 'Dhading', 'Dolakha', 'Kathmandu', 'Kavrepalanchok', 'Lalitpur',
                            'Makwanpur', 'Nuwakot', 'Ramechhap', 'Rasuwa', 'Sindhuli', 'Sindhupalchok'],
        'Gandaki Pradesh': ['Baglung', 'Gorkha', 'Kaski', 'Lamjung', 'Manang', 'Mustang', 'Myagdi', 'Nawalpur',
                            'Parbat',
                            'Syangja', 'Tanahun'],
        'Lumbini Pradesh': ['Arghakhanchi', 'Banke', 'Bardiya', 'Dang', 'Eastern Rukum', 'Gulmi', 'Kapilvastu',
                            'Parasi', 'Palpa', 'Pyuthan', 'Rolpa', 'Rupandehi'],
        'Karnali Pradesh': ['Dailekh', 'Dolpa', 'Humla', 'Jajarkot', 'Jumla', 'Kalikot', 'Mugu', 'Salyan', 'Surkhet',
                            'Western Rukum'],
        'Sudurpashchim Pradesh': ['Achham', 'Baitadi', 'Bajhang', 'Bajura', 'Dadeldhura', 'Darchula', 'Doti',
                                  'Kailali', 'Kanchanpur']
    }

    # Get the districts for the selected province
    filtered_districts = province_district_mapping.get(province, [])

    return JsonResponse(filtered_districts, safe=False)
