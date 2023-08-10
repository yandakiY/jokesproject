from django.contrib import admin
from .models import Joke,Category

class JokeLine(admin.TabularInline):
    model = Joke
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    
    fieldsets = (
        (None, {
            "fields": (
                ["libelle"]
            ),
        }),
    )
    
    inlines = [JokeLine]
    

# Register your models here.
admin.site.register(Category , CategoryAdmin)
admin.site.register(Joke)
# hpelitebook840