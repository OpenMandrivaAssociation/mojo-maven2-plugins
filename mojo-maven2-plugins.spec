# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define _with_gcj_support 1

%define gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

%define section     free
%define repo_dir    m2_repo/repository
%define axistools_namedversion 1.0
%define build_helper_namedversion 1.0
%define castor_namedversion 1.0
%define changes_namedversion 2.0-beta-1
%define clirr_namedversion 2.0
%define cobertura_namedversion 2.1
%define commons_attributes_namedversion 1.0
%define dependency_namedversion 1.0
%define exec_namedversion 1.0.2
%define findbugs_namedversion 1.0-beta-1
%define fit_namedversion 2.0-beta-2
%define idlj_namedversion 1.0
%define javacc_namedversion 2.1
%define javancss_namedversion 2.0-beta-1
%define jaxb2_namedversion 1.2
%define jdepend_namedversion 2.0-beta-1
%define jpox_namedversion 1.1.6
%define jspc_namedversion 1.4.6
%define jxr_namedversion 2.0-beta-1
%define keytool_namedversion 1.0-beta-1
%define sql_namedversion 1.0
%define xdoclet_namedversion 1.0-beta-1-SNAPSHOT
%define xmlbeans_namedversion 2.0
%define xslt_namedversion 1.0


Name:           mojo-maven2-plugins
Version:        1.0
Release:        %mkrel 9.0.1
Epoch:          0
Summary:        Maven2 plugin set from mojo.codehaus.org
License:        APL, MIT 
Group:          Development/Java
URL:            http://mojo.codehaus.org
Source0:    mojo12-pom.xml
Source1:    %{name}-mapdeps.xsl
Source2:    %{name}-jpp-depmap.xml
Source3:    mojo-maven2-plugins-settings.xml

Source4:        aspectj-maven-plugin-1.0-beta-2.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/aspectj-maven-plugin-1.0-beta-2/
Source5:        axistools-maven-plugin-1.0.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/axistools-maven-plugin-1.0/
Source6:        build-helper-maven-plugin-1.0.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/build-helper-maven-plugin-1.0/
Source7:        castor-maven-plugin-1.0.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/castor-maven-plugin-1.0/
Source8:        changelog-maven-plugin-2.0-beta-1.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/changelog-maven-plugin-2.0-beta-1/
Source9:        changes-maven-plugin-2.0-beta-1.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/changes-maven-plugin-2.0-beta-1/
Source10:       clirr-maven-plugin-2.0.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/clirr-maven-plugin-2.0/
Source11:       cobertura-maven-plugin-2.1.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/cobertura-maven-plugin-2.1/
Source12:       commons-attributes-maven-plugin-1.0.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/commons-attributes-maven-plugin-1.0/
Source13:       dependency-maven-plugin-1.0.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/dependency-maven-plugin-1.0/
Source14:       exec-maven-plugin-1.0.2.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/exec-maven-plugin-1.0.2/

# FIXME: Findbugs disabled until JPackage 1.7 is at Java 1.5
Source15:       findbugs-maven-plugin-1.0-beta-1.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/findbugs-maven-plugin-1.0-beta-1/

Source16:       fit-maven-plugin-2.0-beta-2.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/fit-maven-plugin-2.0-beta-2/
Source17:       ideauidesigner-maven-plugin-1.0-alpha-1.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/ideauidesigner-maven-plugin-1.0-alpha-1/
Source18:       idlj-maven-plugin-1.0.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/idlj-maven-plugin-1.0/
Source19:       javacc-maven-plugin-2.1.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/javacc-maven-plugin-2.1/
Source20:       javancss-maven-plugin-2.0-beta-1.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/javancss-maven-plugin-2.0-beta-1/
Source21:       jaxb2-maven-plugin-1.2.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/jaxb2-maven-plugin-1.2/
Source22:       jdepend-maven-plugin-2.0-beta-1.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/jdepend-maven-plugin-2.0-beta-1/
Source23:       jpox-maven-plugin-1.1.6.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/jpox-maven-plugin-1.1.6/
Source24:       jspc-maven-plugin-1.4.6.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/jspc-maven-plugin-1.4.6/
Source25:       jxr-maven-plugin-2.0-beta-1.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/jxr-maven-plugin-2.0-beta-1/
Source26:       keytool-maven-plugin-1.0-beta-1.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/keytool-maven-plugin-1.0-beta-1/
Source27:       nbm-maven-plugin-2.3.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/nbm-maven-plugin-2.3/
Source28:       netbeans-freeform-maven-plugin-2.0.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/netbeans-freeform-maven-plugin-2.0/
Source29:       sablecc-maven-plugin-2.0.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/sablecc-maven-plugin-2.0/
Source30:       smc-maven-plugin-1.0-alpha-1.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/smc-maven-plugin-1.0-alpha-1/
Source31:       sql-maven-plugin-1.0.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/sql-maven-plugin-1.0/
Source32:       taglist-maven-plugin-2.0.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/taglist-maven-plugin-2.0/
Source33:       xdoclet-maven-plugin-1.0-beta-1-SNAPSHOT.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/xdoclet-maven-plugin-1.0-alpha-1/
Source34:       xmlbeans-maven-plugin-2.0.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/xmlbeans-maven-plugin-2.0/
Source35:       xslt-maven-plugin-1.0.tar.gz
# svn export https://svn.codehaus.org/mojo/tags/xslt-maven-plugin-1.0/
Source36:       jdiff-maven-plugin-0.1.tar.gz
# svn export https://svn.codehaus.org/mojo/trunk/mojo/jdiff-maven-plugin/


