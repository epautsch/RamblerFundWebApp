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

# import io
# from django.http import FileResponse
# from reportlab.pdfgen import canvas

# def some_view(request):
# 	buffer = io.BytesIO()
# 	p = canvas.Canvas(buffer)
# 	p.drawString(100, 100, "Hello world.")
# 	p.showPage()
# 	p.save()
# 	buffer.seek(0)
# 	return FileResponse(buffer, as_attachment=False, filename='hello.pdf')