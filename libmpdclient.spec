%define name libmpdclient
%define version 2.1
%define rel 1
%define major	2
%define libname %mklibname mpdclient %major
%define develname %mklibname -d mpdclient
%define stdevelname %mklibname -d -s mpdclient

Name:		%name
Version:	%version
Release:	%mkrel %rel
Summary:	API library for interfacing MPD in the C, C++ & Objective C languages
Group:		System/Libraries
License:	BSD
Url:		http://www.musicpd.org/doc/libmpdclient/index.html
Source0:	%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	doxygen

BuildRoot:	%_tmppath/%{name}-%{version}-%{release}

%description
A stable, documented, asynchronous API library for interfacing MPD in the C, 
C++ & Objective C languages.

#-----------------------------------------------------------------------------
%package -n %libname
Summary:	API library for interfacing MPD in the C, C++ & Objective C languages
Provides:	%{name} = %version-%release
Group:		System/Libraries

%description -n %libname
A stable, documented, asynchronous API library for interfacing MPD in the C, 
C++ & Objective C languages.

%files -n %libname
%defattr(-,root,root,-)
%_libdir/%{name}.so.%{major}*
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
%package -n %develname
Summary:	Devel headers for %name
Requires:	%{libname} = %version
Provides:	%{name}-devel = %version-%release
Group:		Development/C

%description -n %develname
Devel headers for libmpdclient

%files -n %develname
%defattr(-,root,root,-)
%doc COPYING NEWS README
%_datadir/doc/%{name}/*
%_libdir/pkgconfig/%{name}.pc
%dir %_includedir/mpd/
%_includedir/mpd/*
%_libdir/%{name}.so
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
%package -n %stdevelname
Summary:	Devel headers for %name
Requires:	%{libname} = %version
Provides:	%{name}-static-devel = %version-%release
Group:		Development/C

%description -n %stdevelname
Devel headers for libmpdclient

%files -n %stdevelname
%defattr(-,root,root,-)
%_libdir/%{name}.a
%_libdir/%{name}.la
#-----------------------------------------------------------------------------

%prep
%setup -q

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot
