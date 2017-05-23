from django.db import models


class Pet(models.Model):
    pet_name = models.CharField(max_length=200)
    when_born = models.DateTimeField('when was pet born')

    def __str__(self):
        return self.pet_name


class Choice(models.Model):
    person = models.ForeignKey(Pet, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.person