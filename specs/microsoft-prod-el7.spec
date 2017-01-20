Name:		packages-microsoft-prod
Version:        1.0
Release:        1%{?dist}
Summary:	Configuration for packages.microsoft.com

Group:		System Environment/Base
License:	ASL 2.0

URL:		http://packages.microsoft.com
Source0:	https://packages.microsoft.com/config/rhel/7/prod.repo
Source1:	https://packages.microsoft.com/keys/microsoft.asc

BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildArch:	noarch
Vendor:		Microsoft Corporation
Packager:	Microsoft Corporation


%description
This package contains the yum repo configuration 
for packages.microsoft.com and the public GPG key.

%prep
%setup -q -T -cn %{name}-%{version}
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%pre -p /bin/sh

%build
# Nothing to do

%install
rm -rf $RPM_BUILD_ROOT

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0}  \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/microsoft-prod.repo

install -Dpm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-microsoft-prod


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/microsoft-prod.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-microsoft-prod


%changelog
* Fri Jan 20 2017 Stephen Zarkos <stephen.zarkos@microsoft.com>
- Initial package to include repo configuraiton and GPG key