#Source99: mojo-maven2-plugins-cobertura.pom

Patch1:     mojo-maven2-plugins-cobertura-CoberturaReportMojo.patch
Patch2:     mojo-maven2-plugins-changes-JiraMojo.patch
Patch3:     mojo-maven2-plugins-changes-ChangesMojo.patch
Patch4:     mojo-maven2-plugins-clirr-ClirrReport.patch
Patch5:     mojo-maven2-plugins-jpox-pom_xml.patch
Patch6:     mojo-maven2-plugins-fit-FitRunnerMojo.patch
Patch7:     mojo-maven2-plugins-fit-FitRunnerMojoTest.patch
Patch8:     mojo-maven2-plugins-javancss-NcssReportMojo.patch
Patch9:     mojo-maven2-plugins-jdepend-JDependMojo.patch
Patch10:    mojo-maven2-plugins-jxr-JxrReport.patch
Patch11:    mojo-maven2-plugins-taglist-TagListReport.patch
Patch12:    mojo-maven2-plugins-jdiff-JDiffMojo.patch
Patch13:    mojo-maven2-plugins-jdiff-pom_xml.patch
Patch14:    mojo-maven2-plugins-jspc-pom_xml.patch
Patch15:    mojo-maven2-plugins-findbugs-FindBugsMojo.patch
Patch16:    mojo-maven2-plugins-sinjdoc.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%if %{gcj_support}
BuildRequires:          java-gcj-compat-devel
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:    maven2 >= 2.0.4-8jpp
BuildRequires:    maven2-plugin-antrun
BuildRequires:    maven2-plugin-compiler
BuildRequires:    maven2-plugin-install
BuildRequires:    maven2-plugin-jar
BuildRequires:    maven2-plugin-javadoc
BuildRequires:    maven2-plugin-one
BuildRequires:    maven2-plugin-plugin
BuildRequires:    maven2-plugin-resources
BuildRequires:    maven2-plugin-surefire
BuildRequires:    ant
#BuildRequires:    axion
BuildRequires:    axis
BuildRequires:    bea-stax
BuildRequires:    bea-stax-api
#BuildRequires:    castor
BuildRequires:    classworlds
#BuildRequires:    clirr
BuildRequires:    cobertura
#BuildRequires:    jakarta-commons-attributes
BuildRequires:    jakarta-commons-collections
BuildRequires:    jakarta-commons-discovery
BuildRequires:    jakarta-commons-el
BuildRequires:    jakarta-commons-httpclient
BuildRequires:    jakarta-commons-io
BuildRequires:    jakarta-commons-lang
BuildRequires:    jakarta-commons-logging
BuildRequires:    dom4j
BuildRequires:    ecj
BuildRequires:    maven-doxia
BuildRequires:    maven-jxr
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    maven-wagon
#BuildRequires:    findbugs
BuildRequires:    fit
BuildRequires:    gnu.getopt
BuildRequires:    httpunit
BuildRequires:    javacc
#BuildRequires:    javancss
BuildRequires:    jaxen
#BuildRequires:    jboss4-j2ee
BuildRequires:    jdepend
BuildRequires:    jdiff
#BuildRequires:    jetty5
#BuildRequires:    jpox-core
#BuildRequires:    jpox-enhancer
BuildRequires:    junit
BuildRequires:    log4j
BuildRequires:    plexus-archiver
BuildRequires:    plexus-compiler
BuildRequires:    plexus-container-artifact
BuildRequires:    plexus-container-default
BuildRequires:    plexus-i18n
BuildRequires:    plexus-mail-sender
BuildRequires:    plexus-utils
BuildRequires:    plexus-velocity
BuildRequires:    qdox
BuildRequires:    regexp
BuildRequires:    tomcat5-servlet-2.4-api
BuildRequires:    tomcat5-jasper
BuildRequires:    tomcat5-jsp-2.0-api
BuildRequires:    velocity
BuildRequires:    wsdl4j
BuildRequires:    xdoclet
BuildRequires:    xerces-j2
BuildRequires:    xjavadoc
#BuildRequires:    xmlbeans
BuildRequires:    xml-commons-resolver11
Requires:       jpackage-utils >= 0:1.7.2

