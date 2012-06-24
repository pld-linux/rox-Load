%define _name Load
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	ROX-Load displays the load average of Your system
Summary(pl):	ROX-Load wy�wietla �rednie obci��enie Twojego systemu
Name:		rox-%{_name}
Version:	2.1.2
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tar.gz
# Source0-md5:	da82394fd9874e1930b7fc2fa01c642b
Source1:	%{name}.desktop
#Patch0:	%{name}-paths-fix.patch
Patch1:		%{name}-ROX-CLib2-include.patch
Patch2:		%{name}-ROX-apps-paths.patch
Patch3:		%{name}-aclocal.patch
URL:		http://www.kerofin.demon.co.uk/rox/load.html
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel
BuildRequires:	libgtop-devel >= 2.0.0
BuildRequires:	libxml2-devel
BuildRequires:	rox-CLib2-devel >= 2.1.5-2
Requires:	rox >= 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_roxdir	%{_libdir}/rox

%description
ROX-Load is an applet for use in a ROX-Filer panel or pinboard. It
displays the system load average.

%description -l pl
ROX-Load jest apletem, kt�ry mo�e by� u�ywany z panelem lub pulpitem
ROX-Filera. Wy�wietla on �rednie obci��enie systemu.

%prep
%setup -q -n %{_name}
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cd src
%{__autoconf}
cd ..
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_roxdir}/%{_name}/{Help,%{_platform}}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install .DirIcon *.xml AppRun rox_run $RPM_BUILD_ROOT%{_roxdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Help
install %{_platform}/Load $RPM_BUILD_ROOT%{_roxdir}/%{_name}/%{_platform}
install .DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/rox-Load.png

sed -e "s,/lib/,/%{_lib}/," %{SOURCE1} > $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
ln -sf AppRun $RPM_BUILD_ROOT%{_roxdir}/%{_name}/AppletRun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/{Changes,README,Versions}
%attr(755,root,root) %{_roxdir}/%{_name}/App*Run
%attr(755,root,root) %{_roxdir}/%{_name}/rox_run
%attr(755,root,root) %{_roxdir}/%{_name}/%{_platform}
%dir %{_roxdir}/%{_name}
%{_roxdir}/%{_name}/.DirIcon
%{_roxdir}/%{_name}/*.xml
%{_roxdir}/%{_name}/Help
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
