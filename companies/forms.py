from core.forms import BaseModelForm

from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        # نحدد الحقول التي نريد للشركة تعبئتها (استبعدنا الحقول التلقائية مثل created_at)
        fields = [
            'category',
            'title',
            'description',
            'required_skills',
            'location',
            'employment_type',
            'experience_level',
            'min_salary',
            'max_salary',
            'deadline',
            'requirements',
            # 'company',
        ]


        labels = {
            'category': 'مجال الوظيفة',
            'title': 'المسمى الوظيفي',
            'description': 'وصف الوظيفة',
            'requirements': 'المتطلبات الإضافية',
            'required_skills': 'المهارات المطلوبة',
            'location': 'موقع الوظيفة',
            'employment_type': 'نوع الدوام',
            'experience_level': 'مستوى الخبرة',
            'min_salary': 'الحد الأدنى للراتب',
            'max_salary': 'الحد الأعلى للراتب',
            'deadline': 'موعد انتهاء التقديم',
        }
        # إضافة Widgets لتنسيق الحقول ومنحها كلاسات CSS
        widgets = {
            'title': forms.TextInput( attrs={'class': 'input input-bordered ', 'placeholder':'ادخل المسمى الوظيفي'}),
            'category': forms.Select(attrs={'class': 'select select-bordered ','placeholder':'أختر التخصص'}),
            'description': forms.Textarea(attrs={'class': 'textarea textarea-bordered ', 'rows': 2, 'placeholder':'ادخل الوصف الوظيفي'}),
            'requirements': forms.Textarea(attrs={'class': 'textarea textarea-bordered ', 'rows': 2, 'placeholder':'ادخل المطلبات  الإضافية (إختياري)'}),
            # 'required_skills': forms.SelectMultiple(attrs={'class': 'select2-skills w-full',  'multiple': 'multiple'}),
            'location': forms.TextInput(attrs={
                'class': 'input ',
                'placeholder': 'ادخل موقع الوظيفة'
            }),
            'employment_type': forms.Select(attrs={
                'class': 'select ',
            }),
            'experience_level': forms.Select(attrs={
                'class': 'select',
            }),
            'min_salary': forms.NumberInput(attrs={
                'class': 'input ',
                'placeholder': 'الحد الأدنى'
            }),
            'max_salary': forms.NumberInput(attrs={
                'class': 'input ',
                'placeholder': 'الحد الأعلى'
            }),
            'deadline': forms.DateInput(attrs={'class': 'input input-bordered w-full', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #
        # if 'company' in self.fields:
        #     self.fields['company'].widget = forms.HiddenInput()
        #     self.fields['company'].required = False

        for field_name, field in self.fields.items():
            existing = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f"{existing}   w-full  rounded-xl py-2.5 px-4 text-[13px]  focus:border-brand/40 transition-color".strip()



    def clean(self):
        cleaned_data = super().clean()
        min_salary = cleaned_data.get("min_salary")
        max_salary = cleaned_data.get("max_salary")

        if min_salary and max_salary and min_salary > max_salary:
            raise forms.ValidationError("يجب أن يكون الحد الأدنى للراتب أقل من الحد الأعلى.")
        return cleaned_data