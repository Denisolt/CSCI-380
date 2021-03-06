from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.

from .models import College, School, Department, Course, Exam, MC_Question, MA_Question, TF_Question, ORD_Question, ESS_Question, MAT_Question, NUM_Question, SR_Question, FIB_PLUS_Question, FIB_SINGLE_Question
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin


def index(request):
    colleges = College.objects.filter()
    return render(request,'index.html')

def school(request):
    schools = School.objects.filter()
    return render(request,'index.html',{'schools': schools})

class CollegeListView(generic.ListView):
    """
    Generic class-based list view for a list of authors.
    """
    model = College
    paginate_by = 10 

class SchoolListView(generic.ListView):
    model = School
    paginate_by = 10

class SchoolDetailView(generic.DetailView):
    model = School

class CollegeDetailView(generic.DetailView):
	model = College

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CollegeCreate(PermissionRequiredMixin, CreateView):
    model = College
    fields = '__all__'
    initial={'name':'College',}
    permission_required = 'catalog.can_mark_returned'

class CollegeUpdate(PermissionRequiredMixin, UpdateView):
    model = College
    fields = ['name']
    permission_required = 'catalog.can_mark_returned'

class CollegeDelete(PermissionRequiredMixin, DeleteView):
    model = College
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

class SchoolCreate(PermissionRequiredMixin, CreateView):
    model = School
    fields = '__all__'
    initial={'name':'School',}
    permission_required = 'catalog.can_mark_returned'

class SchoolUpdate(PermissionRequiredMixin, UpdateView):
    model = School
    fields = ['name']
    permission_required = 'catalog.can_mark_returned'

class SchoolDelete(PermissionRequiredMixin, DeleteView):
    model = School
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

class DepartmentCreate(PermissionRequiredMixin, CreateView):
    model = Department
    fields = '__all__'
    initial={'name':'Department',}
    permission_required = 'catalog.can_mark_returned'

class DepartmentUpdate(PermissionRequiredMixin, UpdateView):
    model = Department
    fields = ['name']
    permission_required = 'catalog.can_mark_returned'

class DepartmentDelete(PermissionRequiredMixin, DeleteView):
    model = Department
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

class DepartmentDetailView(generic.DetailView):
    model = Department

class CourseCreate(PermissionRequiredMixin, CreateView):
    model = Course
    fields = '__all__'
    initial={'name':'Course', 'courseID':'CSCI-360'}
    permission_required = 'catalog.can_mark_returned'

class CourseUpdate(PermissionRequiredMixin, UpdateView):
    model = Course
    fields = ['name', 'CourseID']
    permission_required = 'catalog.can_mark_returned'

