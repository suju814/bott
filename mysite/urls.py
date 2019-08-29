
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from mysite.loginform import views 
from django.conf.urls.static import static

urlpatterns = [
	path('',views.home,name="home"),

	path('bot/',views.bot,name="bot"),
	path('dw',views.dw,name="dw"),
	path('trade',views.trade,name="trade"),
	path('deposit',views.deposit,name="deposit"),
	path('withdraw',views.withdraw,name="withdraw"),
	path('hexa',views.hexa,name="hexa"),
	path('chain',views.chain,name="chain"),
	path('pro',views.pro,name="pro"),
	path('signup',views.signup,name="signup"),
	path('^oauth/', include('social_django.urls', namespace='social')),
    path('accounts/',include('django.contrib.auth.urls')),
    
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
        )
    