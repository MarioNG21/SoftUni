from django.db import models


class AuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    update_on = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class Department(AuditEntity):
    name = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    GOOGLE = 'Google'
    SOFT_UNI = 'Soft Uni'

    first_name = models.CharField(
        max_length=20
    )

    age = models.IntegerField(

    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    egn = models.CharField(
        max_length=12,
        unique=True
    )

    job_title = models.CharField(
        max_length=20,
        default='No Choice',
        choices=(
            ('1', 'Software Developer'),
            ('2', 'QA Engineer'),
            ('3', 'DevOps Specialist')
        )
    )

    company = models.CharField(
        max_length=max(len(c) for c in [GOOGLE, SOFT_UNI]),
        choices=(
            (GOOGLE, GOOGLE),
            (SOFT_UNI, SOFT_UNI)
        )
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name if self.last_name else ''}"

    class Meta:
        ordering = ('first_name',)


class Project(models.Model):
    name = models.CharField(
        max_length=30,

    )

    dead_line = models.DateField(
        null=True,
        blank=True,
    )

    employees = models.ManyToManyField(
        to=Employee,
    )


class User(models.Model):
    email = models.EmailField(

    )

    employee = models.OneToOneField(
        to=Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )
