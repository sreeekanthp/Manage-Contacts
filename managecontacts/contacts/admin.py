from django.contrib import admin
from contacts.models import Contact
from contracts.models import Contract
from groups.models import Group
from members.models import Member
from contacts.models import Contact

class MemberInline(admin.StackedInline):
    ''' Registers a model of member to admin panel to link\
    member and the group.'''
    model = Member
    extra = 1

class GroupAdmin(admin.ModelAdmin):
    
    inlines = [MemberInline]

    
admin.site.register(Contact) # Registers the Contact Models to admin panel
admin.site.register(Group, GroupAdmin) # Registers the Group Models to admin panel
admin.site.register(Contract) # Registers the Contract Models to admin panel
admin.site.register(Member) # Registers the Member Models to admin panel

