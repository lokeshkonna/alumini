from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from .models import Profile, Post, Job, Event, Message, Skill
from .forms import SignupForm, ProfileForm, PostForm
from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth.decorators import login_required
from django.db.models import Q

def index(request):
    featured_profiles = Profile.objects.filter(role='ALUMNI').order_by('?')[:4]
    events = Event.objects.all().order_by('date')[:3]
    latest_posts = Post.objects.all().order_by('-created_at')[:5]
    
    context = {
        'featured_profiles': featured_profiles,
        'events': events,
        'latest_posts': latest_posts,
    }
    return render(request, 'members/index.html', context)

@login_required
def dashboard_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
        
    context = {
        'screen_name': 'dashboard',
        'profile': profile,
        'upcoming_events': Event.objects.all().order_by('date')[:2],
        'latest_jobs': Job.objects.all().order_by('-posted_at')[:3],
        'stats': {
            'connections': Profile.objects.count(),
            'jobs': Job.objects.count(),
            'events': Event.objects.count(),
            'posts': Post.objects.count(),
            'alumni': Profile.objects.filter(role="ALUMNI").count(),
            'students': Profile.objects.filter(role="STUDENT").count(),
        }
    }
    return render(request, 'stitch/dashboard.html', context)

@login_required
def feed_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect("posts_feed")
    else:
        form = PostForm()

    context = {
        "posts": Post.objects.all().order_by("-created_at"),
        "featured_alumni": Profile.objects.filter(role="ALUMNI")[:5],
        "trending_skills": Skill.objects.all()[:5],
        "form": form,
        "screen_name": "posts_feed",
    }

    return render(request, "stitch/posts_feed.html", context)

def profiles_view(request):
    query = request.GET.get('q')
    if query:
        from django.db.models import Q
        profiles = Profile.objects.filter(
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(company__icontains=query) |
            Q(industry__icontains=query) |
            Q(designation__icontains=query)
        )
    else:
        profiles = Profile.objects.all()
    
    # Dynamic filter data
    industries = Profile.objects.exclude(industry='').values_list('industry', flat=True).distinct()
    locations = Profile.objects.exclude(location='').values_list('location', flat=True).distinct()
    years = Profile.objects.exclude(class_year__isnull=True).values_list('class_year', flat=True).distinct().order_by('-class_year')
    
    context = {
        'screen_name': 'profiles',
        'profiles': profiles,
        'filter_data': {
            'industries': industries,
            'locations': locations,
            'years': years
        }
    }
    return render(request, 'stitch/profiles.html', context)

@login_required
def profile_detail_view(request, profile_id):

    profile = get_object_or_404(Profile, id=profile_id)

    posts = Post.objects.filter(
        author=profile
    ).order_by("-created_at")

    context = {
        "screen_name": "profile_detail",
        "profile": profile,
        "posts": posts,
    }

    return render(
        request,
        "stitch/profile_detail.html",
        context
    )

@login_required
def edit_profile_view(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect("profile_detail", profile_id=profile.id)

    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        "stitch/edit_profile.html",
        {
            "screen_name": "edit_profile",
            "form": form,
        }
    )

@login_required
def create_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()

            return redirect("posts_feed")

    else:
        form = PostForm()

    return render(
        request,
        "stitch/create_post.html",
        {
            "form": form,
            "screen_name": "create_post",
        },
    )

def jobs_view(request):
    context = {
        'screen_name': 'jobs',
        'jobs': Job.objects.all().order_by('-posted_at')
    }
    return render(request, 'stitch/jobs.html', context)

def events_view(request):
    context = {
        'screen_name': 'events',
        'events': Event.objects.all().order_by('date')
    }
    return render(request, 'stitch/events.html', context)

def mentorship_view(request):
    profiles = Profile.objects.filter(role='ALUMNI')
    expertises = Skill.objects.all()
    
    context = {
        'screen_name': 'mentorship',
        'profiles': profiles,
        'expertises': expertises
    }
    return render(request, 'stitch/mentorship.html', context)

@login_required
def messages_view(request):
    # Get latest 20 messages involving the user
    chat_messages = Message.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user)
    ).order_by('timestamp')[:20]
    
    # Get conversation list (profiles of people user has messaged)
    sent_to = Message.objects.filter(sender=request.user).values_list('receiver', flat=True)
    received_from = Message.objects.filter(receiver=request.user).values_list('sender', flat=True)
    conversation_user_ids = set(list(sent_to) + list(received_from))
    
    context = {
        'screen_name': 'messages',
        'chat_messages': chat_messages,
        'conversations': Profile.objects.filter(user_id__in=conversation_user_ids)
    }
    return render(request, 'stitch/messages.html', context)

def signup_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(
                user=user,
                role=form.cleaned_data['role'],
                department=form.cleaned_data.get('department', '')
            )
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'stitch/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
        # Add styling classes to form fields
        form.fields['username'].widget.attrs.update({
            'class': 'academic-input w-full h-14 pl-12 pr-4 rounded-lg border-none focus:ring-0 placeholder:text-outline-variant/60',
            'placeholder': 'Your username'
        })
        form.fields['password'].widget.attrs.update({
            'class': 'academic-input w-full h-14 pl-12 pr-4 rounded-lg border-none focus:ring-0 placeholder:text-outline-variant/60',
            'placeholder': 'Your password'
        })
    return render(request, 'stitch/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')