%description
The Mojo project allows a bunch of people not necessarily 
involved with the Maven project to come along and build 
some plugins. 
Maven plugins may also be developed here because they are 
not compatible with the Apache license. Plugin authors may 
choose to use other licenses (BSD, GPL, MPL ...) to license 
their work or may be forced to because of the nature of the 
plugin and its dependencies. These plugin authors are 
responsible for working with their plugins license but the 
mailing lists are a great place to get help if people get 
confused on what can or can not be done within the mojo project. 


%package -n mojo-maven2-plugin-axistools
Summary:     Axistools plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    axis
Requires:    jakarta-commons-discovery
Requires:    jakarta-commons-logging
Requires:    maven2 >= 0:2.0.4
Requires:    plexus-compiler
Requires:    plexus-utils
Requires:    wsdl4j

%description -n mojo-maven2-plugin-axistools
%{summary}.

%package -n mojo-maven2-plugin-build-helper
Summary:     Build Helper plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.4

%description -n mojo-maven2-plugin-build-helper
%{summary}.

#%package -n mojo-maven2-plugin-castor
#Summary:     Castor plugin from %{name}
#Group:       Development/Java
#Requires:    %{name} = 0:%{version}-%{release}
#Requires:    maven2 >= 0:2.0.4
#Requires:    castor
#Requires:    jakarta-commons-io
#Requires:    jakarta-commons-logging
#Requires:    plexus-compiler
#Requires:    plexus-utils
#Requires:    xerces-j2
#
#%description -n mojo-maven2-plugin-castor
#%{summary}.

%package -n mojo-maven2-plugin-changes
Summary:     Changes plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.4
Requires:    jakarta-commons-httpclient
Requires:    jakarta-commons-logging
Requires:    maven-doxia
Requires:    plexus-mail-sender
Requires:    plexus-velocity
Requires:    velocity

%description -n mojo-maven2-plugin-changes
%{summary}.

#%package -n mojo-maven2-plugin-clirr
#Summary:     Clirr plugin from %{name}
#Group:       Development/Java
#Requires:    %{name} = 0:%{version}-%{release}
#Requires:    maven2 >= 0:2.0.4
#Requires:    clirr
#Requires:    maven-doxia
#Requires:    plexus-i18n
#
#%description -n mojo-maven2-plugin-clirr
#%{summary}.

#%package -n mojo-maven2-plugin-cobertura
#Summary:     Cobertura plugin from %{name}
#Group:       Development/Java
#Requires:    %{name} = 0:%{version}-%{release}
#Requires:    maven2 >= 0:2.0.4
#Requires:    cobertura
#Requires:    gnu-getopt
#Requires:    plexus-container-default
#Requires:    plexus-utils
#Requires:    httpunit
#
#%description -n mojo-maven2-plugin-cobertura
#%{summary}.

#%package -n mojo-maven2-plugin-commons-attributes
#Summary:     Commons Attributes plugin from %{name}
#Group:       Development/Java
#Requires:    %{name} = 0:%{version}-%{release}
#Requires:    maven2 >= 0:2.0.4
#Requires:    jakarta-commons-attributes
#Requires:    jakarta-commons-collections
#Requires:    plexus-container-default
#Requires:    plexus-utils
#Requires:    qdox
#Requires:    xjavadoc
#
#%description -n mojo-maven2-plugin-commons-attributes
#%{summary}.

%package -n mojo-maven2-plugin-dependency
Summary:     Dependency plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.4
Requires:    plexus-archiver

%description -n mojo-maven2-plugin-dependency
%{summary}.

%package -n mojo-maven2-plugin-exec
Summary:     Exec plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.4
Requires:    plexus-container-default
Requires:    plexus-utils

%description -n mojo-maven2-plugin-exec
%{summary}.

