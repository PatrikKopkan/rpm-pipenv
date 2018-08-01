# !!! WARNING !!!
# This package has very fragile tests. If they fail, build it again couple
# times before filling bugz.

Name:           pipenv 
Version:        2018.7.1
Release:        2%{?dist}
Summary:        The higher level Python packaging tool

# Pipenv source code is MIT, there are bundled packages having different licenses

# pipenv/patched/contoml/ is MIT
# pipenv/patched/crayons.py is MIT
# pipenv/patched/pew/ is MIT
# pipenv/patched/pipfile/ is (ASL 2.0 or BSD)
# pipenv/patched/piptools/ is BSD
# pipenv/patched/prettytoml/ is MIT
# pipenv/patched/safety/ is MIT
# pipenv/patched/safety.zip is MIT

# pipenv/patched/notpip/ is MIT
# pipenv/patched/notpip/_vendor/appdirs.py is MIT
# pipenv/patched/notpip/_vendor/cachecontrol/ is ASL 2.0
# pipenv/patched/notpip/_vendor/certifi/ is MPLv2.0
# pipenv/patched/notpip/_vendor/chardet/ is LGPLv2+
# pipenv/patched/notpip/_vendor/colorama/ is BSD
# pipenv/patched/notpip/_vendor/distlib/ is Python
# pipenv/patched/notpip/_vendor/distro.py is ASL 2.0
# pipenv/patched/notpip/_vendor/html5lib/ is MIT
# pipenv/patched/notpip/_vendor/idna/ is Python
# pipenv/patched/notpip/_vendor/ipaddress.py is Python
# pipenv/patched/notpip/_vendor/lockfile/ is Python
# pipenv/patched/notpip/_vendor/msgpack/ is ASL 2.0
# pipenv/patched/notpip/_vendor/packaging/ is (ASL 2.0 or BSD)
# pipenv/patched/notpip/_vendor/pkg_resources/ is MIT 
# pipenv/patched/notpip/_vendor/progress/ is ISC
# pipenv/patched/notpip/_vendor/pyparsing is MIT
# pipenv/patched/notpip/_vendor/pytoml/ is MIT
# pipenv/patched/notpip/_vendor/requests/ is ASL 2.0
# pipenv/patched/notpip/_vendor/retrying.py is ASL 2.0
# pipenv/patched/notpip/_vendor/six.py is ASL 2.0
# pipenv/patched/notpip/_vendor/urllib3/ is MIT
# pipenv/patched/notpip/_vendor/webencodings/ is ASL 2.0

# pipenv/vendor/blindspin/ is MIT
# pipenv/vendor/click_didyoumean/ is MIT
# pipenv/vendor/delegator.py is MIT
# pipenv/vendor/distlib/ is Python
# pipenv/vendor/dotenv/ is BSD
# pipenv/vendor/pipdeptree.py is MIT
# pipenv/vendor/pipreqs/ is Apache2.0
# pipenv/vendor/pythonfinder/ is MIT
# pipenv/vendor/requirements/ is BSD
# pipenv/vendor/requirementslib/ is (Apache2.0 or BSD)
# pipenv/vendor/shellingham/ is ISC
# pipenv/vendor/shutilwhich/ is BSD
# pipenv/vendor/yarg/ is MIT

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

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3dist(flake8) >= 3.0.0
BuildRequires:  python3dist(flaky)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(invoke)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(parver)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-click)
BuildRequires:  python3dist(twine)
BuildRequires:  python3dist(virtualenv)
BuildRequires:  python3dist(virtualenv-clone)

# Optional condition that makes "python" mean Python 2
# Useful to tests if pipenv can manage python 2 venvs, but unnecessary dep
%bcond_with python2_tests

%if %{with python2_tests}
BuildRequires:  python2-devel
BuildRequires:  python2dist(virtualenv)
%endif

# Packages vendored upstream
BuildRequires:  python3dist(appdirs)
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(blindspin) >= 2.0.1
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(click-completion)
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(distlib)
BuildRequires:  python3dist(docopt) >= 0.6.2
BuildRequires:  python3dist(first) >= 2.0.1
BuildRequires:  python3dist(iso8601)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(markupsafe)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(parse)
BuildRequires:  python3dist(pexpect)
BuildRequires:  python3dist(ptyprocess)
BuildRequires:  python3dist(pyparsing)
BuildRequires:  python3dist(pytoml)
BuildRequires:  python3dist(requests) > 2.18.0
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(scandir) >= 1.7
BuildRequires:  python3dist(semver)
BuildRequires:  python3dist(toml)

%{?python_provide:%python_provide python3-%{name}}

Requires:       python3dist(virtualenv-clone)
Requires:       python3dist(virtualenv)

