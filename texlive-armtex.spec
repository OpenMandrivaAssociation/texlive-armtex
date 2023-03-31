Name:		texlive-armtex
Version:	64182
Release:	2
Summary:	A sytem for writing Armenian with TeX and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/armenian/armtex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/armtex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/armtex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex

%description
ArmTeX is a system for typesetting Armenian text with Plain TeX
or LaTeX(2e). It may be used with input: from a standard Latin
keyboard without any special encoding and/or support for
Armenian letters, any keyboard which uses an encoding that has
Armenian letters in the second half (characters 128-255) of the
extended ASCII table (for example ArmSCII8 Armenian standard),
or encoded in UTF-8. Users should note that the manuals (below)
mostly describe the previous (version 2.0) of the package.
Updating work is still under way.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/armenian
%{_texmfdistdir}/fonts/map/dvips/armenian
%{_texmfdistdir}/fonts/source/public/armenian
%{_texmfdistdir}/fonts/tfm/public/armenian
%{_texmfdistdir}/fonts/type1/public/armenian
%{_texmfdistdir}/tex/plain/armenian
%{_texmfdistdir}/tex/latex/armenian
%_texmf_updmap_d/armtex
%doc %{_texmfdistdir}/doc/generic/armenian

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/armtex <<EOF
MixedMap arss.map
MixedMap artm.map
EOF