# FIXME: Findbugs disabled until JPackage 1.7 is at Java 1.5
#%package -n mojo-maven2-plugin-findbugs
#Summary:     Findbugs plugin from %{name}
#Group:       Development/Java
#Requires:    %{name} = 0:%{version}-%{release}
#Requires:    maven2 >= 0:2.0.4
#Requires:    findbugs

#%description -n mojo-maven2-plugin-findbugs
#%{summary}.

#%package -n mojo-maven2-plugin-fit
#Summary:     FIT plugin from %{name}
#Group:       Development/Java
#Requires:    %{name} = 0:%{version}-%{release}
#Requires:    maven2 >= 0:2.0.4
#Requires:    ant
#Requires:    fit
#
#%description -n mojo-maven2-plugin-fit
#%{summary}.

%package -n mojo-maven2-plugin-idlj
Summary:     IDLJ plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.4
Requires:    plexus-compiler
Requires:    plexus-utils

%description -n mojo-maven2-plugin-idlj
%{summary}.

%package -n mojo-maven2-plugin-javacc
Summary:     JavaCC plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.4
Requires:    javacc
Requires:    plexus-compiler
Requires:    plexus-utils

%description -n mojo-maven2-plugin-javacc
%{summary}.

#%package -n mojo-maven2-plugin-javancss
#Summary:     JavaNCSS plugin from %{name}
#Group:       Development/Java
#Requires:    %{name} = 0:%{version}-%{release}
#Requires:    maven2 >= 0:2.0.4
#Requires:    dom4j
#Requires:    javancss
#Requires:    jaxen
#
#%description -n mojo-maven2-plugin-javancss
#%{summary}.

%package -n mojo-maven2-plugin-jdepend
Summary:     JDepend plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.4
Requires:    jdepend

%description -n mojo-maven2-plugin-jdepend
%{summary}.

%package -n mojo-maven2-plugin-jdiff
Summary:     JDiff plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.4
Requires:    jdiff

%description -n mojo-maven2-plugin-jdiff
%{summary}.

#%package -n mojo-maven2-plugin-jpox
#Summary:     JDiff plugin from %{name}
#Group:       Development/Java
#Requires:    %{name} = 0:%{version}-%{release}
#Requires:    maven2 >= 0:2.0.4
#Requires:    jpox-core
#Requires:    jpox-enhancer
#
#%description -n mojo-maven2-plugin-jpox
#%{summary}.

%package -n mojo-maven2-plugin-jspc
Summary:     Jspc plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.4
Requires:    ant
Requires:    ecj
Requires:    jakarta-commons-el
Requires:    jakarta-commons-logging
Requires:    log4j
Requires:    tomcat5-jasper
Requires:    tomcat5-jsp-2.0-api
Requires:    tomcat5-servlet-2.4-api

%description -n mojo-maven2-plugin-jspc
%{summary}.

%package -n mojo-maven2-plugin-jxr
Summary:     JXR plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.4
Requires:    maven-jxr

%description -n mojo-maven2-plugin-jxr
%{summary}.

%package -n mojo-maven2-plugin-keytool
Summary:     Keytool plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.4
Requires:    jakarta-commons-lang
Requires:    plexus-utils

%description -n mojo-maven2-plugin-keytool
%{summary}.

#%package -n mojo-maven2-plugin-sql
#Summary:     SQL plugin from %{name}
#Group:       Development/Java
#Requires:    %{name} = 0:%{version}-%{release}
#Requires:    maven2 >= 0:2.0.4
#Requires:    axion
#
#%description -n mojo-maven2-plugin-sql
#%{summary}.

%package -n mojo-maven2-plugin-taglist
Summary:     Taglist plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.4

%description -n mojo-maven2-plugin-taglist
%{summary}.

#%package -n mojo-maven2-plugin-xdoclet
#Summary:     XDoclet plugin from %{name}
#Group:       Development/Java
#Requires:    %{name} = 0:%{version}-%{release}
#Requires:    maven2 >= 0:2.0.4
#Requires:    maven2-plugin-antrun
#Requires:    jakarta-commons-collections
#Requires:    jakarta-commons-logging
#Requires:    jboss4-j2ee
#Requires:    tomcat5-servlet-2.4-api
#Requires:    xdoclet
#Requires:    xjavadoc
#
#%description -n mojo-maven2-plugin-xdoclet
#%{summary}.

%package -n mojo-maven2-plugin-xmlbeans
Summary:     XmlBeans plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.4
Requires:    bea-stax
Requires:    bea-stax-api
Requires:    classworlds
Requires:    maven-wagon
Requires:    plexus-container-artifact
Requires:    plexus-container-default
Requires:    plexus-utils
Requires:    xml-commons-resolver11
Requires:    xmlbeans

