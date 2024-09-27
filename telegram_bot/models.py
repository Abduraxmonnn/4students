from django.db import models


class TGUser(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Telegram User'
        verbose_name_plural = 'Telegram Users'

    def __str__(self):
        return self.username

    def get_user_id(self):
        return self.user_id

    def get_username(self):
        return self.username
