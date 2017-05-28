from django.db import models


# Create your models here.

class Import(models.Model):
    i = models.CharField(max_length=50, default='')

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


class Notes(models.Model):
    Proizv = models.ForeignKey(NoteProizv)
    Model = models.CharField(max_length=100)
    Image_URL = models.CharField(max_length=300)
    Data = models.CharField(max_length=50)
    Type = models.ForeignKey(NoteType)
    Processor = models.ForeignKey(NoteProcessor)
    kol_yader = models.CharField(max_length=10)
    Color = models.ForeignKey(Color)
    Material = models.ForeignKey(Material)
    Matrica = models.ForeignKey(NoteEkran)
    Razreshenie = models.ForeignKey(NoteRazr)
    Diagonal = models.ForeignKey(NoteDiag)
    Poverchnost = models.ForeignKey(NotePov)
    OMemory = models.CharField(max_length=50)
    Size_OMemory = models.CharField(max_length=100)
    HDD = models.ForeignKey(NoteHHD)
    Size = models.ForeignKey(NoteSizeHDD)
    Type_graph = models.ForeignKey(NoteTypeGraphic)
    Graph_adapter = models.CharField(max_length=50)
    Battery = models.CharField(max_length=20)
    Ves = models.CharField(max_length=10)
    Garanty = models.CharField(max_length=20)
    OS = models.ForeignKey(NoteOS)
    Transformer = models.BooleanField()
    Micro = models.BooleanField()
    Camera = models.BooleanField()
    Sensor = models.BooleanField()
    DVD = models.BooleanField()
    bluetooth = models.BooleanField()
    wifi = models.BooleanField()
    Count_usb2 = models.CharField(max_length=5)
    usb3 = models.BooleanField()
    Count_usb3 = models.CharField(max_length=5)
    usb31 = models.BooleanField()
    Count_usb31 = models.CharField(max_length=5)
    hdmi = models.BooleanField()
    Svet_klava = models.BooleanField()
    Importer = models.ForeignKey(Import)
    sale = models.BooleanField()
    by = models.BooleanField()
    cena = models.CharField(max_length=10)
    o_proizv = models.CharField(max_length=100)

    def __str__(self):
        return (self.Proizv.pr + " " + self.Model)


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
    Proizv = models.ForeignKey(PCProizv)
    Processor = models.ForeignKey(PCProc)
    kol_yader = models.CharField(max_length=10)
    Ventilator = models.ForeignKey(PCVent)
    Mat_plata = models.CharField(max_length=20)
    OMemory = models.ForeignKey(PCPam)
    HDD = models.ForeignKey(PCHDD)
    Graph = models.ForeignKey(PCVideo)
    Color_box = models.ForeignKey(Color)
    Block_pitaniya = models.ForeignKey(PCBlock)
    Importer = models.ForeignKey(Import)
    OS = models.ForeignKey(PCOC)
    sale = models.BooleanField()
    by = models.BooleanField()
    o_proizv = models.CharField(max_length=100)
    cena = models.CharField(max_length=10)

    def __str__(self):
        return (self.Proizv.pr + " " + self.Processor)