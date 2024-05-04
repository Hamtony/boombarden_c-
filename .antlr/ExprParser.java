// Generated from d:/.cosas/.universidad/.Teoria de Compiladores/ODIOC+++++++++++++++++++++++/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, INT=14, FLOAT=15, WS=16, ID=17;
	public static final int
		RULE_program = 0, RULE_expr = 1, RULE_asing = 2, RULE_value = 3;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "expr", "asing", "value"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'+'", "'-'", "'>'", "'!'", "'*'", "'/'", "'%'", "'^'", 
			"'|'", "'('", "')'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, "INT", "FLOAT", "WS", "ID"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ExprParser.EOF, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<AsingContext> asing() {
			return getRuleContexts(AsingContext.class);
		}
		public AsingContext asing(int i) {
			return getRuleContext(AsingContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 184316L) != 0)) {
				{
				{
				setState(10);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(8);
					expr();
					}
					break;
				case 2:
					{
					setState(9);
					asing();
					}
					break;
				}
				setState(12);
				match(T__0);
				}
				}
				setState(18);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(19);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expr);
		int _la;
		try {
			setState(49);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(21);
				value();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(22);
				_la = _input.LA(1);
				if ( !(_la==T__1 || _la==T__2) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(23);
				expr();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				{
				setState(24);
				match(T__3);
				}
				setState(25);
				expr();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(26);
				match(T__4);
				setState(27);
				expr();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(28);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 448L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(29);
				expr();
				setState(30);
				expr();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(32);
				_la = _input.LA(1);
				if ( !(_la==T__1 || _la==T__2) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(33);
				expr();
				setState(34);
				expr();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(36);
				match(T__8);
				setState(37);
				expr();
				setState(38);
				expr();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(40);
				match(T__9);
				setState(41);
				expr();
				setState(42);
				match(T__9);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(44);
				match(T__10);
				setState(45);
				expr();
				setState(46);
				match(T__11);
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(48);
				value();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsingContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AsingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asing; }
	}

	public final AsingContext asing() throws RecognitionException {
		AsingContext _localctx = new AsingContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_asing);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(ID);
			setState(52);
			match(T__12);
			setState(53);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(ExprParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(ExprParser.FLOAT, 0); }
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 180224L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0011:\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0001\u0000\u0001\u0000\u0003"+
		"\u0000\u000b\b\u0000\u0001\u0000\u0001\u0000\u0005\u0000\u000f\b\u0000"+
		"\n\u0000\f\u0000\u0012\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0003\u00012\b\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0000"+
		"\u0000\u0004\u0000\u0002\u0004\u0006\u0000\u0003\u0001\u0000\u0002\u0003"+
		"\u0001\u0000\u0006\b\u0002\u0000\u000e\u000f\u0011\u0011@\u0000\u0010"+
		"\u0001\u0000\u0000\u0000\u00021\u0001\u0000\u0000\u0000\u00043\u0001\u0000"+
		"\u0000\u0000\u00067\u0001\u0000\u0000\u0000\b\u000b\u0003\u0002\u0001"+
		"\u0000\t\u000b\u0003\u0004\u0002\u0000\n\b\u0001\u0000\u0000\u0000\n\t"+
		"\u0001\u0000\u0000\u0000\u000b\f\u0001\u0000\u0000\u0000\f\r\u0005\u0001"+
		"\u0000\u0000\r\u000f\u0001\u0000\u0000\u0000\u000e\n\u0001\u0000\u0000"+
		"\u0000\u000f\u0012\u0001\u0000\u0000\u0000\u0010\u000e\u0001\u0000\u0000"+
		"\u0000\u0010\u0011\u0001\u0000\u0000\u0000\u0011\u0013\u0001\u0000\u0000"+
		"\u0000\u0012\u0010\u0001\u0000\u0000\u0000\u0013\u0014\u0005\u0000\u0000"+
		"\u0001\u0014\u0001\u0001\u0000\u0000\u0000\u00152\u0003\u0006\u0003\u0000"+
		"\u0016\u0017\u0007\u0000\u0000\u0000\u00172\u0003\u0002\u0001\u0000\u0018"+
		"\u0019\u0005\u0004\u0000\u0000\u00192\u0003\u0002\u0001\u0000\u001a\u001b"+
		"\u0005\u0005\u0000\u0000\u001b2\u0003\u0002\u0001\u0000\u001c\u001d\u0007"+
		"\u0001\u0000\u0000\u001d\u001e\u0003\u0002\u0001\u0000\u001e\u001f\u0003"+
		"\u0002\u0001\u0000\u001f2\u0001\u0000\u0000\u0000 !\u0007\u0000\u0000"+
		"\u0000!\"\u0003\u0002\u0001\u0000\"#\u0003\u0002\u0001\u0000#2\u0001\u0000"+
		"\u0000\u0000$%\u0005\t\u0000\u0000%&\u0003\u0002\u0001\u0000&\'\u0003"+
		"\u0002\u0001\u0000\'2\u0001\u0000\u0000\u0000()\u0005\n\u0000\u0000)*"+
		"\u0003\u0002\u0001\u0000*+\u0005\n\u0000\u0000+2\u0001\u0000\u0000\u0000"+
		",-\u0005\u000b\u0000\u0000-.\u0003\u0002\u0001\u0000./\u0005\f\u0000\u0000"+
		"/2\u0001\u0000\u0000\u000002\u0003\u0006\u0003\u00001\u0015\u0001\u0000"+
		"\u0000\u00001\u0016\u0001\u0000\u0000\u00001\u0018\u0001\u0000\u0000\u0000"+
		"1\u001a\u0001\u0000\u0000\u00001\u001c\u0001\u0000\u0000\u00001 \u0001"+
		"\u0000\u0000\u00001$\u0001\u0000\u0000\u00001(\u0001\u0000\u0000\u0000"+
		"1,\u0001\u0000\u0000\u000010\u0001\u0000\u0000\u00002\u0003\u0001\u0000"+
		"\u0000\u000034\u0005\u0011\u0000\u000045\u0005\r\u0000\u000056\u0003\u0002"+
		"\u0001\u00006\u0005\u0001\u0000\u0000\u000078\u0007\u0002\u0000\u0000"+
		"8\u0007\u0001\u0000\u0000\u0000\u0003\n\u00101";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}