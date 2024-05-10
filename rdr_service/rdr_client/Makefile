.venv:
	#conda create -n py311 python=3.11 pip
	# "creating python3 virtual env"
	python3 -m pip install --upgrade pip
	python3 -m pip install virtualenv
	python3 -m virtualenv .venv
	. ./.venv/bin/activate &&\
	python3 -m pip install --upgrade pip &&\
	python3 -m pip install -r requirements.txt &&\
	python3 -m pip freeze > requirements_pip_freeze.txt &&\
	which pip3 && which python3 && python3 --version

work_queue: .venv
	. ./.venv/bin/activate &&\
	./run_client.sh --project all-of-us-rdr-prod --account ${ALLOFUS_PMI_OPS_ORG_ACCOUNT} --service_account ${ALLOFUS_SERVICE_ACCOUNT} work_queue.py
