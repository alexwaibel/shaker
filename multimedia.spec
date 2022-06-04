Name:           aw-qubes-sys-multimedia-salt
Version:  	2.2
Release:        1%{?dist}
Summary:        Salt multimedia template and qubes

License:        GPLv3+
SOURCE0:	multimedia

%description
Salt state for multimedia template and qubes

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/srv/salt
cp -rv %{SOURCE0}/  %{buildroot}/srv/salt

%files
%defattr(-,root,root,-)
/srv/salt/multimedia/*

%post
if [ $1 -eq 1 ]; then
  qubesctl state.apply multimedia.clone
  qubesctl --skip-dom0 --targets=template-multimedia state.apply multimedia.install
  qubesctl state.apply multimedia.create
  qubesctl --skip-dom0 --targets=media state.apply multimedia.configure
fi

%changelog
* Sat Jun 04 2022 alexwaibel <alexwaibel@users.noreply.github.com> - 2.2
- Standardize package names with aw prefix
* Sat May 21 2022 unman <unman@thirdeyesecurity.org> - 2.1
- Standardise package names to 3isec-
* Sun May 15 2022 unman <unman@thirdeyesecurity.org> - 2.0
- Add post install salting
* Wed Feb 03 2021 unman <unman@thirdeyesecurity.org>
- First Build
