Summary:	HTTP Live Video Stream Segmenter and Distributor
Name:		http-live-streaming-tools
Version:	0.1
Release:	4
License:	GPL v2
Group:		Applications/Networking
Source0:	%{name}.tar.bz2
# Source0-md5:	90731a7168cd9393cc4c6e3704b75f11
URL:		http://www.ioncannon.net/projects/http-live-video-stream-segmenter-and-distributor/
Patch0:		makefile.patch
Patch1:		input_filename.patch
BuildRequires:	bzip2-devel
BuildRequires:	ffmpeg-devel >= 0.5
BuildRequires:	rpmbuild(macros) >= 1.484
Requires:	http-live-segmenter = %{version}-%{release}
Requires:	ruby
Requires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is an attempt to make it easier to set up a live
streaming server using Apple's HTTP Live Streaming protocol. The
source includes a Ruby script and a C program that use FFMpeg to
encode and segment an input video stream in the correct format for use
with the HTTP streaming protocol.

%package -n http-live-segmenter
Summary:	HTTP Live Video Stream Segmenter
Group:		Applications

%description -n http-live-segmenter
HTTP Live Video Stream Segmenter.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p live_segmenter $RPM_BUILD_ROOT%{_bindir}
install -p hs_* http_streamer* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md example-configs
%attr(755,root,root) %{_bindir}/hs_config.rb
%attr(755,root,root) %{_bindir}/hs_encoder.rb
%attr(755,root,root) %{_bindir}/hs_transfer.rb
%attr(755,root,root) %{_bindir}/http_streamer.rb
%attr(755,root,root) %{_bindir}/live_segmenter

%files -n http-live-segmenter
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/live_segmenter
