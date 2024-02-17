%define _unpackaged_files_terminate_build 1

Name: adt-test-tools
Version: 0.1.3
Release: alt1

Summary: Test tools for ADT.
License: GPLv2+
Group: Other
URL: https://github.com/AlexSP0/adt-test-tools

BuildArch: noarch

Source0: %name-%version.tar

%description
Test tools for ADT.

%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_sysconfdir/alterator/backends
mkdir -p %buildroot%_datadir/alterator/objects/%name

install -v -p -m 755 -D adt-test-tool %buildroot%_libexecdir/%name
install -v -p -m 644 -D diag.backend %buildroot%_sysconfdir/alterator/backends
install -v -p -m 644 -D diag2.backend %buildroot%_sysconfdir/alterator/backends
install -v -p -m 655 -D diag.alterator %buildroot%_datadir/alterator/objects/%name
install -v -p -m 655 -D diag2.alterator %buildroot%_datadir/alterator/objects/%name

%files
%_libexecdir/%name/adt-test-tool
%_sysconfdir/alterator/backends/diag.backend
%_sysconfdir/alterator/backends/diag2.backend
%_datadir/alterator/objects/%name/diag.alterator
%_datadir/alterator/objects/%name/diag2.alterator

%changelog
* Sat Feb 17 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.3-alt1
- add ReportSuffix key

* Wed Feb 14 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.2-alt1
- fix report method

* Wed Feb 07 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.1-alt1
- add pauses during simulating tests

* Tue Dec 12 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build
