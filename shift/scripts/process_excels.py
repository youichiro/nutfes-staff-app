"""Memo: 同じディレクトリにシフトのxlsxファイルを配置する"""
import os
import openpyxl
from tqdm import tqdm
from shift.scripts.const import row_to_time_str
from shift.models import Shift


def get_value_list(tuple_2d):
    return [[cell.value for cell in row] for row in tuple_2d]


def save(user, day, weather, row, task):
    user = user.replace(' ', '')
    task = task.replace(' ', '').replace('\n', '') if task else None
    time_str = row_to_time_str[row]
    shift, is_created = Shift.objects.get_or_create(user=user, day=day, weather=weather)
    if shift.__getattribute__(time_str):
        return
    shift.__setattr__(time_str, task)
    shift.save()


def register(sheet, day, weather):
    print('Saving: {}_{}_shift'.format(day, weather))

    # 列と名前の対応表の作成
    col_to_name = {}
    name_cells = sheet['B3:EA3'][0]
    for cell in name_cells:
        name = cell.value
        col = cell.col_idx
        col_to_name[col] = name

    # 結合セルのシフト登録
    merged_cells = sheet.merged_cells.ranges
    for merged_cell in tqdm(merged_cells):
        cell_range = merged_cell.ref
        cells = sheet[cell_range]
        task = get_value_list(cells)[0][0]
        for cell in cells:
            cell = cell[0]
            row = cell.row
            col = cell.col_idx

            # シフト範囲外は除く
            if row not in row_to_time_str.keys():
                continue
            if col not in col_to_name.keys():
                continue

            user = col_to_name[col]
            save(user, day, weather, row, task)

    # 結合セル以外のシフト登録
    all_cells = sheet['B4:EA38']
    for row_cells in tqdm(all_cells):
        for cell in row_cells:
            row = cell.row
            col = cell.col_idx
            user = col_to_name[col]
            task = cell.value
            save(user, day, weather, row, task)


def main():
    # Workbooks
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    first_shift_file = os.path.join(current_dir, 'scripts/first_shift.xlsx')
    second_shift_file = os.path.join(current_dir, 'scripts/second_shift.xlsx')
    first_wb = openpyxl.load_workbook(first_shift_file)
    second_wb = openpyxl.load_workbook(second_shift_file)

    # Worksheets
    first_sun_sheet = first_wb['晴']
    first_rain_sheet = first_wb['雨']
    second_sun_sheet = second_wb['晴']
    second_rain_sheet = second_wb['雨']

    # Registration
    register(first_sun_sheet, day='1日目', weather='晴')
    register(first_rain_sheet, day='1日目', weather='雨')
    register(second_sun_sheet, day='2日目', weather='晴')
    register(second_rain_sheet, day='2日目', weather='雨')

    print('Success saving all.')
