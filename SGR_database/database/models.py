from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

"""
Database design following this topic:
https://dba.stackexchange.com/questions/83951/financial-database-design
"""


class User(AbstractUser):
    pass


class IndustryLevel1(models.Model):
    industry_level_1 = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.industry_level_1}"


class Industry(models.Model):
    industry_level_1 = models.ForeignKey(
        IndustryLevel1, on_delete=models.CASCADE, related_name="sub_industries"
    )
    industry_level_2 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.industry_level_1} - {self.industry_level_2}"


class StockExchange(models.Model):
    stock_exchange = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.stock_exchange}"


class Company(models.Model):
    code_vs = models.CharField(max_length=20, null=True)
    code_fiin = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=100)
    industry = models.ForeignKey(
        Industry,
        on_delete=models.SET_NULL,
        null=True,
        related_name="companies",
    )
    exchange = models.ForeignKey(
        StockExchange, on_delete=models.SET_NULL, related_name="companies", null=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["code_vs", "name"], name="unique_company")
        ]

    def __str__(self):
        return f"{self.code_vs}"


class Statement(models.Model):
    class Categories(models.TextChoices):
        DN = "DN", "Doanh nghiệp - Ngân hàng"
        CK = "CK", "Chứng Khoán"
        QLQ = "QLQ", "Quản lý quỹ"
        TC = "TC", "Công ty tài chính"

    statement_category = models.CharField(
        max_length=3, choices=Categories.choices, default=Categories.DN
    )
    statement_name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["statement_category", "statement_name"],
                name="unique_statement",
            )
        ]

    def __str__(self):
        return f"{self.statement_category} - {self.statement_name}"


class StatementRow(models.Model):
    statement = models.ForeignKey(
        Statement, on_delete=models.CASCADE, related_name="rows"
    )
    title = models.CharField(max_length=100)
    row_order = models.IntegerField()
    row_description = models.CharField(max_length=100, null=True, blank=True)
    row_properties = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["statement", "row_order"], name="unique_row"
            )
        ]

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
