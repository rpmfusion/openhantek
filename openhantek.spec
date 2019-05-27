%global optflags %{optflags} -flto
%global build_ldflags %{build_ldflags} -flto

Name:           openhantek
Version:        2.09
Release:        1%{?dist}
Summary:        Hantek and compatible USB digital signal oscilloscope

#Contain nonfree firmware
License:        GPLv3+ and GPLv2+ and ASL 2.0 and nonfree
URL:            https://github.com/OpenHantek/OpenHantek6022
Source0:        %{url}/archive/v%{version}.tar.gz
Source1:        %{name}.desktop

BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  qt5-qtbase-devel
BuildRequires:  fftw-devel
BuildRequires:  libusbx-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qttranslations
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  binutils-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  pkgconfig(udev)

Requires:       hicolor-icon-theme

%description
OpenHantek is a free software for Hantek and compatible
(Voltcraft/Darkwire/Protek/Acetech) USB digital signal oscilloscopes.
Supported devices: 6022BE/BL.

%prep
%autosetup -n OpenHantek6022-%{version}

%build
mkdir build
pushd build
    %cmake3 \
        -DCMAKE_AR=/usr/bin/gcc-ar \
        -DCMAKE_RANLIB=/usr/bin/gcc-ranlib \
        -DCMAKE_NM=/usr/bin/gcc-nm \
        ..
    %make_build
popd

%install
pushd build
    %make_install
popd
mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}/lib/udev/rules.d/60-hantek.rules %{buildroot}%{_udevrulesdir}
desktop-file-install --dir="%{buildroot}%{_datadir}/applications" %{SOURCE1}
install -p -D -m 644 %{name}/res/images/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%files
%license COPYING
%doc readme.md
%{_bindir}/OpenHantek
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_udevrulesdir}/60-hantek.*


%changelog
* Mon May 27 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.09-1
- Update to 2.09

* Thu May 23 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.07-1
- Update to 2.07

* Wed May 15 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.06-1
- Update to 2.06

* Sat May 11 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.05-1
- Update to 2.05

* Fri May 10 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.04-1
- Update to 2.04

* Mon May 06 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.03-1
- Update to 2.03
- Fix crashing in normal mode

* Sat Apr 27 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.01-1
- Update to 2.01

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0-4.20190110giteb33325
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Feb 25 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 0-2.20190110giteb33325
- Update to latest git

* Sat Dec 08 2018 Nicolas Chauvet <kwizart@gmail.com> - 0-3.20180722git7862387
- Drop systemd-udev as it's installed by default.
  This avoid a dependency break in el7 as udev is provided by the systemd package

* Wed Aug 01 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-2.20180722git7862387
- Update to latest git

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 0-2.20180715git57e0beb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 16 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-1.20180715git57e0beb
- Update to latest git

* Wed Jul 11 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-1.20180710git9935f0a
- Update to latest git

* Thu Mar 15 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0-1.20180320git0eff8d4
- Initial package for Fedora
