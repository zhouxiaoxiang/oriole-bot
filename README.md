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
    'svn':  'svn://xxxxxx/%s/trunk/',
    'user': 'xxx',
    'pass': 'xxx',
    'poll': 2,
    'cmds': ['python -mvenv venv', 'source venv/bin/activate; make; o c /ms/dev; pytest'],
    'srcs': [
        'user',
    ]
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

http://localhost:8000
