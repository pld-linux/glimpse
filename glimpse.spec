Summary:	Glimpse indexing and query system
Summary(pl):	System indeksacji i wyszukiwania Glimpse
Name:		glimpse
Version:	4.1
Release:	3
License:	non-profit
Group:		Applications/Text
Source0:	ftp://ftp.cs.arizona.edu/glimpse/%{name}-%{version}.src.tar.gz
# Source0-md5: 6c5c4f3e0011b366c5feaa2e8d1d3b28
Patch0:		%{name}-optflags.patch
Patch1:		%{name}-glibc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glimpse is a very powerful indexing and query system that allows you
to search through all your files very quickly. It can be used by
individuals for their personal file systems as well as by
organizations for large data collections.

%description -l pl
Glimpse jest potê¿nym systemem indeksowania i wyszukiwania informacji.
Dziêki niemu mo¿na bardzo szybko przeszukaæ wiele plików.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} -f Makefile.linux \
	OPTIMIZEFLAGS="%{rpmcflags}" \
	CC="%{__cc}" \
	ISO_CHAR_SET="1"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man1}

install agrep/agrep.1 $RPM_BUILD_ROOT%{_mandir}/man1
install {glimpse,glimpseindex,glimpseserver}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install bin/{agrep,buildcast,cast,glimpse,glimpseindex,tbuild,uncast,wgconvert} \
	$RPM_BUILD_ROOT%{_bindir}
install bin/glimpseserver $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYRIGHT
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
