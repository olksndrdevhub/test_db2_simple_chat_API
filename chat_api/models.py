from django.db import models

# Create your models here.



class Message(models.Model):
    """
    Define model that describe message instances
    """

    text = models.CharField(verbose_name='Text', max_length=100)
    author_email = models.EmailField(verbose_name='Author Email')
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=True)

    def __str__(self):
        return self.author_email + ' ' + str(self.created)

    class Meta:
        ordering = ['created']