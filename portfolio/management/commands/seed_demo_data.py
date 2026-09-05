from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from portfolio.models import Profile, Skill, Project, SkillCategory


class Command(BaseCommand):
    help = "Creates a demo superuser, profile, sample skills and a sample project so the site isn't empty."

    def handle(self, *args, **options):
        # Demo superuser (username: admin / password: admin12345) — CHANGE THIS PASSWORD.
        if not User.objects.filter(username='admin').exists():
            user = User.objects.create_superuser('admin', 'admin@example.com', 'admin12345')
            self.stdout.write(self.style.SUCCESS("Created superuser 'admin' with password 'admin12345' — please change it!"))
        else:
            user = User.objects.get(username='admin')

        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults=dict(
                full_name="Your Name",
                tagline="Python & Django Developer",
                bio="I build clean, reliable web applications with Django and Python. "
                    "Update this bio from the Dashboard or Admin panel.",
                email="you@example.com",
                location="Bengaluru, India",
            )
        )
        if created:
            self.stdout.write(self.style.SUCCESS("Created demo profile."))

        demo_skills = [
            ("Python", SkillCategory.LANGUAGE, 90),
            ("Django", SkillCategory.FRAMEWORK, 85),
            ("JavaScript", SkillCategory.LANGUAGE, 70),
            ("PostgreSQL", SkillCategory.DATABASE, 75),
            ("Git", SkillCategory.TOOL, 80),
            ("Problem Solving", SkillCategory.SOFT, 90),
        ]
        for name, cat, prof in demo_skills:
            Skill.objects.get_or_create(name=name, defaults=dict(category=cat, proficiency=prof))

        if not Project.objects.exists():
            project = Project.objects.create(
                title="Sample Django Project",
                short_description="A demo project so you can see how project cards look.",
                description="Replace this with a real project! Edit or delete it from the Dashboard "
                             "or Django Admin, then add your own projects.",
                featured=True,
            )
            project.technologies.set(Skill.objects.filter(name__in=["Python", "Django"]))
            self.stdout.write(self.style.SUCCESS("Created a sample project."))

        self.stdout.write(self.style.SUCCESS("Demo data seeding complete."))
