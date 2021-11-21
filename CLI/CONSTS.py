
# -*- coding: UTF-8 -*-

# 记录常用常数的接口文件；



CHR_NONE            = '';
CHR_NUL             = '\x00';
CHR_SOH             = '\x01';
CHR_STX             = '\x02';
CHR_ETX             = '\x03';
CHR_EOT             = '\x04';
CHR_ENQ             = '\x05';
CHR_ACK             = '\x06';
CHR_BEL             = '\x07';
CHR_BS              = '\x08';
CHR_TAB             = '\x09';
CHR_LF              = '\x0A';
CHR_VT              = '\x0B';
CHR_FF              = '\x0C';
CHR_CR              = '\x0D';
CHR_SO              = '\x0E';
CHR_SI              = '\x0F';
CHR_DLE             = '\x10';
CHR_DC1             = '\x11';
CHR_DC2             = '\x12';
CHR_DC3             = '\x13';
CHR_DC4             = '\x14';
CHR_NAK             = '\x15';
CHR_SYN             = '\x16';
CHR_ETB             = '\x17';
CHR_CAN             = '\x18';
CHR_EM              = '\x19';
CHR_SUB             = '\x1A';
CHR_ESC             = '\x1B';
CHR_FS              = '\x1C';
CHR_GS              = '\x1D';
CHR_RS              = '\x1E';
CHR_US              = '\x1F';
CHR_DEL             = '\x7F';



CHR_KEY_UP          = '\x1b[A';
CHR_KEY_DOWN        = '\x1b[B';
CHR_KEY_LEFT        = '\x1b[D';
CHR_KEY_RIGHT       = '\x1b[C';

CHR_KEY_BS          = '\x08';
CHR_KEY_TAB         = '\x09';
CHR_KEY_SP          = '\x20';
CHR_KEY_DEL         = '\x7f';

CHR_KEY_HOME        = '\x1b[1~';
CHR_KEY_END         = '\x1b[4~';
CHR_KEY_PGUP        = '\x1b[5~';
CHR_KEY_PGDN        = '\x1b[6~';
CHR_KEY_INS         = '\x1b[2~';

CHR_KEY_F1          = '\x1b[11~';
CHR_KEY_F2          = '\x1b[12~';
CHR_KEY_F3          = '\x1b[13~';
CHR_KEY_F4          = '\x1b[14~';
CHR_KEY_F5          = '\x1b[15~';
CHR_KEY_F6          = '\x1b[16~';

CHR_KEY_F7          = '\x1b[18~';
CHR_KEY_F8          = '\x1b[19~';
CHR_KEY_F9          = '\x1b[20~';
CHR_KEY_F10         = '\x1b[21~';
CHR_KEY_F11         = '\x1b[23~';
CHR_KEY_F12         = '\x1b[24~';

CHR_KEY_ESC         = '\x1B';



CHRS_C0 = (
    '\x00\x01\x02\x03\x04\x05\x06\x07'
    '\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
    '\x10\x11\x12\x13\x14\x15\x16\x17'
    '\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F'
);

CHRS_C1 = (
    '\x80\x81\x82\x83\x84\x85\x86\x87'
    '\x88\x89\x8A\x8B\x8C\x8D\x8E\x8F'
    '\x90\x91\x92\x93\x94\x95\x96\x97'
    '\x98\x99\x9A\x9B\x9C\x9D\x9E\x9F'
);

CHRS_NONPRT = CHRS_C0 + CHR_DEL + CHRS_C1;

CHRS_PRINT = (
    ' !"#$%&\'()*+,-./'
    '0123456789:;<=>?'
    '@ABCDEFGHIJKLMNO'
    'PQRSTUVWXYZ[\\]^_'
    '`abcdefghijklmno'
    'pqrstuvwxyz{|}~'
);

CHRS_EXT = (
    '\x80\x81\x82\x83\x84\x85\x86\x87'
    '\x88\x89\x8A\x8B\x8C\x8D\x8E\x8F'
    '\x90\x91\x92\x93\x94\x95\x96\x97'
    '\x98\x99\x9A\x9B\x9C\x9D\x9E\x9F'
    '\xA0\xA1\xA2\xA3\xA4\xA5\xA6\xA7'
    '\xA8\xA9\xAA\xAB\xAC\xAD\xAE\xAF'
    '\xB0\xB1\xB2\xB3\xB4\xB5\xB6\xB7'
    '\xB8\xB9\xBA\xBB\xBC\xBD\xBE\xBF'
    '\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7'
    '\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF'
    '\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7'
    '\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF'
    '\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7'
    '\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF'
    '\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7'
    '\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF'
);



CHR_CSI_START       = CHR_ESC + '[';
CHRS_CSI_MID        = ' !"#$%&\'()*+,-./';
CHRS_CSI_PARAM      = '0123456789:;<=>?';
CHRS_CSI_END        = '@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~';

