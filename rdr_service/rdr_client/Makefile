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

config_check:
	# print date
	date 
	# make sure you are calling the function from institute network(ACL)
	curl ipinfo.io/ip

	# log in gcloud
	gcloud auth login

work_queue: .venv
	. ./.venv/bin/activate &&\
	./run_client.sh --project ${ALLOFUS_PROJECT_ID} --account ${ALLOFUS_PMI_OPS_ORG_ACCOUNT} --service_account ${ALLOFUS_SERVICE_ACCOUNT} work_queue.py
