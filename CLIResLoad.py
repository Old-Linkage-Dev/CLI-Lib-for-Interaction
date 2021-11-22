
# -*- coding: UTF-8 -*-

# 实现资源管理的相关类；

# 应当实现一个类用于实现资源加载，负责将资源标识识别为文件，将文件内容转变为元素类加载；
# 实现内容如，一个类，通过配置可和特定的文件系统（或数据库系统）形成关系，
# 提供接口输入资源标识符，返回Elem类的实例，或一组Elem类的实例组成的Res类的实例；

from . import CLIRes;
from . import CLIElem;

from ..OLDLog import logger;
from .CONSTS import *;

__all__ = [
    "ResLoad",
];



class ResLoad:
    """
    A resload is a class to load a page, a scene, an UI, etc;
    """
    def __init__(self) -> None:
        """
        Init to the resload;
        """
        return;
    
    def getres(self, res:str) -> CLIRes.Res:
        """
        Called to get a res specified by the res string;
        res: a string specifying the res;
        return a res;
        """
        return None;
    
    def getelem(self, res:str) -> CLIElem.Elem:
        """
        Called to get an elem specified by the res string;
        res: a string specifying the elem;
        return an elem;
        """
        return None;
