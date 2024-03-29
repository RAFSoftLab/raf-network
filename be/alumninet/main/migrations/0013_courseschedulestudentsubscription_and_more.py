# Generated by Django 4.2.1 on 2024-01-10 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_course_studentuser_coursescheduleentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseScheduleStudentSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_schedule_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.coursescheduleentry')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.studentuser')),
            ],
        ),
        migrations.AddField(
            model_name='coursescheduleentry',
            name='subscribed_students',
            field=models.ManyToManyField(blank=True, related_name='subscribed_courses', through='main.CourseScheduleStudentSubscription', to='main.studentuser'),
        ),
    ]
