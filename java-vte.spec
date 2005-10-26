%define		pname	libvte-java
%define		api	0.11
%define		gtkapi	2.4
Summary:	Java interface for vte
Summary(pl):	Wrapper Javy dla vte
Name:		java-vte
Version:	0.11.12
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/java-gnome/%{pname}-%{version}.tar.bz2
# Source0-md5:	aef130d3e51879907d312fbcae7d2694
Patch0:		%{name}-configure.patch
Patch1:		%{name}-version_vars.patch
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 3.3.2
BuildRequires:	gtk+2-devel >= 2:2.4.3
BuildRequires:	java-gtk-devel >= 2.4.2
BuildRequires:	libgcj-devel >= 3.3.2
BuildRequires:	libgnomecanvas-devel >= 2.6.0
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	slocate
BuildRequires:	vte-devel >= 0.11.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java interface for vte.

%description -l pl
Wrapper Javy dla vte.

%package devel
Summary:	Header files for java-vte library
Summary(pl):	Pliki nag³ówkowe biblioteki java-vte
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for java-vte library.

%description devel -l pl
Pliki nag³ówkowe biblioteki java-vte.

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1
%patch1 -p1

%build
vteversion="%{version}"; export vteversion
vteapiversion="%{api}"; export vteapiversion
gtkapiversion="%{gtkapi}"; export gtkapiversion
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/java-gnome,%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/java-gnome/*
