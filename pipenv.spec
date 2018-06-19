Name:           pipenv 
Version:        11.10.4
Release:        2%{?dist}
Summary:        The higher level Python packaging tool

# Pipenv source code is MIT, there are bundled packages having different licenses
# pipenv/patched/safety/ is MIT
# pipenv/patched/crayons/ is MIT
# pipenv/patched/piptools/ is BSD
# pipenv/patched/pew/ is MIT
# pipenv/patched/prettytoml/ is MIT
# pipenv/patched/pipfile/ is (Apache 2.0 or BSD)
# pipenv/patched/notpip/_vendor/cachecontrol/ is Apache 2.0
# pipenv/patched/notpip/_vendor/certifi/ is Mozzila Public License
# pipenv/patched/notpip/_vendor/colorama/ is BSD
# pipenv/patched/notpip/_vendor/chardet/ is LGPL v2.1
# pipenv/patched/notpip/_vendor/distlib/ is Python
# pipenv/patched/notpip/_vendor/distro.py is Apache 2.0
# pipenv/patched/notpip/_vendor/ipaddress.py is Python
# pipenv/patched/notpip/_vendor/idna/ is Python
# pipenv/patched/notpip/_vendor/lockfile/ is Python
# pipenv/patched/notpip/_vendor/ordereddict.py is MIT
# pipenv/patched/notpip/_vendor/packaging/ is (Apache2.0 or BSD)
# pipenv/patched/notpip/_vendor/pipfile/ is (Apache 2.0 or BSD)
# pipenv/patched/notpip/_vendor/pkg_resources/ is MIT 
# pipenv/patched/notpip/_vendor/progress/ is ISC
# pipenv/patched/notpip/_vendor/pyparsing is MIT
# pipenv/patched/notpip/_vendor/requests/ is Apache 2.0
# pipenv/patched/notpip/_vendor/retrying.py is Apache 2.0
# pipenv/patched/notpip/_vendor/six.py is Apache 2.0
# pipenv/patched/notpip/_vendor/urllib3/ is MIT
# pipenv/patched/notpip/_vendor/webencodings/ is Apache 2.0
# pipenv/vendor/pip9/_vendor/certifi/ is Mozzila Public License
# pipenv/vendor/pip9/_vendor/colorama/ is BSD
# pipenv/vendor/pip9/_vendor/chardet/ is LGPL v2.1
# pipenv/vendor/pip9/_vendor/distlib/ is Python
# pipenv/vendor/pip9/_vendor/distro.py is Apache 2.0
# pipenv/vendor/pip9/_vendor/ipaddress.py is Python
# pipenv/vendor/pip9/_vendor/idna/ is Python
# pipenv/vendor/pip9/_vendor/lockfile/ is Python
# pipenv/vendor/pip9/_vendor/ordereddict.py is MIT
# pipenv/vendor/pip9/_vendor/packaging/ is (Apache2.0 or BSD)
# pipenv/vendor/pip9/_vendor/pipfile/ is (Apache 2.0 or BSD)
# pipenv/vendor/pip9/_vendor/pkg_resources/ is MIT 
# pipenv/vendor/pip9/_vendor/progress/ is ISC
# pipenv/vendor/pip9/_vendor/pyparsing is MIT
# pipenv/vendor/pip9/_vendor/requests/ is Apache 2.0
# pipenv/vendor/pip9/_vendor/retrying.py is Apache 2.0
# pipenv/vendor/pip9/_vendor/six.py is Apache 2.0
# pipenv/vendor/pip9/_vendor/urllib3/ is MIT
# pipenv/vendor/pip9/_vendor/webencodings/ is Apache 2.0
# pipenv/vendor/blindspin/ is MIT
# pipenv/vendor/certifi/ is Mozzila Public License
# pipenv/vendor/click-completion.py is MIT
# pipenv/vendor/click-didyoumean.py is MIT
# pipenv/vendor/chardet/ is LGPL v2.1
# pipenv/vendor/delegator.py is MIT 
# pipenv/vendor/dotenv/ is BSD
# pipenv/vendor/first.py is MIT
# pipenv/vendor/pipdeptree is MIT
# pipenv/vendor/pip9 is MIT
# pipenv/vendor/requirements is BSD
# pipenv/vendor/notpip is MIT
# pipenv/vendor/shutilwhich is BSD
# pipenv/vendor/yarg is MIT
License:        MIT and BSD and ASL 2.0 and LGPLv2+ and Python and ISC and MPLv2.0 and (ASL 2.0 or BSD)
URL:            https://github.com/pypa/pipenv
Source0:        https://github.com/pypa/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# Add imports of pypi fixtures, which are moved to tests/integration
# in prep section
Patch1:         0001-pypi-fixtures.patch

# We unbundle a plenty of packages from vendor directory
# 'from pipenv.vendor' imports must be corrected
Patch2:         0002-fix-imports-of-unbundled-pkgs.patch

