from teachers.models import TeachersInfo

class AccountAuthBackend(object):
    def authenticate(self,username=None):
        try:
            user = TeachersInfo.objects.get(email=username)
            if user:
                return user
            else:
                return None
        except TeachersInfo.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return TeachersInfo.objects.get(pk=user_id)
        except TeachersInfo.DoesNotExist:
            return None