CHR_CSI_CUU         = CHR_CSI_START + 'A';
CHR_CSI_CUD         = CHR_CSI_START + 'B';
CHR_CSI_CUF         = CHR_CSI_START + 'C';
CHR_CSI_CUB         = CHR_CSI_START + 'D';
CHR_CSI_CUP         = CHR_CSI_START + 'H';
CHR_CSI_ED0         = CHR_CSI_START + '0J';
CHR_CSI_ED1         = CHR_CSI_START + '1J';
CHR_CSI_ED2         = CHR_CSI_START + '2J';
CHR_CSI_HVP         = CHR_CSI_START + 'f';
CHR_CSI_SGR         = CHR_CSI_START + 'm';
CHR_CSI_SCP         = CHR_CSI_START + 's';
CHR_CSI_RCP         = CHR_CSI_START + 'u';

CHR_CSI_CLR         = CHR_CSI_CUP + CHR_CSI_ED2;

CHR_CRLF            = CHR_CR + CHR_LF;
CHR_CRNUL           = CHR_CR + CHR_NUL;

CHRS_ESC_END        = '@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_';
CHRS_RETURN         = (CHR_CRLF, CHR_CRNUL, CHR_CR, CHR_LF);



def CHRf_CSI_CUU(n):
    assert 0 < n < 32768;
    return CHR_CSI_START + str(n) + 'A';

def CHRf_CSI_CUD(n):
    assert 0 < n < 32768;
    return CHR_CSI_START + str(n) + 'B';

def CHRf_CSI_CUF(n):
    assert 0 < n < 32768;
    return CHR_CSI_START + str(n) + 'C';

def CHRf_CSI_CUB(n):
    assert 0 < n < 32768;
    return CHR_CSI_START + str(n) + 'D';

def CHRf_CSI_CUMOV(y, x):
    assert abs(y) < 32768;
    assert abs(x) < 32768;
    _CUD = ('' if y == 0 else (CHRf_CSI_CUD(y) if y > 0 else CHRf_CSI_CUU(-y)));
    _CUB = ('' if x == 0 else (CHRf_CSI_CUF(x) if x > 0 else CHRf_CSI_CUB(-x)));
    return _CUD + _CUB;

def CHRf_CSI_CHA(y):
    assert 0 < y < 32768;
    return CHR_CSI_START + str(y) + 'G';

def CHRf_CSI_VPA(x):
    assert 0 < x < 32768;
    return CHR_CSI_START + str(x) + 'd';

def CHRf_CSI_CUP(y, x):
    assert 0 < y < 32768;
    assert 0 < x < 32768;
    return CHR_CSI_START + str(y) + ';' + str(x) + 'H';

def CHRf_CSI_HVP(y, x):
    assert 0 < y < 32768;
    assert 0 < x < 32768;
    return CHR_CSI_START + str(y) + b';' + str(x) + 'f';

def CHRf_CSI_SGR(*args):
    _args = ';'.join([str(arg) for arg in args]);
    return CHR_CSI_START + _args + 'm';



T_BOLD              = 1;
T_UNDLIN            = 4;
T_BLINK             = 5;
T_REVERS            = 7;

T_DEBOLD            = 22;
T_DEUNDLIN          = 24;
T_DEBLINK           = 25;
T_DEREVERS          = 27;

T_BLACK             = 30;
T_RED               = 31;
T_GREEN             = 32;
T_YELLO             = 33;
T_BLUE              = 34;
T_MAGEN             = 35;
T_CYAN              = 36;
T_WHITE             = 37;
T_LBLACK            = 90;
T_LRED              = 91;
T_LGREEN            = 92;
T_LYELLO            = 93;
T_LBLUE             = 94;
T_LMAGEN            = 95;
T_LCYAN             = 96;
T_LWHITE            = 97;
T_RST               = 39;

T_BBLACK            = 40;
T_BRED              = 41;
T_BGREEN            = 42;
T_BYELLO            = 43;
T_BBLUE             = 44;
T_BMAGEN            = 45;
T_BCYAN             = 46;
T_BWHITE            = 47;
T_BLBLACK           = 100;
T_BLRED             = 101;
T_BLGREEN           = 102;
T_BLYELLO           = 103;
T_BLBLUE            = 104;
T_BLMAGEN           = 105;
T_BLCYAN            = 106;
T_BLWHITE           = 107;
T_BRST              = 49;



CHR_T_RST           = CHR_CSI_SGR;

