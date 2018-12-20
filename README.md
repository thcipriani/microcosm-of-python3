# Microcosm of Python3

## Types

An outline of the various types in different versions and what they store.

type | Python3 | Python2
--- | --- | ---
`<type 'str'>` | unicode | ascii (also, `bytes`, ugh)
`<type 'unicode'>` | `¯\_(ツ)_/¯` (not a thing) | unicode
`<class 'bytes'>` | `bytes` | alias for `str`

The thing to notices is Python2 -> Python3 `str` becomes `unicode`; `unicode`
-> nothing; and `bytes` becomes `str`. This is because Python capricious and
malicious.

## Functions and the types they return

func | Python3 | Python2
--- | --- | ---
`'quoted text'` | `<type 'str'>` (which is unicode) | `<type 'str'>` (which is ascii)
`u'text'` | `<type 'str'>` | `<type 'unicode'>`
`b'text'` | `<class 'bytes'>` | `<type 'str'>`
`<str>.decode('utf-8')` | `AttributeError` | `<type 'unicode'>`
`<str>.encode('utf-8')` | `<class 'bytes'>` | `UnicodeDecodeError` or `<type 'str'>` (depending on if it contains charscodes > 255)
`<bytes>.decode('utf-8')` | `<type 'str'>` | `bytes` is an alias for `str`
`<bytes>.encode('utf-8')` | `AttributeError` | `bytes` is an alias for `str`
`with(open, 'rt')` | `<type 'str'>` | `<type 'str'>`
`with(open, 'rt')` | `<type 'str'>` | str
