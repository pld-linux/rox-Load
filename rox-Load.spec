%define _name Load
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	ROX-Load displays the load average of Your system
Summary(pl):	ROX-Load wy¶wietla ¶rednie obci±¿enie Twojego systemu
Name:		rox-%{_name}
Version:	1.3.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tgz
Patch0:		%{name}-libxml-includes.patch
Patch1:		%{name}-paths-fix.patch
URL:		http://www.kerofin.demon.co.uk/rox/utils.html#load
BuildRequires:	gtk+-devel
BuildRequires:	libgtop-devel
BuildRequires:	libxml2-devel
BuildRequires:	rox-CLib-devel >= 0.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define   _appsdir  %{_libdir}/ROX-apps

%description
ROX-Load is an applet for use in a ROX-Filer panel or pinboard. It
displays the system load average.

%description -l pl
ROX-Load jest apletem, który mo¿e byæ u¿ywany z panelem lub pulpitem
ROX-Filera. Wy¶wietla on ¶rednie obci±¿enie systemu.

%prep
%setup -q -n %{_name}
%patch0 -p1
%patch1 -p1

%build
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,%{_platform}}

rm -f ../install
install App[IR]* rox_run $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install %{_platform}/Load $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}

ln -sf AppRun $RPM_BUILD_ROOT%{_appsdir}/%{_name}/AppletRun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/Versions
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%attr(755,root,root) %{_appsdir}/%{_name}/rox_run
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/AppletRun
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
