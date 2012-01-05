Name:		rome
Version:	0.9
Release:	4.2%{?dist}.goose.1
Summary:	RSS and Atom Utilities

Group:		Development/Libraries
License:	ASL 2.0
URL:		https://rome.dev.java.net/
# wget https://rome.dev.java.net/source/browse/*checkout*/rome/www/dist/rome-0.9-src.tar.gz?rev=1.1
Source0:	%{name}-%{version}-src.tar.gz
# wget http://download.eclipse.org/tools/orbit/downloads/drops/R20090825191606/bundles/com.sun.syndication_0.9.0.v200803061811.jar
# unzip com.sun.syndication_0.9.0.v200803061811.jar META-INF/MANIFEST.MF
# sed -i 's/\r//' META-INF/MANIFEST.MF
# # We won't have the same SHA-1 sums (class sometimes spills into # cl\nass)
# sed -i -e "/^Name/d" -e "/^SHA/d" -e "/^\ ass$/d" -e "/^$/d" META-INF/MANIFEST.MF
Source1:	MANIFEST.MF
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Patch0:		%{name}-%{version}-addosgimanifest.patch

BuildRequires:	java-devel >= 1:1.6.0
BuildRequires:	jpackage-utils
BuildRequires:	ant
BuildRequires:	jdom
Requires:	java >= 1:1.6.0
Requires:	jpackage-utils
Requires:	jdom

%description
ROME is an set of open source Java tools for parsing, generating and
publishing RSS and Atom feeds.

%package	javadoc
Summary:	Javadocs for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;
mkdir -p target/lib
ln -s %{_javadir}/jdom-1.1.1.jar target/lib
cp -p %{SOURCE1} .
%patch0

%build
ant -Dnoget=true dist

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp dist/docs/api/* \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_javadir}/%{name}-%{version}.jar

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}

%changelog
* Thu Jan  5 2011 Clint Savage <herlo@gooseproject.org> 0.9-4.2.goose.1
- Upstream provides jdom-1.1.1, using that instead of jdom-1.0

* Mon Jan 11 2010 Andrew Overholt <overholt@redhat.com> 0.9-4.2
- Update URL in instructions for getting MANIFEST.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.9-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 30 2009 Andrew Overholt <overholt@redhat.com> 0.9-3
- Fix javadoc Group (rhbz#492761).

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 25 2008 Andrew Overholt <overholt@redhat.com> 0.9-1
- Initial Fedora version
