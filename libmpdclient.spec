%define name libmpdclient
%define version 2.7
%define major   2
%define libname %mklibname mpdclient %{major}
%define develname %mklibname -d mpdclient
%define stdevelname %mklibname -d -s mpdclient

Name:		%{name}
Version:	%{version}
Release:	3
Summary:	API library for interfacing MPD in the C, C++ & Objective C languages
Group:		System/Libraries
License:	BSD
Url:		http://mpd.wikia.com/wiki/ClientLib:libmpdclient
Source0:	http://dl.sourceforge.net/project/musicpd/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch1:		libmpdclient-2.7-automake1.13.patch
BuildRequires:	doxygen

%description
A stable, documented, asynchronous API library for interfacing MPD in the C, 
C++ & Objective C languages.

#-----------------------------------------------------------------------------
%package -n %{libname}
Summary:	API library for interfacing MPD in the C, C++ & Objective C languages
Provides:	%{name} = %{version}-%{release}
Group:		System/Libraries

%description -n %{libname}
A stable, documented, asynchronous API library for interfacing MPD in the C, 
C++ & Objective C languages.

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
%package -n %{develname}
Summary:	Devel headers for %{name}
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Group:		Development/C

%description -n %{develname}
Devel headers for libmpdclient

%files -n %{develname}
%doc COPYING NEWS README
%{_datadir}/doc/%{name}/*
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_includedir}/mpd/
%{_includedir}/mpd/*
%{_libdir}/%{name}.so
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
%package -n %{stdevelname}
Summary:	Devel headers for %{name}
Requires:	%{libname} = %{version}
Provides:	%{name}-static-devel = %{version}-%{release}
Group:		Development/C

%description -n %stdevelname
Devel headers for libmpdclient

%files -n %stdevelname
%{_libdir}/%{name}.a
#-----------------------------------------------------------------------------

%prep
%setup -q
%patch1 -p0 -b .automake113
%build
./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std
rm -rf %buildroot/%{_libdir}/*.la


%changelog
* Mon Feb 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.7-1
+ Revision: 778136
- version update 2.7

* Mon Nov 07 2011 Andrey Bondrov <abondrov@mandriva.org> 2.6-1
+ Revision: 725926
- New version 2.6, new URL, spec cleanup

* Sun Aug 08 2010 Rémy Clouard <shikamaru@mandriva.org> 2.3-1mdv2011.0
+ Revision: 567657
- bump release
- fix Source URL
- remove tabs

* Sun Jan 10 2010 Rémy Clouard <shikamaru@mandriva.org> 2.1-1mdv2010.1
+ Revision: 488717
- bump release

* Wed Nov 04 2009 Rémy Clouard <shikamaru@mandriva.org> 2.0-1mdv2010.1
+ Revision: 460414
- import libmpdclient

