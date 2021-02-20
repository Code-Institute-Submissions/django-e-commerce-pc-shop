from django.contrib import admin
from .models import NewsUsers


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'date_added',)


admin.site.register(NewsUsers, NewsletterAdmin)
