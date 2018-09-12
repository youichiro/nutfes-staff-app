from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


task_colors = {
    '休憩': ['#C0C0C0', 'white'],
    '待機系': ['#FF6600', 'white'],
    'ゲスト業務': ['#00FFFF', 'white'],
    'フレパ': ['#FF00FF', 'white'],
    '×': ['#808080', 'white'],
    '朝食': ['#FFFF33', '#0B3B39'],
    '夕食': ['#FFFF33', '#0B3B39'],
    'MT': ['#FFFF33', '#0B3B39'],
    '執行部MT': ['#FFFF33', '#0B3B39'],
    '指揮系': ['#FF9999', 'white'],
    '対応系': ['#00FF00', '#0B3B39'],
    'その他': ['#0000FF', 'white'],
}

name_colors = {
    '委員長': ['#FF00FF', 'white'],
    '副委員長': ['#FF00FF', 'white'],
    'ゲスト': ['#FF00FF', 'white'],
    '企画': ['#800080', 'white'],
    '渉外': ['#0000FF', 'white'],
    '財務': ['#FF9900', 'white'],
    '制作': ['#FFFF00', '#0B3B39'],
    '総務': ['#008000', 'white'],
}


@register.filter
@stringfilter
def task_color(task):
    if task[-2:] == '待機':
        return task_colors['待機系'][0]
    if task[-2:] == '対応':
        return task_colors['対応系'][0]
    if '指揮' in task:
        return task_colors['指揮系'][0]
    return task_colors.get(task, task_colors['その他'])[0]


@register.filter
@stringfilter
def task_font_color(task):
    if task[-2:] == '待機':
        return task_colors['待機系'][1]
    if task[-2:] == '対応':
        return task_colors['対応系'][1]
    if '指揮' in task:
        return task_colors['指揮系'][1]
    return task_colors.get(task, task_colors['その他'])[1]


@register.filter
@stringfilter
def name_color(name):
    return name_colors.get(name, name_colors['総務'])[0]


@register.filter
@stringfilter
def name_font_color(name):
    return name_colors.get(name, name_colors['総務'])[1]
