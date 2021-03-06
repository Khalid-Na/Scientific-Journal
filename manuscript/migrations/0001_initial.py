# Generated by Django 3.2.8 on 2021-11-10 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categ_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('keyword', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Manu_keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscript.keywords')),
            ],
        ),
        migrations.CreateModel(
            name='Manuscript',
            fields=[
                ('manuscript_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Title', models.TextField(max_length=100)),
                ('Manu_abstract', models.TextField(max_length=500)),
                ('manuscript_category', models.TextField(max_length=200)),
                ('file', models.FileField(upload_to='manuscript/FILES/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.author')),
                ('keyword', models.ManyToManyField(through='manuscript.Manu_keyword', to='manuscript.Keywords')),
                ('reviewers', models.ManyToManyField(blank=True, to='accounts.Reviewer')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('manuscript_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='manuscript.manuscript')),
                ('article_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('keywords', models.TextField()),
            ],
            bases=('manuscript.manuscript',),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('remarks', models.TextField()),
                ('manuscript_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscript.manuscript')),
                ('reviewer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.reviewer')),
            ],
        ),
        migrations.CreateModel(
            name='Manuscript_Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('manuscript_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscript.manuscript')),
            ],
        ),
        migrations.AddField(
            model_name='manu_keyword',
            name='manuscript',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscript.manuscript'),
        ),
    ]
