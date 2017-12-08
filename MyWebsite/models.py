from pickletools import I
from time import timezone

from django.core.validators import URLValidator
from model_utils import models


class Recruiter(models.Model):
    Organization_name = models.CharField(max_length=100,blank=False,null=False)
    Organization_website = models.TextField(validators=[URLValidator()])
    Organization_profile = models.CharField(max_length = 250,blank=True,null=True)
    Offer_Choices = (
        I('JOB ONLY','JOB ONLY'),
         ('INTERNSHIP ONLY ', 'INTERNSHIP ONLY'),
         ('JOB+INTERNSHIP', 'JOB+INTERNSHIP'),
    )
    offer = models.CharField(max_length = 100,choices = Offer_Choices,default = 'JOB ONLY')
    Intern_Choices = (
        ('Yes','Yes'),
        ('No','No'),
        ('Maybe','Maybe'),
    )
    Intern = models.CharField(max_length = 100,choices = Intern_Choices,default = 'No')
    Job_Profile  = models.CharField(max_length =300,blank=False,null=False)
    Job_Description = models.CharFiled(max_length = 500,blank=False,null=False)
    Locations = models.CharField(max_length = 100,blank=False,null=False)
    CTC  = models.IntegerField(blank=False,null=False)
    Service_Choices = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
    service = models.CharField(blank=False,choices = Service_Choices,default='0')
    Bond_Conditions = models.CharField(max_length = 200,blank=True,null=True)
    Tentative_Date = models.DateTimeField(blank = False, null = False,default = timezone.now())
    Other_details = models.TextArea(blank= True,null=True)
    Criteria_Choices = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
    )
    Criteria = models.CharField(blank=False,null=False,choices = Criteria_Choices)
    Offers_intend = models.IntegerField(blank = True,null=True)
    Officials_Visit = models.IntegerField(blank=True,null=True)
    Rooms_required = models.IntegerField(blank = True,null=True)
    Rooms_Type = models.CharField(blank = True,null=True,max_length = 100)
    Logistic_Support = models.CharField(blank = True,null = True,max_length = 100)
    Name = models.CharField(blank = False,null = False,max_length = 100)
    Designation = models.CharField(blank = False,null = False,max_length = 100)
    email = models.EmailField(max_length=50, null=False,blank = False)
    Contact_Number = models.IntegerField(blank = False,null = False)

