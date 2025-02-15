from django.contrib import admin

from account.models import Profile


# Register your models here.
admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_filter = ['id', 'unique_id', 'phone', 'birthdate']
    list_display = ['id', 'unique_id', 'phone', 'birthdate']
    search_fields = ['id', 'unique_id', 'phone', 'birthdate']
    list_display_links = ['id', 'unique_id']
    list_editable = ['phone', 'birthdate']
    list_per_page = 10
    list_max_show_all = 100
    list_select_related = ['user']
    list_display_links_details = True

    readonly_fields = ['unique_id']
    fieldsets = [
        ('Profile Picture', {'fields': ['profile_pic']}),
        ('User Information', {'fields': ['user', 'unique_id', 'phone', 'address', 'birthdate']})
    ]
    add_fieldsets = [
        ('Profile Picture', {'fields': ['profile_pic']}),
        ('User Information', {'fields': ['user', 'unique_id', 'phone', 'address', 'birthdate']})
    ]
    actions = ['delete_selected', 'delete_all']
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    actions_include_pk = True

    def delete_all(self, request, queryset):
        queryset.delete()

    delete_all.short_description = 'Delete all selected profiles'

    def delete_selected(self, request, queryset):
        queryset.delete()

    delete_selected.short_description = 'Delete selected profiles'
