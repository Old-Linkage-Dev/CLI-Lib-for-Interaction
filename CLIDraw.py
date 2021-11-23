
# -*- coding: UTF-8 -*-

# 实现绘制的相关功能函数；

# 模块内的接口应当是，提供各种具象的绘制要求，返回用于绘制的字符串流；
# 实现内容如，给定一个绘制内容、字体信息、绘制位置、绘制范围，返回一个在指定范围内、指定位置进行绘制的字符串；
# 绘制应当采用CSI转义串进行光标、字体等的处理；

import math;

from .CONSTS import *;



__all__ = [
    "chr_width",
    "str_rev",
    "str_width",
    "str_cut_width",
    "str_cut_return",
    "str_split_width",
    "str_split_return",
    "str_trim_at",
    "str_trim_al",
    "str_trim_ar",
    "str_trim_ac",
    "putstr",
    "putstrs",
    "STYLE_CLASSIC",
    "STYLE_CLASSIC_LIGHT",
    "STYLE_BLACKWHITE",
];

def chr_width(c):
    if c == CHR_SO or c == CHR_SI:
        return 0
    for _u, _w in WIDTH_CHR:
        if ord(c) <= _u:
            return _w;
    return 1;

def str_rev(s):
    return s[::-1];

def str_width(s):
    _w = 0;
    for _c in s:
        _w += chr_width(_c);
    return _w;

def str_cut_width(s, w):
    _sw = 0;
    for _i in range(len(s)):
        _w = chr_width(s[_i]);
        if _sw + _w > w:
            return s[:_i], s[_i:];
    return s, '';

def str_cut_return(s):
    for _i in range(len(s)):
        if s[_i : _i+2] == CHR_CRLF:
            return s[:_i], s[_i+2:];
        elif s[_i : _i+2] == CHR_CRNUL:
            return s[:_i], s[_i+2:];
        elif s[_i : _i+1] == CHR_CR:
            return s[:_i], s[_i+1:];
        elif s[_i : _i+1] == CHR_LF:
            return s[:_i], s[_i+1:];
    return s, '';

def str_split_width(s, w):
    _splt = [];
    while s:
        _s, s = str_cut_width(s, w);
        _splt.append(_s);
    return _splt;

def str_split_return(s):
    _splt = [];
    while s:
        _s, s = str_cut_return(s);
        _splt.append(_s);
    return _splt;

def str_trim_at(s, pl, pr):
    if pl < pr:
        _w = 0;
        _i = 0;
        _i1 = 0;
        _i2 = 0;
        while _i < len(s) and _w < pl:
            _w += chr_width(s[_i]);
            _i += 1;
        _el = _w - pl;
        _i1 = _i;
        _er = 0;
        while _i < len(s) and _w < pr:
            _er = pr - _w;
            _w += chr_width(s[_i]);
            _i += 1;
        if _w == pr:
            _er = 0;
        _i2 = _i;
        _s = ' ' * _el + s[_i1 : _i2] + ' ' * _er;
        return _s;
    else:
        return '';

def str_trim_al(s, w):
    if str_width(s) <= w:
        _e = w - str_width(s);
        return s + ' ' * _e;
    else:
        s, _ = str_cut_width(s, w);
        _e = w - str_width(s);
        return s + ' ' * _e;

def str_trim_ar(s, w):
    if str_width(s) <= w:
        _e = w - str_width(s);
        return ' ' * _e + s;
    else:
        s, _ = str_cut_width(str_rev(s), w);
        _e = w - str_width(s);
        return ' ' * _e + str_rev(s);

def str_trim_ac(s, w):
    if str_width(s) <= w:
        _e = w - str_width(s);
        _el = round(_e / 2);
        _er = _e - _el;
        return ' ' * _el + s + ' ' * _er;
    else:
        _xl = round((str_width(s) - w) / 2);
        _, s = str_cut_width(s, _xl);
        s, _ = str_cut_width(s, w);
        _e = w - str_width(s);
        return s + ' ' * _e;

def putstr(y, x, s ,*args):
    _s = CHRf_CSI_SGR(0, *args) + CHRf_CSI_CUP(y, x) + s;
    return _s;

def putstrs(y, x, ss, *args):
    _s = CHRf_CSI_SGR(0, *args);
    for _i in range(len(ss)):
        _s += CHRf_CSI_CUP(y + _i, x) + ss[_i];
    return _s;

STYLE_CLASSIC = {
    "NORMAL"    : [T_BBLACK, T_WHITE],
    "NONACT"    : [T_BBLUE, T_WHITE],
    "INTERACT"  : [T_BBLUE, T_CYAN],
    "FOCUSED"   : [T_BCYAN, T_BLUE],
}

STYLE_CLASSIC_LIGHT = {
    "NORMAL"    : [T_BLBLACK, T_LWHITE],
    "NONACT"    : [T_BLBLUE, T_LWHITE],
    "INTERACT"  : [T_BLBLUE, T_LCYAN],
    "FOCUSED"   : [T_BLCYAN, T_LBLUE],
}

STYLE_BLACKWHITE = {
    "NORMAL"    : [T_BBLACK, T_WHITE],
    "NONACT"    : [T_BLBLACK, T_WHITE],
    "INTERACT"  : [T_BLBLACK, T_LWHITE],
    "FOCUSED"   : [T_BWHITE, T_LBLACK],
}
