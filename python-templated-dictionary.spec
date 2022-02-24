%define pypi_name templated-dictionary

Summary:	Dictionary with Jinja2 expansion
Name:		python-%{pypi_name}
Version:	1.1
Release:	2
License:	GPLv2+
Group:		Development/Python
Url:		https://github.com/xsuchy/templated-dictionary
Source0:	https://github.com/xsuchy/templated-dictionary/archive/refs/tags/python-%{pypi_name}-%{version}-1.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3dist(jinja2)
BuildRequires:	python3dist(setuptools)
%rename python3-%{pypi_name}

%description
Dictionary where __getitem__() is run through Jinja2 template.

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/templated_dictionary-*.egg-info/
%{python3_sitelib}/templated_dictionary/

%prep
%autosetup -p1 -n %{pypi_name}-%{name}-%{version}-1

%build
%py3_build

%install
%py3_install
