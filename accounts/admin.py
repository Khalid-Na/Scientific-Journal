from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import UserManager
from accounts.models import Account,Author,Reviewer,Editor,EditorInChief,Publisher
from journals.models import Journals,Volume,Issue
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _


class AccountAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email' ,'password', )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name' , 'country')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 
                                       'is_reviewer', 'is_editor' , 'is_chief_editor', 'is_author','is_publisher' ,
                                    )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
           
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ['email', 'first_name', 'last_name', 'is_staff','last_login']
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', )
    readonly_fields = ('date_joined','last_login')
    filter_horizontal =()
    list_filter = ('is_staff', 'date_joined')
    
# @admin.register(Author)
class AuthorAdmin(UserManager):
    actions = [
        'activate_users',
    ]

    def activate_users(self, request, queryset):
        cnt = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, 'Activated {} users.'.format(cnt))
    activate_users.short_description = 'Activate Users'  # type: ignore
  
    
    

    
admin.site.register(Account, AccountAdmin)
admin.site.register(Author)
admin.site.register(Reviewer)
admin.site.register(Editor)
admin.site.register(EditorInChief)
admin.site.register(Publisher)
admin.site.site_header = "Scientific  Journal Administration"
 
admin.site.register(Journals)
admin.site.register(Volume)
admin.site.register(Issue)