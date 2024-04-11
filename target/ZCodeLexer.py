# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u018e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\7+\u0119\n")
        buf.write("+\f+\16+\u011c\13+\3,\3,\3-\3-\3.\3.\5.\u0124\n.\3/\3")
        buf.write("/\3/\3/\3/\3/\7/\u012c\n/\f/\16/\u012f\13/\3/\3/\3/\3")
        buf.write("\60\3\60\3\60\5\60\u0137\n\60\3\60\5\60\u013a\n\60\5\60")
        buf.write("\u013c\n\60\3\61\6\61\u013f\n\61\r\61\16\61\u0140\3\62")
        buf.write("\3\62\7\62\u0145\n\62\f\62\16\62\u0148\13\62\3\63\3\63")
        buf.write("\5\63\u014c\n\63\3\63\6\63\u014f\n\63\r\63\16\63\u0150")
        buf.write("\3\64\3\64\3\65\6\65\u0156\n\65\r\65\16\65\u0157\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\7\66\u0160\n\66\f\66\16\66\u0163")
        buf.write("\13\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\7\67\u016d")
        buf.write("\n\67\f\67\16\67\u0170\13\67\3\67\3\67\3\67\5\67\u0175")
        buf.write("\n\67\3\67\3\67\38\38\38\58\u017c\n8\39\39\39\39\39\3")
        buf.write("9\79\u0184\n9\f9\169\u0187\139\39\39\39\3:\3:\3:\2\2;")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W\2Y\2[-]._/a\2c\2e\2g\60i\61k\62m\63o\2q\64s\65")
        buf.write("\3\2\20\5\2C\\aac|\6\2\62;C\\aac|\6\2\f\f\16\17$$^^\t")
        buf.write("\2))^^ddhhppttvv\3\2))\3\2$$\3\2\62;\4\2GGgg\4\2--//\3")
        buf.write("\2\f\f\5\2\n\13\16\17\"\"\4\2\f\f\16\17\3\3\f\f\4\2\n")
        buf.write("\n\16\17\2\u019d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2")
        buf.write("_\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\3u\3\2\2\2\5z\3\2\2\2\7\u0080\3")
        buf.write("\2\2\2\t\u0087\3\2\2\2\13\u008c\3\2\2\2\r\u0093\3\2\2")
        buf.write("\2\17\u009a\3\2\2\2\21\u009e\3\2\2\2\23\u00a6\3\2\2\2")
        buf.write("\25\u00ab\3\2\2\2\27\u00af\3\2\2\2\31\u00b5\3\2\2\2\33")
        buf.write("\u00b8\3\2\2\2\35\u00be\3\2\2\2\37\u00c7\3\2\2\2!\u00ca")
        buf.write("\3\2\2\2#\u00cf\3\2\2\2%\u00d4\3\2\2\2\'\u00da\3\2\2\2")
        buf.write(")\u00de\3\2\2\2+\u00e0\3\2\2\2-\u00e2\3\2\2\2/\u00e4\3")
        buf.write("\2\2\2\61\u00e6\3\2\2\2\63\u00e8\3\2\2\2\65\u00ea\3\2")
        buf.write("\2\2\67\u00ed\3\2\2\29\u00f0\3\2\2\2;\u00f2\3\2\2\2=\u00f5")
        buf.write("\3\2\2\2?\u00f7\3\2\2\2A\u00fa\3\2\2\2C\u00fe\3\2\2\2")
        buf.write("E\u0101\3\2\2\2G\u0105\3\2\2\2I\u0108\3\2\2\2K\u010c\3")
        buf.write("\2\2\2M\u010e\3\2\2\2O\u0110\3\2\2\2Q\u0112\3\2\2\2S\u0114")
        buf.write("\3\2\2\2U\u0116\3\2\2\2W\u011d\3\2\2\2Y\u011f\3\2\2\2")
        buf.write("[\u0123\3\2\2\2]\u0125\3\2\2\2_\u0133\3\2\2\2a\u013e\3")
        buf.write("\2\2\2c\u0142\3\2\2\2e\u0149\3\2\2\2g\u0152\3\2\2\2i\u0155")
        buf.write("\3\2\2\2k\u015b\3\2\2\2m\u0166\3\2\2\2o\u017b\3\2\2\2")
        buf.write("q\u017d\3\2\2\2s\u018b\3\2\2\2uv\7v\2\2vw\7t\2\2wx\7w")
        buf.write("\2\2xy\7g\2\2y\4\3\2\2\2z{\7h\2\2{|\7c\2\2|}\7n\2\2}~")
        buf.write("\7u\2\2~\177\7g\2\2\177\6\3\2\2\2\u0080\u0081\7p\2\2\u0081")
        buf.write("\u0082\7w\2\2\u0082\u0083\7o\2\2\u0083\u0084\7d\2\2\u0084")
        buf.write("\u0085\7g\2\2\u0085\u0086\7t\2\2\u0086\b\3\2\2\2\u0087")
        buf.write("\u0088\7d\2\2\u0088\u0089\7q\2\2\u0089\u008a\7q\2\2\u008a")
        buf.write("\u008b\7n\2\2\u008b\n\3\2\2\2\u008c\u008d\7u\2\2\u008d")
        buf.write("\u008e\7v\2\2\u008e\u008f\7t\2\2\u008f\u0090\7k\2\2\u0090")
        buf.write("\u0091\7p\2\2\u0091\u0092\7i\2\2\u0092\f\3\2\2\2\u0093")
        buf.write("\u0094\7t\2\2\u0094\u0095\7g\2\2\u0095\u0096\7v\2\2\u0096")
        buf.write("\u0097\7w\2\2\u0097\u0098\7t\2\2\u0098\u0099\7p\2\2\u0099")
        buf.write("\16\3\2\2\2\u009a\u009b\7x\2\2\u009b\u009c\7c\2\2\u009c")
        buf.write("\u009d\7t\2\2\u009d\20\3\2\2\2\u009e\u009f\7f\2\2\u009f")
        buf.write("\u00a0\7{\2\2\u00a0\u00a1\7p\2\2\u00a1\u00a2\7c\2\2\u00a2")
        buf.write("\u00a3\7o\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5\7e\2\2\u00a5")
        buf.write("\22\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8\7w\2\2\u00a8")
        buf.write("\u00a9\7p\2\2\u00a9\u00aa\7e\2\2\u00aa\24\3\2\2\2\u00ab")
        buf.write("\u00ac\7h\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7t\2\2\u00ae")
        buf.write("\26\3\2\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1\7p\2\2\u00b1")
        buf.write("\u00b2\7v\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4\7n\2\2\u00b4")
        buf.write("\30\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6\u00b7\7{\2\2\u00b7")
        buf.write("\32\3\2\2\2\u00b8\u00b9\7d\2\2\u00b9\u00ba\7t\2\2\u00ba")
        buf.write("\u00bb\7g\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7m\2\2\u00bd")
        buf.write("\34\3\2\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0\7q\2\2\u00c0")
        buf.write("\u00c1\7p\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3\7k\2\2\u00c3")
        buf.write("\u00c4\7p\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6\7g\2\2\u00c6")
        buf.write("\36\3\2\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9\7h\2\2\u00c9")
        buf.write(" \3\2\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7n\2\2\u00cc")
        buf.write("\u00cd\7u\2\2\u00cd\u00ce\7g\2\2\u00ce\"\3\2\2\2\u00cf")
        buf.write("\u00d0\7g\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2\7k\2\2\u00d2")
        buf.write("\u00d3\7h\2\2\u00d3$\3\2\2\2\u00d4\u00d5\7d\2\2\u00d5")
        buf.write("\u00d6\7g\2\2\u00d6\u00d7\7i\2\2\u00d7\u00d8\7k\2\2\u00d8")
        buf.write("\u00d9\7p\2\2\u00d9&\3\2\2\2\u00da\u00db\7g\2\2\u00db")
        buf.write("\u00dc\7p\2\2\u00dc\u00dd\7f\2\2\u00dd(\3\2\2\2\u00de")
        buf.write("\u00df\7-\2\2\u00df*\3\2\2\2\u00e0\u00e1\7/\2\2\u00e1")
        buf.write(",\3\2\2\2\u00e2\u00e3\7,\2\2\u00e3.\3\2\2\2\u00e4\u00e5")
        buf.write("\7\61\2\2\u00e5\60\3\2\2\2\u00e6\u00e7\7\'\2\2\u00e7\62")
        buf.write("\3\2\2\2\u00e8\u00e9\7?\2\2\u00e9\64\3\2\2\2\u00ea\u00eb")
        buf.write("\7>\2\2\u00eb\u00ec\7/\2\2\u00ec\66\3\2\2\2\u00ed\u00ee")
        buf.write("\7#\2\2\u00ee\u00ef\7?\2\2\u00ef8\3\2\2\2\u00f0\u00f1")
        buf.write("\7>\2\2\u00f1:\3\2\2\2\u00f2\u00f3\7>\2\2\u00f3\u00f4")
        buf.write("\7?\2\2\u00f4<\3\2\2\2\u00f5\u00f6\7@\2\2\u00f6>\3\2\2")
        buf.write("\2\u00f7\u00f8\7@\2\2\u00f8\u00f9\7?\2\2\u00f9@\3\2\2")
        buf.write("\2\u00fa\u00fb\7\60\2\2\u00fb\u00fc\7\60\2\2\u00fc\u00fd")
        buf.write("\7\60\2\2\u00fdB\3\2\2\2\u00fe\u00ff\7?\2\2\u00ff\u0100")
        buf.write("\7?\2\2\u0100D\3\2\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7p\2\2\u0103\u0104\7f\2\2\u0104F\3\2\2\2\u0105\u0106")
        buf.write("\7q\2\2\u0106\u0107\7t\2\2\u0107H\3\2\2\2\u0108\u0109")
        buf.write("\7p\2\2\u0109\u010a\7q\2\2\u010a\u010b\7v\2\2\u010bJ\3")
        buf.write("\2\2\2\u010c\u010d\7*\2\2\u010dL\3\2\2\2\u010e\u010f\7")
        buf.write("+\2\2\u010fN\3\2\2\2\u0110\u0111\7]\2\2\u0111P\3\2\2\2")
        buf.write("\u0112\u0113\7_\2\2\u0113R\3\2\2\2\u0114\u0115\7.\2\2")
        buf.write("\u0115T\3\2\2\2\u0116\u011a\5W,\2\u0117\u0119\5Y-\2\u0118")
        buf.write("\u0117\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2")
        buf.write("\u011a\u011b\3\2\2\2\u011bV\3\2\2\2\u011c\u011a\3\2\2")
        buf.write("\2\u011d\u011e\t\2\2\2\u011eX\3\2\2\2\u011f\u0120\t\3")
        buf.write("\2\2\u0120Z\3\2\2\2\u0121\u0124\5\3\2\2\u0122\u0124\5")
        buf.write("\5\3\2\u0123\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124\\")
        buf.write("\3\2\2\2\u0125\u012d\7$\2\2\u0126\u012c\n\4\2\2\u0127")
        buf.write("\u0128\7^\2\2\u0128\u012c\t\5\2\2\u0129\u012a\t\6\2\2")
        buf.write("\u012a\u012c\t\7\2\2\u012b\u0126\3\2\2\2\u012b\u0127\3")
        buf.write("\2\2\2\u012b\u0129\3\2\2\2\u012c\u012f\3\2\2\2\u012d\u012b")
        buf.write("\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u0130\3\2\2\2\u012f")
        buf.write("\u012d\3\2\2\2\u0130\u0131\7$\2\2\u0131\u0132\b/\2\2\u0132")
        buf.write("^\3\2\2\2\u0133\u013b\5a\61\2\u0134\u013c\5c\62\2\u0135")
        buf.write("\u0137\5c\62\2\u0136\u0135\3\2\2\2\u0136\u0137\3\2\2\2")
        buf.write("\u0137\u0139\3\2\2\2\u0138\u013a\5e\63\2\u0139\u0138\3")
        buf.write("\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c\3\2\2\2\u013b\u0134")
        buf.write("\3\2\2\2\u013b\u0136\3\2\2\2\u013c`\3\2\2\2\u013d\u013f")
        buf.write("\t\b\2\2\u013e\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140")
        buf.write("\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141b\3\2\2\2\u0142")
        buf.write("\u0146\7\60\2\2\u0143\u0145\t\b\2\2\u0144\u0143\3\2\2")
        buf.write("\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147")
        buf.write("\3\2\2\2\u0147d\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014b")
        buf.write("\t\t\2\2\u014a\u014c\t\n\2\2\u014b\u014a\3\2\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c\u014e\3\2\2\2\u014d\u014f\t\b\2\2")
        buf.write("\u014e\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u014e\3")
        buf.write("\2\2\2\u0150\u0151\3\2\2\2\u0151f\3\2\2\2\u0152\u0153")
        buf.write("\t\13\2\2\u0153h\3\2\2\2\u0154\u0156\t\f\2\2\u0155\u0154")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0155\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\b\65\3")
        buf.write("\2\u015aj\3\2\2\2\u015b\u015c\7%\2\2\u015c\u015d\7%\2")
        buf.write("\2\u015d\u0161\3\2\2\2\u015e\u0160\n\r\2\2\u015f\u015e")
        buf.write("\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2\u0161")
        buf.write("\u0162\3\2\2\2\u0162\u0164\3\2\2\2\u0163\u0161\3\2\2\2")
        buf.write("\u0164\u0165\b\66\3\2\u0165l\3\2\2\2\u0166\u016e\7$\2")
        buf.write("\2\u0167\u016d\n\4\2\2\u0168\u0169\7^\2\2\u0169\u016d")
        buf.write("\t\5\2\2\u016a\u016b\t\6\2\2\u016b\u016d\t\7\2\2\u016c")
        buf.write("\u0167\3\2\2\2\u016c\u0168\3\2\2\2\u016c\u016a\3\2\2\2")
        buf.write("\u016d\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3")
        buf.write("\2\2\2\u016f\u0174\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0172")
        buf.write("\7\17\2\2\u0172\u0175\7\f\2\2\u0173\u0175\t\16\2\2\u0174")
        buf.write("\u0171\3\2\2\2\u0174\u0173\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0177\b\67\4\2\u0177n\3\2\2\2\u0178\u017c\t\17")
        buf.write("\2\2\u0179\u017a\7^\2\2\u017a\u017c\n\5\2\2\u017b\u0178")
        buf.write("\3\2\2\2\u017b\u0179\3\2\2\2\u017cp\3\2\2\2\u017d\u0185")
        buf.write("\7$\2\2\u017e\u0184\n\4\2\2\u017f\u0180\7^\2\2\u0180\u0184")
        buf.write("\t\5\2\2\u0181\u0182\t\6\2\2\u0182\u0184\t\7\2\2\u0183")
        buf.write("\u017e\3\2\2\2\u0183\u017f\3\2\2\2\u0183\u0181\3\2\2\2")
        buf.write("\u0184\u0187\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3")
        buf.write("\2\2\2\u0186\u0188\3\2\2\2\u0187\u0185\3\2\2\2\u0188\u0189")
        buf.write("\5o8\2\u0189\u018a\b9\5\2\u018ar\3\2\2\2\u018b\u018c\13")
        buf.write("\2\2\2\u018c\u018d\b:\6\2\u018dt\3\2\2\2\26\2\u011a\u0123")
        buf.write("\u012b\u012d\u0136\u0139\u013b\u0140\u0146\u014b\u0150")
        buf.write("\u0157\u0161\u016c\u016e\u0174\u017b\u0183\u0185\7\3/")
        buf.write("\2\b\2\2\3\67\3\39\4\3:\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    ADD = 20
    SUB = 21
    MUL = 22
    DIV = 23
    MOD = 24
    EQ = 25
    ASSIGN = 26
    NEQ = 27
    LT = 28
    LTE = 29
    GT = 30
    GTE = 31
    CONCAT = 32
    EQEQ = 33
    AND = 34
    OR = 35
    NOT = 36
    LPAREN = 37
    RPAREN = 38
    LBRACK = 39
    RBRACK = 40
    COMMA = 41
    ID = 42
    BOOLEAN = 43
    STRINGLIT = 44
    NUMBERLIT = 45
    NEWLINE = 46
    WS = 47
    COMMENTS = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'and'", "'or'", 
            "'not'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "EQ", "ASSIGN", "NEQ", "LT", "LTE", "GT", "GTE", "CONCAT", 
            "EQEQ", "AND", "OR", "NOT", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
            "COMMA", "ID", "BOOLEAN", "STRINGLIT", "NUMBERLIT", "NEWLINE", 
            "WS", "COMMENTS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "ADD", 
                  "SUB", "MUL", "DIV", "MOD", "EQ", "ASSIGN", "NEQ", "LT", 
                  "LTE", "GT", "GTE", "CONCAT", "EQEQ", "AND", "OR", "NOT", 
                  "LPAREN", "RPAREN", "LBRACK", "RBRACK", "COMMA", "ID", 
                  "IDSTART", "IDCHAR", "BOOLEAN", "STRINGLIT", "NUMBERLIT", 
                  "INT", "DEC", "EXP", "NEWLINE", "WS", "COMMENTS", "UNCLOSE_STRING", 
                  "ILLEGAL", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[45] = self.STRINGLIT_action 
            actions[53] = self.UNCLOSE_STRING_action 
            actions[55] = self.ILLEGAL_ESCAPE_action 
            actions[56] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

               if (len(self.text) >= 2 and self.text[-2:] == '\r\n'):
                  raise UncloseString(self.text[1:-2])
               elif self.text[-1] == '\n':
                  raise UncloseString(self.text[1:-1])
               else:
                  raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise IllegalEscape(self.text[1:]);

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


