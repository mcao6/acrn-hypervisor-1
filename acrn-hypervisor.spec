#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : acrn-hypervisor
Version  : 2018w26.3.150000p
Release  : 34
URL      : https://github.com/projectacrn/acrn-hypervisor/archive/acrn-2018w26.3-150000p.tar.gz
Source0  : https://github.com/projectacrn/acrn-hypervisor/archive/acrn-2018w26.3-150000p.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC-BY-4.0 ISC
Requires: acrn-hypervisor-bin
Requires: acrn-hypervisor-config
Requires: acrn-hypervisor-autostart
Requires: acrn-hypervisor-data
Requires: acrn-hypervisor-license
Requires: acpica-unix2
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
BuildRequires : libevent-dev
BuildRequires : libusb-dev
BuildRequires : libxml2-dev
BuildRequires : pip
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(zlib)
BuildRequires : python-kconfiglib
BuildRequires : python3
BuildRequires : systemd-dev
BuildRequires : telemetrics-client-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0002-acrn-bridge-Do-not-overwrite-system-files.patch
Patch2: 0003-acrn-bridge-improve-systemd-network-units.patch

%description
This directory contains configuration files to ignore errors found in
the build and test process which are known to the developers and for
now can be safely ignored.

%package autostart
Summary: autostart components for the acrn-hypervisor package.
Group: Default

%description autostart
autostart components for the acrn-hypervisor package.


%package bin
Summary: bin components for the acrn-hypervisor package.
Group: Binaries
Requires: acrn-hypervisor-data
Requires: acrn-hypervisor-config
Requires: acrn-hypervisor-license

%description bin
bin components for the acrn-hypervisor package.


%package config
Summary: config components for the acrn-hypervisor package.
Group: Default

%description config
config components for the acrn-hypervisor package.


%package data
Summary: data components for the acrn-hypervisor package.
Group: Data

%description data
data components for the acrn-hypervisor package.


%package license
Summary: license components for the acrn-hypervisor package.
Group: Default

%description license
license components for the acrn-hypervisor package.


%prep
%setup -q -n acrn-hypervisor-acrn-2018w26.3-150000p
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530098393
make  %{?_smp_mflags} all sbl-hypervisor

%install
export SOURCE_DATE_EPOCH=1530098393
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/acrn-hypervisor
cp LICENSE %{buildroot}/usr/share/doc/acrn-hypervisor/LICENSE
cp tools/acrn-crashlog/license_header %{buildroot}/usr/share/doc/acrn-hypervisor/tools_acrn-crashlog_license_header
cp scripts/kconfig/LICENSE.kconfiglib %{buildroot}/usr/share/doc/acrn-hypervisor/scripts_kconfig_LICENSE.kconfiglib
cp doc/LICENSE %{buildroot}/usr/share/doc/acrn-hypervisor/doc_LICENSE
%make_install install sbl-hypervisor-install
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../usercrash.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/usercrash.service
ln -s ../prepare.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/prepare.service
ln -s ../acrnprobe.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/acrnprobe.service
ln -s ../cbc_attach.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/cbc_attach.service
ln -s ../cbc_lifecycle.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/cbc_lifecycle.service
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/usercrash.service %{buildroot}/usr/share/clr-service-restart/usercrash.service
ln -sf /usr/lib/systemd/system/prepare.service %{buildroot}/usr/share/clr-service-restart/prepare.service
ln -sf /usr/lib/systemd/system/acrnprobe.service %{buildroot}/usr/share/clr-service-restart/acrnprobe.service
ln -sf /usr/lib/systemd/system/cbc_attach.service %{buildroot}/usr/share/clr-service-restart/cbc_attach.service
ln -sf /usr/lib/systemd/system/cbc_lifecycle.service %{buildroot}/usr/share/clr-service-restart/cbc_lifecycle.service
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib/acrn/acrn.efi
/usr/lib/acrn/acrn.sbl

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/acrnprobe.service
/usr/lib/systemd/system/multi-user.target.wants/cbc_attach.service
/usr/lib/systemd/system/multi-user.target.wants/cbc_lifecycle.service
/usr/lib/systemd/system/multi-user.target.wants/prepare.service
/usr/lib/systemd/system/multi-user.target.wants/usercrash.service

%files bin
%defattr(-,root,root,-)
/usr/bin/acrn-dm
/usr/bin/acrnctl
/usr/bin/acrnlog
/usr/bin/acrnprobe
/usr/bin/acrnprobe_prepare.sh
/usr/bin/acrntrace
/usr/bin/cbc_attach
/usr/bin/cbc_lifecycle
/usr/bin/debugger
/usr/bin/usercrash_c
/usr/bin/usercrash_s

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/acrnprobe.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/cbc_attach.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/cbc_lifecycle.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/prepare.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/usercrash.service
/usr/lib/systemd/network/50-acrn.netdev
/usr/lib/systemd/network/50-acrn.network
/usr/lib/systemd/network/50-acrn_tap0.netdev
/usr/lib/systemd/network/50-eth.network
/usr/lib/systemd/system.conf.d/40-watchdog.conf
/usr/lib/systemd/system/acrnlog.service
/usr/lib/systemd/system/acrnprobe.service
/usr/lib/systemd/system/cbc_attach.service
/usr/lib/systemd/system/cbc_lifecycle.service
/usr/lib/systemd/system/prepare.service
/usr/lib/systemd/system/usercrash.service

%files data
%defattr(-,root,root,-)
/usr/share/acrn/bios/VSBL.bin
/usr/share/acrn/bios/VSBL_debug.bin
/usr/share/acrn/samples/apl-mrb/launch_uos.sh
/usr/share/acrn/samples/apl-mrb/sos_bootargs_debug.txt
/usr/share/acrn/samples/apl-mrb/sos_bootargs_release.txt
/usr/share/acrn/samples/nuc/acrn.conf
/usr/share/acrn/samples/nuc/launch_uos.sh
/usr/share/clr-service-restart/acrnprobe.service
/usr/share/clr-service-restart/cbc_attach.service
/usr/share/clr-service-restart/cbc_lifecycle.service
/usr/share/clr-service-restart/prepare.service
/usr/share/clr-service-restart/usercrash.service
/usr/share/defaults/telemetrics/acrnprobe.xml

%files license
%defattr(-,root,root,-)
/usr/share/doc/acrn-hypervisor/LICENSE
/usr/share/doc/acrn-hypervisor/doc_LICENSE
/usr/share/doc/acrn-hypervisor/scripts_kconfig_LICENSE.kconfiglib
/usr/share/doc/acrn-hypervisor/tools_acrn-crashlog_license_header
