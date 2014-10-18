Summary:	Raptor RDF Parser Toolkit
Name:		raptor2
Version:	2.0.14
Release:	1
License:	LGPL v2.1+ or GPL v2+ or Apache v2.0+
Group:		Libraries
Source0:	http://download.librdf.org/source/%{name}-%{version}.tar.gz
# Source0-md5:	d3e0b43866197a5367b781b25510f728
URL:		http://librdf.org/raptor/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	pkg-config
BuildRequires:	yajl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Raptor is the RDF Parser Toolkit for Redland written in C consisting
of two parsers for the RDF/XML and N-Triples syntaxes for RDF. Raptor
is designed to work efficiently when used with Redland but is entirely
separate.

%package devel
Summary:	libraptor2 library header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libraptor2 library header files.

%package apidocs
Summary:	libraptor2 API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libraptor2 API documentation.

%package rapper
Summary:	Raptor RDF parser test program
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description rapper
Raptor RDF parser test program.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# avoid using parsedate from libinn, use curl_getdate instead
%configure \
	ac_cv_header_libinn_h=no	\
	--disable-static		\
	--enable-release		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE.txt NEWS NOTICE README RELEASE.html UPGRADING.html
%attr(755,root,root) %ghost %{_libdir}/libraptor2.so.0
%attr(755,root,root) %{_libdir}/libraptor2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libraptor2.so
%dir %{_includedir}/raptor2
%{_includedir}/raptor2/raptor.h
%{_includedir}/raptor2/raptor2.h
%{_pkgconfigdir}/raptor2.pc
%{_mandir}/man3/libraptor2.3*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/raptor2

%files rapper
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rapper
%{_mandir}/man1/rapper.1*

