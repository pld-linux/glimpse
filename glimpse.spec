Summary:	Glimpse indexing and query system
Summary(pl):	System indeksowania i wyszukiwania Glimpse
Name:		glimpse
Version:	4.17.4
Release:	1
License:	non-profit
Group:		Applications/Text
#Source0:	ftp://ftp.cs.arizona.edu/glimpse/%{name}-%{version}.src.tar.gz
Source0:	http://webglimpse.net/trial/%{name}-%{version}.tar.gz
# Source0-md5:	c005f3ca3f3ab64473405a1d5901dd3f
Patch0:		%{name}-optflags.patch
Patch1:		%{name}-stdarg.patch
URL:		http://webglimpse.net/
# this package contains updated version of agrep - maybe it should
# be packaged from here not agrep.spec (which is for old '92 sources)?
Obsoletes:	agrep
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glimpse is a very powerful indexing and query system that allows you
to search through all your files very quickly. It can be used by
individuals for their personal file systems as well as by
organizations for large data collections.

%description -l pl
Glimpse jest potê¿nym systemem indeksowania i wyszukiwania informacji.
Dziêki niemu mo¿na bardzo szybko przeszukaæ wiele plików. Mo¿e byæ
u¿ywany przez osoby prywatne na swoich systemach plików, a tak¿e przez
organizacje na du¿ych zbiorach danych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# don't do this - configure was manually modified, configure.in is outdated
#%{__autoconf}
touch configure
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1

install -d $RPM_BUILD_ROOT%{_sbindir}
mv -f $RPM_BUILD_ROOT%{_bindir}/glimpseserver \
	$RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTIONS COPYRIGHT ChangeLog KNOWN_BUGS README README.install TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
