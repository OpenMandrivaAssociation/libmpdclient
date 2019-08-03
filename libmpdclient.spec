%define	major	2
%define	libname		%mklibname mpdclient %{major}
%define	develname	%mklibname -d mpdclient

Name:		libmpdclient
Version:	2.16
Release:	1
Summary:	API library for interfacing MPD in the C, C++ & Objective C languages
Group:		System/Libraries
License:	BSD
Url:		http://www.musicpd.org
Source0:	http://www.musicpd.org/download/libmpdclient/2/%{name}-%{version}.tar.xz
BuildRequires:	doxygen
BuildRequires:  meson

%description
A stable, documented, asynchronous API library for interfacing MPD in the C, 
C++ & Objective C languages.

#-----------------------------------------------------------------------------

%package -n %{libname}
Summary:	API library for interfacing MPD in the C, C++ & Objective C languages
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Requires:	mpd >= 0.18

%description -n %{libname}
A stable, documented, asynchronous API library for interfacing MPD in the C, 
C++ & Objective C languages.

%files -n %{libname}
%doc COPYING
%{_libdir}/%{name}.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{develname}
Summary:	Devel headers for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n %{develname}
Devel headers for %{name}.

%files -n %{develname}
%doc COPYING NEWS README
%doc doc/api/html/*
%{_datadir}/doc/%{name}/*
%{_datadir}/vala/vapi/%{name}.vapi
%dir %{_includedir}/mpd/
%{_includedir}/mpd/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install


%changelog
* Mon Mar 24 2014 Giovanni Mariani <mc2374@mclink.it> 2.9-1
- New release 2.9 (needs mpd >= 0.18)
- Updated Source and URL tags
- Dropped static libraries and package
- Added some docs to keep rpmlint happy
- Fixed file list

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

