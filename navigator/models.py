from django.db import models

# Create your models here.

room_types = (('ClassRoom', 'ClassRoom'), ('ComputerLab', 'ComputerLab'), ('ECELab', 'ECELab'), ('Library', 'Library'),
              ('StaffRoom', 'StaffRoom'), ('WorkSpace', 'WorkSpace'), ('AcadamicOffice', 'AcadamicOffice'),
              ('RegistarOffice', 'RegistarOffice'))


class Rooms(models.Model):
    number = models.PositiveIntegerField(null=False)
    floor = models.PositiveIntegerField()
    block = models.PositiveIntegerField(default=1)
    type = models.CharField(choices=room_types, max_length=15)

    def __str__(self):
        return str(self.number)


event_locations = (('Basement', 'Basement'), ('AcadamicBlock', 'AcadamicBlock'), ('BoysHostel-1', 'BoysHostel-1'),
                   ('BoysHostel-2', 'BoysHostel-2'), ('GirlsHostel', 'GirlsHostel'),
                   ('Basketball', 'Basketball'), ('CricketGround', 'CricketGround'),
                   ('Football', 'Football'), ('Canteen', 'Canteen'))


class Events(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    location = models.CharField(choices=event_locations, max_length=20)
    room = models.ForeignKey(Rooms, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Professor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    room = models.ForeignKey(Rooms, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


days_choice = (('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'),
               ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'))


class Classes(models.Model):
    room_no = models.ForeignKey(Rooms, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=30)
    Day = models.CharField(choices=days_choice, max_length=15)
    professor = models.ForeignKey(Professor, null=True, blank=True, on_delete=models.CASCADE)
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return self.subject
