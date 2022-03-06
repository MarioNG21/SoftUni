from workshop1.petstagram.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]


