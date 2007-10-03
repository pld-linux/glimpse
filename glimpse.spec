Summary:	Glimpse indexing and query system
Summary(pl.UTF-8):	System indeksowania i wyszukiwania Glimpse
Name:		glimpse
Version:	4.18.5
Release:	1
License:	non-profit
Group:		Applications/Text
#Source0:	ftp://ftp.cs.arizona.edu/glimpse/%{name}-%{version}.src.tar.gz
Source0:	http://webglimpse.net/trial/%{name}-%{version}.tar.gz
# Source0-md5:	10204ab813f3bbb558e22dedf19d1dfb
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

%description -l pl.UTF-8
Glimpse jest potężnym systemem indeksowania i wyszukiwania informacji.
Dzięki niemu można bardzo szybko przeszukać wiele plików. Może być
używany przez osoby prywatne na swoich systemach plików, a także przez
organizacje na dużych zbiorach danych.

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
%doc CHANGES CONTRIBUTIONS COPYRIGHT ChangeLog KNOWN_BUGS README README.install
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
