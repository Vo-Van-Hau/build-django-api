from django.contrib import admin

# Register your models here.
class MultiDBModel(admin.ModelAdmin):

    # Tell Django to save objects to the 'other' database
    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    # Tell Django to delete objects from the 'other' database
    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    # Tell Django to look for objects on the 'other' database
    def get_queryset(self, request):
        return super().get_queryset(request).using(using=self.using)

    # Tell Django to populate ForeignKey widgets using a query on the 'other' database
    def formfield_for_foreign_keys(self, db_field, request, **kwargs):
        return super().formfield_for_foreign_keys(db_field, request, using=self.using, **kwargs)

    # Tell Django to populate ManyToMany widgets using a query on the 'other' database
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

# Testing
class ProfileSelectionAdmin(MultiDBModel):
    using = 'resumeapp'