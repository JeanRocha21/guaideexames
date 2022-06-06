from django.db import models


tempodejejum = (
    ('4HORAS', '4 Horas'),
    ('6HORAS', '6 Horas'),
    ('8HORAS', '8 Horas'),
    ('12HORAS', '12 Horas'),
    ('NÃO_NECESSARIO', 'Não é necessário'),
)

tiposdeamostras = (
    ('SORO', 'Soro'),
    ('EDTA', 'Sangue Total'),
    ('EDTAPLASMA', 'Plasma EDTA'),
    ('CITRATO', 'Plasma Citrato'),
    ('HEPARINA', 'Heparina'),
    ('TRACE', 'Tubo Trace'),
)

class Exame(models.Model):

    Nome = models.CharField(max_length=100)
    Jejum = models.CharField(max_length=25, choices=tempodejejum)
    Material = models.CharField(max_length=25, choices=tiposdeamostras)
    Prazo = models.CharField(max_length=15)
    Ativo = models.BooleanField(default=True)

    class Meta:
            verbose_name = 'Exame'
            verbose_name_plural = 'Exames'

    def __str__(self):
        return self.Nome

