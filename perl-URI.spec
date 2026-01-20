Name:       perl-URI
Summary:    A Perl module implementing URI parsing and manipulation
Version:    5.28
Release:    1
License:    GPL+ or Artistic
BuildArch:  noarch
URL:        http://search.cpan.org/dist/URI/
Source0:    URI-%{version}.tar.gz
Requires:   perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:  perl(MIME::Base64) >= 2
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
This module implements the URI class. Objects of this class represent
"Uniform Resource Identifier references" as specified in RFC 2396 (and
updated by RFC 2732).

%prep
%setup -q -n URI-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name perllocal.pod -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/URI*
%doc %{_mandir}/man3/*.3*
