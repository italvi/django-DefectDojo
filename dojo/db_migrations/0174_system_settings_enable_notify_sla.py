# Generated by Django 3.2.16 on 2022-11-19 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0173_alter_risk_acceptance_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='system_settings',
            name='enable_notify_sla_active',
            field=models.BooleanField(default=False, help_text="Enables Notify when time to remediate according to Finding SLA's is breached for active Findings.", verbose_name="Enable Notifiy SLA's Breach for active Findings"),
        ),
        migrations.AddField(
            model_name='system_settings',
            name='enable_notify_sla_active_verified',
            field=models.BooleanField(default=False, help_text="Enables Notify when time to remediate according to Finding SLA's is breached for active, verified Findings.", verbose_name="Enable Notifiy SLA's Breach for active, verified Findings"),
        ),
    ]
