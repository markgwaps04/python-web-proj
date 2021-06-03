import os
import uuid
import xlrd
import random
import string
import secrets

def file_should_excel(value):
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.xlsx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def path_unique_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('personIds', filename)


def excel_algo(selected_file):

    wb = xlrd.open_workbook(file_contents=selected_file.read(), formatting_info=True)
    ws = wb.sheet_by_name("Sheet2")
    font_list = wb.font_list

    values = {}
    current_key = None
    keyToKey = False

    for row in range(1, ws.nrows):

        items = {}
        items_active = False
        items_current_key = None
        items_index = 0

        for col in range(1, ws.ncols):
            cell = ws.cell(row, col)

            xfx = ws.cell_xf_index(row, col)
            xf = wb.xf_list[xfx]
            font = font_list[xf.font_index]
            bgx = xf.background.pattern_colour_index
            pattern_colour = wb.colour_map[bgx]

            if cell.value:

                if font.underlined == 1 \
                        and current_key \
                        and (len(values[current_key]['items']) <= 0 or keyToKey):
                    keyToKey = True
                    values[current_key]["items"].append({
                        cell.value: {
                            "sub_key": True,
                            "items": []
                        }
                    })
                    continue

                    pass

                if font.underlined == 1 and keyToKey == False:
                    values[cell.value] = {
                        "sub_key": False,
                        "items": [],
                    }
                    current_key = cell.value
                    continue
                    pass

                # bgx = 50 GREEN (first green item)
                if bgx == 50 and items_active != True:
                    items[cell.value] = {
                        "weekly": None,
                        "bi-weekly": None,
                        "monthly": None,
                        "yearly": None,
                        "others": [],
                        "is_invalid": False,
                        "code" : ''.join(secrets.choice(string.ascii_lowercase) for x in range(10))
                    }
                    items_active = True
                    items_current_key = cell.value
                    continue
                    pass

                if items_active:

                    items[items_current_key]["is_invalid"] = False

                    # bgx = 50 GREEN (after first green item)
                    if bgx == 50:
                        items[items_current_key]["is_invalid"] = True
                        pass

                    if (len(items[items_current_key].keys()) - 1) > items_index:
                        current_item_type = tuple(items[items_current_key].keys())[items_index]
                        items[items_current_key][current_item_type] = cell.value
                        items_index += 1
                        continue
                        pass

                    items[items_current_key]["others"].append(cell.value)
                    items_index += 1
                    continue

                    pass

                items_active = False

                pass;

            pass;

        # Adding of items to the keys

        if items_current_key and items[items_current_key]["is_invalid"]:
            keyToKey = False
            continue
            pass;

        if len(values) > 0 and not keyToKey and len(items) > 0:
            current_value = tuple(values.keys())[-1]
            values[current_value]['items'].append(items)
            pass

        elif len(values) > 0 and keyToKey and len(items) > 0:
            current_value = tuple(values.keys())[-1]
            current_value_items = values[current_value]['items']

            current_val_item = tuple(current_value_items)[-1]
            current_val_item_key = tuple(current_val_item.keys())[-1]
            current_val_item[current_val_item_key]['items'].append(items)
        continue

        pass

    return values
