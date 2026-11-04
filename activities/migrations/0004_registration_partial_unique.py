from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("activities", "0003_activity_responsible")]
    operations = [
        migrations.RemoveConstraint(model_name="registration", name="one_registration_per_student_activity"),
        migrations.AddConstraint(
            model_name="registration",
            constraint=models.UniqueConstraint(
                condition=models.Q(("cancelled_at__isnull", True)),
                fields=("student", "activity"),
                name="one_registration_per_student_activity",
            ),
        ),
    ]
