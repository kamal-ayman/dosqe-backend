from django.db import models


class School(models.Model):
    name = models.CharField(null=False, max_length=50)
    level = models.IntegerField(null=False)
    def __str__(self):
        return self.name + " " + str(self.level)
    

class User(models.Model):
    name = models.CharField(null=False, max_length=50)
    email = models.CharField(null=False, max_length=30)
    phone = models.CharField(null=False, max_length=11)
    username = models.CharField(null=False, max_length=50)
    password = models.CharField(null=False, max_length=50)
    date_of_birth = models.DateField(auto_now=True)

class Servant(User):
    school = models.ManyToManyField(School)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)

class Served(User):
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING)

class ServedPresence(models.Model):
    served = models.ForeignKey(Served, on_delete=models.DO_NOTHING)
    is_presence = models.BooleanField()
    date = models.DateTimeField(auto_now=True)

class Subject(models.Model):
    subj = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(null=False, max_length=50)
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING) 
    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    name = models.CharField(null=False, max_length=50)
    video_link = models.CharField(null=True, max_length=100)

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING)
    img_link = models.CharField(null=True, max_length=50)
    question = models.TextField(null=True)
    question_type = models.CharField(null=True, max_length=20)

# QuizFillEmpty
class QuizFillEmpty(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    class Meta:
        pass
        # verbose_name = 'quiz_fill_empty'
        # db_table = 'quiz_fill_empty'

class QuizFillEmptyOption(models.Model):
    word = models.CharField(max_length=50)
    t_index = models.IntegerField()
    f_index = models.IntegerField()
    quiz_fill_empty = models.ForeignKey(QuizFillEmpty, on_delete=models.DO_NOTHING)

class QuizFillEmptyOptionAnser(models.Model):
    word = models.CharField(max_length=50)
    index = models.IntegerField()
    quiz_fill_empty = models.ForeignKey(QuizFillEmpty, on_delete=models.DO_NOTHING)
    served = models.ForeignKey(Served, on_delete=models.DO_NOTHING)
    date_anser = models.DateTimeField(auto_now=True)

# Quiz Choose
class QuizChoose(models.Model):
    anser_index = models.IntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)

class QuizChooseOption(models.Model):
    text = models.CharField(max_length=150)
    index = models.IntegerField()
    quiz_choose = models.ForeignKey(QuizChoose, on_delete=models.DO_NOTHING)

class QuizChooseAnser(models.Model):
    served = models.ForeignKey(Served, on_delete=models.DO_NOTHING)
    index = models.IntegerField()
    quiz_choose = models.ForeignKey(QuizChoose, on_delete=models.DO_NOTHING)
    date_anser = models.DateTimeField(auto_now=True)

# Quiz Voice
class QuizVoice(models.Model):
    text = models.CharField(max_length=150)
    voice_link = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)

class QuizVoiceAnser(models.Model):
    quiz_voice = models.ForeignKey(QuizVoice, on_delete=models.DO_NOTHING)
    served = models.ForeignKey(Served, on_delete=models.DO_NOTHING)
    date_anser = models.DateTimeField(auto_now=True)
    is_right_anser = models.BooleanField(null=True, default=None)
    voice_link = models.CharField(max_length=200)
