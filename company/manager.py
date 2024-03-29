from django.db import models
from .queryset import CompanyQuerySet

class CompanyManager(models.Manager):
    
    def get_queryset(self):
        return CompanyQuerySet(model=self.model, using=self._db, hints=self._hints)
    
    def list_companies(self, active: bool):
        return self.get_queryset().list_companies(active)