# A couple of tests fails in the mock environment, add option
# to skip these using special pytest marker
# TODO fix and propose changes upstream
Patch3:         0003-rpmfail-pytest-marker.patch

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(flake8) >= 3.0.0

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-click)
BuildRequires:  python3dist(twine)
BuildRequires:  python3dist(flask)
BuildRequires:  git 

BuildRequires:  python3dist(virtualenv-clone)
BuildRequires:  python3dist(virtualenv)

# Packages vendored upstream
BuildRequires:  python3dist(appdirs)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(docopt)
BuildRequires:  python3dist(iso8601)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(markupsafe)
BuildRequires:  python3dist(parse)
BuildRequires:  python3dist(pathlib2)
BuildRequires:  python3dist(pexpect)
BuildRequires:  python3dist(requests) > 2.18.0
BuildRequires:  python3dist(semver)
BuildRequires:  python3dist(toml)

%{?python_provide:%python_provide python3-%{name}}

Requires:       python3dist(virtualenv-clone)
Requires:       python3dist(virtualenv)

# Packages vendored upstream
Requires:       python3dist(appdirs)
Requires:       python3dist(click)
Requires:       python3dist(colorama)
Requires:       python3dist(certifi)
Requires:       python3dist(docopt)
Requires:       python3dist(iso8601)
Requires:       python3dist(jinja2)
Requires:       python3dist(markupsafe)
Requires:       python3dist(parse)
Requires:       python3dist(pathlib2)
Requires:       python3dist(pexpect)
Requires:       python3dist(ptyprocess)
Requires:       python3dist(pytoml)
Requires:       python3dist(requests) > 2.18.0
Requires:       python3dist(six)
Requires:       python3dist(semver)
Requires:       python3dist(toml)

# Following packages bundled under vendor directory are not
# packaged for Fedora yet.
# TODO package for Fedora and unbundle
Provides:       bundled(python3dist(blindspin)) == 2.0.1
Provides:       bundled(python3dist(click_completion)) == 0.2.1
Provides:       bundled(python3dist(click_didyoumean)) == 0.0.3
Provides:       bundled(python3dist(delegator)) == 0.1.0
Provides:       bundled(python3dist(dotenv)) == 0.6.2
Provides:       bundled(python3dist(first)) == 2.0.1
Provides:       bundled(python3dist(pip)) == 9.0.3
Provides:       bundled(python3dist(pipreqs)) == 0.4.9
Provides:       bundled(python3dist(pipdeptree))
Provides:       bundled(python3dist(requirements)) == 0.2.0
Provides:       bundled(python3dist(shutilwhich)) == 1.1.0
Provides:       bundled(python3dist(yarg)) == 0.1.9

# The sources contains patched versions of following packages:
Provides:       bundled(python3dist(contoml))
Provides:       bundled(python3dist(crayons)) == 0.1.2
Provides:       bundled(python3dist(pew)) == 1.1.5
Provides:       bundled(python3dist(pipfile)) == 0.0.2
Provides:       bundled(python3dist(pip-tools)) == 2.0.1
Provides:       bundled(python3dist(prettytoml)) == 0.3
Provides:       bundled(python3dist(pip)) == 9.0.3
Provides:       bundled(python3dist(safety))
# The packages bundled with pip:
Provides:       bundled(python3dist(setuptools)) == 39.1.0
Provides:       bundled(python3dist(apdirs)) == 1.4.0
Provides:       bundled(python3dist(distlib)) == 0.2.4
Provides:       bundled(python3dist(distro)) == 1.2.0
Provides:       bundled(python3dist(html5lib)) == 1.0b10
Provides:       bundled(python3dist(six)) == 1.10.0
Provides:       bundled(python3dist(colorama)) == 0.3.7
Provides:       bundled(python3dist(requests)) == 2.18.4
Provides:       bundled(python3dist(chardet)) == 3.0.4
Provides:       bundled(python3dist(idna)) == 2.6
Provides:       bundled(python3dist(urllib3)) == 1.22
Provides:       bundled(python3dist(certifi)) == 2018.1.18
Provides:       bundled(python3dist(CacheControl)) == 0.11.7
Provides:       bundled(python3dist(lockfile)) == 0.12.2
Provides:       bundled(python3dist(ordereddict)) == 1.1
Provides:       bundled(python3dist(progress)) == 1.2
Provides:       bundled(python3dist(ipaddress)) == 1.0.17
Provides:       bundled(python3dist(packaging)) == 16.8
Provides:       bundled(python3dist(pyparsing)) == 2.1.10
Provides:       bundled(python3dist(retrying)) == 1.3.3
Provides:       bundled(python3dist(webencodings)) == 0.5

%description
The officially recommended Python packaging tool that aims to bring
the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.)
to the Python world. It automatically creates and manages a virtualenv for 
your projects, as well as adds/removes packages from your Pipfile as you 
install/uninstall packages. It also generates the ever–important Pipfile.lock, 
which is used to produce deterministic builds.

