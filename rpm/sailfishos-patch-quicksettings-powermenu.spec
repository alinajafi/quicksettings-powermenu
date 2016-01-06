Name: sailfishos-patch-quicksettings-powermenu
BuildArch: noarch
Summary: Adds quick settings to top edge swipe power menu
Version: 0.7
Release: 1
Group: System/Patches
License: GPLv3
Source0: %{name}-%{version}.tar.xz
Requires: patchmanager
Requires: sailfish-version >= 2.0.0

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}


%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}

mkdir -p %{buildroot}/usr/share/themes/jolla-ambient/meegotouch/z1.0/icons/
cp -r icons/* %{buildroot}/usr/share/themes/jolla-ambient/meegotouch/z1.0/icons/

mkdir -p %{buildroot}/usr/share/jolla-settings/pages/%{name}
cp -r settings/*.qml %{buildroot}/usr/share/jolla-settings/pages/%{name}
cp -r settings/*.png %{buildroot}/usr/share/jolla-settings/pages/%{name}
mkdir -p %{buildroot}/usr/share/jolla-settings/entries
cp -r settings/*.json %{buildroot}/usr/share/jolla-settings/entries/

mkdir -p %{buildroot}/usr/share/translations
cp -r translations/* %{buildroot}/usr/share/translations

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}
%{_datadir}/themes/jolla-ambient/meegotouch/z1.0/icons/
%{_datadir}/jolla-settings/entries
%{_datadir}/jolla-settings/pages
%{_datadir}/translations
