from django.contrib import admin
from .models import API, Biodata
from .models import Album, Song
# Register your models here.

class BiodataAdmin(admin.ModelAdmin):
    #untuk membuat tabel yang rapi pada tabel dashboard admin
    list_display = ('user','nama','telp','alamat')
    #untuk seacrh data pada table dashboard admin
    search_fields = ('user','nama')

admin.site.register(Biodata, BiodataAdmin)
admin.site.register(Album)
admin.site.register(Song)

class APIAdmin(admin.ModelAdmin):
    list_display = ('user', 'api_key')
admin.site.register(API, APIAdmin)