%description -n mojo-maven2-plugin-xmlbeans
%{summary}.

%package -n mojo-maven2-plugin-xslt
Summary:     Xslt plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.4
Requires:    plexus-utils

%description -n mojo-maven2-plugin-xslt
%{summary}.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires(post):   /bin/rm,/bin/ln
Requires(postun): /bin/rm

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c -T -n mojo
cp %{SOURCE0} pom.xml
cp %{SOURCE3} maven2-settings.xml
# aspectj:
#gzip -dc %{SOURCE4} | tar -xf -
# axistools:
gzip -dc %{SOURCE5} | tar -xf -
# build-helper:
gzip -dc %{SOURCE6} | tar -xf -
chmod -x build-helper-*/pom.xml
# castor:
#gzip -dc %{SOURCE7} | tar -xf -
# changelog:
#gzip -dc %{SOURCE8} | tar -xf -
# changes:
gzip -dc %{SOURCE9} | tar -xf -
# clirr:
gzip -dc %{SOURCE10} | tar -xf -
# cobertura:
#gzip -dc %{SOURCE11} | tar -xf -
# commons-attributes:
#gzip -dc %{SOURCE12} | tar -xf -
# dependency:
gzip -dc %{SOURCE13} | tar -xf -
# exec:
gzip -dc %{SOURCE14} | tar -xf -
# findbugs:
#gzip -dc %{SOURCE15} | tar -xf -
# fit:
#gzip -dc %{SOURCE16} | tar -xf -
# ideauidesigner:
#gzip -dc %{SOURCE17} | tar -xf -
# idlj:
gzip -dc %{SOURCE18} | tar -xf -
# javacc:
gzip -dc %{SOURCE19} | tar -xf -
# javancss:
#gzip -dc %{SOURCE20} | tar -xf -
# jaxb2:
#gzip -dc %{SOURCE21} | tar -xf -
# jdepend:
gzip -dc %{SOURCE22} | tar -xf -
# jpox:
#gzip -dc %{SOURCE23} | tar -xf -
# jspc:
gzip -dc %{SOURCE24} | tar -xf -
# jxr:
gzip -dc %{SOURCE25} | tar -xf -
# keytool:
gzip -dc %{SOURCE26} | tar -xf -
# nbm:
#gzip -dc %{SOURCE27} | tar -xf -
# netbeans-freeform:
#gzip -dc %{SOURCE28} | tar -xf -
# sablecc:
#gzip -dc %{SOURCE29} | tar -xf -
# smc:
#gzip -dc %{SOURCE30} | tar -xf -
# sql:
#gzip -dc %{SOURCE31} | tar -xf -
# taglist:
gzip -dc %{SOURCE32} | tar -xf -
# xdoclet:
#gzip -dc %{SOURCE33} | tar -xf -
# xmlbeans:
gzip -dc %{SOURCE34} | tar -xf -
# xslt:
gzip -dc %{SOURCE35} | tar -xf -
# jdiff:
gzip -dc %{SOURCE36} | tar -xf -

#mkdir -p m2_repo/repository/JPP/cobertura/1.7/
#cp %{SOURCE99} m2_repo/repository/JPP/cobertura/1.7/cobertura-1.7.pom
mkdir -p m2_repo/repository/JPP/maven2/default_poms
cp %{SOURCE0} m2_repo/repository/JPP/maven2/default_poms/JPP.mojo-mojo.pom

#%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav
#%patch5 -b .sav
#%patch6 -b .sav
#%patch7 -b .sav
#%patch8 -b .sav
%patch9 -b .sav
%patch10 -b .sav
%patch11 -b .sav
%patch12 -b .sav
%patch13 -b .sav
%patch14 -b .sav
%patch16 -p1

%build

mkdir -p m2_repo/repository/org/apache/maven/plugins
pushd m2_repo/repository/org/apache/maven/plugins
ln -sf /usr/share/maven2/plugins/org/apache/maven/plugins/maven-antrun-plugin.jar .
popd

export MAVEN_REPO_LOCAL=`pwd`/%{repo_dir}

mvn-jpp \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE2} \
    install javadoc:javadoc

%install
rm -rf $RPM_BUILD_ROOT

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

