# Generated by Django 5.0.6 on 2024-10-27 23:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Campaign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("goal_amount", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Donor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                (
                    "contact_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
            ],
            options={
                "verbose_name": "Donor",
                "verbose_name_plural": "Donor_list",
            },
        ),
        migrations.CreateModel(
            name="Donation",
            fields=[
                ("donation_id", models.AutoField(primary_key=True, serialize=False)),
                ("donation_date", models.DateTimeField(auto_now_add=True)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("bank_transfer", "Bank Transfer"),
                            ("credit_card", "Credit Card"),
                            ("cash", "Cash"),
                        ],
                        max_length=20,
                    ),
                ),
                ("transaction_id", models.CharField(max_length=100, unique=True)),
                ("is_recurring", models.BooleanField(default=False)),
                (
                    "frequency",
                    models.CharField(
                        choices=[
                            ("one_time", "One-Time"),
                            ("monthly", "Monthly"),
                            ("annually", "Annually"),
                        ],
                        default="one_time",
                        max_length=20,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("completed", "Completed"),
                            ("pending", "Pending"),
                            ("failed", "Failed"),
                        ],
                        default="completed",
                        max_length=20,
                    ),
                ),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "campaign",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="smilehub.campaign",
                    ),
                ),
                (
                    "donor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="smilehub.donor"
                    ),
                ),
            ],
        ),
    ]
