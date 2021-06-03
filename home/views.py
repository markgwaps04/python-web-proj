from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from app.misc import excel_algo
import json




# Create your views here.

class GenerateView(View):

    @method_decorator(login_required)
    def post(self, request):
        selected_file = request.FILES.get("file")
        generate = excel_algo(selected_file)
        request.session['generated_data'] = generate
        return render(request, "upload_review.html", {
            "data" : generate
        })
        pass

    pass


class SaveView(View):

    def post(self, request):
        if 'generated_data' in request.session:

            return HttpResponse(json.dumps({
                "status" : "Invalid Action",
                "status_code" : 309
            }), content_type='application/json', status=404)

            pass

        return HttpResponse(json.dumps({
                "status" : "Invalid Action",
                "status_code" : 309
            }), content_type='application/json', status=404)

        pass

    pass
