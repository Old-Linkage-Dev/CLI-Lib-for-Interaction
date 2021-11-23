
# -*- coding: UTF-8 -*-

# 实现绘制的相关功能函数；

# 模块内的接口应当是，提供各种具象的绘制要求，返回用于绘制的字符串流；
# 实现内容如，给定一个绘制内容、字体信息、绘制位置、绘制范围，返回一个在指定范围内、指定位置进行绘制的字符串；
# 绘制应当采用CSI转义串进行光标、字体等的处理；

__all__ = [
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

def str_al(s, w):
    if str_width(s) <= w:
        _e = w - str_width(s);
        return s + ' ' * _e;
    else:
        s, _ = str_cut_width(s, w);
        _e = w - str_width(s);
        return s + ' ' * _e;

def str_ar(s, w):
    if str_width(s) <= w:
        _e = w - str_width(s);
        return ' ' * _e + s;
    else:
        s, _ = str_cut_width(str_rev(s), w);
        _e = w - str_width(s);
        return ' ' * _e + str_rev(s);

def str_ac(s, w):
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

def get_style(style:dict):
    class _Style:
        @property
        def NRM(self):
            _b = style["B_NRM"];
            _f = style["F_NRM"];
            return CHRf_CSI_SGR(0, *_b, *_f);
        @property
        def OBJ(self):
            _b = style["B_OBJ"] if "B_OBJ" in style else style["B_NRM"];
            _f = style["F_OBJ"] if "F_OBJ" in style else style["F_NRM"];
            return CHRf_CSI_SGR(0, *_b, *_f);
        @property
        def OBJSIDE(self):
            _b = style["B_OBS"] if "B_OBS" in style else style["B_OBJ"] if "B_OBJ" in style else style["B_NRM"];
            _f = style["F_OBS"] if "F_OBS" in style else style["F_NRM"];
            return CHRf_CSI_SGR(0, *_b, *_f);
        @property
        def ACT(self):
            _b = style["B_ACT"] if "B_ACT" in style else style["B_NRM"];
            _f = style["F_ACT"] if "F_ACT" in style else style["F_NRM"];
            return CHRf_CSI_SGR(0, *_b, *_f);
        @property
        def ACTSIDE(self):
            _b = style["B_ACS"] if "B_ACS" in style else style["B_ACT"] if "B_ACT" in style else style["B_NRM"];
            _f = style["F_ACS"] if "F_ACS" in style else style["F_NRM"];
            return CHRf_CSI_SGR(0, *_b, *_f);
        @property
        def FOC(self):
            _b = style["B_FOC"] if "B_FOC" in style else style["B_NRM"];
            _f = style["F_FOC"] if "F_FOC" in style else style["F_NRM"];
            return CHRf_CSI_SGR(0, *_b, *_f);
        @property
        def FOCSIDE(self):
            _b = style["B_FOS"] if "B_FOS" in style else style["B_FOC"] if "B_FOC" in style else style["B_NRM"];
            _f = style["F_FOS"] if "F_FOS" in style else style["F_NRM"];
            return CHRf_CSI_SGR(0, *_b, *_f);
    return _Style();

STYLE_CLASSIC = {
    "B_NRM" : [T_BBLACK, T_BLBLACK],
    "F_NRM" : [T_WHITE, T_LWHITE],
    "B_OBJ" : [T_BBLACK, T_BLBLACK],
    "F_OBJ" : [T_CYAN, T_LCYAN],
    "B_ACT" : [T_BBLUE, T_BLBLUE],
    "F_ACT" : [T_CYAN, T_LCYAN],
    "B_FOC" : [T_BCYAN, T_BLCYAN],
    "F_FOC" : [T_BLACK, T_LBLACK],
    "F_FOS" : [T_BLACK, T_LBLACK],
}
