from django.contrib import admin
from .models import FileUpload

# Register the FileUpload model
@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')  # Display the file and uploaded_at fields in the admin list view
