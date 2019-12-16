from django.db import models

# Create your models here.
class Rating(models.Model):
    user_id = models.CharField(max_length=16)
    content_id = models.CharField(max_length=16)
    rating = models.DecimalField(decimal_places=2, max_digits=4)
    rating_timestamp = models.DateTimeField()
    type = models.CharField(max_length=8,default='explicit')

    def __str__(self):
        return "user_id: {}, movie_id: {}, rating: {}, type: {}"\
            .format(self.user_id, self.content_id, self.rating, self.type)
