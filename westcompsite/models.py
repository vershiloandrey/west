from django.db import models


# Create your models here.

class Import(models.Model):
    i = models.CharField(max_length=200, default='')

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
    cena = models.IntegerField()
    o_proizv = models.CharField(max_length=200)
    new = models.BooleanField(default=False)

    def __str__(self):
        return (self.Proizv.pr + " " + self.Model)


class PCProizv(models.Model):
    p = models.CharField(max_length=20)

    def __str__(self):
        return self.p


class PCOC(models.Model):
    oc = models.CharField(max_length=50)

    def __str__(self):
        return self.oc


class PCProc(models.Model):
    p = models.CharField(max_length=50)

    def __str__(self):
        return self.p


class PCVent(models.Model):
    v = models.CharField(max_length=50)

    def __str__(self):
        return self.v


class PCPam(models.Model):
    p = models.CharField(max_length=50)

    def __str__(self):
        return self.p


class PCHDD(models.Model):
    h = models.CharField(max_length=50)

    def __str__(self):
        return self.h


class PCVideo(models.Model):
    v = models.CharField(max_length=50)

    def __str__(self):
        return self.v


class PCBlock(models.Model):
    b = models.CharField(max_length=50)

    def __str__(self):
        return self.b


class PC(models.Model):
    Image_URL = models.CharField(max_length=300)
    Name = models.CharField(max_length=100)
    Processor = models.CharField(max_length=100)
    Mat_plata = models.CharField(max_length=100)
    OMemory = models.CharField(max_length=100)
    power_box = models.CharField(max_length=100)
    HDD = models.CharField(max_length=100)
    CDROM = models.CharField(max_length=100)
    Graph = models.CharField(max_length=100)
    Color_box = models.CharField(max_length=100)
    Box = models.CharField(max_length=100)
    Monitor = models.CharField(max_length=100)
    Importer = models.CharField(max_length=100)
    o_proizv = models.CharField(max_length=100)
    sale = models.BooleanField()
    by = models.BooleanField()
    cena = models.IntegerField()
    new = models.BooleanField()


    def __str__(self):
        return (self.Name)


class TypePer(models.Model):
    t = models.CharField(max_length=50)

    def __str__(self):
        return self.t


class Raznoe(models.Model):
    Image_URL = models.CharField(max_length=300)
    Name = models.CharField(max_length=100)
    Type = models.ForeignKey(TypePer)
    Text = models.TextField()
    cena = models.CharField(max_length=20)
    new = models.BooleanField()
    sale = models.BooleanField()
    by = models.BooleanField()

    def __str__(self):
        return (self.Type.t + " " + self.Name)