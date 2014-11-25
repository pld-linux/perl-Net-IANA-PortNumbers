#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Net
%define		pnam	IANA-PortNumbers
%include	/usr/lib/rpm/macros.perl
Summary:	Net::IANA::PortNumbers - translate ports to services and vice versa
Summary(pl.UTF-8):	Net::IANA::PortNumbers - tłumaczenie portów na usługi i na odwrót
Name:		perl-Net-IANA-PortNumbers
Version:	1.16
Release:	3
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	056000346da9c0c4352f6bff7e506034
URL:		http://search.cpan.org/dist/Net-IANA-PortNumbers/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Net::IANA::PortNumbers Perl module, which
translates port numbers and services to ports, services, descriptions,
protocols, and ranges.

%description -l pl.UTF-8
Ten pakiet zawiera moduł Perla Net::IANA::PortNumbers tłumaczący
numery portów i usługi na porty, usługi, opisy, protokoły i zakresy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
rm -f t/0-signature.t

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
# the only user of Net/IANA for now
%dir %{perl_vendorlib}/Net/IANA
%{perl_vendorlib}/Net/IANA/*.pm
%{_mandir}/man3/*
