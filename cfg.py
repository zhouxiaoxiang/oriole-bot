config = {
    'svn':  'svn://xxxxxxx/%s/trunk/',
    'user': 'xxx',
    'pass': 'xxx',
    'poll': 5,
    'cmds': ['pip install pytest; pytest'],
    'srcs': [
        "user",
    ],
    'mail': {
        'fromaddr': "x@y",
        'sendToInterestedUsers': False,
        'extraRecipients': ["x@y"],
        'relayhost': "smtp.163.com",
        'smtpPort': 25,
        'smtpUser': "xxx",
        'smtpPassword': "xxx",
    },
    'web': "http://localhost:8000/",
}
