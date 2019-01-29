Summary:	Matchbox test theme
Summary(pl.UTF-8):	Motyw testowy Matchboksa
Name:		matchbox-tests
Version:	0.4
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.yoctoproject.org/releases/matchbox/matchbox-tests/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	3081ab35216b75d044754732b0bcb7ac
URL:		https://www.yoctoproject.org/software-item/matchbox/
BuildRequires:	libmatchbox-devel >= 1.1
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXtst-devel
Requires:	libmatchbox >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matchbox test theme.

%description -l pl.UTF-8
Motyw testowy Matchboksa.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{_datadir}/themes/mbtest
