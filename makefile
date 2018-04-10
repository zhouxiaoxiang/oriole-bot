.PHONY: all start stop clean

mpro := buildbot
wpro := buildbot-worker
mdir := oriole_bot/master/master
wdir := oriole_bot/worker/worker

all:
	@python setup.py develop

start:
	@$(mpro) start $(mdir)
	@$(wpro) start $(wdir)

stop:
	@$(mpro) stop $(mdir)
	@$(wpro) stop $(wdir)

clean:
	@$(mpro) cleanupdb $(mdir)
