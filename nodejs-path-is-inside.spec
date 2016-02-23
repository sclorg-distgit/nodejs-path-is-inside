%{?scl:%scl_package nodejs-path-is-inside}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-path-is-inside_1.0.0

%global npmname path-is-inside
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-path-is-inside
Version:        1.0.1
Release:        1%{?dist}
Summary:        Tests whether one path is inside another path
Url:            https://github.com/domenic/path-is-inside
Source0:        http://registry.npmjs.org/%{npmname}/-/%{npmname}-%{version}.tgz
License:        WTFPL

BuildArch:      noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Tests whether one path is inside another path

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/path-is-inside
cp -pr package.json lib/ %{buildroot}%{nodejs_sitelib}/path-is-inside
%nodejs_symlink_deps

%files
%{nodejs_sitelib}/path-is-inside
%doc LICENSE.txt README.md

%changelog
* Thu Feb 18 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-1
- New upstream release
- add BuildArch and ExclusiveArch

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-2
- Rebuilt with new metapackage

* Wed Feb 12 2014 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-1
- Initial build