# There is only one version of each plugin, so we can just iterate through name-*/pom.xml
# Removed:
# findbugs-maven-plugin 
# sql-maven-plugin
# castor-maven-plugin
# clirr-maven-plugin
# commons-attributes-maven-plugin
# javancss-maven-plugin
# xdoclet-maven-plugin
# jpox-maven-plugin
# cobertura-maven-plugin
# fit-maven-plugin
#  xmlbeans-maven-plugin
for i in axistools-maven-plugin \
         build-helper-maven-plugin \
         changes-maven-plugin \
         dependency-maven-plugin \
         exec-maven-plugin \
         idlj-maven-plugin \
         javacc-maven-plugin \
         jdepend-maven-plugin \
         jdiff-maven-plugin \
         jspc-maven-plugin \
         jxr-maven-plugin \
         keytool-maven-plugin \
         taglist-maven-plugin \
         xslt-maven-plugin; do
    cp $i-*/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-$i.pom

    ver=`echo $i-* | sed -e s:$i-::g`

    # If someone were to put in a source that is not in $name-$version format, 
    # it can cause trouble. Check to make sure version is sensible...

    # If the build is failing on the line below, ensure that the plugin dir 
    # is in format $name-$version (check assumes that $version starts with a digit)
    echo ${ver:0:1} | grep -qP "\\d"

    %add_to_maven_depmap org.codehaus.mojo $i $ver JPP/mojo $i
done

cp pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-mojo.pom
%add_to_maven_depmap org.codehaus.mojo 12 JPP/mojo mojo 

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/mojo
for jar in $(find * -type f -name "*.jar" | grep -E target/.*.jar); do
        install -m 644 $jar $RPM_BUILD_ROOT%{_javadir}/mojo/`basename $jar | sed -e s:mojo-::g`
        ln -sf `basename $jar | sed -e s:mojo-::g` $RPM_BUILD_ROOT%{_javadir}/mojo/`basename $jar | sed -e s:mojo-::g -e s:"\\(.*maven-plugin\\).*\\.jar":\\\1:g`.jar
done

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
for plu in $(find * -type d -name apidocs | sed -e 's|-maven-plugin.*||'); do
  install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/${plu}
  cp -pr ${plu}-maven-plugin*/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/${plu}
done
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_maven_depmap

%postun
%update_maven_depmap

%if %{gcj_support}
%post -n mojo-maven2-plugin-axistools
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun -n mojo-maven2-plugin-axistools
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post -n mojo-maven2-plugin-build-helper
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun -n mojo-maven2-plugin-build-helper
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

#%if %{gcj_support}
#%post -n mojo-maven2-plugin-castor
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif
#
#%if %{gcj_support}
#%postun -n mojo-maven2-plugin-castor
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif

%if %{gcj_support}
%post -n mojo-maven2-plugin-changes
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun -n mojo-maven2-plugin-changes
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

#%if %{gcj_support}
#%post -n mojo-maven2-plugin-clirr
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif
#
#%if %{gcj_support}
#%postun -n mojo-maven2-plugin-clirr
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif

#%if %{gcj_support}
#%post -n mojo-maven2-plugin-cobertura
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif
#
#if %{gcj_support}
#%postun -n mojo-maven2-plugin-cobertura
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif

#%if %{gcj_support}
#%post -n mojo-maven2-plugin-commons-attributes
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif
#
#%if %{gcj_support}
#%postun -n mojo-maven2-plugin-commons-attributes
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif

%if %{gcj_support}
%post -n mojo-maven2-plugin-dependency
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun -n mojo-maven2-plugin-dependency
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post -n mojo-maven2-plugin-exec
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun -n mojo-maven2-plugin-exec
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

#%if %{gcj_support}
#%post -n mojo-maven2-plugin-findbugs
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif

#%if %{gcj_support}
#%postun -n mojo-maven2-plugin-findbugs
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif

#%if %{gcj_support}
#%post -n mojo-maven2-plugin-fit
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif
#
#%if %{gcj_support}
#%postun -n mojo-maven2-plugin-fit
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif

%if %{gcj_support}
%post -n mojo-maven2-plugin-idlj
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun -n mojo-maven2-plugin-idlj
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post -n mojo-maven2-plugin-javacc
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun -n mojo-maven2-plugin-javacc
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

#%if %{gcj_support}
#%post -n mojo-maven2-plugin-javancss
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif
#
#%if %{gcj_support}
#%postun -n mojo-maven2-plugin-javancss
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif

%if %{gcj_support}
%post -n mojo-maven2-plugin-jdepend
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun -n mojo-maven2-plugin-jdepend
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post -n mojo-maven2-plugin-jdiff
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun -n mojo-maven2-plugin-jdiff
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

