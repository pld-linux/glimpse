Summary:	Glimpse indexing and query system
Summary(pl):	System indeksacji i wyszukiwania Glimpse
Name:		glimpse 
Version:	4.1
Release:	2
Group:		Utilities/Text
Copyright:	Non-profit redistribution & use only
Source:		ftp://ftp.cs.arizona.edu:/glimpse/%{name}-%{version}.src.tar.gz
Patch0:		%{name}-optflags.patch
Patch1:		%{name}-glibc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glimpse is a very powerful indexing and query system that allows you to
search through all your files very quickly.  It can be used by
individuals for their personal file systems as well as by organizations
for large data collections.

%description -l pl
Glimpse jest pot�nym systemem indeksacji i wyszukiwania informacji.
Dzi�ki niemu mo�esz bardzo szybko przeszuka� wiele plik�w. 

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make -f Makefile.linux \
	OPTIMIZEFLAGS="$RPM_OPT_FLAGS" \
	CC="cc" ISO_CHAR_SET="1" \

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man1}

install agrep/agrep.1 $RPM_BUILD_ROOT%{_mandir}/man1
install {glimpse,glimpseindex,glimpseserver}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -s bin/{agrep,buildcast,cast,glimpse,glimpseindex,tbuild,uncast,wgconvert} \
	$RPM_BUILD_ROOT%{_bindir}
install -s bin/glimpseserver $RPM_BUILD_ROOT%{_sbindir}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* README COPYRIGHT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz COPYRIGHT.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
