#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Reply
Summary:	Email::Reply - reply to a message
Summary(pl):	Email::Reply - odpowied¼ na e-mail
Name:		perl-Email-Reply
Version:	1.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	914687ef7e0f9a680d57ad4aeae162e1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-Abstract
BuildRequires:	perl-Email-Address
BuildRequires:	perl-Email-MIME
BuildRequires:	perl-Email-MIME-Creator >= 1.2
BuildRequires:	perl-Email-MIME-Modifier >= 1.2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This software takes the hard out of generating replies to email
messages.

%description -l pl
Pakiet ten usuwa trudno¶æ generowania odpowiedzi na wiadomo¶ci e-mail.

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
