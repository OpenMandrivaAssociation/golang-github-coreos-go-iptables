# http://github.com/coreos/go-iptables
%global goipath         github.com/coreos/go-iptables
Version:                0.4.0

%gometa

Name:           golang-github-coreos-go-iptables
Release:        1%{?dist}
Summary:        Go wrapper around iptables utility
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

go-iptables wraps invokation of iptables utility with functions
to append and delete rules; create, clear and delete chains.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .


%install
%goinstall glide.lock glide.yaml


%check
%gochecks -d iptables

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Nov 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Release 0.4.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.15.20170629git259c8e6
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git259c8e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.20170629git259c8e6
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20170629git259c8e6
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git259c8e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git259c8e6
- Bump to upstream 259c8e6a4275d497442c721fa52204d7a58bde8b
  related: #1262543

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitfbb7337
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitfbb7337
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitfbb7337
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.6.gitfbb7337
- Bump to upstream fbb73372b87f6e89951c2b6b31470c2c9d5cfae3
  related: #1262543

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git74b0926
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git74b0926
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git74b0926
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git74b0926
- Update to spec-2.1
  related: #1262543

* Tue Sep 01 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git74b0926
- First package for Fedora
  resolves: #1258878