#%if %{gcj_support}
#%post -n mojo-maven2-plugin-jpox
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif
#
#%if %{gcj_support}
#%postun -n mojo-maven2-plugin-jpox
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif

%if %{gcj_support}
%post -n mojo-maven2-plugin-jspc
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun -n mojo-maven2-plugin-jspc
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post -n mojo-maven2-plugin-jxr
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun -n mojo-maven2-plugin-jxr
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post -n mojo-maven2-plugin-keytool
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun -n mojo-maven2-plugin-keytool
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

#%if %{gcj_support}
#%post -n mojo-maven2-plugin-sql
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif
#
#%if %{gcj_support}
#%postun -n mojo-maven2-plugin-sql
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif

%if %{gcj_support}
%post -n mojo-maven2-plugin-taglist
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun -n mojo-maven2-plugin-taglist
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

#%if %{gcj_support}
#%post -n mojo-maven2-plugin-xdoclet
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif
#
#%if %{gcj_support}
#%postun -n mojo-maven2-plugin-xdoclet
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif

#%if %{gcj_support}
#%post -n mojo-maven2-plugin-xmlbeans
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif
#
#%if %{gcj_support}
#%postun -n mojo-maven2-plugin-xmlbeans
#if [ -x %{_bindir}/rebuild-gcj-db ]
#then
#  %{_bindir}/rebuild-gcj-db
#fi
#%endif

