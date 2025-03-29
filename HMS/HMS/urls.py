# """
# URL configuration for HMS project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('Doctor.urls')),
# ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


def first_non_repeated_char(s):
    for i in range(len(s)):  # Iterate through each character
        temp = s[i]
        for j in range(i+1, len(s)):  # Compare with every other character
            if temp == s[j]:  # If a duplicate is found, break
                break
            else:  # This executes if no break occurred (unique character)
                print(s[j])
    return None  # Return None if no unique character exists
# print(first_non_repeated_char(s))

s = "SWISS" 
for i in range(len(s)): 
    temp = s[i]
    for j in range(i+1, len(s)): 
        if temp == s[j]: 
            break
        else: 
            u