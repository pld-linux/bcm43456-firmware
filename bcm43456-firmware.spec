Summary:	Firmware files for Broadcom BCM43456 Wi-Fi/Bluetooth chip
Name:		bcm43456-firmware
Version:	7.84.17.1
Release:	1
License:	Unknown
Group:		Base
Source0:	https://github.com/RPi-Distro/firmware-nonfree/raw/bullseye/debian/config/brcm80211/brcm/brcmfmac43456-sdio.bin
# NoSource0-md5:	570abf11436bc4f272935d615d91d9af
NoSource:	0
Source1:	https://github.com/RPi-Distro/firmware-nonfree/raw/bullseye/debian/config/brcm80211/brcm/brcmfmac43456-sdio.clm_blob
# NoSource1-md5:	92388bf1a5b7796c25473e8c55827371
NoSource:	1
Source2:	https://github.com/RPi-Distro/firmware-nonfree/raw/bullseye/debian/config/brcm80211/brcm/brcmfmac43456-sdio.txt
# NoSource2-md5:	b2b726be6a54cd6c001767962c1782a0
NoSource:	2
Source3:	https://github.com/armbian/firmware/raw/master/brcm/BCM4345C5.hcd
# NoSource3-md5:	fc394331d03baa5847e2b5de94ffbc9b
NoSource:	3
URL:		https://www.broadcom.com/products/wireless/wireless-lan-bluetooth/bcm43456
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firmware files for Broadcom BCM43456 Wi-Fi/Bluetooth chip.

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/lib/firmware/brcm

cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT/lib/firmware/brcm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/brcm/BCM4345C5.hcd
/lib/firmware/brcm/brcmfmac43456-sdio.bin
/lib/firmware/brcm/brcmfmac43456-sdio.clm_blob
/lib/firmware/brcm/brcmfmac43456-sdio.txt
