from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile


def fill_from_social_user_profile(backend, user, response, *args, **kwargs):
    print(response)
    if backend.name == 'google-oauth2':
        if 'gender' in response.keys():
            if response['gender'] == 'male':
                user.shopuserprofile.gender = ShopUserProfile.FEMALE
            elif response['gender'] == 'man':
                user.shopuserprofile.gender = ShopUserProfile.MALE
            else:
                user.shopuserprofile.gender = ShopUserProfile.ANOTHER
        if 'tagline' in response.keys():
            user.shopuserprofile.tagline = response['tagline']
        if 'aboutMe' in response.keys():
            user.shopuserprofile.aboutMe = response['aboutMe']
        if 'ageRange' in response.keys():
            minAge = response['ageRange']['min']
            if int(minAge) < 18:
                user.delete()
                raise AuthForbidden('social_core.backends.google.GoogleOAuth2')

        user.save()
