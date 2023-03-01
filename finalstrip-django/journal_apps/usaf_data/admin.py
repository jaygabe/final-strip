from django.contrib import admin
from .models import USAFencingInfo


class USAFencingInfoAdmin(admin.ModelAdmin):
    # member_fields = [field.name for field in USAFencingInfo._meta.get_fields()]
    # member_filters = ['fencer', 'middle name']
    # member_fields.remove('fencer')
    member_fields = ['id', 'member_id', 'last_name', 'first_name','gender', 
'birthdate','division','region','club1_abv','school_abv','sabre', 'epee', 'foil']
    list_display = member_fields
 


admin.site.register(USAFencingInfo, USAFencingInfoAdmin)

# 'fencer', 'id', 'member_id', 'last_name', 'first_name', 'middle_name', 'suffix', 'nickname', 'gender', 
# 'birthdate', 'birthdate_verified', 'division', 'club1', 'club1_abv', 'club1_id', 'club2', 'club2_abv', 'club2_id', 
# 'school', 'school_abv', 'school_id', 'member_type', 'checked', 'competitive', 'expiration', 'sabre', 'epee', 'foil', 
# 'us_citizen', 'permanent', 'country', 'region', 'background_expires', 'safesport_expires', 'non_competitive', 
# 'highest_ref_rating', 'us_ref_foil', 'us_ref_foil_year', 'us_ref_epee', 'us_ref_epee_year', 'us_ref_sabre', 
# 'us_ref_sabre_year', 'fie_ref_foil', 'fie_ref_foil_year', 
# 'fie_ref_epee', 'fie_ref_epee_year', 'fie_ref_sabre', 'fie_ref_sabre_year'