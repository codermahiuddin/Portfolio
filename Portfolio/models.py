from django.db import models

# Create your models here.
class Portfolio(models.Model):
    ProjectName = models.CharField(max_length=50)
    ProjectTitle = models.CharField(max_length=150)
    ClinentName = models.CharField(max_length=50)
    LanguageUse = models.CharField(max_length=250)
    ProjectUrl = models.CharField(max_length=250)
    METADATA_FIELD = (
        ('0', 'Image'),
        ('1', 'Slider Image'),
        ('2', 'Online Video'),
        ('3', 'Local Video'),
    )
    UploadOption = models.CharField(max_length=1, choices=METADATA_FIELD, default=0)
    ProjectImage = models.ImageField(upload_to='portfolio/')
    LocalVideo = models.FileField(upload_to='portfolio/video/',blank=True)
    OnlineVieoUrl = models.URLField(max_length=250,blank=True)
    
    def __str__(self):
        return self.ProjectTitle+' -> '+ self.ProjectName

class MultipleImageUpload(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.portfolio.ProjectTitle+' -> '+ self.portfolio.ProjectName