%package -n %{name}-doc
Summary:        Pipenv documentation
%description -n %{name}-doc
Documentation for Pipenv

%prep
%autosetup -p1 -n %{name}-%{version}

# Remove packages that are already packaged for Fedora from vendor directory
UNBUNDLED="appdirs click colorama docopt iso8601 jinja2 markupsafe parse pathlib2 pexpect ptyprocess pytoml requests semver six toml backports"
# pipenv/vendor/pip9/_vendor/cachecontrol/ is Apache 2.0

_vendordir="pipenv/vendor/"

for pkg in ${UNBUNDLED[@]}; do
  rm -rf $_vendordir$pkg
  rm -rf $_vendordir$pkg".py"
  rm -rf $_vendordir$pkg".LICENSE*"
done

mv tests/pytest-pypi/pytest_pypi tests/integration/fixtures
rm -rf tests/pytest-pypi
           
%build
%py3_build
# generate html docs
sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
rm -rf html/_sources/

%install
%py3_install
# Remove shebang lines from scripts in project directory
grep "/usr/bin/env python" -lR %{buildroot}%{python3_sitelib}/%{name}| xargs sed -i '1d'

%check
export PATH=$PATH:%{buildroot}%{_bindir}
export PYTHONPATH=$PYTHONPATH:%{buildroot}%{python3_sitelib}
export PYPI_VENDOR_DIR="$(pwd)/tests/pypi/"
pytest-3 -v -n auto -m "not rpmfail" tests

%files
%license LICENSE
# for the sake of simplicity, files are listed twice. we know about it
%license %{python3_sitelib}/%{name}/patched/crayons.LICENSE 
%license %{python3_sitelib}/%{name}/patched/safety/LICENSE
%license %{python3_sitelib}/%{name}/patched/pipfile/LICENSE
%license %{python3_sitelib}/%{name}/patched/pipfile/LICENSE.BSD
%license %{python3_sitelib}/%{name}/patched/pipfile/LICENSE.APACHE
%license %{python3_sitelib}/%{name}/patched/piptools/LICENSE
%license %{python3_sitelib}/%{name}/patched/prettytoml/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/appdirs.LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/cachecontrol/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/colorama/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/distlib/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/distro.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/html5lib/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/ipaddress.LICENSE 
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/idna/LICENSE.rst
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/lockfile/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/ordereddict.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/packaging/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/packaging/LICENSE.BSD
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/packaging/LICENSE.APACHE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/pkg_resources/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/progress/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/pyparsing.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/retrying.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/requests/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/six.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/urllib3/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/webencodings/LICENSE
%license %{python3_sitelib}/%{name}/vendor/blindspin/LICENSE
%license %{python3_sitelib}/%{name}/vendor/certifi/LICENSE
%license %{python3_sitelib}/%{name}/vendor/chardet/LICENSE
%license %{python3_sitelib}/%{name}/vendor/click-completion.LICENSE 
%license %{python3_sitelib}/%{name}/vendor/click-didyoumean.LICENSE 
%license %{python3_sitelib}/%{name}/vendor/first.LICENSE
%license %{python3_sitelib}/%{name}/vendor/delegator.py.LICENSE 
%license %{python3_sitelib}/%{name}/vendor/dotenv/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pip9/LICENSE.txt
%license %{python3_sitelib}/%{name}/vendor/pipdeptree.LICENSE 
%license %{python3_sitelib}/%{name}/vendor/pipreqs/LICENSE
%license %{python3_sitelib}/%{name}/vendor/requirements/LICENSE.rst
%license %{python3_sitelib}/%{name}/vendor/shutilwhich/LICENSE
%license %{python3_sitelib}/%{name}/vendor/yarg/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/appdirs.LICENSE.txt
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/cachecontrol/LICENSE.txt
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/colorama/LICENSE.txt
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/distlib/LICENSE.txt
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/distro.LICENSE
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/html5lib/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/ipaddress.LICENSE 
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/idna/LICENSE.rst
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/lockfile/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/ordereddict.LICENSE
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/packaging/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/packaging/LICENSE.BSD
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/packaging/LICENSE.APACHE
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/pkg_resources/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/progress/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/pyparsing.LICENSE
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/retrying.LICENSE
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/requests/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/six.LICENSE
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/urllib3/LICENSE.txt
%license %{python3_sitelib}/%{name}/vendor/pip9/_vendor/webencodings/LICENSE
%doc README.rst
%{_bindir}/pipenv
%{_bindir}/pipenv-resolver
%{_bindir}/pewtwo
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py?.?.egg-info
%exclude %{python3_sitelib}/tests
%exclude %{python3_sitelib}/tasks

%files -n %{name}-doc
%doc html
%license LICENSE

%changelog
* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 11.10.4-2
- Rebuilt for Python 3.7

* Fri Apr 13 2018 Michal Cyprian <mcyprian@redhat.com> - 11.10.4-1
- Initial package.
