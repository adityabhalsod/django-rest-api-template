from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    exclude = ("created_date_time", "updated_date_time")
