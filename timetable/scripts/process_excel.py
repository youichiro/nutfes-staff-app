"""Memo: 同じディレクトリにシフトのxlsxファイルを配置する"""
import os
import openpyxl
from tqdm import tqdm
from timetable.scripts.const import row_to_time_attr
from timetable.models import Timetable


def get_value_list(tuple_2d):
    return [[cell.value for cell in row] for row in tuple_2d]


def save(day, weather, sheet_id, place, row, event):
    time_attr = row_to_time_attr[row]
    timetable, is_created = Timetable.objects.get_or_create(day=day, weather=weather, sheet_id=sheet_id, place=place)
    if timetable.__getattribute__(time_attr):
        return
    timetable.__setattr__(time_attr, event)
    timetable.save()


def register(sheet, end_column, day, weather, sheet_id):
    print('Saving {}{}_table'.format(day, weather))

    col_to_place = {}
    place_cells = sheet['B1:'+end_column+'1'][0]
    for cell in place_cells:
        place = cell.value
        col = cell.col_idx
        col_to_place[col] = place

    # 結合セルの登録
    merged_cells = sheet.merged_cells.ranges
    for merged_cell in tqdm(merged_cells):
        cell_range = merged_cell.ref
        cells = sheet[cell_range]
        event = get_value_list(cells)[0][0]
        for cell in cells:
            cell = cell[0]
            row = cell.row
            col = cell.col_idx

            # 範囲外は除く
            if row not in row_to_time_attr.keys():
                continue
            if col not in col_to_place.keys():
                continue

            place = col_to_place[col]
            save(day, weather, sheet_id, place, row, event)


def main():
    # files
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    timetable_file = os.path.join(current_dir, 'scripts/timetable.xlsx')

    # Workbooks
    timetable_wb = openpyxl.load_workbook(timetable_file)

    # Worksheets
    first_sun_sheet = timetable_wb['1日目晴']
    first_rain_sheet = timetable_wb['1日目雨']
    second_sun_sheet = timetable_wb['2日目晴']
    second_rain_sheet = timetable_wb['2日目雨']

    # Delete all
    Timetable.objects.all().delete()

    # Registration
    register(first_sun_sheet, end_column='G', day='1日目', weather='晴', sheet_id=1)
    register(first_rain_sheet, end_column='G', day='1日目', weather='雨', sheet_id=2)
    register(second_sun_sheet, end_column='G', day='2日目', weather='晴', sheet_id=3)
    register(second_rain_sheet, end_column='F', day='2日目', weather='雨', sheet_id=4)

    print('Success saving all.')
