from django.db import models

# Create your models here.

from django.db import models
from django.utils.text import slugify

from assessment_management.models import Assesment

class Question(models.Model):

    assessment = models.ForeignKey(
        Assesment,
        on_delete=models.CASCADE,
        related_name="question"
    )

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    description = models.TextField(blank=True)

    order = models.PositiveIntegerField(
       
        help_text="question within the assessment",
        null= True
    )

   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

# we take the question of whichever assesment is passed and take its last order and updates it by 1 to get the corct order        
        question_instance = Question.objects.filter(assessment=self.assessment).last()

        if question_instance:

            self.order = question_instance.order + 1
        else:
            self.order = 1

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.assessment.title} - {self.title}"

    class Meta:
        ordering = ["order"]
        unique_together = ["assessment", "order"]