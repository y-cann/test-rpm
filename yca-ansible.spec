Name:           yca-ansible
Version:        1.0.0
Release:        1%{?dist}
Summary:        Test ansible

License:        MIT
URL:            https://github.com/y-cann/test-rpm
#Source0:        

#BuildRequires:  
#Requires:       

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc



%changelog
