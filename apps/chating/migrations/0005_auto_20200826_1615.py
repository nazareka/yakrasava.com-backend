# Generated by Django 3.0.5 on 2020-08-26 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chating', '0004_auto_20200826_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupchatmessage',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='privatechatmessage',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='savedmessagesmessage',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterField(
            model_name='groupchatmessage',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='chating.GroupChat'),
        ),
        migrations.AlterField(
            model_name='privatechatmessage',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='chating.PrivateChat'),
        ),
        migrations.AlterField(
            model_name='savedmessagesmessage',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='chating.SavedMessagesChat'),
        ),
    ]
