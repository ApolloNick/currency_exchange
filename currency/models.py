from django.db import models
from currency import model_choices


class Source(models.Model):
    name = models.CharField(max_length=64, unique=True)
    code_name = models.PositiveSmallIntegerField(choices=model_choices.SourceDigitName.choices,
                                                 unique=True)

    def __str__(self):
        return self.name


class CurrencyRate(models.Model):
    convert_from = models.CharField(choices=model_choices.RateType.choices,
                                    default=model_choices.RateType.USD)
    convert_to = models.CharField(choices=model_choices.RateType.choices,
                                  default=model_choices.RateType.UAH)
    register_date = models.DateTimeField(auto_now_add=True)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sell = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='sources')