CHR_T_BOLD          = CHRf_CSI_SGR(1);
CHR_T_LIGHT         = CHRf_CSI_SGR(2);
CHR_T_ITALIC        = CHRf_CSI_SGR(3);
CHR_T_UNDLIN        = CHRf_CSI_SGR(4);
CHR_T_BLINK         = CHRf_CSI_SGR(5);
CHR_T_BLINKS        = CHRf_CSI_SGR(6);
CHR_T_REVERS        = CHRf_CSI_SGR(7);
CHR_T_HIDDEN        = CHRf_CSI_SGR(8);
CHR_T_DELETE        = CHRf_CSI_SGR(9);

CHR_T_FONT0         = CHRf_CSI_SGR(10);
CHR_T_FONT1         = CHRf_CSI_SGR(11);
CHR_T_FONT2         = CHRf_CSI_SGR(12);
CHR_T_FONT3         = CHRf_CSI_SGR(13);
CHR_T_FONT4         = CHRf_CSI_SGR(14);
CHR_T_FONT5         = CHRf_CSI_SGR(15);
CHR_T_FONT6         = CHRf_CSI_SGR(16);
CHR_T_FONT7         = CHRf_CSI_SGR(17);
CHR_T_FONT8         = CHRf_CSI_SGR(18);
CHR_T_FONT9         = CHRf_CSI_SGR(19);

CHR_T_FRAKT         = CHRf_CSI_SGR(20);
CHR_T_HEAVY         = CHRf_CSI_SGR(21);
CHR_T_NORMW         = CHRf_CSI_SGR(22);
CHR_T_NORMF         = CHRf_CSI_SGR(23);

CHR_T_DEUNDLIN      = CHRf_CSI_SGR(24);
CHR_T_DEBLINK       = CHRf_CSI_SGR(25);
CHR_T_DEREVERS      = CHRf_CSI_SGR(27);
CHR_T_DEHIDDEN      = CHRf_CSI_SGR(28);
CHR_T_DEDELETE      = CHRf_CSI_SGR(29);

CHR_T_FC_BLACK      = CHRf_CSI_SGR(30);
CHR_T_FC_RED        = CHRf_CSI_SGR(31);
CHR_T_FC_GREEN      = CHRf_CSI_SGR(32);
CHR_T_FC_YELLO      = CHRf_CSI_SGR(33);
CHR_T_FC_BLUE       = CHRf_CSI_SGR(34);
CHR_T_FC_MAGEN      = CHRf_CSI_SGR(35);
CHR_T_FC_CYAN       = CHRf_CSI_SGR(36);
CHR_T_FC_WHITE      = CHRf_CSI_SGR(37);
CHR_T_FC_LBLACK     = CHRf_CSI_SGR(90);
CHR_T_FC_LRED       = CHRf_CSI_SGR(91);
CHR_T_FC_LGREEN     = CHRf_CSI_SGR(92);
CHR_T_FC_LYELLO     = CHRf_CSI_SGR(93);
CHR_T_FC_LBLUE      = CHRf_CSI_SGR(94);
CHR_T_FC_LMAGEN     = CHRf_CSI_SGR(95);
CHR_T_FC_LCYAN      = CHRf_CSI_SGR(96);
CHR_T_FC_LWHITE     = CHRf_CSI_SGR(97);
CHR_T_FC_RST        = CHRf_CSI_SGR(39);

CHR_T_BC_BLACK      = CHRf_CSI_SGR(40);
CHR_T_BC_RED        = CHRf_CSI_SGR(41);
CHR_T_BC_GREEN      = CHRf_CSI_SGR(42);
CHR_T_BC_YELLO      = CHRf_CSI_SGR(43);
CHR_T_BC_BLUE       = CHRf_CSI_SGR(44);
CHR_T_BC_MAGEN      = CHRf_CSI_SGR(45);
CHR_T_BC_CYAN       = CHRf_CSI_SGR(46);
CHR_T_BC_WHITE      = CHRf_CSI_SGR(47);
CHR_T_BC_LBLACK     = CHRf_CSI_SGR(100);
CHR_T_BC_LRED       = CHRf_CSI_SGR(101);
CHR_T_BC_LGREEN     = CHRf_CSI_SGR(102);
CHR_T_BC_LYELLO     = CHRf_CSI_SGR(103);
CHR_T_BC_LBLUE      = CHRf_CSI_SGR(104);
CHR_T_BC_LMAGEN     = CHRf_CSI_SGR(105);
CHR_T_BC_LCYAN      = CHRf_CSI_SGR(106);
CHR_T_BC_LWHITE     = CHRf_CSI_SGR(107);
CHR_T_BC_RST        = CHRf_CSI_SGR(49);

CHR_T_FRAMED        = CHRf_CSI_SGR(50);
CHR_T_ENCIRC        = CHRf_CSI_SGR(51);
CHR_T_UPLIN         = CHRf_CSI_SGR(52);
CHR_T_DEFRMENC      = CHRf_CSI_SGR(53);
CHR_T_DEUPLIN       = CHRf_CSI_SGR(54);
