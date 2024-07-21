# Generated by Django 5.0.7 on 2024-07-21 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255, verbose_name='Muallif')),
                ('title', models.CharField(max_length=255, verbose_name='Kitob nomi')),
                ('publisher', models.CharField(max_length=255, verbose_name='Nashriyot')),
                ('year', models.IntegerField(verbose_name='Nashr yili')),
                ('pages', models.IntegerField(verbose_name='Sahifalar soni')),
                ('price', models.IntegerField(verbose_name='Narxi')),
                ('quantity', models.IntegerField(verbose_name='Jami kitoblar')),
                ('qr_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='QR-kod')),
                ('link_to_book', models.CharField(blank=True, max_length=255, null=True, verbose_name='Kitob havolasi')),
            ],
            options={
                'verbose_name': 'Kitob',
                'verbose_name_plural': 'Kitoblar',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hemis_id', models.BigIntegerField(unique=True, verbose_name='HEMIS ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Tuliq ismi')),
                ('citizenship', models.CharField(max_length=255, verbose_name='Fuqaroligi')),
                ('country', models.CharField(max_length=255, verbose_name='Mamlakati')),
                ('nationality', models.CharField(max_length=255, verbose_name='Millati')),
                ('region', models.CharField(max_length=255, verbose_name='Viloyati')),
                ('district', models.CharField(max_length=255, verbose_name='Tumani')),
                ('gender', models.CharField(max_length=255, verbose_name='Jinsi')),
                ('dob', models.DateField(verbose_name="Tug'ilgan sanasi")),
                ('passport', models.CharField(max_length=255, verbose_name='Pasport seriyasi')),
                ('JSHSHIR', models.CharField(max_length=255, verbose_name='JSHSHIR')),
                ('passport_given_date', models.DateField(verbose_name='Pasport berilgan sana')),
                ('course', models.CharField(choices=[('1-kurs', '1-kurs'), ('2-kurs', '2-kurs'), ('3-kurs', '3-kurs'), ('4-kurs', '4-kurs'), ('5-kurs', '5-kurs')], max_length=255, verbose_name='Kursi')),
                ('faculty', models.CharField(blank=True, max_length=255, null=True, verbose_name='Fakulteti')),
                ('group', models.CharField(max_length=255, verbose_name='Guruh')),
                ('academic_year', models.CharField(max_length=255, verbose_name="O'quv yili")),
                ('semester', models.CharField(max_length=255, verbose_name='Semestr')),
                ('is_graduated', models.BooleanField(verbose_name='Bitirganmi')),
                ('speciality', models.CharField(max_length=255, verbose_name="Yo'nalishi")),
                ('type_of_education', models.CharField(max_length=255, verbose_name="Ta'lim turi")),
                ('form_of_education', models.CharField(max_length=255, verbose_name="Ta'lim shakli")),
                ('payment_form', models.CharField(max_length=255, verbose_name="To'lov shakli")),
                ('previous_education', models.CharField(max_length=255, verbose_name="Oldingi ta'lim")),
                ('student_category', models.CharField(max_length=255, verbose_name='Talaba kategoriyasi')),
                ('social_category', models.CharField(max_length=255, verbose_name='Ijtimoiy kategoriyasi')),
                ('command', models.CharField(max_length=255, verbose_name='Buyruq')),
                ('registration_date', models.DateField(blank=True, null=True, verbose_name="Ro'yxatga olingan sana")),
            ],
            options={
                'verbose_name': 'Talaba',
                'verbose_name_plural': 'Talabalar',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='IssueBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_date', models.DateField(auto_now_add=True, verbose_name='Berilgan kuni')),
                ('returned_date', models.DateField(blank=True, null=True, verbose_name='Qaytish sansi')),
                ('quantity', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.book', verbose_name='Kitob')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student', verbose_name='Talaba')),
            ],
            options={
                'verbose_name': 'Berilgan kitob',
                'verbose_name_plural': 'Berilgan kitoblar',
                'ordering': ['student'],
            },
        ),
    ]
