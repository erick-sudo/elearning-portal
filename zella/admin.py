from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import College, Course, Unit, Quiz, Question, Choice, ZellaUser\

from .forms import ZellaUserCreationForm, ZellaUserChangeForm

from .models import ZellaUser

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    classes = ['collapse']

class QuestionInline(admin.StackedInline):
    extra = 0
    model = Question
    fieldsets = [
        ('Question', {'fields': ['question_text']}),
        ('Creation Date', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    classes = ['collapse']
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date' )

class QuizInline(admin.StackedInline):
    extra = 0
    model = Quiz
    fieldsets = [
        ('Quiz', {"fields": ['Description','due_date']}),
    ]
    classes = ['collapse']
    inlines = [QuestionInline]

class UnitInline(admin.StackedInline):
    extra = 0
    model = Unit
    fieldsets = [
        ('Unit Name', {"fields": ['name']}),
        ('Unit Abbreviation', {"fields": ['abbr']}),
    ]
    classes = ['collapse']
    inlines = [QuizInline]

class CourseInline(admin.StackedInline):
    extra = 0
    model = Course
    fieldsets = [
        ('Course Name', {"fields": ['name']}),
        ('Course Abbreviation', {"fields": ['abbr']}),
        ('Course Duration', {"fields": ['duration']}),
    ]
    classes = ['collapse']
    inlines = [UnitInline]

class CollegeAdmin(admin.ModelAdmin):
    model = College
    fieldsets = [
        ('College Name', {"fields": ['name']}),
        ('College Abbreviation', {"fields": ['abbr']}),
    ]
    inlines = [CourseInline]


class ZellaUserAdmin(UserAdmin):
    add_form = ZellaUserCreationForm
    form = ZellaUserChangeForm
    model = ZellaUser
    list_display = ('firstname', 'lastname', 'email', 'course', 'is_staff', 'is_active')
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )


admin.site.register(College, CollegeAdmin)
admin.site.register(Course)
admin.site.register(Unit)
admin.site.register(Quiz)
admin.site.register(Question)

admin.site.register(ZellaUser, ZellaUserAdmin)