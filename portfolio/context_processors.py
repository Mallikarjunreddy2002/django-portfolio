from .models import Profile


def profile_context(request):
    """Makes the site owner's profile available in every template as {{ site_profile }}."""
    profile = Profile.objects.first()
    return {'site_profile': profile}
