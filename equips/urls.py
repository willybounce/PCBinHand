from django.urls import path

from django.conf.urls import url

from . import views

app_name = 'equips'
urlpatterns = [
	url(r'signup/$',views.signup,name="signup"),
	path('logout',views.logout,name="logout"),
	path('',views.index,name='index'),
	path('about',views.about,name='about'),
	path('physics',views.physics,name='physics'),
	path('chemistry',views.chemistry,name='chemistry'),
	path('biology',views.biology,name='biology'),
	path('<int:equip_id>/',views.detail,name='detail'),
	path('<int:equip_id>/results/',views.results,name='results'),
	path('<int:equip_id>/add_in_wishlist/',views.add_in_wishlist,name='add_in_wishlist'),
]