# Packages vendored upstream
Requires:       python3dist(appdirs)
Requires:       python3dist(attrs)
Requires:       python3dist(blindspin) >= 2.0.1
Requires:       python3dist(click)
Requires:       python3dist(click-completion)
Requires:       python3dist(colorama)
Requires:       python3dist(certifi)
Requires:       python3dist(distlib)
Requires:       python3dist(docopt) >= 0.6.2
Requires:       python3dist(first) >= 2.0.1
Requires:       python3dist(iso8601)
Requires:       python3dist(jinja2)
Requires:       python3dist(markupsafe)
Requires:       python3dist(packaging)
Requires:       python3dist(parse)
Requires:       python3dist(pexpect)
Requires:       python3dist(ptyprocess)
Requires:       python3dist(pyparsing)
Requires:       python3dist(pytoml)
Requires:       python3dist(requests) > 2.18.0
Requires:       python3dist(six)
Requires:       python3dist(scandir) >= 1.7
Requires:       python3dist(semver)
Requires:       python3dist(toml)

# Following packages bundled under vendor directory are not
# packaged for Fedora yet.
# TODO package for Fedora and unbundle
Provides:       bundled(python3dist(click-didyoumean)) == 0.0.3
Provides:       bundled(python3dist(delegator)) == 0.1.0
Provides:       bundled(python3dist(pipdeptree))
Provides:       bundled(python3dist(pipreqs)) == 0.4.9
Provides:       bundled(python3dist(python-dotenv)) == 0.6.2
Provides:       bundled(python3dist(pythonfinder))
Provides:       bundled(python3dist(requirementslib)) == 1.0.9
Provides:       bundled(python3dist(requirements-parser)) == 0.2.0
Provides:       bundled(python3dist(requirements)) == 0.2.0
Provides:       bundled(python3dist(shellingham)) == 1.1.0
Provides:       bundled(python3dist(shutilwhich)) == 1.1.0
Provides:       bundled(python3dist(yarg)) == 0.1.9

# The sources contains patched versions of following packages:
Provides:       bundled(python3dist(contoml))
Provides:       bundled(python3dist(crayons)) == 0.1.2
Provides:       bundled(python3dist(pew)) == 1.1.5
Provides:       bundled(python3dist(pipfile)) == 0.0.2
Provides:       bundled(python3dist(pip-tools)) == 2.0.1
Provides:       bundled(python3dist(prettytoml)) == 0.3
Provides:       bundled(python3dist(pip)) == 10.0.1
Provides:       bundled(python3dist(piptools)) == 2.0.2
Provides:       bundled(python3dist(safety))

# The packages bundled with pip:
Provides:       bundled(python3dist(appdirs)) = 1.4.3
Provides:       bundled(python3dist(distlib)) = 0.2.7
Provides:       bundled(python3dist(distro)) = 1.2.0
Provides:       bundled(python3dist(html5lib)) = 1.0.1
Provides:       bundled(python3dist(six)) = 1.11.0
Provides:       bundled(python3dist(colorama)) = 0.3.9
Provides:       bundled(python3dist(CacheControl)) = 0.12.4
Provides:       bundled(python3dist(msgpack-python)) = 0.5.6
Provides:       bundled(python3dist(lockfile)) = 0.12.2
Provides:       bundled(python3dist(progress)) = 1.3
Provides:       bundled(python3dist(ipaddress)) = 1.0.19
Provides:       bundled(python3dist(packaging)) = 17.1
Provides:       bundled(python3dist(pyparsing)) = 2.2.0
Provides:       bundled(python3dist(pytoml)) = 0.1.14
Provides:       bundled(python3dist(retrying)) = 1.3.3
Provides:       bundled(python3dist(requests)) = 2.18.4
Provides:       bundled(python3dist(chardet)) = 3.0.4
Provides:       bundled(python3dist(idna)) = 2.6
Provides:       bundled(python3dist(urllib3)) = 1.22
Provides:       bundled(python3dist(certifi)) = 2018.1.18
Provides:       bundled(python3dist(setuptools)) = 39.1.0
Provides:       bundled(python3dist(webencodings)) = 0.5.1

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
UNBUNDLED="appdirs attr blindspin certifi chardet click click_completion colorama distlib docopt first idna iso8601 jinja2 markupsafe packaging parse pathlib2 pexpect ptyprocess pyparsing pytoml requests semver scandir six toml urllib3 backports"

_vendordir="pipenv/vendor/"

for pkg in ${UNBUNDLED[@]}; do
  if [ -d $_vendordir$pkg ]; then
    rm -r $_vendordir$pkg
  elif [ -f $_vendordir$pkg.py ]; then
    rm $_vendordir$pkg".py"
  else
    echo 'Unbundling error:' $pkg 1>&2
    exit 1
  fi
  rm -rf $_vendordir$pkg".LICENSE"*
done

mv tests/pytest-pypi/pytest_pypi tests/integration/fixtures
rm -rf tests/pytest-pypi
           
%build
%py3_build
# generate html docs
export PYTHONPATH=$PWD/build/lib
sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
rm -rf html/_sources/

%install
%py3_install
# Remove shebang lines from scripts in project directory
grep "/usr/bin/env python" -lR %{buildroot}%{python3_sitelib}/%{name}| xargs sed -i '1d'

