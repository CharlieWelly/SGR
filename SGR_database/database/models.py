from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

"""
Database design following this topic:
https://dba.stackexchange.com/questions/83951/financial-database-design
"""


class User(AbstractUser):
    pass


class Industry(models.Model):
    industry_level1 = models.CharField(max_length=100)
    industry_level2 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.industry_level1} - {self.industry_level2}"


class Company(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    industry = models.ForeignKey(
        Industry, on_delete=models.CASCADE, related_name="companies"
    )

    def __str__(self):
        return f"{self.code}"


class Statement(models.Model):
    statement_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.statement_name}"


class StatementRow(models.Model):
    statement = models.ForeignKey(
        Statement, on_delete=models.CASCADE, related_name="rows"
    )
    title = models.CharField(max_length=100)
    row_order = models.IntegerField()
    row_description = models.CharField(max_length=100, null=True, blank=True)
    row_properties = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.row_order}: {self.statement} - {self.title}"


class StatementFact(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="statements"
    )
    statement_row = models.ForeignKey(
        StatementRow, on_delete=models.CASCADE, related_name="companies"
    )
    date = models.DateField()
    Value = models.FloatField()

    def __str__(self):
        return f"{self.company}| {self.statement_row}| {self.date}| {self.value}"
