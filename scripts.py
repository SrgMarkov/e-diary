import os
import random
import django
from datacenter.models import Schoolkid, Chastisement, Mark, Lesson, Commendation


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


def fix_marks(schoolkid):
    child = Schoolkid.objects.get(full_name__contains=schoolkid)
    while Mark.objects.filter(schoolkid=child, points__lt=4).count() != 0:
        marks = Mark.objects.filter(schoolkid=child, points__lt=4).first()
        marks.points = 5
        marks.save()


def remove_chastisements(schoolkid):
    child = Schoolkid.objects.get(full_name__contains=schoolkid)
    chastisement = Chastisement.objects.filter(schoolkid=child)
    chastisement.delete()


def create_commendation(schoolkid, lesson):
    praise = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 
              'Ты меня приятно удивил!', 'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 
              'Именно этого я давно ждал от тебя!', 'Сказано здорово – просто и ясно!', 
              'Ты, как всегда, точен!', 'Очень хороший ответ!', 'Талантливо!', 
              'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!', 
              'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!', 
              'Ты на верном пути!', 'Здорово!', 'Это как раз то, что нужно!', 'Я тобой горжусь!', 
              'С каждым разом у тебя получается всё лучше!', 'Мы с тобой не зря поработали!', 
              'Я вижу, как ты стараешься!', 'Ты растешь над собой!', 'Ты многое сделал, я это вижу!', 
              'Теперь у тебя точно все получится!']
    praised_lesson = Lesson.objects.filter(group_letter='А', year_of_study=6, subject__title=lesson)\
                    .order_by('-date').first()
    child = Schoolkid.objects.get(full_name__contains=schoolkid)
    Commendation.objects.create(text=random.choice(praise), created=praised_lesson.date, schoolkid=child, 
                                subject=praised_lesson.subject, teacher=praised_lesson.teacher)

fix_marks('Голубев Феофан')
