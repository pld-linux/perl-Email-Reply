#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Reply
Summary:	Email::Reply - reply to a message
Summary(pl.UTF-8):	Email::Reply - odpowiadanie na e-mail
Name:		perl-Email-Reply
Version:	1.202
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Email/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a1d1758016232c98e4119b653d7e1421
URL:		http://search.cpan.org/dist/Email-Reply/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-Abstract >= 2.01
BuildRequires:	perl-Email-Address >= 1.80
BuildRequires:	perl-Email-MIME >= 1.82
BuildRequires:	perl-Email-MIME-Creator >= 1.41
BuildRequires:	perl-Email-MIME-Modifier >= 1.42
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This software takes the hard out of generating replies to email
messages.

%description -l pl.UTF-8
Pakiet ten usuwa trudność generowania odpowiedzi na wiadomości e-mail.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes
%{perl_vendorlib}/Email/*.pm
%{_mandir}/man3/*
