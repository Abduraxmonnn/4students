from django.db import models

from telegram_bot.models import TGUser


def content_file_name(instance, filename):
    return '/'.join(['answers', instance.subject.faculty.direction, instance.subject.faculty.short_name,
                     f'SEMESTER_{instance.semester}', filename])


class Faculty(models.Model):
    ENGINEERING = 'ENGINEERING'
    BUSINESS_FINANCE = 'BUSINESS_FINANCE'
    EDUCATION = 'EDUCATION'
    ARTS = 'ARTS'
    MEDICINES = 'MEDICINES'

    DIRECTIONS = (
        (ENGINEERING, 'SCHOOL OF ENGINEERING'),
        (BUSINESS_FINANCE, 'SCHOOL OF BUSINESS FINANCE'),
        (EDUCATION, 'SCHOOL OF EDUCATION'),
        (ARTS, 'SCHOOL OF ARTS'),
        (MEDICINES, 'SCHOOL OF MEDICINES'),
    )

    direction = models.CharField(max_length=16, choices=DIRECTIONS)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=5)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'
        unique_together = ('name', 'short_name')

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name.upper()

    def get_short_name(self):
        return self.short_name.upper()


class Subject(models.Model):
    name = models.CharField(max_length=150)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.name

    def get_faculty(self):
        return self.faculty

    def get_name(self):
        return self.name


class Answer(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to=content_file_name)
    file_name = models.CharField(max_length=100)
    file_type = models.CharField(max_length=100)
    by = models.ForeignKey(TGUser, on_delete=models.SET_NULL, null=True)
    is_anonymous = models.BooleanField(default=False)

    year = models.IntegerField(null=True, blank=True)
    semester = models.IntegerField()

    pages = models.IntegerField(null=True, blank=True)
    answers = models.IntegerField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Answer File'
        verbose_name_plural = 'Answer Files'
        unique_together = ('file_name', 'file_type', 'by', 'semester')

    def __str__(self):
        return self.file_name

    def get_file_name(self):
        return self.file_name

    def get_by_user_id(self):
        return self.by.user_id


class FeedBack(models.Model):
    subject = models.CharField(max_length=150)
    message = models.TextField()
    owner = models.ForeignKey(TGUser, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return f'{self.subject}: {self.owner}'
