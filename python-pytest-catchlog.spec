#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_without	tests	# py.test tests

Summary:	py.test plugin to capture log messages
Summary(pl.UTF-8):	Wtyczka py.test do przechwytywania logowanych komunikatów
Name:		python-pytest-catchlog
Version:	1.2.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/pytest-catchlog
Source0:	https://pypi.python.org/packages/source/p/pytest-catchlog/pytest-catchlog-%{version}.zip
# Source0-md5:	09d890c54c7456c818102b7ff8c182c8
URL:		https://github.com/eisensheng/pytest-catchlog
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-py >= 1.1.1
BuildRequires:	python-pytest >= 2.6
BuildConflicts:	python-pytest-capturelog
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-py >= 1.1.1
BuildRequires:	python3-pytest >= 2.6
BuildConflicts:	python3-pytest-capturelog
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
# this module provides the same pytest options, both cannot be installed
Obsoletes:	python-pytest-capturelog
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
py.test plugin to capture log messages. This is a fork of
python-capturelog.

%description -l pl.UTF-8
Wtyczka py.test do przechwytywania logowanych komunikatów. Jest to
odgałęzienie projektu python-capturelog.

%package -n python3-pytest-catchlog
Summary:	py.test plugin to capture log messages
Summary(pl.UTF-8):	Wtyczka py.test do przechwytywania logowanych komunikatów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2
# this module provides the same pytest options, both cannot be installed
Obsoletes:	python3-pytest-capturelog

%description -n python3-pytest-catchlog
py.test plugin to capture log messages. This is a fork of
python-capturelog.

%description -n python3-pytest-catchlog -l pl.UTF-8
Wtyczka py.test do przechwytywania logowanych komunikatów. Jest to
odgałęzienie projektu python-capturelog.

%prep
%setup -q -n pytest-catchlog-%{version}

%build
%if %{with python2}
%py_build

%{?with_tests:%{__python} -m pytest}
%endif

%if %{with python3}
%py3_build

%{?with_tests:%{__python3} -m pytest}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.txt README.rst
%{py_sitescriptdir}/pytest_catchlog.py[co]
%{py_sitescriptdir}/pytest_catchlog-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-catchlog
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.txt README.rst
%{py3_sitescriptdir}/pytest_catchlog.py
%{py3_sitescriptdir}/__pycache__/pytest_catchlog.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_catchlog-%{version}-py*.egg-info
%endif
