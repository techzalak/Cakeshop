from django.contrib import admin

# Register your models here.

from .models import Birthday
# Register your models here.
@admin.register(Birthday)

class BirthdayAdmin(admin.ModelAdmin):
  list_display = ('bpid','bname','bimage','bdescrip','bprice500','bprice1','bprice2')
