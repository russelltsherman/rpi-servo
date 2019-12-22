
packages = python3-pip python3-dev

## install required apt packages
apt:
	sudo apt install -y $(packages)
.PHONY: apt

## install project requirements
bootstrap: apt
	sudo pip3 install -r requirements.txt
.PHONY: bootstrap

## update repo and update dependencies
update:
	git pull
	sudo apt-get update
	make bootstrap
.PHONY: update
