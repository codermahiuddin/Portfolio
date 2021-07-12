from django.db import models
from django.db.models import fields

# Create your models here.

class Isavailable(models.Model):
    availableinfo = models.CharField(max_length=50)

    def __str__(self):
        return self.availableinfo
    
class AuthorPeronal(models.Model):
    FullName = models.CharField(max_length=50, default='Md Mahiuddin')
    Address  = models.CharField(max_length=50, default='Panchagarch')
    Phone = models.CharField(max_length=50, default='+8801')
    Email = models.CharField(max_length=50, default=' @gmail.com')
    Github = models.CharField(max_length=150)
    Linkdin = models.CharField(max_length=150)
    BrithInfo = models.DateField()
    Nationality  = models.CharField(max_length=50,default='Bangladesh')
    Langages = models.CharField(max_length=50)
    availableinfo = models.OneToOneField(Isavailable, on_delete=models.CASCADE)
    shortDesc = models.TextField(max_length=500, default='')
 
    def __str__(self):
        return self.FullName
    
    def age(self):
        import datetime
        return int((datetime.date.today() - self.BrithInfo).days / 365.25)

class CvUpload(models.Model):
    name = models.CharField(default='Md Mahiuddin', max_length=50)
    mycv = models.FileField(upload_to='Cv/')

class Boxes(models.Model):
    Number = models.IntegerField()
    FlineText = models.CharField(max_length=50)
    LlineText = models.CharField(max_length=50)

    def __str__(self):
        return self.FlineText+' '+self.LlineText+' '+ str(self.Number)

class Skills(models.Model): 
    SkillName = models.CharField(max_length=50)
    SkillPercen = models.IntegerField()

    def __str__(self):
        return self.SkillName + ' ' + str(self.SkillPercen) + ' %'

class Expreance(models.Model):
    CompanyName = models.CharField(max_length=50)
    Role = models.CharField(max_length=50)
    Joindate = models.DateField(auto_now=False, auto_now_add=False)
    METADATA_FIELD_TYPE = (
        ('0', 'Present'),
        ('1', 'End date'),
    )
    fieldtype = models.CharField(max_length=1, choices=METADATA_FIELD_TYPE, default=0)
    Present = models.CharField(max_length=50, blank=True, null= True)
    Lastdate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null= True)
    shortDec = models.TextField(max_length=250,default='')

    @property
    def value(self):
        if self.fieldtype == '0':
            return self.Present
        return self.Lastdate
    

    def __str__(self):
        return self.Role

class Education(models.Model):
    schoolName = models.CharField(max_length=150)
    degreeName = models.CharField(max_length=50)
    Joindate = models.DateField(auto_now=False, auto_now_add=False)
    METADATA_FIELD_TYPE = (
        ('0', 'Present'),
        ('1', 'End date'),
    )
    fieldtype = models.CharField(max_length=1, choices=METADATA_FIELD_TYPE, default=0)
    Present = models.CharField(max_length=50, blank=True, null= True)
    Lastdate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null= True)
    shortDec = models.TextField(max_length=250,default='')

    @property
    def value(self):
        if self.fieldtype == '0':
            return self.Present
        return self.Lastdate
    

    def __str__(self):
        return self.schoolName+' '+ self.degreeName



