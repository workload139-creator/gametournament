from django.shortcuts import render

class MaintenanceMiddleware:

    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):

        maintenance=False

        if maintenance and not request.user.is_staff:

            return render(request,"maintenance.html")

        return self.get_response(request)
