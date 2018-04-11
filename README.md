# Oriole-bot 

Test oriole-service based projects.

1. Create python3 environment
```
    cd /opt/oriole-bot/
    python -mvenv venv
    source venv/bin/activate
    make
```

2. Edit cfg.py 

For svn://xxxxxx/user/trunk/, edit as follows:
```
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
```

3. start 
```
    make start
```

4. stop
```
    make stop
```

5. clean
```
    make clean
```

6. web
```
    http://localhost:8000
```
