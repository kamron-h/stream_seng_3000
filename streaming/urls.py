"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from streaming import views


urlpatterns = [
    path('', views.home, name='stream_dash'),
    path('stream/', views.stream_dash, name='stream_dash'),
    path('index/', views.api_index, name='api_index'),
    path('api/', include('streaming.urls_api')),
]
