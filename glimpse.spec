Summary:     Glimpse indexing and query system
Summary(pl): System indeksacji i wyszukiwania Glimpse
Name:        glimpse 
Version:     4.1
Release:     1
Source:      ftp://ftp.cs.arizona.edu:/glimpse/%{name}-%{version}.src.tar.gz
Patch:       %{name}-optflags.patch
Patch1:      %{name}-glibc.patch
Copyright:   Non-profit redistribution & use only
Group:       Utilities/Text
Buildroot:   /tmp/%{name}-%{version}-root

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
%patch -p1 -b .optflags
%patch1 -p1 -b .glibc

%build
make -f Makefile.linux \
	"OPTIMIZEFLAGS=$RPM_OPT_FLAGS" \
	CC=egcs \
	ISO_CHAR_SET=1 \

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{bin,man/man1,sbin}

install agrep/agrep.1 $RPM_BUILD_ROOT/usr/man/man1
install {glimpse,glimpseindex,glimpseserver}.1 $RPM_BUILD_ROOT/usr/man/man1

install -s bin/{agrep,buildcast,cast,glimpse,glimpseindex,tbuild,uncast,wgconvert} $RPM_BUILD_ROOT/usr/bin
install -s bin/glimpseserver $RPM_BUILD_ROOT/usr/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README COPYRIGHT
%attr(755, root, root) /usr/bin/*
%attr(755, root, root) /usr/sbin/*
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Fri Sep 25 1998 Marcin Korzonek <mkorz@shadow.eu.org>
- allow building from non root account,
- added pl translation.
