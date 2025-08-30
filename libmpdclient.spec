%define	major	2
%define	libname		%mklibname mpdclient1
%define	oldlibname	%mklibname mpdclient 2
%define	develname	%mklibname -d mpdclient

Summary:	API library for interfacing MPD in the C, C++ & Objective C languages
Name:	libmpdclient
Version:	2.23
Release:	2
Group:	System/Libraries
License:	BSD
Url:		https://www.musicpd.org
Source0:	http://www.musicpd.org/download/libmpdclient/2/%{name}-%{version}.tar.xz
BuildRequires:	doxygen
BuildRequires:	meson

%description
A stable, documented, asynchronous API library for interfacing MPD in the C, 
C++ & Objective C languages.

#-----------------------------------------------------------------------------

%package -n %{libname}
Summary:	API library for interfacing MPD in the C, C++ & Objective C languages
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
%rename %{oldlibname}
Requires:	mpd >= 0.24.4

%description -n %{libname}
A stable, documented, asynchronous API library for interfacing MPD in the C, 
C++ & Objective C languages.

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{develname}
Summary:	Devel headers for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Devel headers for %{name}.

%files -n %{develname}
%doc NEWS README.rst
%{_docdir}/%{name}/
%{_includedir}/mpd/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%meson -Ddocumentation=true
%meson_build


%install
%meson_install
