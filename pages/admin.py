from django.contrib import admin
from . models import Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

  # def fullname(self,object):
  #   return object.first_name+" "+object.last_name

  def thumbnail(self,object):
    return format_html('<img src="{}" width="50" style="border-radius: 20px" />'.format(object.photo.url))
  thumbnail.short_description='Photo'

  list_display=('id','thumbnail','first_name','designation','created_date')
  list_display_links=('id','thumbnail','first_name',)
  search_fields=('first_name','last_name','designation')

admin.site.register(Team,TeamAdmin)