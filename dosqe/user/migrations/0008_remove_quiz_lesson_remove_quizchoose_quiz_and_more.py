# Generated by Django 5.0.1 on 2024-01-09 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_quizfillempty_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='quizchoose',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='quizfillempty',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='quizvoice',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='quizchooseanser',
            name='quiz_choose',
        ),
        migrations.RemoveField(
            model_name='quizchooseoption',
            name='quiz_choose',
        ),
        migrations.RemoveField(
            model_name='quizchooseanser',
            name='served',
        ),
        migrations.RemoveField(
            model_name='quizfillemptyoptionanser',
            name='quiz_fill_empty',
        ),
        migrations.RemoveField(
            model_name='quizfillemptyoption',
            name='quiz_fill_empty',
        ),
        migrations.RemoveField(
            model_name='quizfillemptyoptionanser',
            name='served',
        ),
        migrations.RemoveField(
            model_name='quizvoiceanser',
            name='quiz_voice',
        ),
        migrations.RemoveField(
            model_name='quizvoiceanser',
            name='served',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='school',
        ),
        migrations.RemoveField(
            model_name='servant',
            name='school',
        ),
        migrations.RemoveField(
            model_name='served',
            name='school',
        ),
        migrations.RemoveField(
            model_name='servant',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='served',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='servedpresence',
            name='served',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subj',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='QuizChoose',
        ),
        migrations.DeleteModel(
            name='QuizChooseOption',
        ),
        migrations.DeleteModel(
            name='QuizChooseAnser',
        ),
        migrations.DeleteModel(
            name='QuizFillEmpty',
        ),
        migrations.DeleteModel(
            name='QuizFillEmptyOption',
        ),
        migrations.DeleteModel(
            name='QuizFillEmptyOptionAnser',
        ),
        migrations.DeleteModel(
            name='QuizVoice',
        ),
        migrations.DeleteModel(
            name='QuizVoiceAnser',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Servant',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Served',
        ),
        migrations.DeleteModel(
            name='ServedPresence',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
