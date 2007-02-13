%define		pname	libvte-java
Summary:	Java interface for vte
Summary(pl.UTF-8):	Wrapper Javy dla vte
Name:		java-vte
Version:	0.12.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libvte-java/0.12/%{pname}-%{version}.tar.bz2
# Source0-md5:	c6572bb4892353652ba22a3478649102
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 5:3.3.2
BuildRequires:	java-gtk-devel >= 2.10.0
BuildRequires:	libgcj-devel >= 5:3.3.2
BuildRequires:	libtool
BuildRequires:	vte-devel >= 0.14.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		macros	%{_datadir}/glib-java/macros

%description
Java interface for vte.

%description -l pl.UTF-8
Wrapper Javy dla vte.

%package devel
Summary:	Header files for java-vte library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki java-vte
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for java-vte library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki java-vte.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I `pkg-config --variable macro_dir gtk2-java` -I %{macros}
%{__automake}
%{__autoconf}
%configure \
	GCJFLAGS="%{rpmcflags}" \
	JAR=%{_bindir}/fastjar \
	--without-javadocs
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_libdir},%{_pkgconfigdir}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_docdir}/%{pname}-%{version}/examples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/examples/*.in
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{pname}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*-0.12.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvtejava.so
%attr(755,root,root) %{_libdir}/libvtejni.so
%{_javadir}/*
%{_libdir}/*.la
%{_pkgconfigdir}/*.pc
%{_examplesdir}/%{name}-%{version}
