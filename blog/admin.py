from django.contrib import admin
from .models import Post, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)

# customize the admin title and header
admin.site.site_header = "Glen Admin"
admin.site.site_title = "Glen Admin"
admin.site.index_text = "Welocome Back, Glen"
