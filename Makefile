all: setup cacher
	echo "Making All"

setup:
	sudo dnf install fedora-packager rpmdevtools gcc
	rpmdev-setuptree
	echo "Copying spec files"
	cp *.spec ~/rpmbuild/SPECS
	echo "Copying source files"
	find . -type d -not -path '*/.*' -not -path '.' -exec cp -rt $HOME/rpmbuild/SOURCES {} +

cacher:
	rpmbuild -bb $HOME/rpmbuild/SPECS/cacher.spec
