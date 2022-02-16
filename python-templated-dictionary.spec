%define pypi_name templated-dictionary

Summary:	Dictionary with Jinja2 expansion
Name:		python-%{pypi_name}
Version:	1.1
Release:	1
License:	GPLv2+
Group:		Development/Python
Url:		https://github.com/xsuchy/templated-dictionary
Source0:	https://github.com/xsuchy/templated-dictionary/archive/refs/tags/python-%{pypi_name}-%{version}-1.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3dist(jinja2)
BuildRequires:	python3dist(setuptools)

%description
Dictionary where __getitem__() is run through Jinja2 template.

#----------------------------------------------------------------------------

%package -n python3-%{pypi_name}
Summary:	Dictionary with Jinja2 expansion
Group:		Development/Python
Provides:	python-%{pypi_name} = %{EVRD}

%description -n python3-%{pypi_name}
Dictionary where __getitem__() is run through Jinja2 template.

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/templated_dictionary-*.egg-info/
%{python3_sitelib}/templated_dictionary/

#----------------------------------------------------------------------------

%prep
%setup -qn %{pypi_name}-%{name}-%{version}-1

%build
%py3_build

%install
%py3_install
