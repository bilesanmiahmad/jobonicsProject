from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    maiden_name = models.CharField(max_length=20, blank='true')
    gender = models.Field(choices=[('M', 'Male'), ('F', 'Female')])
    birth_date = models.DateField()
    user_type = models.Field(choices=[('Admin', 'Administrator'), ('Recruit', 'Recruiter'), ('seeker', 'Job Seeker')])
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    facebook = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)
    linkedIn = models.CharField(max_length=30)
    score = models.IntegerField()
    date_created = models.DateField(auto_now=True)


class Country(models.Model):
    name = models.CharField(max_length=20)
    created_by = models.ForeignKey('auth.User', related_name='countries', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)


class EntitySize(models.Model):
    size_info = models.CharField(max_length=15)
    created_by = models.ForeignKey('auth.User', related_name='entity_sizes', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)


class Entity(models.Model):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=200)
    primary_industry = models.CharField(max_length=50)
    num_of_employees = models.IntegerField()
    about_company = models.TextField()
    facebook = models.CharField(max_length=50)
    linkedIn = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    date_established = models.DateField()
    organisation_type = models.CharField(max_length=20)
    tags = models.CharField(max_length=200)
    entity_admin = models.ForeignKey(User)
    location = models.CharField(max_length=30)
    company_size = models.ForeignKey(EntitySize)
    country = models.ForeignKey(Country)
    company = models.ForeignKey('self', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)


class Industry(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='industries', on_delete=models.CASCADE)


class Profession(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='professions', on_delete=models.CASCADE)


class JobType(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='job_types', on_delete=models.CASCADE)


class JobStatus(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='statuses', on_delete=models.CASCADE)


class Job(models.Model):
    title = models.CharField(max_length=40)
    summary = models.TextField()
    description = models.TextField()
    entity = models.ForeignKey(Entity)
    industry = models.ForeignKey(Industry)
    creator = models.ForeignKey(User)
    job_type = models.ForeignKey(JobType)
    profession = models.ForeignKey(Profession)
    min_qualification = models.CharField(max_length=100)
    min_experience = models.CharField(max_length=100)
    deadline_date = models.DateField()
    score = models.IntegerField()
    tags = models.CharField(max_length=100)
    date_created = models.DateField(auto_now=True)
    job_status = models.ForeignKey(JobStatus)


class ApplicationStage(models.Model):
    status = models.CharField(max_length=20)
    rank = models.IntegerField()
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='app_stages', on_delete=models.CASCADE)


class Applications(models.Model):
    applicant = models.ForeignKey(User)
    job = models.ForeignKey(Job)
    status = models.ForeignKey(ApplicationStage)
    match = models.IntegerField()
    date_created = models.DateField(auto_now=True)


class Schedule(models.Model):
    application = models.ForeignKey(Applications)
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    date_created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User)