%if %{gcj_support}
%post -n mojo-maven2-plugin-xslt
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun -n mojo-maven2-plugin-xslt
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%defattr(-,root,root,-)
%dir %{_javadir}/mojo
%{_datadir}/maven2/poms/JPP.mojo-mojo.pom
%config(noreplace) %{_mavendepmapfragdir}/*
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%endif

%files -n mojo-maven2-plugin-axistools
%{_javadir}/mojo/axistools*.jar
%{_datadir}/maven2/poms/JPP.mojo-axistools-maven-plugin*.pom
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/axistools-*.jar.*
%endif

%files -n mojo-maven2-plugin-build-helper
%{_javadir}/mojo/build-helper*.jar
%{_datadir}/maven2/poms/JPP.mojo-build-helper-maven-plugin*.pom
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/build-helper-*.jar.*
%endif

#%files -n mojo-maven2-plugin-castor
#%{_javadir}/mojo/castor*.jar
#%{_datadir}/maven2/poms/JPP.mojo-castor-maven-plugin*.pom
#%if %{gcj_support}
#%attr(-,root,root) %{_libdir}/gcj/%{name}/castor-*.jar.*
#%endif

%files -n mojo-maven2-plugin-changes
%{_javadir}/mojo/changes*.jar
%{_datadir}/maven2/poms/JPP.mojo-changes-maven-plugin*.pom
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/changes-*.jar.*
%endif

#%files -n mojo-maven2-plugin-clirr
#%{_javadir}/mojo/clirr*.jar
#%{_datadir}/maven2/poms/JPP.mojo-clirr-maven-plugin*.pom
#%if %{gcj_support}
#%attr(-,root,root) %{_libdir}/gcj/%{name}/clirr-*.jar.*
#%endif

#%files -n mojo-maven2-plugin-cobertura
#%{_javadir}/mojo/cobertura*.jar
#%{_datadir}/maven2/poms/JPP.mojo-cobertura-maven-plugin*.pom
#%if %{gcj_support}
#%attr(-,root,root) %{_libdir}/gcj/%{name}/cobertura-*.jar.*
#%endif

#%files -n mojo-maven2-plugin-commons-attributes
#%{_javadir}/mojo/commons-attributes*.jar
#%{_datadir}/maven2/poms/JPP.mojo-commons-attributes-maven-plugin*.pom
#%if %{gcj_support}
#%attr(-,root,root) %{_libdir}/gcj/%{name}/commons-attributes-*.jar.*
#%endif

%files -n mojo-maven2-plugin-dependency
%{_javadir}/mojo/dependency*.jar
%{_datadir}/maven2/poms/JPP.mojo-dependency-maven-plugin*.pom
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/dependency-*.jar.*
%endif

%files -n mojo-maven2-plugin-exec
%{_javadir}/mojo/exec*.jar
%{_datadir}/maven2/poms/JPP.mojo-exec-maven-plugin*.pom
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/exec-*.jar.*
%endif

#%files -n mojo-maven2-plugin-findbugs
#%{_javadir}/mojo/findbugs*.jar
#%{_datadir}/maven2/poms/JPP.mojo-findbugs-maven-plugin*.pom
#%if %{gcj_support}
#%attr(-,root,root) %{_libdir}/gcj/%{name}/findbugs-*.jar.*
#%endif

#%files -n mojo-maven2-plugin-fit
#%{_javadir}/mojo/fit*.jar
#%{_datadir}/maven2/poms/JPP.mojo-fit-maven-plugin*.pom
#%if %{gcj_support}
#%attr(-,root,root) %{_libdir}/gcj/%{name}/fit-*.jar.*
#%endif

%files -n mojo-maven2-plugin-idlj
%{_javadir}/mojo/idlj*.jar
%{_datadir}/maven2/poms/JPP.mojo-idlj-maven-plugin*.pom
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/idlj-*.jar.*
%endif

%files -n mojo-maven2-plugin-javacc
%{_javadir}/mojo/javacc*.jar
%{_datadir}/maven2/poms/JPP.mojo-javacc-maven-plugin*.pom
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/javacc-*.jar.*
%endif

#%files -n mojo-maven2-plugin-javancss
#%{_javadir}/mojo/javancss*.jar
#%{_datadir}/maven2/poms/JPP.mojo-javancss-maven-plugin*.pom
#%if %{gcj_support}
#%attr(-,root,root) %{_libdir}/gcj/%{name}/javancss-*.jar.*
#%endif

%files -n mojo-maven2-plugin-jdepend
%{_javadir}/mojo/jdepend*.jar
%{_datadir}/maven2/poms/JPP.mojo-jdepend-maven-plugin*.pom
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/jdepend-*.jar.*
%endif

%files -n mojo-maven2-plugin-jdiff
%{_javadir}/mojo/jdiff*.jar
%{_datadir}/maven2/poms/JPP.mojo-jdiff-maven-plugin*.pom
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/jdiff-*.jar.*
%endif

#%files -n mojo-maven2-plugin-jpox
#%{_javadir}/mojo/jpox*.jar
#%{_datadir}/maven2/poms/JPP.mojo-jpox-maven-plugin*.pom
#%if %{gcj_support}
#%attr(-,root,root) %{_libdir}/gcj/%{name}/jpox-*.jar.*
#%endif

%files -n mojo-maven2-plugin-jspc
%{_javadir}/mojo/jspc*.jar
%{_datadir}/maven2/poms/JPP.mojo-jspc-maven-plugin*.pom
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/jspc-*.jar.*
%endif

%files -n mojo-maven2-plugin-jxr
%{_javadir}/mojo/jxr*.jar
%{_datadir}/maven2/poms/JPP.mojo-jxr-maven-plugin*.pom
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/jxr-*.jar.*
%endif

%files -n mojo-maven2-plugin-keytool
%{_javadir}/mojo/keytool*.jar
%{_datadir}/maven2/poms/JPP.mojo-keytool-maven-plugin*.pom
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/keytool-*.jar.*
%endif

#%files -n mojo-maven2-plugin-sql
#%{_javadir}/mojo/sql*.jar
#%{_datadir}/maven2/poms/JPP.mojo-sql-maven-plugin*.pom
#%if %{gcj_support}
#%attr(-,root,root) %{_libdir}/gcj/%{name}/sql-*.jar.*
#%endif

%files -n mojo-maven2-plugin-taglist
%{_javadir}/mojo/taglist*.jar
%{_datadir}/maven2/poms/JPP.mojo-taglist-maven-plugin*.pom
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/taglist-*.jar.*
%endif

#%files -n mojo-maven2-plugin-xdoclet
#%{_javadir}/mojo/xdoclet*.jar
#%{_datadir}/maven2/poms/JPP.mojo-xdoclet-maven-plugin*.pom
#%if %{gcj_support}
#%attr(-,root,root) %{_libdir}/gcj/%{name}/xdoclet-*.jar.*
#%endif

#%files -n mojo-maven2-plugin-xmlbeans
#%{_javadir}/mojo/xmlbeans*.jar
#%{_datadir}/maven2/poms/JPP.mojo-xmlbeans-maven-plugin*.pom
#%if %{gcj_support}
#%attr(-,root,root) %{_libdir}/gcj/%{name}/xmlbeans-*.jar.*
#%endif

%files -n mojo-maven2-plugin-xslt
%{_javadir}/mojo/xslt*.jar
%{_datadir}/maven2/poms/JPP.mojo-xslt-maven-plugin*.pom
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/xslt-*.jar.*
%endif

%files javadoc
%defattr(-,root,root,-)
%doc %{_javadocdir}/*

   /usr/share/java/mojo/taglist-maven-plugin-2.0.jar
   /usr/share/java/mojo/taglist-maven-plugin.jar
