Name:           ooreboot
Version:        0.1.0
Release:        1%{?dist}
Summary:        Executes safe system reboot invoking sync and unmount hooks.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooreboot
Source0:        ooreboot-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooreboot is a sovereign, capability-bounded SAFE REBOOTER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooreboot
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooreboot-uninstall

%files
/usr/bin/ooreboot
/usr/bin/ooreboot-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
