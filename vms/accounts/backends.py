# from django.conf import settings
# from django.db.models import Q
# from django.contrib.auth.backends import ModelBackend
#
# UserModel = settings.AUTH_USER_MODEL
#
#
# class EmailBackend(object):
#     def authenticate(self, username=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(email=username)
#         except User.MultipleObjectsReturned:
#             user = User.objects.filter(email=username).order_by('id').first()
#         except User.DoesNotExist:
#             return None
#
#         if getattr(user, 'is_active') and user.check_password(password):
#             return user
#         return None
#
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
#
#
# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
#         except UserModel.DoesNotExist:
#             UserModel().set_password(password)
#             return
#         except UserModel.MultipleObjectsReturned:
#             user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by(
#                 'id').first()
#
#         if user.check_password(password) and self.user_can_authenticate(user):
#             return user
#
#
# class EmailBackend(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         try:
#             user = UserModel.objects.get(Q(email__iexact=email))
#         except UserModel.DoesNotExist:
#             UserModel().set_password(password)
#             return
#         except UserModel.MultipleObjectsReturned:
#             user = UserModel.objects.filter(Q(email__iexact=email)).order_by('id').first()
#
#         if user.check_password(password) and self.user_can_authenticate(user):
#             return user
