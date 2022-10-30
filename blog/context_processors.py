from blog.models import Social


def social_profiles(request):
    return dict(social_links=Social.objects.all())
