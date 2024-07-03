from django.db import models
from base.models import BaseModel


class Chantier(BaseModel):
    nom = models.CharField(max_length=100)
    localisation = models.CharField(max_length=200)  # Champ pour la localisation
    date_debut = models.DateField()                  # Champ pour la date de début
    date_fin = models.DateField(blank=True, null=True)  # Champ pour la date de fin (optionnel)

    def __str__(self):
        return self.nom

    def __str__(self):
        return self.nom

class Materiel(BaseModel):
    DESCRIPTION_CHOICES = [
        ('SAPIN BLANC 3m', 'SAPIN BLANC 3m'),
        ('SAPIN BLANC 4m', 'SAPIN BLANC 4m'),
        ('DOUKA 2.90 POUTRE H20', 'DOUKA 2.90 POUTRE H20'),
        ('DOUKA 3.90 POUTRE H20', 'DOUKA 3.90 POUTRE H20'),
        ('KAUFMANN 80 X 2900', 'KAUFMANN 80 X 2900'),
        ('KAUFMANN 80 X 3900', 'KAUFMANN 80 X 3900'),
        ('ECHAFFAUDAGE 1m', 'ECHAFFAUDAGE 1m'),
        ('ECHAFFAUDAGE 70cm', 'ECHAFFAUDAGE 70cm'),
    ]
    description = models.CharField(max_length=100, choices=DESCRIPTION_CHOICES)
    quantite = models.PositiveIntegerField()
    unite_mesure = models.CharField(max_length=20)  # Ex: "pièce", "mètre", "litre"
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2)
    num_bon_commande = models.CharField(max_length=50, blank=True, null=True)
    num_bon_livraison = models.CharField(max_length=50, blank=True, null=True)
    fournisseur = models.CharField(max_length=100)
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)  # Ajout d'un champ pour les notes

    def __str__(self):
        return f"{self.description} - {self.quantite} {self.unite_mesure}"
