from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from openpyxl import load_workbook
from openpyxl.styles.colors import RGB
from openpyxl.styles.colors import Color, COLOR_INDEX
from openpyxl.formula import Tokenizer
import xlrd
from styleframe import StyleFrame, utils


# Create your views here.

class UploadView(View):

    @method_decorator(login_required)
    def post(self, request):
        selected_file = request.FILES.get("file")
        wb = xlrd.open_workbook(file_contents=selected_file.read(), formatting_info=True)
        ws = wb.sheet_by_name("Sheet2")
        for row in range(1, ws.nrows):
            print("================================")
            for col in range(1, ws.ncols):
                cell = ws.cell(row, col)
                if cell.value:
                    print(cell.value)
                    xfx = ws.cell_xf_index(row, col)
                    xf = wb.xf_list[xfx]
                    bgx = xf.background.pattern_colour_index
                    pattern_colour = wb.colour_map[bgx]
                    print("RGB " + str(pattern_colour))
                    print("INDEX " + str(bgx))
                    print("----------------------------")
                    pass;

                pass;
            pass

        return HttpResponse("Success 1")
        pass

    pass
