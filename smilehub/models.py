from django.db import models

# Create your models here.

class Donor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Donor"
        verbose_name_plural = "Donor_list"

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Donation(models.Model):
    PAYMENT_METHODS = [
        ('bank_transfer', 'Bank Transfer'),
        ('credit_card', 'Credit Card'),
        ('cash', 'Cash'),
    ]
    FREQUENCIES = [
        ('one_time', 'One-Time'),
        ('monthly', 'Monthly'),
        ('annually', 'Annually'),
    ]
    STATUSES = [
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    ]

    donation_id = models.AutoField(primary_key=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True, blank=True)
    donation_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100, unique=True)
    is_recurring = models.BooleanField(default=False)
    frequency = models.CharField(max_length=20, choices=FREQUENCIES, default='one_time')
    status = models.CharField(max_length=20, choices=STATUSES, default='completed')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Donation {self.donation_id} by {self.donor.name}"

