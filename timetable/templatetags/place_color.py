from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


place_colors_sun = {
    'メインステージ': ['#FF0000', 'white'],
    'サブステージ': ['#FF0000', 'white'],
    'A講義室': ['#FF0000', 'white'],
    '体育館': ['#FF9900', 'white'],
    'D講義室': ['#FF9900', 'white'],
    'マルチメディア': ['#FFFF00', '#0B3B39'],
    'F講義室': ['#FFFF00', '#0B3B39'],
}

place_colors_rain = {
    '体育館': ['#0000FF', 'white'],
    'D講義室': ['#0000FF', 'white'],
    'マルチメディア': ['#00FFFF', '#0B3B39'],
    'F講義室': ['#00FFFF', '#0B3B39'],
    '武道館': ['#00FFFF', '#0B3B39'],
    'A講義室': ['#800080', 'white'],
    '103講義室': ['#800080', 'white'],
}


back_colors = {
    '晴': '#F3E2A9',
    '雨': '#CEECF5',
}


@register.filter
@stringfilter
def place_color_sun(place):
    return place_colors_sun[place][0]


@register.filter
@stringfilter
def place_color_rain(place):
    return place_colors_rain[place][0]


@register.filter
@stringfilter
def place_font_color_sun(place):
    return place_colors_sun[place][1]


@register.filter
@stringfilter
def place_font_color_rain(place):
    return place_colors_rain[place][1]


@register.filter
@stringfilter
def back_color(weather):
    return back_colors[weather]
