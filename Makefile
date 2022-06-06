all: setup cacher debian-11-minimal debian-11 gpg multimedia openvpn print qubes-ssh-agent
	echo "Making All"

.PHONY: cacher debian-11-minimal debian-11 gpg multimedia openvpn print qubes-ssh-agent

setup:
	rm -rf ./openvpn/.git ./qubes-ssh-agent/.git
	sudo dnf install fedora-packager rpmdevtools gcc
	rpmdev-setuptree
	echo "Copying spec files"
	cp *.spec ~/rpmbuild/SPECS
	echo "Copying source files"
	find . -type d -not -path '*/.*' -not -path '.' -exec cp -rt "${HOME}/rpmbuild/SOURCES" {} +

cacher:
	rpmbuild -bb "${HOME}/rpmbuild/SPECS/cacher.spec"

debian-11-minimal:
	rpmbuild -bb "${HOME}/rpmbuild/SPECS/debian-11-minimal.spec"

debian-11:
	rpmbuild -bb "${HOME}/rpmbuild/SPECS/debian-11.spec"

gpg:
	rpmbuild -bb "${HOME}/rpmbuild/SPECS/gpg.spec"

multimedia:
	rpmbuild -bb "${HOME}/rpmbuild/SPECS/multimedia.spec"

openvpn:
	rpmbuild -bb "${HOME}/rpmbuild/SPECS/openvpn.spec"

print:
	rpmbuild -bb "${HOME}/rpmbuild/SPECS/print.spec"

qubes-ssh-agent:
	rpmbuild -bb "${HOME}/rpmbuild/SPECS/qubes-ssh-agent.spec"