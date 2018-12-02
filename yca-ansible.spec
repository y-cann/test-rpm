Name:           yca-ansible
Version:        1.0.0
Release:        1%{?dist}
Summary:        Test ansible

License:        MIT
URL:            https://github.com/y-cann/test-rpm
Source0:        %{name}-%{version}.tar.gz

#BuildRequires:  
#Requires:       

%description
YCA ansible

%prep
%setup -q

%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/ansible
cp -r ansible %{buildroot}%{_datadir}/ansible/%{name}

%files
%{_datadir}/ansible/%{name}


%changelog
