from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ws_exercise.petstagram.views import photo_like, \
    HomeView, \
    DashboardView, CreatePetView, EditPetView, PetPhotoDetails, AddPhotoView, DeletePetView, EditPhotoView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', HomeView.as_view(), name='home'),

                  path('dashboard/', DashboardView.as_view(), name='dashboard'),
                  path('accounts/', include('ws_exercise.auth_accounts.urls')),

                  path('pet/add/', CreatePetView.as_view(), name='add pet'),
                  path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit pet'),
                  path('pet/delete/<int:pk>', DeletePetView.as_view(), name='delete pet'),

                  path('photo/add/', AddPhotoView.as_view(), name='add photo'),
                  path('photo/edit/<int:pk>/', EditPhotoView.as_view(), name='edit photo'),
                  path('photo/details/<int:pk>/', PetPhotoDetails.as_view(), name='photo_details'),
                  path('photo/likes/<int:pk>/', photo_like, name='like')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
