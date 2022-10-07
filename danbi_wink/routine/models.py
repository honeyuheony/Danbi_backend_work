from django.db import models
from account.models import user

# Create your models here.
class routine(models.model):
    routine_type = models.TextChoices('MIRACLE', 'HOMEWORK')

    routine_id = models.AutoField(unique=True, primary_key=True)
    account_id = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField()
    category = models.CharField(choices=routine_type.choices)
    goal = models.CharField()
    is_alarm = models.BooleanField()
    is_deleted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.account_id} {self.goal} {self.title}"

class routine_result(models.model):
    result_type = models.TextChoices('NOT', 'TRY', 'DONE')

    routine_result_id = models.AutoField(unique=True, primary_key=True)
    routine_id = models.ForeignKey(routine, on_delete=models.CASCADE)
    result = models.CharField(choices=result_type.choices)
    is_deleted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.routine_id} {self.result}"

class routine_day(models.model):
    day = models.JSONField()
    routine_id = models.ForeignKey(routine, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.routine_id} {self.day}"