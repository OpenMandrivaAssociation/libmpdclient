%define name libmpdclient
%define version 2.10
%define major   2
%define libname %mklibname mpdclient %{major}
%define develname %mklibname -d mpdclient
%define stdevelname %mklibname -d -s mpdclient

Name:		%{name}
Version:	%{version}
Release:	1
Summary:	API library for interfacing MPD in the C, C++ & Objective C languages
Group:		System/Libraries
License:	BSD
Url:		http://mpd.wikia.com/wiki/ClientLib:libmpdclient
Source0:	http://dl.sourceforge.net/project/musicpd/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	doxygen

%description
A stable, documented, asynchronous API library for interfacing MPD in the C, 
C++ & Objective C languages.

%package -n %{libname}
Summary:	API library for interfacing MPD in the C, C++ & Objective C languages
Provides:	%{name} = %{version}-%{release}
Group:		System/Libraries

%description -n %{libname}
A stable, documented, asynchronous API library for interfacing MPD in the C, 
C++ & Objective C languages.

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

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
%{_datadir}/vala/vapi/libmpdclient.vapi

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
%apply_patches

%build
%configure	--enable-static
%make

%install
%makeinstall_std
