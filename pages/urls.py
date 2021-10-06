from django.urls import path
from .views import (HomePageView, 
	AboutPageView, 
	TeamPageView, 
	MacroPageView,
	PortfolioPageView,
	DepartmentsPageView,
	GetInvolvedPageView)

urlpatterns = [
	path('getinvolved/', GetInvolvedPageView.as_view(), name='getinvolved'),
	path('departments/', DepartmentsPageView.as_view(), name='departments'),
	path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
	path('macro/', MacroPageView.as_view(), name='macro'),
	path('team/', TeamPageView.as_view(), name='team'),
	path('about/', AboutPageView.as_view(), name='about'),
	path('', HomePageView.as_view(), name='home'),
]