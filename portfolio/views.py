from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q

from .models import Profile, Skill, Project, Testimonial, ContactMessage
from .forms import ContactForm, ProjectForm, SkillForm, ProfileForm


def home(request):
    profile = None

    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()

    featured_projects = Project.objects.filter(featured=True)[:6]
    skills = Skill.objects.all()[:12]
    testimonials = Testimonial.objects.all()[:6]

    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'skills': skills,
        'testimonials': testimonials,
    }

    return render(request, 'portfolio/home.html', context)


def about(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    return render(request, 'portfolio/about.html', {'profile': profile, 'skills': skills})


def project_list(request):
    projects = Project.objects.all()
    query = request.GET.get('q')
    tech_filter = request.GET.get('tech')
    if query:
        projects = projects.filter(
            Q(title__icontains=query) | Q(short_description__icontains=query)
        )
    if tech_filter:
        projects = projects.filter(technologies__id=tech_filter)
    all_skills = Skill.objects.all()
    return render(request, 'portfolio/project_list.html', {
        'projects': projects.distinct(),
        'all_skills': all_skills,
        'query': query or '',
        'tech_filter': tech_filter or '',
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.exclude(pk=project.pk).filter(
        technologies__in=project.technologies.all()
    ).distinct()[:3]
    return render(request, 'portfolio/project_detail.html', {
        'project': project,
        'related_projects': related_projects,
    })


def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/skills.html', {'skills': skills})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            # Try to email the site owner; safe to fail silently in dev (console backend).
            try:
                send_mail(
                    subject=f"New portfolio contact: {contact_message.subject or 'No subject'}",
                    message=(
                        f"From: {contact_message.name} <{contact_message.email}>\n\n"
                        f"{contact_message.message}"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})


# ---------------------------------------------------------------------
# Dashboard views — these let the logged-in owner add/edit/delete
# Projects and Skills straight from the website (no admin panel needed).
# ---------------------------------------------------------------------

@login_required
def dashboard(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    messages_list = ContactMessage.objects.all()[:10]
    return render(request, 'portfolio/dashboard.html', {
        'projects': projects,
        'skills': skills,
        'messages_list': messages_list,
    })


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Project added successfully.")
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/project_form.html', {'form': form, 'title': 'Add Project'})


@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully.")
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/project_form.html', {'form': form, 'title': 'Edit Project'})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project deleted.")
        return redirect('dashboard')
    return render(request, 'portfolio/confirm_delete.html', {'object': project, 'type': 'project'})


@login_required
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill added successfully.")
            return redirect('dashboard')
    else:
        form = SkillForm()
    return render(request, 'portfolio/skill_form.html', {'form': form, 'title': 'Add Skill'})


@login_required
def skill_update(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill updated successfully.")
            return redirect('dashboard')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'portfolio/skill_form.html', {'form': form, 'title': 'Edit Skill'})


@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, "Skill deleted.")
        return redirect('dashboard')
    return render(request, 'portfolio/confirm_delete.html', {'object': skill, 'type': 'skill'})


@login_required
def profile_update(request):
    profile, _ = Profile.objects.get_or_create(
        user=request.user,
        defaults={'full_name': request.user.username, 'tagline': '', 'bio': '', 'email': request.user.email},
    )
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'portfolio/profile_form.html', {'form': form})
