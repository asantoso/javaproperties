from javaproperties import loads

def test_loads_simple():
    assert loads('key=value') == {"key": "value"}

def test_loads_key_only():
    assert loads("key") == {"key": ""}

def test_loads_space_equals():
    assert loads("key =value") == {"key": "value"}

def test_loads_equals_space():
    assert loads("key= value") == {"key": "value"}

def test_loads_padded_equals():
    assert loads("key = value") == {"key": "value"}

def test_loads_nokey():
    assert loads("=value") == {"": "value"}

def test_loads_spacekey():
    assert loads(" =value") == {"": "value"}

def test_loads_trailing_space():
    assert loads("key=value ") == {"key": "value "}

def test_loads_leading_space():
    assert loads(" key=value") == {"key": "value"}

def test_loads_space_equals_space():
    assert loads(' = ') == {"": ""}

def test_loads_equals_only():
    assert loads('=') == {"": ""}

def test_loads_nothing():
    assert loads('') == {}

def test_loads_space():
    assert loads(' ') == {}

def test_loads_linefeed():
    assert loads('\n') == {}

def test_loads_crlf():
    assert loads('\r\n') == {}

def test_loads_cr():
    assert loads('\r') == {}

def test_loads_comment():
    assert loads('#This is a comment.') == {}

def test_loads_comment_key_value():
    assert loads('#This is a comment.\nkey = value') == {"key": "value"}

def test_loads_key_value_comment():
    assert loads('key = value\n#This is a comment.') == {"key": "value"}

def test_loads_bang_comment():
    assert loads('!This is a comment.') == {}

def test_loads_bang_comment_key_value():
    assert loads('!This is a comment.\nkey = value') == {"key": "value"}

def test_loads_key_value_bang_comment():
    assert loads('key = value\n!This is a comment.') == {"key": "value"}

def test_loads_continued_value():
    assert loads('key = val\\\nue') == {"key": "value"}

def test_loads_continued_value_spaced():
    assert loads('key = val\\\n    ue') == {"key": "value"}

def test_loads_continued_key():
    assert loads('ke\\\ny = value') == {"key": "value"}

def test_loads_continued_key_spaced():
    assert loads('ke\\\n    y = value') == {"key": "value"}

def test_loads_three_words():
    assert loads('one two three') == {"one": "two three"}

def test_loads_simple_linefeed():
    assert loads('key=value\n') == {"key": "value"}

def test_loads_simple_crlf():
    assert loads('key=value\r\n') == {"key": "value"}

def test_loads_simple_cr():
    assert loads('key=value\r') == {"key": "value"}

def test_loads_key_colon_value():
    assert loads('key:value') == {"key": "value"}

def test_loads_key_space_value():
    assert loads('key value') == {"key": "value"}

def test_loads_surrogate_pair():
    assert loads('goat = \\uD83D\\uDC10') == {"goat": u"\U0001F410"}

def test_loads_bad_surrogate():
    assert loads('taog = \\uDC10\\uD83D') == {"taog": u"\uDC10\uD83D"}

def test_loads_continue_comment():
    assert loads('key = value\\\n    # comment') == {"key": "value# comment"}

def test_loads_continue_empty():
    assert loads('key = value\\\n') == {"key": "value"}

def test_loads_continue_EOF():
    assert loads('key = value\\') == {"key": "value"}

def test_loads_continue_space():
    assert loads('key = value\\\n    ') == {"key": "value"}

def test_loads_comment_continue():
    assert loads('# comment\\\nkey = value') == {"key": "value"}

def test_loads_blank_continue():
    assert loads('\\\n') == {}

def test_loads_continue_pair():
    assert loads('\\\nkey = value') == {"key": "value"}

def test_loads_space_continue_pair():
    assert loads(' \\\nkey = value') == {"key": "value"}

def test_loads_multiple():
    assert loads('key = value\nfoo = bar') == {"key": "value", "foo": "bar"}

def test_loads_reassign():
    assert loads('key = value1\nkey = value2') == {"key": "value2"}

def test_loads_bmp_escape():
    assert loads('snowman = \\u2603') == {"snowman": u"\u2603"}

def test_loads_latin1_escape():
    assert loads('pokmon = \\u00E9') == {"pokmon": u"\u00E9"}

def test_loads_long_escape():
    assert loads('newline = \\u000a') == {"newline": "\n"}

def test_loads_continue_continue():
    assert loads('key = value\\\n\\\nend') == {"key": "valueend"}

def test_loads_continue_space_continue():
    assert loads('key = value\\\n    \\\nend') == {"key": "valueend"}

def test_loads_escaped_continue():
    assert loads('key = value\\\\\nend') == {"key": "value\\", "end": ""}

def test_loads_hash_in_key():
    assert loads('c#sharp = sucks') == {"c#sharp": "sucks"}

def test_loads_hash_in_value():
    assert loads('fifth = #5') == {"fifth": "#5"}


# \n, \r, etc. escape sequences
# escaped space/=/: in key
# escaped non-special character
# blank lines
# multiple backslashes (even & odd numbers) in a row
# `str`s in Python 2