%check
# dirty dirty hack (TODO find a better way)
# for the tests to run, we need to set PYTHONPATH to something that:
#   - has our pipenv (%%{buildroot}%%{python3_sitelib})
#   - has our unbundled deps (%%{python3_sitelib} and %%{python3_sitearch})
#   - doesn't have pip (venv installed pips may have different API)
#   - doesn't have requests (a test uninstalls it and checks it)
# (even externally run pythons read PYTHONPATH and use modules from it)
mkdir check_pythonpath
ln -sf %{buildroot}%{python3_sitelib}/* %{python3_sitelib}/* %{python3_sitearch}/* check_pythonpath/
unlink check_pythonpath/pip
unlink check_pythonpath/pip-*info
unlink check_pythonpath/__pycache__
mkdir check_pythonpath/__pycache__
ln -sf %{python3_sitelib}/__pycache__/* %{python3_sitearch}/__pycache__/* check_pythonpath/__pycache__/

# we also make sure "python" and "virtualenv" exists and means something
mkdir check_path
%if %{with python2_tests}
ln -s %{__python2} check_path/python
ln -s %{_bindir}/virtualenv-2 check_path/virtualenv
%else
ln -s %{__python3} check_path/python
ln -s %{_bindir}/virtualenv-3 check_path/virtualenv
%endif

export PATH=$PWD/check_path:$PATH:%{buildroot}%{_bindir}
export PYTHONPATH=$PWD/check_pythonpath
export PYPI_VENDOR_DIR="$(pwd)/tests/pypi/"
pytest-3 -v -n auto -m "not rpmfail" tests

rm -rf check_pythonpath check_path


%files
%license LICENSE
# for the sake of simplicity, files are listed twice. we know about it
%license %{python3_sitelib}/%{name}/patched/contoml/LICENSE
%license %{python3_sitelib}/%{name}/patched/crayons.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/appdirs.LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/cachecontrol/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/certifi/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/chardet/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/colorama/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/distlib/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/distro.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/html5lib/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/idna/LICENSE.rst
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/ipaddress.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/lockfile/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/msgpack/COPYING
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/packaging/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/packaging/LICENSE.APACHE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/packaging/LICENSE.BSD
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/pkg_resources/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/progress/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/pyparsing.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/pytoml/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/requests/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/retrying.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/six.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/urllib3/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/webencodings/LICENSE
%license %{python3_sitelib}/%{name}/patched/pew/LICENSE
%license %{python3_sitelib}/%{name}/patched/pipfile/LICENSE
%license %{python3_sitelib}/%{name}/patched/pipfile/LICENSE.APACHE
%license %{python3_sitelib}/%{name}/patched/pipfile/LICENSE.BSD
%license %{python3_sitelib}/%{name}/patched/piptools/LICENSE
%license %{python3_sitelib}/%{name}/patched/prettytoml/LICENSE
%license %{python3_sitelib}/%{name}/patched/safety/LICENSE
%license %{python3_sitelib}/%{name}/vendor/click_didyoumean/LICENSE
%license %{python3_sitelib}/%{name}/vendor/delegator.py.LICENSE
%license %{python3_sitelib}/%{name}/vendor/dotenv/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pipdeptree.LICENSE
%license %{python3_sitelib}/%{name}/vendor/pipreqs/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pythonfinder/LICENSE.txt
%license %{python3_sitelib}/%{name}/vendor/requirementslib/LICENSE
%license %{python3_sitelib}/%{name}/vendor/requirementslib/LICENSE.APACHE
%license %{python3_sitelib}/%{name}/vendor/requirementslib/LICENSE.BSD
%license %{python3_sitelib}/%{name}/vendor/requirementslib/_vendor/pipfile/LICENSE
%license %{python3_sitelib}/%{name}/vendor/requirementslib/_vendor/pipfile/LICENSE.APACHE
%license %{python3_sitelib}/%{name}/vendor/requirementslib/_vendor/pipfile/LICENSE.BSD
%license %{python3_sitelib}/%{name}/vendor/requirements/LICENSE.rst
%license %{python3_sitelib}/%{name}/vendor/shellingham/LICENSE
%license %{python3_sitelib}/%{name}/vendor/shutilwhich/LICENSE
%license %{python3_sitelib}/%{name}/vendor/yarg/LICENSE

# We don't ship those requests:
%exclude %{python3_sitelib}/%{name}/vendor/yarg/LICENSE-REQUESTS

# https://github.com/pypa/pipenv/issues/2678
%exclude %{python3_sitelib}/%{name}/patched/piptools/LICENSE.txt

%doc README.rst NOTICES CHANGELOG.rst HISTORY.txt
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
* Wed Aug 01 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.7.1-2
- Correct the name of bundled dotenv to python-dotenv

* Fri Jul 27 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.7.1-1
- Update to 2018.7.1 (#1609432)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Miro Hrončok <mhroncok@redhat.com> - 11.10.4-3
- Do not require pathlib2, it's intended for Python < 3.5

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 11.10.4-2
- Rebuilt for Python 3.7
- Add patch for patched/bundled prettytoml to work with 3.7

* Fri Apr 13 2018 Michal Cyprian <mcyprian@redhat.com> - 11.10.4-1
- Initial package.
