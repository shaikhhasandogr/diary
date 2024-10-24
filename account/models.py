from django.db import models

class Employee(models.Model):
    CATEGORY_CHOICES = [
        ('GEN', 'General'),
        ('OBC', 'Other Backward Class'),
        ('SC', 'Scheduled Caste'),
        ('ST', 'Scheduled Tribe'),
        ('NT', 'Nomadic Tribe'),
        ('OTH', 'Other'),
    ]

    CAT_CHOICES = [  # Renamed variable for clarity
        ('SCI', 'Scientific'),
        ('TECH', 'Technical'),
        ('ADMN', 'Administration'),
        ('MTS', 'Skilled Supporting Staff'),
    ]

    GROUP_CHOICES = [  # Renamed variable for clarity
        ('A', 'A Group'),
        ('B', 'B Group'),
        ('C', 'C Group'),
    ]

    emp_id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    emp_name = models.CharField(max_length=50)
    emp_desi = models.CharField(max_length=25)  # Designation
    emp_email = models.EmailField(max_length=50, unique=True)
    emp_mobile = models.CharField(max_length=10, unique=True)  # Assuming 10 digits, local
    emp_whatapps_no = models.CharField(max_length=10, blank=True)
    emp_caste = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='GEN')
    emp_category = models.CharField(max_length=4, choices=CAT_CHOICES, default='SCI')
    emp_group = models.CharField(max_length=1, choices=GROUP_CHOICES, default='A')
    emp_icar_joining_date = models.DateField(null=True, blank=True)
    emp_dogr_joining_date = models.DateField(null=True, blank=True)
    emp_birth_date = models.DateField(null=True, blank=True)
    emp_panno = models.CharField(max_length=15, blank=True, unique=True)
    emp_adharno = models.CharField(max_length=12, blank=True, unique=True)
    emp_bank_acccount_no = models.CharField(max_length=20, blank=True, unique=True)
    emp_bank_branch_name = models.CharField(max_length=30, blank=True, unique=True)
    emp_bank_ifsc_code = models.CharField(max_length=10, blank=True, unique=True)
    emp_is_staff = models.BooleanField(default=True)  # True if employee is a staff member
    emp_is_active = models.BooleanField(default=True)
    emp_left_date = models.DateField(null=True, blank=True)  # Make it nullable for active employees
    
    def __str__(self):
        return self.emp_name



class Project(models.Model):
    project_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    project_code = models.IntegerField()  # Integer field for account code
    project_name = models.CharField(max_length=45)  # Varchar equivalent
    project_desc = models.CharField(max_length=255, blank=True, null=True)  # Varchar equivalent, can be optional
    project_pi = models.IntegerField()  # Integer field for PI (assuming it's an integer)
    project_company = models.CharField(max_length=60, blank=True, null=True)  # Varchar equivalent, can be optional
    project_amt = models.IntegerField()  # Integer field for amount
    project_startdate = models.DateField()  # Date field for start date
    project_enddate = models.DateField(blank=True, null=True)  # Date field for end date, optional

    def __str__(self):
        return self.project_name  # Display account name when referenced



class Vendor(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150)
    address = models.TextField()
    mobile = models.CharField(max_length=15)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    gst_no = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.name} - {self.company_name}"




class Document(models.Model):
    TYPE_CHOICES = [
        ('Imprest', 'Imprest'),
        ('General', 'General'),
        ('Administrative', 'Administrative'),
        ('Scientific', 'Scientific'),
    ]

    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('French', 'French'),
    ]

    doc_no = models.CharField(max_length=50, unique=True)
    received_date = models.DateField()
    received_from = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='documents')  # ForeignKey to Vendor
    doc_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
#    to = models.ManyToManyField(Employee)  # Reference to Employee model (many-to-many)
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.doc_no

