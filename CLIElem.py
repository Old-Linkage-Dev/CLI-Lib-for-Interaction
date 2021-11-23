
# -*- coding: UTF-8 -*-

# 实现界面元素的相关类；

# 模块内应当有一个Elem的基类，和若干基于此的派生，用于实现界面元素的处理，
# 每个类应当实现对输入数据流的接收、响应、自我更新，提供绘制接口，返回用于绘制的字符串流；
# 实现内容如，一个响应键入操作，记录键入内容，提供绘制的文本框；



from ..OLDLog import logger
from .CONSTS import *;
from .CLIDraw import *;



__all__ = [
    "Elem",
];



class Elem:
    """
    An elem is an element on a page, a scene, an UI, etc;
    """

    def __init__(self, y:int = 0, x:int = 0, h:int = 0, w:int = 0, value:any = None) -> None:
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
