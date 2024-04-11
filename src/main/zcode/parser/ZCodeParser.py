# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u0196\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\7\2")
        buf.write("\\\n\2\f\2\16\2_\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3")
        buf.write("h\n\3\3\4\3\4\3\4\3\4\5\4n\n\4\3\5\3\5\3\5\5\5s\n\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0080\n")
        buf.write("\6\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\5\n\u008f\n\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u0098")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00a0\n\r\3\r\3\r\5\r")
        buf.write("\u00a4\n\r\3\r\3\r\5\r\u00a8\n\r\3\16\3\16\5\16\u00ac")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\5\17\u00b3\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\5\20\u00bc\n\20\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u00c2\n\21\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\5\22\u00cd\n\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\5\24\u00d5\n\24\3\24\3\24\3\24\3\24\3\25\3")
        buf.write("\25\3\25\3\25\3\26\3\26\3\26\3\26\5\26\u00e3\n\26\3\26")
        buf.write("\3\26\5\26\u00e7\n\26\3\27\3\27\3\27\3\27\3\27\3\27\5")
        buf.write("\27\u00ef\n\27\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u00f7")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\5\31\u00fe\n\31\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u010e\n\33\3\34\3\34\3\34\3\35\3\35\3")
        buf.write("\35\3\36\3\36\3\36\5\36\u0119\n\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u0121\n\37\3\37\3\37\3\37\3 \3 \3 \3 ")
        buf.write("\5 \u012a\n \3 \3 \3!\3!\3!\3!\5!\u0132\n!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\5\"\u013c\n\"\3#\3#\3#\3#\3#\5#\u0143")
        buf.write("\n#\3$\3$\3$\3$\3$\5$\u014a\n$\3%\3%\3%\3%\3%\3%\7%\u0152")
        buf.write("\n%\f%\16%\u0155\13%\3&\3&\3&\3&\3&\3&\7&\u015d\n&\f&")
        buf.write("\16&\u0160\13&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0168\n\'\f")
        buf.write("\'\16\'\u016b\13\'\3(\3(\3(\5(\u0170\n(\3)\3)\3)\3)\5")
        buf.write(")\u0176\n)\3*\3*\5*\u017a\n*\3*\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\5+\u018b\n+\3,\3,\3,\3,\3-\6-\u0192")
        buf.write("\n-\r-\16-\u0193\3-\2\5HJL.\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX\2\7")
        buf.write("\3\2\5\7\5\2\33\33\35!##\3\2$%\3\2\26\27\3\2\30\32\2\u019e")
        buf.write("\2]\3\2\2\2\4g\3\2\2\2\6m\3\2\2\2\br\3\2\2\2\n\177\3\2")
        buf.write("\2\2\f\u0081\3\2\2\2\16\u0083\3\2\2\2\20\u0087\3\2\2\2")
        buf.write("\22\u008e\3\2\2\2\24\u0090\3\2\2\2\26\u0097\3\2\2\2\30")
        buf.write("\u0099\3\2\2\2\32\u00ab\3\2\2\2\34\u00b2\3\2\2\2\36\u00b4")
        buf.write("\3\2\2\2 \u00c1\3\2\2\2\"\u00cc\3\2\2\2$\u00ce\3\2\2\2")
        buf.write("&\u00d4\3\2\2\2(\u00da\3\2\2\2*\u00de\3\2\2\2,\u00ee\3")
        buf.write("\2\2\2.\u00f6\3\2\2\2\60\u00f8\3\2\2\2\62\u00ff\3\2\2")
        buf.write("\2\64\u0103\3\2\2\2\66\u010f\3\2\2\28\u0112\3\2\2\2:\u0115")
        buf.write("\3\2\2\2<\u011c\3\2\2\2>\u0125\3\2\2\2@\u012d\3\2\2\2")
        buf.write("B\u013b\3\2\2\2D\u0142\3\2\2\2F\u0149\3\2\2\2H\u014b\3")
        buf.write("\2\2\2J\u0156\3\2\2\2L\u0161\3\2\2\2N\u016f\3\2\2\2P\u0175")
        buf.write("\3\2\2\2R\u0179\3\2\2\2T\u018a\3\2\2\2V\u018c\3\2\2\2")
        buf.write("X\u0191\3\2\2\2Z\\\7\60\2\2[Z\3\2\2\2\\_\3\2\2\2][\3\2")
        buf.write("\2\2]^\3\2\2\2^`\3\2\2\2_]\3\2\2\2`a\5\4\3\2ab\7\2\2\3")
        buf.write("b\3\3\2\2\2cd\5\6\4\2de\5\4\3\2eh\3\2\2\2fh\5\6\4\2gc")
        buf.write("\3\2\2\2gf\3\2\2\2h\5\3\2\2\2in\5\30\r\2jk\5\b\5\2kl\5")
        buf.write("X-\2ln\3\2\2\2mi\3\2\2\2mj\3\2\2\2n\7\3\2\2\2os\5\n\6")
        buf.write("\2ps\5\16\b\2qs\5\20\t\2ro\3\2\2\2rp\3\2\2\2rq\3\2\2\2")
        buf.write("s\t\3\2\2\2tu\5\f\7\2uv\7,\2\2vw\5\22\n\2w\u0080\3\2\2")
        buf.write("\2xy\5\f\7\2yz\7,\2\2z{\7)\2\2{|\5\26\f\2|}\7*\2\2}~\5")
        buf.write("\22\n\2~\u0080\3\2\2\2\177t\3\2\2\2\177x\3\2\2\2\u0080")
        buf.write("\13\3\2\2\2\u0081\u0082\t\2\2\2\u0082\r\3\2\2\2\u0083")
        buf.write("\u0084\7\t\2\2\u0084\u0085\7,\2\2\u0085\u0086\5\24\13")
        buf.write("\2\u0086\17\3\2\2\2\u0087\u0088\7\n\2\2\u0088\u0089\7")
        buf.write(",\2\2\u0089\u008a\5\22\n\2\u008a\21\3\2\2\2\u008b\u008c")
        buf.write("\7\34\2\2\u008c\u008f\5D#\2\u008d\u008f\3\2\2\2\u008e")
        buf.write("\u008b\3\2\2\2\u008e\u008d\3\2\2\2\u008f\23\3\2\2\2\u0090")
        buf.write("\u0091\7\34\2\2\u0091\u0092\5D#\2\u0092\25\3\2\2\2\u0093")
        buf.write("\u0094\7/\2\2\u0094\u0095\7+\2\2\u0095\u0098\5\26\f\2")
        buf.write("\u0096\u0098\7/\2\2\u0097\u0093\3\2\2\2\u0097\u0096\3")
        buf.write("\2\2\2\u0098\27\3\2\2\2\u0099\u009a\7\13\2\2\u009a\u009b")
        buf.write("\7,\2\2\u009b\u009c\7\'\2\2\u009c\u009d\5\32\16\2\u009d")
        buf.write("\u00a7\7(\2\2\u009e\u00a0\5X-\2\u009f\u009e\3\2\2\2\u009f")
        buf.write("\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a8\5<\37\2")
        buf.write("\u00a2\u00a4\5X-\2\u00a3\u00a2\3\2\2\2\u00a3\u00a4\3\2")
        buf.write("\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a8\5:\36\2\u00a6\u00a8")
        buf.write("\5X-\2\u00a7\u009f\3\2\2\2\u00a7\u00a3\3\2\2\2\u00a7\u00a6")
        buf.write("\3\2\2\2\u00a8\31\3\2\2\2\u00a9\u00ac\5\34\17\2\u00aa")
        buf.write("\u00ac\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2")
        buf.write("\u00ac\33\3\2\2\2\u00ad\u00ae\5\36\20\2\u00ae\u00af\7")
        buf.write("+\2\2\u00af\u00b0\5\34\17\2\u00b0\u00b3\3\2\2\2\u00b1")
        buf.write("\u00b3\5\36\20\2\u00b2\u00ad\3\2\2\2\u00b2\u00b1\3\2\2")
        buf.write("\2\u00b3\35\3\2\2\2\u00b4\u00bb\5\f\7\2\u00b5\u00bc\7")
        buf.write(",\2\2\u00b6\u00b7\7,\2\2\u00b7\u00b8\7)\2\2\u00b8\u00b9")
        buf.write("\5\26\f\2\u00b9\u00ba\7*\2\2\u00ba\u00bc\3\2\2\2\u00bb")
        buf.write("\u00b5\3\2\2\2\u00bb\u00b6\3\2\2\2\u00bc\37\3\2\2\2\u00bd")
        buf.write("\u00be\5\"\22\2\u00be\u00bf\5 \21\2\u00bf\u00c2\3\2\2")
        buf.write("\2\u00c0\u00c2\3\2\2\2\u00c1\u00bd\3\2\2\2\u00c1\u00c0")
        buf.write("\3\2\2\2\u00c2!\3\2\2\2\u00c3\u00cd\5$\23\2\u00c4\u00cd")
        buf.write("\5&\24\2\u00c5\u00cd\5*\26\2\u00c6\u00cd\5\64\33\2\u00c7")
        buf.write("\u00cd\58\35\2\u00c8\u00cd\5\66\34\2\u00c9\u00cd\5:\36")
        buf.write("\2\u00ca\u00cd\5@!\2\u00cb\u00cd\5<\37\2\u00cc\u00c3\3")
        buf.write("\2\2\2\u00cc\u00c4\3\2\2\2\u00cc\u00c5\3\2\2\2\u00cc\u00c6")
        buf.write("\3\2\2\2\u00cc\u00c7\3\2\2\2\u00cc\u00c8\3\2\2\2\u00cc")
        buf.write("\u00c9\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cb\3\2\2\2")
        buf.write("\u00cd#\3\2\2\2\u00ce\u00cf\5\b\5\2\u00cf\u00d0\5X-\2")
        buf.write("\u00d0%\3\2\2\2\u00d1\u00d5\7,\2\2\u00d2\u00d3\7,\2\2")
        buf.write("\u00d3\u00d5\5(\25\2\u00d4\u00d1\3\2\2\2\u00d4\u00d2\3")
        buf.write("\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\7\34\2\2\u00d7")
        buf.write("\u00d8\5D#\2\u00d8\u00d9\5X-\2\u00d9\'\3\2\2\2\u00da\u00db")
        buf.write("\7)\2\2\u00db\u00dc\5B\"\2\u00dc\u00dd\7*\2\2\u00dd)\3")
        buf.write("\2\2\2\u00de\u00df\7\21\2\2\u00df\u00e2\5\60\31\2\u00e0")
        buf.write("\u00e3\5,\27\2\u00e1\u00e3\3\2\2\2\u00e2\u00e0\3\2\2\2")
        buf.write("\u00e2\u00e1\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e7\5")
        buf.write(".\30\2\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5")
        buf.write("\3\2\2\2\u00e7+\3\2\2\2\u00e8\u00e9\7\23\2\2\u00e9\u00ea")
        buf.write("\5\60\31\2\u00ea\u00eb\5,\27\2\u00eb\u00ef\3\2\2\2\u00ec")
        buf.write("\u00ed\7\23\2\2\u00ed\u00ef\5\60\31\2\u00ee\u00e8\3\2")
        buf.write("\2\2\u00ee\u00ec\3\2\2\2\u00ef-\3\2\2\2\u00f0\u00f1\7")
        buf.write("\22\2\2\u00f1\u00f2\5X-\2\u00f2\u00f3\5\"\22\2\u00f3\u00f7")
        buf.write("\3\2\2\2\u00f4\u00f5\7\22\2\2\u00f5\u00f7\5\"\22\2\u00f6")
        buf.write("\u00f0\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7/\3\2\2\2\u00f8")
        buf.write("\u00fd\5\62\32\2\u00f9\u00fa\5X-\2\u00fa\u00fb\5\"\22")
        buf.write("\2\u00fb\u00fe\3\2\2\2\u00fc\u00fe\5\"\22\2\u00fd\u00f9")
        buf.write("\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe\61\3\2\2\2\u00ff\u0100")
        buf.write("\7\'\2\2\u0100\u0101\5D#\2\u0101\u0102\7(\2\2\u0102\63")
        buf.write("\3\2\2\2\u0103\u0104\7\f\2\2\u0104\u0105\7,\2\2\u0105")
        buf.write("\u0106\7\r\2\2\u0106\u0107\5D#\2\u0107\u0108\7\16\2\2")
        buf.write("\u0108\u010d\5D#\2\u0109\u010e\5\"\22\2\u010a\u010b\5")
        buf.write("X-\2\u010b\u010c\5\"\22\2\u010c\u010e\3\2\2\2\u010d\u0109")
        buf.write("\3\2\2\2\u010d\u010a\3\2\2\2\u010e\65\3\2\2\2\u010f\u0110")
        buf.write("\7\20\2\2\u0110\u0111\5X-\2\u0111\67\3\2\2\2\u0112\u0113")
        buf.write("\7\17\2\2\u0113\u0114\5X-\2\u01149\3\2\2\2\u0115\u0118")
        buf.write("\7\b\2\2\u0116\u0119\5D#\2\u0117\u0119\3\2\2\2\u0118\u0116")
        buf.write("\3\2\2\2\u0118\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a")
        buf.write("\u011b\5X-\2\u011b;\3\2\2\2\u011c\u011d\7\24\2\2\u011d")
        buf.write("\u0120\5X-\2\u011e\u0121\5 \21\2\u011f\u0121\3\2\2\2\u0120")
        buf.write("\u011e\3\2\2\2\u0120\u011f\3\2\2\2\u0121\u0122\3\2\2\2")
        buf.write("\u0122\u0123\7\25\2\2\u0123\u0124\5X-\2\u0124=\3\2\2\2")
        buf.write("\u0125\u0126\7,\2\2\u0126\u0129\7\'\2\2\u0127\u012a\5")
        buf.write("B\"\2\u0128\u012a\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u0128")
        buf.write("\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\7(\2\2\u012c")
        buf.write("?\3\2\2\2\u012d\u012e\7,\2\2\u012e\u0131\7\'\2\2\u012f")
        buf.write("\u0132\5B\"\2\u0130\u0132\3\2\2\2\u0131\u012f\3\2\2\2")
        buf.write("\u0131\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0134\7")
        buf.write("(\2\2\u0134\u0135\5X-\2\u0135A\3\2\2\2\u0136\u0137\5D")
        buf.write("#\2\u0137\u0138\7+\2\2\u0138\u0139\5B\"\2\u0139\u013c")
        buf.write("\3\2\2\2\u013a\u013c\5D#\2\u013b\u0136\3\2\2\2\u013b\u013a")
        buf.write("\3\2\2\2\u013cC\3\2\2\2\u013d\u013e\5F$\2\u013e\u013f")
        buf.write("\7\"\2\2\u013f\u0140\5F$\2\u0140\u0143\3\2\2\2\u0141\u0143")
        buf.write("\5F$\2\u0142\u013d\3\2\2\2\u0142\u0141\3\2\2\2\u0143E")
        buf.write("\3\2\2\2\u0144\u0145\5H%\2\u0145\u0146\t\3\2\2\u0146\u0147")
        buf.write("\5H%\2\u0147\u014a\3\2\2\2\u0148\u014a\5H%\2\u0149\u0144")
        buf.write("\3\2\2\2\u0149\u0148\3\2\2\2\u014aG\3\2\2\2\u014b\u014c")
        buf.write("\b%\1\2\u014c\u014d\5J&\2\u014d\u0153\3\2\2\2\u014e\u014f")
        buf.write("\f\4\2\2\u014f\u0150\t\4\2\2\u0150\u0152\5J&\2\u0151\u014e")
        buf.write("\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154I\3\2\2\2\u0155\u0153\3\2\2\2\u0156")
        buf.write("\u0157\b&\1\2\u0157\u0158\5L\'\2\u0158\u015e\3\2\2\2\u0159")
        buf.write("\u015a\f\4\2\2\u015a\u015b\t\5\2\2\u015b\u015d\5L\'\2")
        buf.write("\u015c\u0159\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c\3")
        buf.write("\2\2\2\u015e\u015f\3\2\2\2\u015fK\3\2\2\2\u0160\u015e")
        buf.write("\3\2\2\2\u0161\u0162\b\'\1\2\u0162\u0163\5N(\2\u0163\u0169")
        buf.write("\3\2\2\2\u0164\u0165\f\4\2\2\u0165\u0166\t\6\2\2\u0166")
        buf.write("\u0168\5N(\2\u0167\u0164\3\2\2\2\u0168\u016b\3\2\2\2\u0169")
        buf.write("\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016aM\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u016d\7&\2\2\u016d\u0170\5N(\2\u016e")
        buf.write("\u0170\5P)\2\u016f\u016c\3\2\2\2\u016f\u016e\3\2\2\2\u0170")
        buf.write("O\3\2\2\2\u0171\u0172\7\27\2\2\u0172\u0176\5P)\2\u0173")
        buf.write("\u0176\5R*\2\u0174\u0176\5T+\2\u0175\u0171\3\2\2\2\u0175")
        buf.write("\u0173\3\2\2\2\u0175\u0174\3\2\2\2\u0176Q\3\2\2\2\u0177")
        buf.write("\u017a\7,\2\2\u0178\u017a\5> \2\u0179\u0177\3\2\2\2\u0179")
        buf.write("\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\7)\2\2")
        buf.write("\u017c\u017d\5B\"\2\u017d\u017e\7*\2\2\u017eS\3\2\2\2")
        buf.write("\u017f\u018b\7/\2\2\u0180\u018b\7.\2\2\u0181\u018b\7\3")
        buf.write("\2\2\u0182\u018b\7\4\2\2\u0183\u018b\7,\2\2\u0184\u018b")
        buf.write("\5V,\2\u0185\u0186\7\'\2\2\u0186\u0187\5D#\2\u0187\u0188")
        buf.write("\7(\2\2\u0188\u018b\3\2\2\2\u0189\u018b\5> \2\u018a\u017f")
        buf.write("\3\2\2\2\u018a\u0180\3\2\2\2\u018a\u0181\3\2\2\2\u018a")
        buf.write("\u0182\3\2\2\2\u018a\u0183\3\2\2\2\u018a\u0184\3\2\2\2")
        buf.write("\u018a\u0185\3\2\2\2\u018a\u0189\3\2\2\2\u018bU\3\2\2")
        buf.write("\2\u018c\u018d\7)\2\2\u018d\u018e\5B\"\2\u018e\u018f\7")
        buf.write("*\2\2\u018fW\3\2\2\2\u0190\u0192\7\60\2\2\u0191\u0190")
        buf.write("\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194Y\3\2\2\2\']gmr\177\u008e\u0097\u009f")
        buf.write("\u00a3\u00a7\u00ab\u00b2\u00bb\u00c1\u00cc\u00d4\u00e2")
        buf.write("\u00e6\u00ee\u00f6\u00fd\u010d\u0118\u0120\u0129\u0131")
        buf.write("\u013b\u0142\u0149\u0153\u015e\u0169\u016f\u0175\u0179")
        buf.write("\u018a\u0193")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'and'", 
                     "'or'", "'not'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "ASSIGN", 
                      "NEQ", "LT", "LTE", "GT", "GTE", "CONCAT", "EQEQ", 
                      "AND", "OR", "NOT", "LPAREN", "RPAREN", "LBRACK", 
                      "RBRACK", "COMMA", "ID", "BOOLEAN", "STRINGLIT", "NUMBERLIT", 
                      "NEWLINE", "WS", "COMMENTS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_listDeclared = 1
    RULE_declared = 2
    RULE_variablesDeclared = 3
    RULE_explicitTypeDeclared = 4
    RULE_explicitType = 5
    RULE_implicitVarDeclared = 6
    RULE_implicitDynamicDeclared = 7
    RULE_initVariableValueOrNull = 8
    RULE_initVariableValue = 9
    RULE_numbersList = 10
    RULE_functionDeclared = 11
    RULE_prametersList = 12
    RULE_paramsPrime = 13
    RULE_param = 14
    RULE_statementList = 15
    RULE_statement = 16
    RULE_declaredStatement = 17
    RULE_assignmentStatement = 18
    RULE_indexOperatorNew = 19
    RULE_conditionStatement = 20
    RULE_elseIfStatement = 21
    RULE_elseStatement = 22
    RULE_conditionAndStatement = 23
    RULE_conditionExpress = 24
    RULE_forStatement = 25
    RULE_continueStatement = 26
    RULE_breakStatement = 27
    RULE_returnStatement = 28
    RULE_blockStatement = 29
    RULE_callFunction = 30
    RULE_callStatement = 31
    RULE_expressList = 32
    RULE_express = 33
    RULE_express1 = 34
    RULE_express2 = 35
    RULE_express3 = 36
    RULE_express4 = 37
    RULE_express5 = 38
    RULE_express6 = 39
    RULE_express7 = 40
    RULE_express8 = 41
    RULE_arrayLiteral = 42
    RULE_ignore = 43

    ruleNames =  [ "program", "listDeclared", "declared", "variablesDeclared", 
                   "explicitTypeDeclared", "explicitType", "implicitVarDeclared", 
                   "implicitDynamicDeclared", "initVariableValueOrNull", 
                   "initVariableValue", "numbersList", "functionDeclared", 
                   "prametersList", "paramsPrime", "param", "statementList", 
                   "statement", "declaredStatement", "assignmentStatement", 
                   "indexOperatorNew", "conditionStatement", "elseIfStatement", 
                   "elseStatement", "conditionAndStatement", "conditionExpress", 
                   "forStatement", "continueStatement", "breakStatement", 
                   "returnStatement", "blockStatement", "callFunction", 
                   "callStatement", "expressList", "express", "express1", 
                   "express2", "express3", "express4", "express5", "express6", 
                   "express7", "express8", "arrayLiteral", "ignore" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    ADD=20
    SUB=21
    MUL=22
    DIV=23
    MOD=24
    EQ=25
    ASSIGN=26
    NEQ=27
    LT=28
    LTE=29
    GT=30
    GTE=31
    CONCAT=32
    EQEQ=33
    AND=34
    OR=35
    NOT=36
    LPAREN=37
    RPAREN=38
    LBRACK=39
    RBRACK=40
    COMMA=41
    ID=42
    BOOLEAN=43
    STRINGLIT=44
    NUMBERLIT=45
    NEWLINE=46
    WS=47
    COMMENTS=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listDeclared(self):
            return self.getTypedRuleContext(ZCodeParser.ListDeclaredContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 88
                self.match(ZCodeParser.NEWLINE)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.listDeclared()
            self.state = 95
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListDeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(ZCodeParser.DeclaredContext,0)


        def listDeclared(self):
            return self.getTypedRuleContext(ZCodeParser.ListDeclaredContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_listDeclared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListDeclared" ):
                return visitor.visitListDeclared(self)
            else:
                return visitor.visitChildren(self)




    def listDeclared(self):

        localctx = ZCodeParser.ListDeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_listDeclared)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.declared()
                self.state = 98
                self.listDeclared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDeclared(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionDeclaredContext,0)


        def variablesDeclared(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesDeclaredContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = ZCodeParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declared)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.functionDeclared()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.variablesDeclared()
                self.state = 105
                self.ignore()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesDeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explicitTypeDeclared(self):
            return self.getTypedRuleContext(ZCodeParser.ExplicitTypeDeclaredContext,0)


        def implicitVarDeclared(self):
            return self.getTypedRuleContext(ZCodeParser.ImplicitVarDeclaredContext,0)


        def implicitDynamicDeclared(self):
            return self.getTypedRuleContext(ZCodeParser.ImplicitDynamicDeclaredContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variablesDeclared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariablesDeclared" ):
                return visitor.visitVariablesDeclared(self)
            else:
                return visitor.visitChildren(self)




    def variablesDeclared(self):

        localctx = ZCodeParser.VariablesDeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variablesDeclared)
        try:
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.explicitTypeDeclared()
                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.implicitVarDeclared()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.implicitDynamicDeclared()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplicitTypeDeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explicitType(self):
            return self.getTypedRuleContext(ZCodeParser.ExplicitTypeContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def initVariableValueOrNull(self):
            return self.getTypedRuleContext(ZCodeParser.InitVariableValueOrNullContext,0)


        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def numbersList(self):
            return self.getTypedRuleContext(ZCodeParser.NumbersListContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_explicitTypeDeclared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicitTypeDeclared" ):
                return visitor.visitExplicitTypeDeclared(self)
            else:
                return visitor.visitChildren(self)




    def explicitTypeDeclared(self):

        localctx = ZCodeParser.ExplicitTypeDeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_explicitTypeDeclared)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.explicitType()
                self.state = 115
                self.match(ZCodeParser.ID)
                self.state = 116
                self.initVariableValueOrNull()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.explicitType()
                self.state = 119
                self.match(ZCodeParser.ID)
                self.state = 120
                self.match(ZCodeParser.LBRACK)
                self.state = 121
                self.numbersList()
                self.state = 122
                self.match(ZCodeParser.RBRACK)
                self.state = 123
                self.initVariableValueOrNull()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplicitTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_explicitType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicitType" ):
                return visitor.visitExplicitType(self)
            else:
                return visitor.visitChildren(self)




    def explicitType(self):

        localctx = ZCodeParser.ExplicitTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_explicitType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplicitVarDeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def initVariableValue(self):
            return self.getTypedRuleContext(ZCodeParser.InitVariableValueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicitVarDeclared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicitVarDeclared" ):
                return visitor.visitImplicitVarDeclared(self)
            else:
                return visitor.visitChildren(self)




    def implicitVarDeclared(self):

        localctx = ZCodeParser.ImplicitVarDeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_implicitVarDeclared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(ZCodeParser.VAR)
            self.state = 130
            self.match(ZCodeParser.ID)
            self.state = 131
            self.initVariableValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplicitDynamicDeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def initVariableValueOrNull(self):
            return self.getTypedRuleContext(ZCodeParser.InitVariableValueOrNullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicitDynamicDeclared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicitDynamicDeclared" ):
                return visitor.visitImplicitDynamicDeclared(self)
            else:
                return visitor.visitChildren(self)




    def implicitDynamicDeclared(self):

        localctx = ZCodeParser.ImplicitDynamicDeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_implicitDynamicDeclared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(ZCodeParser.DYNAMIC)
            self.state = 134
            self.match(ZCodeParser.ID)
            self.state = 135
            self.initVariableValueOrNull()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitVariableValueOrNullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def express(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_initVariableValueOrNull

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitVariableValueOrNull" ):
                return visitor.visitInitVariableValueOrNull(self)
            else:
                return visitor.visitChildren(self)




    def initVariableValueOrNull(self):

        localctx = ZCodeParser.InitVariableValueOrNullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_initVariableValueOrNull)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(ZCodeParser.ASSIGN)
                self.state = 138
                self.express()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitVariableValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def express(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_initVariableValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitVariableValue" ):
                return visitor.visitInitVariableValue(self)
            else:
                return visitor.visitChildren(self)




    def initVariableValue(self):

        localctx = ZCodeParser.InitVariableValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_initVariableValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(ZCodeParser.ASSIGN)
            self.state = 143
            self.express()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumbersListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def numbersList(self):
            return self.getTypedRuleContext(ZCodeParser.NumbersListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numbersList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumbersList" ):
                return visitor.visitNumbersList(self)
            else:
                return visitor.visitChildren(self)




    def numbersList(self):

        localctx = ZCodeParser.NumbersListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_numbersList)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(ZCodeParser.NUMBERLIT)
                self.state = 146
                self.match(ZCodeParser.COMMA)
                self.state = 147
                self.numbersList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.match(ZCodeParser.NUMBERLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def prametersList(self):
            return self.getTypedRuleContext(ZCodeParser.PrametersListContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnStatementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionDeclared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclared" ):
                return visitor.visitFunctionDeclared(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclared(self):

        localctx = ZCodeParser.FunctionDeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functionDeclared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ZCodeParser.FUNC)
            self.state = 152
            self.match(ZCodeParser.ID)
            self.state = 153
            self.match(ZCodeParser.LPAREN)
            self.state = 154
            self.prametersList()
            self.state = 155
            self.match(ZCodeParser.RPAREN)
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 156
                    self.ignore()


                self.state = 159
                self.blockStatement()
                pass

            elif la_ == 2:
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 160
                    self.ignore()


                self.state = 163
                self.returnStatement()
                pass

            elif la_ == 3:
                self.state = 164
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrametersListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramsPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamsPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_prametersList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrametersList" ):
                return visitor.visitPrametersList(self)
            else:
                return visitor.visitChildren(self)




    def prametersList(self):

        localctx = ZCodeParser.PrametersListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_prametersList)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.paramsPrime()
                pass
            elif token in [ZCodeParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramsPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamsPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramsPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamsPrime" ):
                return visitor.visitParamsPrime(self)
            else:
                return visitor.visitChildren(self)




    def paramsPrime(self):

        localctx = ZCodeParser.ParamsPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramsPrime)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.param()
                self.state = 172
                self.match(ZCodeParser.COMMA)
                self.state = 173
                self.paramsPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explicitType(self):
            return self.getTypedRuleContext(ZCodeParser.ExplicitTypeContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def numbersList(self):
            return self.getTypedRuleContext(ZCodeParser.NumbersListContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.explicitType()
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 179
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 180
                self.match(ZCodeParser.ID)
                self.state = 181
                self.match(ZCodeParser.LBRACK)
                self.state = 182
                self.numbersList()
                self.state = 183
                self.match(ZCodeParser.RBRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statementList(self):
            return self.getTypedRuleContext(ZCodeParser.StatementListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = ZCodeParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statementList)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.statement()
                self.state = 188
                self.statementList()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaredStatement(self):
            return self.getTypedRuleContext(ZCodeParser.DeclaredStatementContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(ZCodeParser.AssignmentStatementContext,0)


        def conditionStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ConditionStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ForStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(ZCodeParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ContinueStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnStatementContext,0)


        def callStatement(self):
            return self.getTypedRuleContext(ZCodeParser.CallStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_statement)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.declaredStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.assignmentStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.conditionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.forStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 197
                self.breakStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 198
                self.continueStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 199
                self.returnStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 200
                self.callStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 201
                self.blockStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variablesDeclared(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesDeclaredContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaredStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaredStatement" ):
                return visitor.visitDeclaredStatement(self)
            else:
                return visitor.visitChildren(self)




    def declaredStatement(self):

        localctx = ZCodeParser.DeclaredStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_declaredStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.variablesDeclared()
            self.state = 205
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def express(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def indexOperatorNew(self):
            return self.getTypedRuleContext(ZCodeParser.IndexOperatorNewContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignmentStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = ZCodeParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 207
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 208
                self.match(ZCodeParser.ID)
                self.state = 209
                self.indexOperatorNew()
                pass


            self.state = 212
            self.match(ZCodeParser.ASSIGN)
            self.state = 213
            self.express()
            self.state = 214
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexOperatorNewContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def expressList(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressListContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_indexOperatorNew

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexOperatorNew" ):
                return visitor.visitIndexOperatorNew(self)
            else:
                return visitor.visitChildren(self)




    def indexOperatorNew(self):

        localctx = ZCodeParser.IndexOperatorNewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_indexOperatorNew)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(ZCodeParser.LBRACK)
            self.state = 217
            self.expressList()
            self.state = 218
            self.match(ZCodeParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def conditionAndStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ConditionAndStatementContext,0)


        def elseIfStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ElseIfStatementContext,0)


        def elseStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ElseStatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_conditionStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionStatement" ):
                return visitor.visitConditionStatement(self)
            else:
                return visitor.visitChildren(self)




    def conditionStatement(self):

        localctx = ZCodeParser.ConditionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_conditionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(ZCodeParser.IF)
            self.state = 221
            self.conditionAndStatement()
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 222
                self.elseIfStatement()
                pass

            elif la_ == 2:
                pass


            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 226
                self.elseStatement()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def conditionAndStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ConditionAndStatementContext,0)


        def elseIfStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ElseIfStatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elseIfStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIfStatement" ):
                return visitor.visitElseIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def elseIfStatement(self):

        localctx = ZCodeParser.ElseIfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_elseIfStatement)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(ZCodeParser.ELIF)
                self.state = 231
                self.conditionAndStatement()
                self.state = 232
                self.elseIfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(ZCodeParser.ELIF)
                self.state = 235
                self.conditionAndStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elseStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStatement" ):
                return visitor.visitElseStatement(self)
            else:
                return visitor.visitChildren(self)




    def elseStatement(self):

        localctx = ZCodeParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elseStatement)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(ZCodeParser.ELSE)
                self.state = 239
                self.ignore()
                self.state = 240
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(ZCodeParser.ELSE)
                self.state = 243
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionAndStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionExpress(self):
            return self.getTypedRuleContext(ZCodeParser.ConditionExpressContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_conditionAndStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionAndStatement" ):
                return visitor.visitConditionAndStatement(self)
            else:
                return visitor.visitChildren(self)




    def conditionAndStatement(self):

        localctx = ZCodeParser.ConditionAndStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_conditionAndStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.conditionExpress()
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.state = 247
                self.ignore()
                self.state = 248
                self.statement()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.state = 250
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionExpressContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def express(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_conditionExpress

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionExpress" ):
                return visitor.visitConditionExpress(self)
            else:
                return visitor.visitChildren(self)




    def conditionExpress(self):

        localctx = ZCodeParser.ConditionExpressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_conditionExpress)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(ZCodeParser.LPAREN)
            self.state = 254
            self.express()
            self.state = 255
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def express(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = ZCodeParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(ZCodeParser.FOR)
            self.state = 258
            self.match(ZCodeParser.ID)
            self.state = 259
            self.match(ZCodeParser.UNTIL)
            self.state = 260
            self.express()
            self.state = 261
            self.match(ZCodeParser.BY)
            self.state = 262
            self.express()
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.state = 263
                self.statement()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.state = 264
                self.ignore()
                self.state = 265
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continueStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = ZCodeParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(ZCodeParser.CONTINUE)
            self.state = 270
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = ZCodeParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ZCodeParser.BREAK)
            self.state = 273
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def express(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = ZCodeParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(ZCodeParser.RETURN)
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.LBRACK, ZCodeParser.ID, ZCodeParser.STRINGLIT, ZCodeParser.NUMBERLIT]:
                self.state = 276
                self.express()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 280
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def statementList(self):
            return self.getTypedRuleContext(ZCodeParser.StatementListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = ZCodeParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_blockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(ZCodeParser.BEGIN)
            self.state = 283
            self.ignore()
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 284
                self.statementList()
                pass

            elif la_ == 2:
                pass


            self.state = 288
            self.match(ZCodeParser.END)
            self.state = 289
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def expressList(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_callFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallFunction" ):
                return visitor.visitCallFunction(self)
            else:
                return visitor.visitChildren(self)




    def callFunction(self):

        localctx = ZCodeParser.CallFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_callFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(ZCodeParser.ID)
            self.state = 292
            self.match(ZCodeParser.LPAREN)
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.LBRACK, ZCodeParser.ID, ZCodeParser.STRINGLIT, ZCodeParser.NUMBERLIT]:
                self.state = 293
                self.expressList()
                pass
            elif token in [ZCodeParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 297
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def expressList(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_callStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = ZCodeParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_callStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(ZCodeParser.ID)
            self.state = 300
            self.match(ZCodeParser.LPAREN)
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.LBRACK, ZCodeParser.ID, ZCodeParser.STRINGLIT, ZCodeParser.NUMBERLIT]:
                self.state = 301
                self.expressList()
                pass
            elif token in [ZCodeParser.RPAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 305
            self.match(ZCodeParser.RPAREN)
            self.state = 306
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expressList(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expressList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressList" ):
                return visitor.visitExpressList(self)
            else:
                return visitor.visitChildren(self)




    def expressList(self):

        localctx = ZCodeParser.ExpressListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expressList)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.express()
                self.state = 309
                self.match(ZCodeParser.COMMA)
                self.state = 310
                self.expressList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.express()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Express1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Express1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_express

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpress" ):
                return visitor.visitExpress(self)
            else:
                return visitor.visitChildren(self)




    def express(self):

        localctx = ZCodeParser.ExpressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_express)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.express1()
                self.state = 316
                self.match(ZCodeParser.CONCAT)
                self.state = 317
                self.express1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.express1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Express1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Express2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Express2Context,i)


        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def EQEQ(self):
            return self.getToken(ZCodeParser.EQEQ, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LTE(self):
            return self.getToken(ZCodeParser.LTE, 0)

        def GTE(self):
            return self.getToken(ZCodeParser.GTE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_express1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpress1" ):
                return visitor.visitExpress1(self)
            else:
                return visitor.visitChildren(self)




    def express1(self):

        localctx = ZCodeParser.Express1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_express1)
        self._la = 0 # Token type
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.express2(0)
                self.state = 323
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ) | (1 << ZCodeParser.NEQ) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LTE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GTE) | (1 << ZCodeParser.EQEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 324
                self.express2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.express2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Express2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express3(self):
            return self.getTypedRuleContext(ZCodeParser.Express3Context,0)


        def express2(self):
            return self.getTypedRuleContext(ZCodeParser.Express2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_express2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpress2" ):
                return visitor.visitExpress2(self)
            else:
                return visitor.visitChildren(self)



    def express2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Express2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_express2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.express3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Express2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_express2)
                    self.state = 332
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 333
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 334
                    self.express3(0) 
                self.state = 339
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Express3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express4(self):
            return self.getTypedRuleContext(ZCodeParser.Express4Context,0)


        def express3(self):
            return self.getTypedRuleContext(ZCodeParser.Express3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_express3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpress3" ):
                return visitor.visitExpress3(self)
            else:
                return visitor.visitChildren(self)



    def express3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Express3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_express3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.express4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Express3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_express3)
                    self.state = 343
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 344
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 345
                    self.express4(0) 
                self.state = 350
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Express4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express5(self):
            return self.getTypedRuleContext(ZCodeParser.Express5Context,0)


        def express4(self):
            return self.getTypedRuleContext(ZCodeParser.Express4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_express4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpress4" ):
                return visitor.visitExpress4(self)
            else:
                return visitor.visitChildren(self)



    def express4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Express4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_express4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.express5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 359
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Express4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_express4)
                    self.state = 354
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 355
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 356
                    self.express5() 
                self.state = 361
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Express5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def express5(self):
            return self.getTypedRuleContext(ZCodeParser.Express5Context,0)


        def express6(self):
            return self.getTypedRuleContext(ZCodeParser.Express6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_express5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpress5" ):
                return visitor.visitExpress5(self)
            else:
                return visitor.visitChildren(self)




    def express5(self):

        localctx = ZCodeParser.Express5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_express5)
        try:
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(ZCodeParser.NOT)
                self.state = 363
                self.express5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.LPAREN, ZCodeParser.LBRACK, ZCodeParser.ID, ZCodeParser.STRINGLIT, ZCodeParser.NUMBERLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.express6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Express6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def express6(self):
            return self.getTypedRuleContext(ZCodeParser.Express6Context,0)


        def express7(self):
            return self.getTypedRuleContext(ZCodeParser.Express7Context,0)


        def express8(self):
            return self.getTypedRuleContext(ZCodeParser.Express8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_express6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpress6" ):
                return visitor.visitExpress6(self)
            else:
                return visitor.visitChildren(self)




    def express6(self):

        localctx = ZCodeParser.Express6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_express6)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.match(ZCodeParser.SUB)
                self.state = 368
                self.express6()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.express7()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 370
                self.express8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Express7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def callFunction(self):
            return self.getTypedRuleContext(ZCodeParser.CallFunctionContext,0)


        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def expressList(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressListContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_express7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpress7" ):
                return visitor.visitExpress7(self)
            else:
                return visitor.visitChildren(self)




    def express7(self):

        localctx = ZCodeParser.Express7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_express7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 373
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 374
                self.callFunction()
                pass


            self.state = 377
            self.match(ZCodeParser.LBRACK)
            self.state = 378
            self.expressList()
            self.state = 379
            self.match(ZCodeParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Express8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERLIT(self):
            return self.getToken(ZCodeParser.NUMBERLIT, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def arrayLiteral(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayLiteralContext,0)


        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def express(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def callFunction(self):
            return self.getTypedRuleContext(ZCodeParser.CallFunctionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_express8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpress8" ):
                return visitor.visitExpress8(self)
            else:
                return visitor.visitChildren(self)




    def express8(self):

        localctx = ZCodeParser.Express8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_express8)
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(ZCodeParser.NUMBERLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.match(ZCodeParser.STRINGLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 383
                self.match(ZCodeParser.TRUE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 384
                self.match(ZCodeParser.FALSE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 385
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 386
                self.arrayLiteral()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 387
                self.match(ZCodeParser.LPAREN)
                self.state = 388
                self.express()
                self.state = 389
                self.match(ZCodeParser.RPAREN)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 391
                self.callFunction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def expressList(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressListContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = ZCodeParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arrayLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(ZCodeParser.LBRACK)
            self.state = 395
            self.expressList()
            self.state = 396
            self.match(ZCodeParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 398
                self.match(ZCodeParser.NEWLINE)
                self.state = 401 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[35] = self.express2_sempred
        self._predicates[36] = self.express3_sempred
        self._predicates[37] = self.express4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def express2_sempred(self, localctx:Express2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def express3_sempred(self, localctx:Express3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def express4_sempred(self, localctx:Express4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




