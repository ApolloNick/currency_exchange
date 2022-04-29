from django.db import models


class RateType(models.TextChoices):
    UAH = 'UAH', 'Hrivna'
    USD = 'USD', 'Dollar'
    EUR = 'EUR', 'Euro'
    BTC = 'BTC', 'Bitcoin'


class SourceDigitName(models.IntegerChoices):
    PRIVATBANK = 1, 'PrivatBank'
    MONOBANK = 2, 'MonoBank'
    VKURSE = 3, "Vkurse"
    BINANCE = 4, 'Binance'