class CourseDelete(PermissionRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

class CourseDetailView(generic.DetailView):
    model = Course

class ExamCreate(PermissionRequiredMixin, CreateView):
    model = Exam
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class ExamUpdate(PermissionRequiredMixin, UpdateView):
    model = Exam
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class ExamDelete(PermissionRequiredMixin, DeleteView):
    model = Exam
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

class ExamDetailView(generic.DetailView):
    model = Exam

# here it is
class printing_exam():
    model = Exam

#--------------------------------------------------------#

class MCQDetailView(generic.DetailView):
    model = MC_Question

class MAQDetailView(generic.DetailView):
    model = MA_Question

class TFQDetailView(generic.DetailView):
    model = TF_Question

class ESSQDetailView(generic.DetailView):
    model = ESS_Question

class ORDQDetailView(generic.DetailView):
    model = ORD_Question

class MATQDetailView(generic.DetailView):
    model = MAT_Question

class NUMQDetailView(generic.DetailView):
    model = NUM_Question

class SRQDetailView(generic.DetailView):
    model = SR_Question

class FIBQDetailView(generic.DetailView):
    model = FIB_SINGLE_Question

class FIBPLUSQDetailView(generic.DetailView):
    model = FIB_PLUS_Question

#--------------------------------------------------------#

class MCQListView(generic.ListView):
    model = MC_Question

class MAQListView(generic.ListView):
    model = MA_Question

class TFQListlView(generic.ListView):
    model = TF_Question

class ESSQListlView(generic.ListView):
    model = ESS_Question

class ORDQListlView(generic.ListView):
    model = ORD_Question

class MATQListView(generic.ListView):
    model = MAT_Question

class NUMQListlView(generic.ListView):
    model = NUM_Question

class SRQListView(generic.ListView):
    model = SR_Question

class FIBQListView(generic.ListView):
    model = FIB_SINGLE_Question

class FIBPLUSQListView(generic.ListView):
    model = FIB_PLUS_Question

#--------------------------------------------------------#

class MCQCreate(PermissionRequiredMixin, CreateView):
    model = MC_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class MCQUpdate(PermissionRequiredMixin, UpdateView):
    model = MC_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class MCQDelete(PermissionRequiredMixin, DeleteView):
    model = MC_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'
#--------------------------------------------------------#

class MAQCreate(PermissionRequiredMixin, CreateView):
    model = MA_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class MAQUpdate(PermissionRequiredMixin, UpdateView):
    model = MA_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class MAQDelete(PermissionRequiredMixin, DeleteView):
    model = MA_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

#--------------------------------------------------------#

class TFQCreate(PermissionRequiredMixin, CreateView):
    model = TF_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class TFQUpdate(PermissionRequiredMixin, UpdateView):
    model = TF_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class TFQDelete(PermissionRequiredMixin, DeleteView):
    model = TF_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

#--------------------------------------------------------#

class ESSQCreate(PermissionRequiredMixin, CreateView):
    model = ESS_Question
    fields = '__all__'
    initial={'name': 'Midterm'}
    permission_required = 'catalog.can_mark_returned'

class ESSQUpdate(PermissionRequiredMixin, UpdateView):
    model = ESS_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class ESSQDelete(PermissionRequiredMixin, DeleteView):
    model = ESS_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

#--------------------------------------------------------#

class ORDQCreate(PermissionRequiredMixin, CreateView):
    model = ORD_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class ORDQUpdate(PermissionRequiredMixin, UpdateView):
    model = ORD_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class ORDQDelete(PermissionRequiredMixin, DeleteView):
    model = ORD_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

#--------------------------------------------------------#

class MATQCreate(PermissionRequiredMixin, CreateView):
    model = MAT_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class MATQUpdate(PermissionRequiredMixin, UpdateView):
    model = MAT_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class MATQDelete(PermissionRequiredMixin, DeleteView):
    model = MAT_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

#--------------------------------------------------------#

class NUMQCreate(PermissionRequiredMixin, CreateView):
    model = NUM_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class NUMQUpdate(PermissionRequiredMixin, UpdateView):
    model = NUM_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class NUMQDelete(PermissionRequiredMixin, DeleteView):
    model = NUM_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

#--------------------------------------------------------#

class SRQCreate(PermissionRequiredMixin, CreateView):
    model = SR_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class SRQUpdate(PermissionRequiredMixin, UpdateView):
    model = SR_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class SRQDelete(PermissionRequiredMixin, DeleteView):
    model = SR_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

#--------------------------------------------------------#

class FIBCreate(PermissionRequiredMixin, CreateView):
    model = FIB_SINGLE_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class FIBUpdate(PermissionRequiredMixin, UpdateView):
    model = FIB_SINGLE_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class FIBDelete(PermissionRequiredMixin, DeleteView):
    model = FIB_SINGLE_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

#--------------------------------------------------------#

class FIB_PLUS_Create(PermissionRequiredMixin, CreateView):
    model = FIB_PLUS_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class FIB_PLUS_Update(PermissionRequiredMixin, UpdateView):
    model = FIB_PLUS_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class FIB_PLUS_Delete(PermissionRequiredMixin, DeleteView):
    model = FIB_PLUS_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

#--------------------------------------------------------#
#printing things starts here

class printing_v1(generic.DetailView):
    model = Exam
    template_name = "catalog/exam_question_only.html"

class printing_v2(generic.DetailView):
    model = Exam
    template_name = "catalog/sample_exam_BB.html"

class printing_v3(generic.DetailView):
    model = Exam
    template_name = "catalog/sample_exam_qa.html"