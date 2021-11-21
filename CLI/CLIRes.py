
# -*- coding: UTF-8 -*-

# 实现资源的相关类；

# 模块内应当有一个Res的基类，和若干可能的此类的派生，用于作为资源，
# 单个Res是一个独立的界面单位，应当可以在加载后通过其定义的接口与其他系统交互，并可对其内的内容完成自决；
# 实现内容如，管理当前Res的若干Elem，对外接入接口并提供给Elem作为回调，或在内部实现可内部完成的回调；

from .CLILog import logger;
from .CONSTS import *;

class Res:
    """
    A res is a page, a scene, an UI, etc;
    """
    
    def __init__(self, h:int, w:int) -> None:
        """
        Init to the res;
        h, w: window / display size;
        """
        self._elems = {};
        self._focus = -1;
        self._winsize = (h, w);
        return;
    
    @property
    def elems(self) -> dict:
        """
        The contained elems of this res;
        """
        return self._elems;
    
    @property
    def focus(self) -> int:
        """
        The focus of this res;
        """
        return self._focus;
    
    @property
    def winsize(self) -> tuple:
        """
        The window / display size of this res;
        """
        return self._winsize;
    
    @winsize.setter
    def winsize(self, val:tuple) -> None:
        self._winsize = val;
        return;
    
    def update(self, input:str) -> None:
        """
        Called to transmit the control flow to the res;
        input: control flow to the res;
        return none;
        """
        return;
    
    def draw(self) -> str:
        """
        Called to get the draw flow of the res;
        return the string to draw the res;
        """
        return '';
