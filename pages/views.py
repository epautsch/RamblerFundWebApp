from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = 'home.html'

class AboutPageView(TemplateView):
	template_name = 'about.html'

class TeamPageView(TemplateView):
	template_name = 'team.html'

class MacroPageView(TemplateView):
	template_name = 'macro.html'

class PortfolioPageView(TemplateView):
	template_name = 'portfolio.html'

class DepartmentsPageView(TemplateView):
	template_name = 'departments.html'

class GetInvolvedPageView(TemplateView):
	template_name = 'getinvolved.html'