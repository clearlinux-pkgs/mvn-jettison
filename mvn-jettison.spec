#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jettison
Version  : 1.1
Release  : 1
URL      : https://github.com/jettison-json/jettison/archive/jettison-1.1.tar.gz
Source0  : https://github.com/jettison-json/jettison/archive/jettison-1.1.tar.gz
Source1  : https://repo1.maven.org/maven2/org/codehaus/jettison/jettison/1.1/jettison-1.1.jar
Source2  : https://repo1.maven.org/maven2/org/codehaus/jettison/jettison/1.1/jettison-1.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-jettison-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-jettison package.
Group: Data

%description data
data components for the mvn-jettison package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jettison/jettison/1.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jettison/jettison/1.1/jettison-1.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jettison/jettison/1.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/jettison/jettison/1.1/jettison-1.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/jettison/jettison/1.1/jettison-1.1.jar
/usr/share/java/.m2/repository/org/codehaus/jettison/jettison/1.1/jettison-1.1.pom
