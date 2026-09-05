from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class Profile(models.Model):
    """The single 'owner' profile shown on the About/Home pages."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=150)
    tagline = models.CharField(max_length=200, help_text="e.g. 'Full Stack Python Developer'")
    bio = models.TextField(help_text="A short paragraph about yourself.")
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.full_name


class SkillCategory(models.TextChoices):
    LANGUAGE = 'LANG', 'Programming Language'
    FRAMEWORK = 'FRAME', 'Framework / Library'
    DATABASE = 'DB', 'Database'
    TOOL = 'TOOL', 'Tool / Platform'
    SOFT = 'SOFT', 'Soft Skill'
    OTHER = 'OTHER', 'Other'


class Skill(models.Model):
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=10, choices=SkillCategory.choices, default=SkillCategory.OTHER)
    proficiency = models.PositiveIntegerField(
        default=70,
        help_text="Proficiency percentage from 0 to 100, shown as a progress bar."
    )
    icon_class = models.CharField(
        max_length=60, blank=True,
        help_text="Optional Bootstrap Icons class, e.g. 'bi-filetype-py'."
    )
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers show first.")

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    short_description = models.CharField(max_length=250, help_text="Shown on the project cards.")
    description = models.TextField(help_text="Full description shown on the project detail page.")
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    technologies = models.ManyToManyField(Skill, blank=True, related_name='projects')
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    featured = models.BooleanField(default=False, help_text="Featured projects appear on the home page.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})


class Testimonial(models.Model):
    name = models.CharField(max_length=120)
    designation = models.CharField(max_length=120, blank=True)
    message = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Testimonial from {self.name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} <{self.email}> - {self.subject or 'No subject'}"
