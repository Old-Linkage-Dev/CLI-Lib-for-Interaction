
# -*- coding: UTF-8 -*-

# 实现界面元素的相关类；

# 模块内应当有一个Elem的基类，和若干基于此的派生，用于实现界面元素的处理，
# 每个类应当实现对输入数据流的接收、响应、自我更新，提供绘制接口，返回用于绘制的字符串流；
# 实现内容如，一个响应键入操作，记录键入内容，提供绘制的文本框；



from ..OLDLog import logger;
from .CONSTS import *;
from .CLIDraw import *;



__all__ = [
    "Elem",
    "ElemText",
];



class Elem:
    """
    An elem is an element on a page, a scene, an UI, etc;
    """

    def __init__(self, y: int = 1, x: int = 1, h: int = 0, w: int = 0, value: any = None) -> None:
        """
        Init to the elem;
        y, x: relative coordinate of this elem;
        h, w: size of this elem;
        """
        self._rect = (y, x, h, w);
        self._val = value;
        return;
    
    @property
    def rect(self) -> tuple:
        """
        The relative coordinate of this elem;
        """
        return self._rect;
    
    @rect.setter
    def rect(self, val:tuple) -> None:
        self._rect = val;
        return;

    @property
    def y(self) -> tuple:
        """
        The relative coordinate y of this elem;
        """
        return self._rect[0];
    
    @y.setter
    def y(self, val:int) -> None:
        self._rect = (val, self._rect[1], self._rect[2], self._rect[3]);
        return;
    
    @property
    def x(self) -> tuple:
        """
        The relative coordinate x of this elem;
        """
        return self._rect[1];
    
    @x.setter
    def x(self, val:int) -> None:
        self._rect = (self._rect[0], val, self._rect[2], self._rect[3]);
        return;
    
    @property
    def h(self) -> tuple:
        """
        The height of this elem;
        """
        return self._rect[2];
    
    @h.setter
    def h(self, val:int) -> None:
        self._rect = (self._rect[0], self._rect[1], val, self._rect[3]);
        return;
    
    @property
    def w(self) -> tuple:
        """
        The width of this elem;
        """
        return self._rect[3];
    
    @w.setter
    def w(self, val:int) -> None:
        self._rect = (self._rect[0], self._rect[1], self._rect[2], val);
        return;
    
    @property
    def y0(self) -> int:
        """
        The relative coordinate x0 of this elem;
        """
        return self._rect[0];
    
    @y0.setter
    def y0(self, val:int) -> None:
        self._rect = (val, self._rect[1], self._rect[2], self._rect[3]);
        return;

    @property
    def x0(self) -> int:
        """
        The relative coordinate x0 of this elem;
        """
        return self._rect[1];
    
    @x0.setter
    def x0(self, val:int) -> None:
        self._rect = (self._rect[0], val, self._rect[2], self._rect[3]);
        return;

    @property
    def y1(self) -> tuple:
        """
        The relative coordinate y1 of this elem;
        """
        return self._rect[0] + self._rect[2] - 1;
    
    @y1.setter
    def y1(self, val:int) -> None:
        if val >= self._rect[0]:
            self._rect = (self._rect[0], self._rect[1], val - self._rect[0] + 1, self._rect[3]);
        return;
    
    @property
    def x1(self) -> tuple:
        """
        The relative coordinate x1 of this elem;
        """
        return self._rect[1] + self._rect[3] - 1;
    
    @x1.setter
    def x1(self, val:int) -> None:
        if val >= self._rect[1]:
            self._rect = (self._rect[0], self._rect[1], self._rect[2], val - self._rect[1] + 1);
        return;
    
    @property
    def value(self) -> any:
        """
        The value of this elem;
        """
        return self._val;
    
    @value.setter
    def value(self, val:any) -> None:
        self._val = val;
        return;
    
    def on_act(self, sender) -> None:
        """
        Callback to the action of the elem;
        """
        return;
    
    def update(self, input:str) -> None:
        """
        Called to transmit the control flow to the elem;
        input: control flow to the elem;
        return none;
        """
        return;
    
    def draw(self, y:int, x:int, h:int, w:int, f:bool) -> str:
        """
        Called to get the draw flow of the elem;
        y, x: absolute coordinate to draw of this elem;
        h, w: boundary to draw of this elem;
        f: if this elem is focused;
        return the string to draw the elem;
        """
        return '';



