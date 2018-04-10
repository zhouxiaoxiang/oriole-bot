config = {
    'svn':  'svn://xxxxxx/%s/trunk/',
    'user': 'xxx',
    'pass': 'xxx',
    'poll': 2,
    'cmds': ['virtualenv venv', 'source venv/bin/activate; make; o c /ms/dev; pytest'],
    'srcs': [
        "activity",
        "config",
        "consumer",
        "log",
        "machine",
        "mail",
        "merchandise",
        "payment",
        "report",
        "transaction",
        "user",
    ]
}
