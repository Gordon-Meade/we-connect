from django_summernote.fields import SummernoteTextField
from django.db import models

# RATING = ((1, "Highly Dissatisfied"), (2, "Dissatisfied"),(3,"Neutral"),(4,"Satisfied")(5,"Highly Satisfied"))

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    max_participation = models.PositiveIntegerField(blank=True, null=True)
    event_type = models.CharField(max_length=50, blank=True, null=True)

    

    # review = models.TextField(blank=True, null=True)
    # rating = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
       ordering = ["-date"]


    def __str__(self):
        return self.title


# class Review(models.Model):
#     title = models.ForeignKey(
#         Event, on_delete=models.CASCADE, related_name="event-title")
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="user_name")
#     reviewbody = models.TextField()
#     rating = models.IntegerField(choices=RATING, default=5)
#     approved = models.BooleanField(default=False)
#     created_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ["-rating"]

#     def __str__(self):
#         return f"Review {self.reviewbody} by {self.user}"