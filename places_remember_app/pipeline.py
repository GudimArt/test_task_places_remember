def get_profile_image(backend, response, user=None, *args, **kwargs):
    url = None
    if backend.name == 'vk-oauth2':
        url = response['photo']
    elif backend.name == 'google-oauth2':
        url = response['picture']
    if url:
        user.profile.avatar = url
        user.save()
