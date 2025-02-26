from django.contrib import admin
from admin_dashboard.models import Student, Document, DocumentFile

class DocumentInline(admin.TabularInline):
    model = Document
    extra = 1

class DocumentFileInline(admin.TabularInline):
    model = DocumentFile
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'user', 'status', 'created_at', 'updated_at')
    search_fields = ('unique_id', 'user__username', 'user__email')
    list_filter = ('status', 'intake_month', 'intake_year', 'gender', 'education_level')
    inlines = [DocumentInline]

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_type', 'student', 'verification_status', 'is_latest', 'created_at', 'updated_at')
    search_fields = ('document_type', 'student__unique_id')
    list_filter = ('verification_status', 'document_type')
    inlines = [DocumentFileInline]

@admin.register(DocumentFile)
class DocumentFileAdmin(admin.ModelAdmin):
    list_display = ('document', 'expiry_date', 'score', 'created_at', 'updated_at')
    search_fields = ('document__document_type', 'document__student__unique_id')
    list_filter = ('expiry_date',)