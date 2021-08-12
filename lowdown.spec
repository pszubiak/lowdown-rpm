Name:           lowdown
Version:        0.8.6
Release:        1%{?dist}
Summary:        Simple markdown translator
License:        ICS
URL:            https://kristaps.bsd.lv/lowdown/
Source0:        https://github.com/kristapsdz/lowdown/archive/refs/tags/VERSION_0_8_6.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  coreutils

%description
lowdown is a Markdown translator producing HTML5,
roff documents in the ms and man formats, LaTeX,
gemini, and terminal output.
The open source C source code has no dependencies.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
For details about the programming API, please see the docs
on the project's site (https://kristaps.bsd.lv/lowdown/)

%prep
%setup -n %{name}-VERSION_0_8_6

%build
export CFLAGS='%{build_cflags}'
export LDFLAGS='%{build_ldflags}'
./configure PREFIX=%{_prefix} LIBDIR=%{_libdir} MANDIR=%{_mandir}
%make_build

%install
%make_install
chmod -R u+w $RPM_BUILD_ROOT

%ldconfig_scriptlets

%files
%{_bindir}/%{name}*
%{_libdir}/*.a
%{_mandir}/man1/*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*
%{_mandir}/man5/*

%changelog
* Thu Aug 22 2021 Piotr Szubiakowski - 0.8.6-1
- Initial build.
