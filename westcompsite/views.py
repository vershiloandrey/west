from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib import auth
from .models import Notes
from .models import PC
from .models import Raznoe


def post_list(request):
    return render(request, 'westcompsite/post_list.html', {})


def post_detail(request, pk):
    post = get_object_or_404(Notes, pk=pk)
    return render(request, 'westcompsite/post_detail.html', {'post': post})


def raznoe_detail(request, pk):
    post = get_object_or_404(Raznoe, pk=pk)
    return render(request, 'westcompsite/raznoe_detail.html', {'post': post})


def contacts(request):
    return render(request, 'westcompsite/contacts.html', {})


def price(request):
    return render(request, 'westcompsite/price.html', {})


def credit(request):
    return render(request, 'westcompsite/credit.html', {})


def calculator(request):
    return render(request, 'westcompsite/calculator.html', {})


def ecredit(request):
    return render(request, 'westcompsite/ecredit.html', {})


def creditb(request):
    return render(request, 'westcompsite/creditb.html', {})


def rassrochka(request):
    return render(request, 'westcompsite/rassrochka.html', {})


def shop(request):
    return render(request, 'westcompsite/shop.html', {})


def notes(request):
    notes = Notes.objects.all()
    return render(request, 'westcompsite/notes.html', {'notes': notes})


def hp(request):
    notes = Notes.objects.filter(Proizv__pr='HP').order_by('cena')
    return render(request, 'westcompsite/hp.html', {'notes': notes})


def lenovo(request):
    notes = Notes.objects.filter(Proizv__pr='Lenovo').order_by('cena')
    return render(request, 'westcompsite/lenovo.html', {'notes': notes})


def pcs(request):
    products = PC.objects.all().order_by('Proizv')
    return render(request, 'westcompsite/pcs.html', {'products': products})


def access(request):
    products = Raznoe.objects.filter(Type__t='Аксессуары').order_by('Text')
    return render(request, 'westcompsite/access.html', {'products': products})


def periphery(request):
    products = Raznoe.objects.filter(Type__t='Периферия').order_by('Text')
    return render(request, 'westcompsite/periphery.html', {'products': products})


def complect(request):
    products = Raznoe.objects.filter(Type__t='Комплектующие').order_by('Text')
    return render(request, 'westcompsite/complect.html', {'products': products})


def by(request):
    notes = Notes.objects.filter(by=True).order_by('cena')
    pcs = PC.objects.filter(by=True).order_by('cena')
    products = Raznoe.objects.filter(by=True).order_by('cena')
    return render(request, 'westcompsite/by.html', {'notes': notes, 'products': products, 'pcs': pcs})


def sales(request):
    notes = Notes.objects.filter(sale=True).order_by('cena')
    pcs = PC.objects.filter(sale=True).order_by('cena')
    products = Raznoe.objects.filter(sale=True).order_by('cena')
    return render(request, 'westcompsite/sales.html', {'notes': notes, 'products': products, 'pcs': pcs})


def news(request):
    notes = Notes.objects.filter(new=True).order_by('cena')
    pcs = PC.objects.filter(new=True).order_by('cena')
    products = Raznoe.objects.filter(new=True).order_by('cena')
    return render(request, 'westcompsite/news.html', {'notes': notes, 'products': products, 'pcs': pcs})


def remont(request):
    return render(request, 'westcompsite/remont.html', {})


def product_detail(request):
    return render(request, 'westcompsite/post_detail.html', {})


def detail_kart(request):
    return render(request, 'westcompsite/detail_kart.html', {})


def detail_print(request):
    return render(request, 'westcompsite/detail_print.html', {})


def remont_note_vent(request):
    return render(request, 'westcompsite/remont_note_vent.html', {})


def remont_note_2(request):
    return render(request, 'westcompsite/remont_note_2.html', {})


def remont_note_3(request):
    return render(request, 'westcompsite/remont_note_3.html', {})


def detail_note_cabel(request):
    return render(request, 'westcompsite/detail_note_cabel.html', {})


def detail_note_cabel_1(request):
    return render(request, 'westcompsite/detail_note_cabel_1.html', {})


def detail_note_cabel_2(request):
    return render(request, 'westcompsite/detail_note_cabel_2.html', {})


def detail_note_vent(request):
    return render(request, 'westcompsite/detail_note_vent.html', {})


def detail_note_cooler(request):
    return render(request, 'westcompsite/detail_note_cooler.html', {})


def detail_note_klav(request):
    return render(request, 'westcompsite/detail_note_klav.html', {})


def detail_note_klav_1(request):
    return render(request, 'westcompsite/detail_note_klav_1.html', {})


def detail_note_klav_2(request):
    return render(request, 'westcompsite/detail_note_klav_2.html', {})


def detail_note_razem(request):
    return render(request, 'westcompsite/detail_note_razem.html', {})


def detail_note_zalit(request):
    return render(request, 'westcompsite/detail_note_zalit.html', {})


def detail_note_hdd(request):
    return render(request, 'westcompsite/detail_note_hdd.html', {})


def detail_note_disp(request):
    return render(request, 'westcompsite/detail_note_disp.html', {})


def detail_note_mat(request):
    return render(request, 'westcompsite/detail_note_mat.html', {})


def detail_note_modern(request):
    return render(request, 'westcompsite/detail_note_modern.html', {})


def detail_note_sh(request):
    return render(request, 'westcompsite/detail_note_sh.html', {})


def remont_phone_1(request):
    return render(request, 'westcompsite/remont_phone_1.html', {})


def remont_phone_2(request):
    return render(request, 'westcompsite/remont_phone_2.html', {})


def remont_phone_3(request):
    return render(request, 'westcompsite/remont_phone_3.html', {})


def detail_phone_tach(request):
    return render(request, 'westcompsite/detail_phone_tach.html', {})


def detail_phone_disp(request):
    return render(request, 'westcompsite/detail_phone_disp.html', {})


def detail_phone_raz(request):
    return render(request, 'westcompsite/detail_phone_raz.html', {})


def detail_phone_bat(request):
    return render(request, 'westcompsite/detail_phone_bat.html', {})


def detail_phone_sim(request):
    return render(request, 'westcompsite/detail_phone_sim.html', {})


def detail_phone_oc(request):
    return render(request, 'westcompsite/detail_phone_oc.html', {})


def detail_phone_virus(request):
    return render(request, 'westcompsite/detail_phone_virus.html', {})


def remont_pc_1(request):
    return render(request, 'westcompsite/remont_pc_1.html', {})


def remont_pc_2(request):
    return render(request, 'westcompsite/remont_pc_2.html', {})


def detail_pc_block(request):
    return render(request, 'westcompsite/detail_pc_block.html', {})


def detail_pc_hdd(request):
    return render(request, 'westcompsite/detail_pc_hdd.html', {})


def detail_pc_clear(request):
    return render(request, 'westcompsite/detail_pc_clear.html', {})


def detail_pc_mat(request):
    return render(request, 'westcompsite/detail_pc_mat.html', {})


def detail_pc_modern(request):
    return render(request, 'westcompsite/detail_pc_modern.html', {})


def detail_pc_video(request):
    return render(request, 'westcompsite/detail_pc_video.html', {})


def detail_oc(request):
    return render(request, 'westcompsite/detail_oc.html', {})
