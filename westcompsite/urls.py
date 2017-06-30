from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^pc/(?P<pk>[0-9]+)/$', views.pc_detail, name='pc_detail'),
    url(r'^shop/(?P<pk>[0-9]+)/$', views.raznoe_detail, name='raznoe_detail'),
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^notes/$', views.notes, name='notes'),

    url(r'^hp/$', views.hp, name='hp'),
    url(r'^acer/$', views.acer, name='acer'),
    url(r'^asus/$', views.asus, name='asus'),
    url(r'^dell/$', views.dell, name='dell'),
    url(r'^lenovo/$', views.lenovo, name='lenovo'),

    url(r'^pcs/$', views.pcs, name='pcs'),
    url(r'^complect/$', views.complect, name='complect'),
    url(r'^complect_cooler/$', views.complect_cooler, name='complect_cooler'),
    url(r'^complect_optical/$', views.complect_optical, name='complect_optical'),
    url(r'^complect_mat/$', views.complect_mat, name='complect_mat'),
    url(r'^complect_hdd/$', views.complect_hdd, name='complect_hdd'),
    url(r'^complect_mem/$', views.complect_mem, name='complect_mem'),
    url(r'^complect_power_block/$', views.complect_power_block, name='complect_power_block'),
    url(r'^complect_processor/$', views.complect_processor, name='complect_processor'),
    url(r'^complect_video/$', views.complect_video, name='complect_video'),

    url(r'^periphery/$', views.periphery, name='peryphery'),
    url(r'^access/$', views.access, name='access'),
    url(r'^access_mouse/$', views.access_mouse, name='access_mouse'),
    url(r'^access_klav/$', views.access_klav, name='access_klav'),
    url(r'^access_usb/$', views.access_usb, name='access_usb'),
    url(r'^access_cabel/$', views.access_cabel, name='access_cabel'),
    url(r'^access_naush/$', views.access_naush, name='access_naush'),
    url(r'^access_web/$', views.access_web, name='access_web'),

    url(r'^by/$', views.by, name='by'),
    url(r'^sales/$', views.sales, name='sales'),
    url(r'^news/$', views.news, name='news'),

    url(r'^remont/$', views.remont, name='remont'),
    url(r'^remont_note/$', views.remont_note, name='remont_note'),
    url(r'^remont_phone/$', views.remont_phone, name='remont_phone'),
    url(r'^remont_print/$', views.remont_print, name='remont_print'),
    url(r'^remont_comp/$', views.remont_comp, name='remont_comp'),

    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^price/$', views.price, name='price'),

    url(r'^calculator/$', views.calculator, name='calculator'),
    url(r'^credit/$', views.credit, name='credit'),
    url(r'^ecredit/$', views.ecredit, name='ecredit'),
    url(r'^creditb/$', views.creditb, name='creditb'),
    url(r'^rassrochka/$', views.rassrochka, name='rassrochka'),

    url(r'^detail_kart/$', views.detail_kart, name='detail_kart'),
    url(r'^detail_print/$', views.detail_print, name='detail_print'),

    url(r'^remont_note_vent/$', views.remont_note_vent, name='remont_note_vent'),
    url(r'^remont_note_2/$', views.remont_note_2, name='remont_note_2'),
    url(r'^remont_note_3/$', views.remont_note_3, name='remont_note_3'),

    url(r'^detail_note_cabel/$', views.detail_note_cabel, name='detail_note_cabel'),
    url(r'^detail_note_cabel_1/$', views.detail_note_cabel_1, name='detail_note_cabel_1'),
    url(r'^detail_note_cabel_2/$', views.detail_note_cabel_2, name='detail_note_cabel_2'),

    url(r'^detail_note_vent/$', views.detail_note_vent, name='detail_note_vent'),
    url(r'^detail_note_cooler/$', views.detail_note_cooler, name='detail_note_cooler'),

    url(r'^detail_note_klav/$', views.detail_note_klav, name='detail_note_klav'),
    url(r'^detail_note_klav_1/$', views.detail_note_klav_1, name='detail_note_klav_1'),
    url(r'^detail_note_klav_2/$', views.detail_note_klav_2, name='detail_note_klav_2'),

    url(r'^detail_note_razem/$', views.detail_note_razem, name='detail_note_razem'),
    url(r'^detail_note_zalit/$', views.detail_note_zalit, name='detail_note_zalit'),
    url(r'^detail_note_hdd/$', views.detail_note_hdd, name='detail_note_hdd'),
    url(r'^detail_note_disp/$', views.detail_note_disp, name='detail_note_disp'),
    url(r'^detail_note_mat/$', views.detail_note_mat, name='detail_note_mat'),
    url(r'^detail_note_modern/$', views.detail_note_modern, name='detail_note_modern'),
    url(r'^detail_note_sh/$', views.detail_note_sh, name='detail_note_sh'),

    url(r'^remont_phone_1/$', views.remont_phone_1, name='remont_phone_1'),
    url(r'^remont_phone_2/$', views.remont_phone_2, name='remont_phone_2'),
    url(r'^remont_phone_3/$', views.remont_phone_3, name='remont_phone_3'),

    url(r'^detail_phone_tach$', views.detail_phone_tach, name='detail_phone_tach'),
    url(r'^detail_phone_disp/$', views.detail_phone_disp, name='detail_phone_disp'),
    url(r'^detail_phone_raz/$', views.detail_phone_raz, name='detail_phone_raz'),
    url(r'^detail_phone_bat/$', views.detail_phone_bat, name='detail_phone_bat'),
    url(r'^detail_phone_sim/$', views.detail_phone_sim, name='detail_phone_sim'),
    url(r'^detail_phone_oc/$', views.detail_phone_oc, name='detail_phone_oc'),
    url(r'^detail_phone_virus/$', views.detail_phone_virus, name='detail_phone_virus'),

    url(r'^remont_pc_1/$', views.remont_pc_1, name='remont_pc_1'),
    url(r'^remont_pc_2/$', views.remont_pc_2, name='remont_pc_2'),

    url(r'^detail_pc_block/$', views.detail_pc_block, name='detail_pc_block'),
    url(r'^detail_pc_clear/$', views.detail_pc_clear, name='detail_pc_clear'),
    url(r'^detail_pc_hdd/$', views.detail_pc_hdd, name='detail_pc_hdd'),
    url(r'^detail_pc_mat/$', views.detail_pc_mat, name='detail_pc_mat'),
    url(r'^detail_pc_modern/$', views.detail_pc_modern, name='detail_pc_modern'),
    url(r'^detail_pc_video/$', views.detail_pc_video, name='detail_pc_video'),

    url(r'^detail_oc/$', views.detail_oc, name='detail_oc'),
]
