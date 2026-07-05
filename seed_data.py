import os
import django
import random
from datetime import datetime, timedelta
from django.utils import timezone

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alumini_project.settings')
django.setup()

from django.contrib.auth.models import User
from members.models import Profile, Post, Job, Event, Skill

def seed():
    print("Starting data seeding...")
    
    # 1. Clear existing data
    User.objects.filter(is_superuser=False).delete()
    Post.objects.all().delete()
    Job.objects.all().delete()
    Event.objects.all().delete()
    Skill.objects.all().delete()

    # 2. Create Skills
    skill_names = ["Python", "Django", "Machine Learning", "UI/UX Design", "React", "Cloud Architecture", "Data Science", "Marketing Strategy", "Public Speaking", "Financial Modeling"]
    skills = [Skill.objects.create(name=name) for name in skill_names]

    # 3. Create Users & Profiles
    alumni_data = [
        {"username": "jdoe", "email": "john.doe@example.edu", "first": "John", "last": "Doe", "role": "ALUMNI", "dept": "Computer Science", "bio": "Senior Software Architect at TechGiant. Passionate about AI and scalable systems.", "company": "TechGiant", "designation": "Senior Architect"},
        {"username": "asmith", "email": "alice.smith@example.edu", "first": "Alice", "last": "Smith", "role": "ALUMNI", "dept": "Architecture", "bio": "Urban Designer focused on sustainable cities. Award-winning architect.", "company": "EcoBuild", "designation": "Principal Architect"},
        {"username": "rkapoor", "email": "raj.kapoor@example.edu", "first": "Raj", "last": "Kapoor", "role": "ALUMNI", "dept": "Business Administration", "bio": "Venture Capitalist and Angel Investor. Helping startups scale globally.", "company": "VentureFlow", "designation": "Partner"},
        {"username": "mgarcia", "email": "maria.garcia@example.edu", "first": "Maria", "last": "Garcia", "role": "ALUMNI", "dept": "Visual Arts", "bio": "Creative Director at StudioX. Exploring the intersection of art and technology.", "company": "StudioX", "designation": "Creative Director"},
        {"username": "slewis", "email": "sam.lewis@example.edu", "first": "Sam", "last": "Lewis", "role": "STUDENT", "dept": "Physics", "bio": "Junior researcher interested in quantum computing and dark matter.", "company": "Uni Lab", "designation": "Research Intern"},
    ]

    profiles = []
    for data in alumni_data:
        user = User.objects.create_user(username=data["username"], email=data["email"], password="password123", first_name=data["first"], last_name=data["last"])
        profile = Profile.objects.create(
            user=user,
            role=data["role"],
            department=data["dept"],
            bio=data["bio"],
            class_year=random.randint(2010, 2023),
            company=data["company"],
            designation=data["designation"],
            industry=random.choice(["Technology", "Finance", "Healthcare", "Education", "Arts"]),
            location=random.choice(["New York, NY", "London, UK", "Remote", "San Francisco, CA", "Singapore"])
        )
        
        # Add random skills
        profile.skills.set(random.sample(skills, k=3))
        profiles.append(profile)

    # 4. Create Posts
    post_contents = [
        "Excited to announce that I'll be speaking at the upcoming Global Tech Summit! Looking forward to meeting fellow alumni there.",
        "Just finished a great mentorship session. It's so rewarding to see the next generation of architects growing.",
        "Does anyone have recommendations for a good Cloud Security certification?",
        "Our latest urban rejuvenation project in Singapore just got approved. Sustainability is the future!",
        "Reflecting on my time at the university. Grateful for the foundation it gave me for my venture capital career."
    ]

    for i, content in enumerate(post_contents):
        Post.objects.create(
            author=profiles[i % len(profiles)], # Relates to Profile
            content=content,
            image_url=f"https://picsum.photos/seed/post{i}/800/400"
        )

    # 5. Create Jobs
    jobs_data = [
        {"title": "Senior Backend Developer", "company": "NexGen AI", "location": "Remote", "type": "FULL_TIME", "salary": "$120k - $150k"},
        {"title": "Urban Planning Consultant", "company": "GreenBuild", "location": "New York, NY", "type": "CONTRACT", "salary": "$80/hr"},
        {"title": "Product Marketing Manager", "company": "GrowthScale", "location": "San Francisco, CA", "type": "FULL_TIME", "salary": "$110k - $140k"},
        {"title": "Remote Research Assistant", "company": "Global Systems", "location": "Remote", "type": "REMOTE", "salary": "$40/hr"},
    ]

    for data in jobs_data:
        Job.objects.create(
            title=data["title"],
            company=data["company"],
            location=data["location"],
            employment_type=data["type"],
            salary_range=data["salary"],
            description=f"Join our team at {data['company']} as a {data['title']}. We are looking for passionate individuals to help us lead the industry.",
            industry="Technology",
            hiring_manager=random.choice(profiles)
        )

    # 6. Create Events
    events_data = [
        {"title": "Annual Alumni Gala 2026", "location": "Grand Ballroom, Main Campus", "category": "REUNION"},
        {"title": "Web3 & Blockchain Workshop", "location": "Online (Zoom)", "category": "WEBINAR"},
        {"title": "Architecture Portfolio Review", "location": "Hall of Arts", "category": "NETWORKING"},
        {"title": "Tech Summit: Spring 2026", "location": "Student Activity Center", "category": "SUMMIT"},
    ]

    for i, data in enumerate(events_data):
        target_date = timezone.now() + timedelta(days=(i+1)*7)
        Event.objects.create(
            title=data["title"],
            description=f"A great opportunity to engage in {data['category'].lower()} and network with peers.",
            date=target_date.date(),
            time=target_date.time(),
            location=data["location"],
            category=data["category"],
            image_url=f"https://picsum.photos/seed/event{i}/800/400"
        )

    print("Data seeding completed successfully!")

if __name__ == "__main__":
    seed()
