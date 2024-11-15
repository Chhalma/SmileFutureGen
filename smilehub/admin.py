from django.contrib import admin

from smilehub.models import Donor
from smilehub.models import Campaign
from smilehub.models import Donation
# Register your models here.

admin.site.register(Donor)
admin.site.register(Campaign)
admin.site.register(Donation)