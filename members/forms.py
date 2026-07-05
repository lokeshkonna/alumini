
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'academic-input w-full h-14 px-4 rounded-lg', 'placeholder': 'Pick a unique username'}),
            'email': forms.EmailInput(attrs={'class': 'academic-input w-full h-14 px-4 rounded-lg', 'placeholder': 'Enter your student/alumni email'}),
            'first_name': forms.TextInput(attrs={'class': 'academic-input w-full h-14 px-4 rounded-lg', 'placeholder': 'Your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'academic-input w-full h-14 px-4 rounded-lg', 'placeholder': 'Your last name'}),
            'password': forms.PasswordInput(attrs={'class': 'academic-input w-full h-14 px-4 rounded-lg', 'placeholder': 'Create a strong password'}),
        }

    role = forms.ChoiceField(
        choices=Profile.ROLE_CHOICES, 
        required=True,
        widget=forms.Select(attrs={'class': 'w-full bg-surface-container-low border-0 border-b-2 border-outline-variant/20 rounded-t-xl px-4 py-4 focus:ring-0 focus:bg-white focus:border-primary transition-all appearance-none text-on-surface font-medium'})
    )
    department = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'academic-input w-full h-14 px-4 rounded-lg', 'placeholder': 'e.g. Computer Science'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'academic-input w-full h-14 px-4 rounded-lg', 'placeholder': 'Repeat your password'}),
        required=True
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
    
    
    def clean_username(self):
        username = self.cleaned_data.get("username")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")

        return username
    

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already registered.")

        return email
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "profile_picture",
            "bio",
            "company",
            "designation",
            "department",
            "location",
            "class_year",
            "skills",
        ]

        widgets = {
            "bio": forms.Textarea(attrs={
                "rows": 4,
                "class": "academic-input w-full rounded-lg p-4",
                "placeholder": "Tell everyone about yourself..."
            }),

            "company": forms.TextInput(attrs={
                "class": "academic-input w-full h-12 px-4 rounded-lg",
                "placeholder": "Company"
            }),

            "designation": forms.TextInput(attrs={
                "class": "academic-input w-full h-12 px-4 rounded-lg",
                "placeholder": "Designation"
            }),

            "department": forms.TextInput(attrs={
                "class": "academic-input w-full h-12 px-4 rounded-lg",
                "placeholder": "Department"
            }),

            "location": forms.TextInput(attrs={
                "class": "academic-input w-full h-12 px-4 rounded-lg",
                "placeholder": "Location"
            }),

            "class_year": forms.NumberInput(attrs={
                "class": "academic-input w-full h-12 px-4 rounded-lg"
            }),

            "skills": forms.SelectMultiple(attrs={
                "class": "academic-input w-full rounded-lg p-2"
            }),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content", "post_image"]

        widgets = {
            "content": forms.Textarea(attrs={
                "rows": 4,
                "class": "academic-input w-full rounded-lg p-4",
                "placeholder": "What's on your mind?"
            }),

            "post_image": forms.ClearableFileInput(attrs={
                "class": "academic-input w-full"
            }),
        }
