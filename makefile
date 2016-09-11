# Microservices Project Make File

VIRTUALENV = $(shell which virtualenv)

clean: shutdown
	rm -rf microservices.egg-info
	rm -rf venv

venv:
	$(VIRTUALENV) venv

install: clean venv
	. venv/bin/activate; python setup.py install
	. venv/bin/activate; python setup.py develop

launch: venv shutdown
	. venv/bin/activate; python  services/pig_latin.py &

shutdown:
	ps -ef | grep "services/pig_latin.py" | grep -v grep | awk '{print $$2}' | xargs kill  

