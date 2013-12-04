Name:           python-isodate
Version:        0.4.7
Release:        1
Summary:        An ISO 8601 date/time/duration parser and formater
Group:          Development/Python
License:        BSD
URL:            http://pypi.python.org/pypi/isodate
Source0:        http://pypi.python.org/packages/source/i/isodate/isodate-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-distribute

%description
This module implements ISO 8601 date, time and duration parsing. The
implementation follows ISO8601:2004 standard, and implements only date/time
representations mentioned in the standard. If something is not mentioned there,
then it is treated as non existent, and not as an allowed option.

For instance, ISO8601:2004 never mentions 2 digit years. So, it is not intended
by this module to support 2 digit years. (while it may still be valid as ISO
date, because it is not explicitly forbidden.) Another example is, when no time
zone information is given for a time, then it should be interpreted as local
time, and not UTC.

As this module maps ISO 8601 dates/times to standard Python data types, like
date, time, datetime and timedelta, it is not possible to convert all possible
ISO 8601 dates/times. For instance, dates before 0001-01-01 are not allowed by
the Python date and datetime classes. Additionally fractional seconds are
limited to microseconds. That means if the parser finds for instance
nanoseconds it will round it to microseconds.

%package -n python3-isodate
Summary:        An ISO 8601 date/time/duration parser and formater
Group:          Development/Python
Requires:       python3

%description -n python3-isodate
This module implements ISO 8601 date, time and duration parsing. The
implementation follows ISO8601:2004 standard, and implements only date/time
representations mentioned in the standard. If something is not mentioned there,
then it is treated as non existent, and not as an allowed option.

For instance, ISO8601:2004 never mentions 2 digit years. So, it is not intended
by this module to support 2 digit years. (while it may still be valid as ISO
date, because it is not explicitly forbidden.) Another example is, when no time
zone information is given for a time, then it should be interpreted as local
time, and not UTC.

As this module maps ISO 8601 dates/times to standard Python data types, like
date, time, datetime and timedelta, it is not possible to convert all possible
ISO 8601 dates/times. For instance, dates before 0001-01-01 are not allowed by
the Python date and datetime classes. Additionally fractional seconds are
limited to microseconds. That means if the parser finds for instance
nanoseconds it will round it to microseconds.

%prep
%setup -qc
mv isodate-%{version} python2
cp -a python2 python3

%build
pushd python2
%{__python} setup.py build
popd
pushd python3
python3 setup.py build
popd

%install
pushd python3
python3 setup.py install -O1 --skip-build --root %{buildroot}
popd
pushd python2
python2 setup.py install -O1 --skip-build --root %{buildroot}
popd

%files
%doc python2/README.txt python2/TODO.txt
%{python_sitelib}/isodate
%{python_sitelib}/isodate*.egg-info

%files -n python3-isodate
%doc python2/README.txt python2/TODO.txt
%{python3_sitelib}/isodate
%{python3_sitelib}/isodate*.egg-info
