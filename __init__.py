
# -*- coding: UTF-8 -*-

from . import CLICommandInterface;
from . import CLIGraphInterface;
from . import CLIRes;
from . import CLIElem;
from . import CLIResLoad;
from . import CLIDraw;

from .CLICommandInterface import *;
from .CLIGraphInterface import *;
from .CLIRes import *;
from .CLIElem import *;
from .CLIResLoad import *;
from .CLIDraw import *;

from ..OLDLog import logger;



__all__ = (
    [
        "CLICommandInterface",
        "CLIGraphInterface",
        "CLIRes",
        "CLIElem",
        "CLIResLoad",
        "CLIDraw",
        "logger",
    ] +
    CLICommandInterface.__all__ +
    CLIGraphInterface.__all__ +
    CLIRes.__all__ +
    CLIElem.__all__ +
    CLIResLoad.__all__ +
    CLIDraw.__all__
);

__author__ = "Tarcadia, Mundanity-fc";
__url__ = "https://github.com/Tarcadia/CLI-Lib-for-Interaction";
__copyright__ = "Copyright 2021";
__credits__ = ["Tarcadia", "Mundanity-fc"];
__license__ = "GNU GENERAL PUBLIC LICENSE VERSION 3";
__version__ = "ProtoType 1.0.0";

logger.info('OLD.CLI Loaded.');
logger.info('Locense: %s' % __license__);
logger.info('Version: %s' % __version__);
logger.info('Find on: %s' % __url__);
logger.info('%s (c) %s' % (__author__, __copyright__));