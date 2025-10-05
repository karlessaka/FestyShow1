from django.db import models


# Create your models here.


class Artist(models.Model):
    style_choices = [
            ("ROCK", "Rock"),
            ("JAZZ", "Jazz"),
            ("POP", "Pop"),
            ("RAP", "Rap"),
        ]
    bio = models.TextField(max_length=500)
    link = models.URLField(max_length=200)
    Full_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    style = models.CharField(max_length=10, choices=style_choices, default="ROCK")

    def __str__(self):
        return self.Full_name
    

class Concert(models.Model):
    title = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    seats_available = models.IntegerField(default=150)

    def __str__(self):
        return f"{self.artist.Full_name} - {self.date_time} at {self.location}"
    

class Booking(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    code_booking = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Booking for {self.user_name} - {self.concert.title} at {self.concert.location} enjoy!"
    

class Administrator(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)  

    def __str__(self):
        return self.username


    

