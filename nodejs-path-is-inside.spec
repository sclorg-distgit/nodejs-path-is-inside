%{?scl:%scl_package nodejs-path-is-inside}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-path-is-inside_1.0.0

%global npmname path-is-inside
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-path-is-inside
Version:        1.0.0
Release:        1.sc1%{?dist}
Summary:        Tests whether one path is inside another path
Url:            https://github.com/domenic/path-is-inside
Source0:        http://registry.npmjs.org/path-is-inside/-/path-is-inside-1.0.0.tgz
License:        WTFPL

BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Tests whether one path is inside another path

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/path-is-inside
cp -pr package.json lib/ %{buildroot}%{nodejs_sitelib}/path-is-inside
%nodejs_symlink_deps

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/path-is-inside

%doc LICENSE.txt README.md

%changelog
* Wed Feb 12 2014 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-1
- Initial build

