from django.db import models


class Categoria(models.Model):
    nome = models.CharField("Nome", max_length=100, blank=False)
    ativa = models.BooleanField("ativa", default=True)

    def __str__(self):
        return self.nome


class Conta(models.Model):
    descricao = models.CharField("Descrição", max_length=100, blank=False)
    categoria = models.ForeignKey(Categoria, verbose_name="Categoria", blank=False)
    valor = models.DecimalField("Valor", max_digits=9, decimal_places=2, blank=False)
    vencimento = models.DateField("Vencimento", blank=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_valid = None

    def __str__(self):
        return self.descricao