class BSElem(Elem):

    def __init__(self, y: int = 1, x: int = 1, h: int = 0, w: int = 0, value: any = None, boxstyle: str = '', colorstyle: dict = STYLE_CLASSIC) -> None:
        self._Elem = super();
        self._Elem.__init__(y = y, x = x, h = h, w = w, value = value);
        self.rect = self._Elem.rect;
        self.y = self._Elem.y;
        self.x = self._Elem.x;
        self.h = self._Elem.h;
        self.w = self._Elem.w;
        self.y0 = self._Elem.y0;
        self.x0 = self._Elem.x0;
        self.y1 = self._Elem.y1;
        self.x1 = self._Elem.x1;
        self.value = self._Elem.value;
        self._rect = (y, x, h, w);
        self._val = value;
        self._boxstyle = boxstyle;
        self._colstyle = colorstyle;
    
    @property
    def boxstyle(self) -> str:
        """
        The box style of this elem;
        """
        return self._boxstyle;
    
    @boxstyle.setter
    def boxstyle(self, val:str) -> None:
        if val in ('-', '=', ' ', ''):
            self._boxstyle = val;
        self._update_drawbox();
        return;
    
    @property
    def colorstyle(self) -> dict:
        """
        The color style of this elem;
        """
        return self._colstyle;
    
    @colorstyle.setter
    def colorstyle(self, val:dict) -> None:
        self._colstyle = val;
        return;



class ElemLabel(Elem):
    
    def __init__(self, y: int = 1, x: int = 1, h: int = 1, w: int = 0, value: str = '', align: str = 'l', autoscale: bool = False, colorstyle: dict = STYLE_CLASSIC) -> None:
        self._super = super();
        self._super.__init__(y = y, x = x, h = 1, w = w, value = value);
        self.rect = self._super.rect;
        self.y = self._super.y;
        self.x = self._super.x;
        self.h = self._super.h;
        self.w = self._super.w;
        self.y0 = self._super.y0;
        self.x0 = self._super.x0;
        self.y1 = self._super.y1;
        self.x1 = self._super.x1;
        self._rect = (y, x, 1, w);
        self._val = value;
        self._autoscale = autoscale;
        self._style = colorstyle;
        if align in ('l', 'c', 'r'):
            self._align = align;
        else:
            self._align = 'l';
        self._drawraw = '';
        self._update_drawraw();
    
    def _update_drawraw(self):
        _s, _ = str_cut_return(self._val);
        if self._autoscale:
            self._rect = (self._rect[0], self._rect[1], 1, str_width(_s));
            self._drawraw = _s;
        elif self._align == 'l':
            self._drawraw = str_trim_al(_s, self.w);
        elif self._align == 'r':
            self._drawraw = str_trim_ar(_s, self.w);
        elif self._align == 'c':
            self._drawraw = str_trim_ac(_s, self.w);
        else:
            self._drawraw = '';
    
    @property
    def value(self) -> str:
        """
        The string of this elem;
        """
        return self._val;
    
    @value.setter
    def value(self, val:str) -> None:
        self._val = val;
        self._update_drawraw();
        return;
    
    @property
    def align(self) -> str:
        """
        The alignment of the string of this elem;
        """
        return self._align;
    
    @align.setter
    def align(self, val:str) -> None:
        if val in ('l', 'c', 'r'):
            self._align = val;
        self._update_drawraw();
        return;
    
    @property
    def autoscale(self) -> bool:
        return self._autoscale;
    
    @autoscale.setter
    def autoscale(self, val:bool) -> None:
        self._autoscale = val;
        self._update_drawraw();
        return;

    @property
    def colorstyle(self) -> dict:
        return self._style;
    
    @colorstyle.setter
    def colorstyle(self, val:dict) -> None:
        self._style = val;
        return;

    def draw(self, y:int = 1, x:int = 1, h:int = 0, w:int = 0, f:bool = False) -> str:
        if (
            (y + h - 1 < self.y) or
            (y > self.y + self.h - 1) or
            (x + w - 1 < self.x) or
            (x > self.x + self.w - 1)
        ):
            return '';
        else:
            _pl = 0 if (x <= self.x) else (x - self.x);
            _pr = self.w if (x + w >= self.x + self.w) else (x + w -self.x);
            _x = (self.x - x + 1) if (x <= self.x) else 1;
            _y = (self.y - y + 1) if (y <= self.y) else 1;
            _s = str_trim_at(self._drawraw, _pl, _pr);
            _style = self._style["FOCUSED"] if f else self._style["NONACT"];
            return putstr(_y, _x, _s, *_style);
