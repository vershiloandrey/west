from django.db import models

# Create your models here.

class Import(models.Model):
    i = models.CharField(max_length=50)

    def __str__(self):
        return self.i


class Color(models.Model):
    c = models.CharField(max_length=20)

    def __str__(self):
        return self.c


class NoteHHD(models.Model):
    type = models.CharField(max_length=5)

    def __str__(self):
        return self.type


class NoteOS(models.Model):
    os = models.CharField(max_length=50)

    def __str__(self):
        return self.os


class NoteEkran(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class NoteType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Material(models.Model):
    material = models.CharField(max_length=20)

    def __str__(self):
        return self.material


class NoteRazr(models.Model):
    razr = models.CharField(max_length=20)

    def __str__(self):
        return self.razr


class NoteDiag(models.Model):
    diag = models.CharField(max_length=20)

    def __str__(self):
        return self.diag


class NoteProizv(models.Model):
    pr = models.CharField(max_length=20)

    def __str__(self):
        return self.pr


class NoteProcessor(models.Model):
    pr = models.CharField(max_length=20)

    def __str__(self):
        return self.pr


class NotePov(models.Model):
    pov = models.CharField(max_length=20)

    def __str__(self):
        return self.pov


class NoteSizeHDD(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size


class NoteTypeGraphic(models.Model):
    g = models.CharField(max_length=20)

    def __str__(self):
        return self.g


class Note(models.Model):
    Производитель = models.ForeignKey(NoteProizv)
    Модель = models.CharField(max_length=100)
    Картинка = models.ImageField(upload_to='bdimage/notes/')
    Дата_выпуска = models.CharField(max_length=50)
    Тип = models.ForeignKey(NoteType)
    Процессор = models.ForeignKey(NoteProcessor)
    Цвет = models.ForeignKey(Color)
    Материал = models.ForeignKey(Material)
    Матрица = models.ForeignKey(NoteEkran)
    Разрешение = models.ForeignKey(NoteRazr)
    Диагональ = models.ForeignKey(NoteDiag)
    Поверхность = models.ForeignKey(NotePov)
    Оперативная_память = models.CharField(max_length=50)
    Объем_оперативной_памяти = models.CharField(max_length=100)
    Жесткий_диск = models.ForeignKey(NoteHHD)
    Размер = models.ForeignKey(NoteSizeHDD)
    Тип_графического_адаптера = models.ForeignKey(NoteTypeGraphic)
    Графический_адаптер = models.CharField(max_length=50)
    Батарея = models.CharField(max_length=20)
    Вес = models.CharField(max_length=10)
    Гарантия = models.CharField(max_length=20)
    ОС = models.ForeignKey(NoteOS)
    Трансформер = models.BooleanField()
    Микрофон = models.BooleanField()
    Камера = models.BooleanField()
    Количество_пикселей = models.CharField(max_length=5)
    Сенсорный_экран = models.BooleanField()
    Привод = models.BooleanField()
    bluetooth = models.BooleanField()
    wifi = models.BooleanField()
    Количество_usb2 = models.CharField(max_length=5)
    usb3 = models.BooleanField()
    Количество_usb3 = models.CharField(max_length=5)
    usb31 = models.BooleanField()
    Количество_usb31 = models.CharField(max_length=5)
    hdmi = models.BooleanField()
    Подсветка_клавиатуры = models.BooleanField()
    Импортер = models.ForeignKey(Import)
    def __str__(self):
        return self.Производитель







class PCProizv(models.Model):
    p = models.CharField(max_length=20)

    def __str__(self):
        return self.p


class PCOC(models.Model):
    oc = models.CharField(max_length=20)

    def __str__(self):
        return self.oc


class PCProc(models.Model):
    p = models.CharField(max_length=20)

    def __str__(self):
        return self.p


class PCVent(models.Model):
    v = models.CharField(max_length=20)

    def __str__(self):
        return self.v


class PCPam(models.Model):
    p = models.CharField(max_length=10)

    def __str__(self):
        return self.p


class PCHDD(models.Model):
    h = models.CharField(max_length=20)

    def __str__(self):
        return self.h


class PCVideo(models.Model):
    v = models.CharField(max_length=50)

    def __str__(self):
        return self.v


class PCBlock(models.Model):
    b = models.CharField(max_length=20)

    def __str__(self):
        return self.b


class PC(models.Model):
    Производитель = models.ForeignKey(PCProizv)
    Процессор = models.ForeignKey(PCProc)
    Вентилятор = models.ForeignKey(PCVent)
    Мат_плата = models.CharField(max_length=20)
    Опер_память = models.ForeignKey(PCPam)
    Жесткий_диск = models.ForeignKey(PCHDD)
    Видеокарта = models.ForeignKey(PCVideo)
    Цвет_корпуса = models.ForeignKey(Color)
    Блок_питания = models.ForeignKey(PCBlock)
    Импортер = models.ForeignKey(Import)
    OC = models.ForeignKey(PCOC)