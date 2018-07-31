from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from instagram.users import models as user_models
from instagram.images import models as image_models
# Create your models here.
class Notification(image_models.TimeStampedModel):
    TYPE_CHOICES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow')
    )
    creator = models.ForeignKey(user_models.User, related_name="creator", on_delete=models.CASCADE)
    to = models.ForeignKey(user_models.User, related_name="to", on_delete=models.CASCADE)

    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ForeignKey(image_models.Image, on_delete=models.CASCADE, null=True, blank=True)
