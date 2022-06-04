Name:           aw-debian-11-salt
Version:  	1.1
Release:        1%{?dist}
Summary:        Salt debian-11-template in Qubes

License:        GPLv3+
SOURCE0:	templates

%description
Salt state to implement debian-11 template in Qubes

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/srv/salt
cp -rv %{SOURCE0}/*  %{buildroot}/srv/salt

%files
%defattr(-,root,root,-)
/srv/salt/*

%post
if [ $1 -eq 1 ]; then
  qubesctl state.apply template-debian-11
fi


%changelog
* Sat Jun 04 2022 alexwaibel <alexwaibel@users.noreply.github.com> - 1.1
- Standardize package names with aw prefix
* Sun May 15 2022 unman <unman@thirdeyesecurity.org> - 1.0
- First Build
