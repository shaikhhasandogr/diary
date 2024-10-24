from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Document, Employee, Project, Vendor


from django.utils.translation import gettext_lazy as _

# Change the titles and headers
admin.site.site_header = "Your Custom Admin Header"  # Header on the admin site
admin.site.site_title = "Your Custom Admin Title"  # Title on the browser tab
admin.site.index_title = "Welcome to Your Admin Dashboard"  # Title on the admin index page



class DocumentAdminForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'

    # Use the FilteredSelectMultiple widget for the employees field
    To_employees = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=FilteredSelectMultiple("Employees", is_stacked=False),
        required=True
    )

class DocumentAdmin(admin.ModelAdmin):
    form = DocumentAdminForm
    list_display = ['doc_no', 'remark', 'received_date']
    search_fields = ['doc_no', 'remark']

admin.site.register(Document, DocumentAdmin)
admin.site.register(Employee)
admin.site.register(Vendor)
admin.site.register(Project)
