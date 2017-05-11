from django.contrib import admin
from .models import Note
from .models import NoteType
from .models import NoteHHD
from .models import NoteEkran
from .models import NoteOS
from .models import NoteDiag
from .models import NoteRazr
from .models import NoteProizv
from .models import NoteProcessor
from .models import NotePov
from .models import NoteSizeHDD
from .models import NoteTypeGraphic
from .models import Material

from .models import PC
from .models import PCBlock
from .models import PCHDD
from .models import PCOC
from .models import PCPam
from .models import PCProc
from .models import PCProizv
from .models import PCVent
from .models import PCVideo

admin.site.register(Note)
admin.site.register(NoteType)
admin.site.register(NoteHHD)
admin.site.register(NoteRazr)
admin.site.register(NoteDiag)
admin.site.register(NoteOS)
admin.site.register(NoteEkran)
admin.site.register(NoteProizv)
admin.site.register(NoteProcessor)
admin.site.register(NotePov)
admin.site.register(NoteSizeHDD)
admin.site.register(Material)
admin.site.register(NoteTypeGraphic)


admin.site.register(PC)
admin.site.register(PCVideo)
admin.site.register(PCVent)
admin.site.register(PCProizv)
admin.site.register(PCProc)
admin.site.register(PCPam)
admin.site.register(PCOC)
admin.site.register(PCHDD)
admin.site.register(PCBlock)