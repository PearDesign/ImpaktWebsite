from django.db import models
from django.utils.text import slugify


class Metric(models.Model):
    positive_image = models.ImageField(
        blank=True, null=True,
        verbose_name='Positive Image',
        help_text='Icon to display when a company scores positively on this metric')
    negative_image = models.ImageField(
        blank=True, null=True,
        verbose_name='Negative Image',
        help_text='Icon to display when a company scores negatively on this metric')
    neutral_image = models.ImageField(
        blank=True, null=True,
        verbose_name='Neutral Image',
        help_text='Icon to display when a company scores neutrally on this metric')
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        help_text='Which metric, if any, this metric should appear nested under in user dropdowns')
    text = models.CharField(max_length=63, db_index=True)

    def __str__(self):
        return self.text


class Company(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    ASIN = models.CharField(
        max_length=127,
        db_index=True, unique=True,
        null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    sustainalytics_id = models.IntegerField(
        null=True, blank=True,
        unique=True)

    slug = models.CharField(max_length=255, db_index=True, editable=False, unique=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Assessment(models.Model):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    data_source = models.CharField(
        max_length=127, db_index=True,
        choices=(
            ('impakt', 'Directly-supplied by Impakt researchers'),
            ('sustainalytics', 'Sustainalytics')
        ),
        help_text='Where the information for this assessment came from',
        verbose_name='Data Source')
    justification = models.TextField(null=True, blank=True)
    link = models.CharField(
        max_length=255,
        blank=True, null=True,
        help_text='Link users to more info about why Impakt gave this assessment')
    metric = models.ForeignKey('companies.Metric', on_delete=models.CASCADE)
    sentiment = models.CharField(
        max_length=63, db_index=True,
        choices=(
            ('positive', 'Positive'),
            ('negative', 'Negative'),
            ('strongly_negative', 'Strongly Negative'),
            ('neutral', 'Neutral'))
        )

    def __str__(self):
        return f"{self.company} {self.metric}"


class Incident(models.Model):
    '''Qualitative assessment for a given metric in response to a specific incident'''
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    text = models.TextField()
