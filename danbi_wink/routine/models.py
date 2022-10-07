from django.db import models
from account.models import User

# Create your models here.
class Routine(models.Model):
    routine_type = (('MIRACLE', 'MIRACLE'), ('HOMEWORK', 'HOMEWORK'))

    routine_id = models.AutoField(unique=True, primary_key=True)
    # account_id = models.ForeignKey(user, on_delete=models.CASCADE)
    account_id = models.CharField(max_length = 20)
    title = models.CharField(max_length = 50)
    category = models.CharField(choices=routine_type, max_length = 10)
    goal = models.CharField(max_length = 200)
    is_alarm = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.account_id}_{self.goal}_{self.title}"

class Routine_result(models.Model):
    result_type = (('NOT', 'NOT'), ('TRY', 'TRY'), ('DONE', 'DONE'))

    routine_result_id = models.AutoField(unique=True, primary_key=True)
    routine_id = models.ForeignKey(Routine, on_delete=models.CASCADE)
    result = models.CharField(choices=result_type, max_length=10, default="NOT")
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.routine_id}_{self.result}"

class Routine_day(models.Model):
    day = models.JSONField()
    routine_id = models.ForeignKey(Routine, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.routine_id}_{self.day}"