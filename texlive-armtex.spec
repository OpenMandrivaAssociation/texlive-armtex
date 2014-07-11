# revision 33894
# category Package
# catalog-ctan /language/armenian/armtex
# catalog-date 2014-04-25 11:20:11 +0200
# catalog-license lppl
# catalog-version 3.0-beta3
Name:		texlive-armtex
Version:	3.0.beta3
Release:	2
Summary:	A sytem for writing Armenian with TeX and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/armenian/armtex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/armtex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/armtex.doc.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/armenian/arssb10.afm
%{_texmfdistdir}/fonts/afm/public/armenian/arssbs10.afm
%{_texmfdistdir}/fonts/afm/public/armenian/arssr10.afm
%{_texmfdistdir}/fonts/afm/public/armenian/arsssl10.afm
%{_texmfdistdir}/fonts/afm/public/armenian/artmb10.afm
%{_texmfdistdir}/fonts/afm/public/armenian/artmbi10.afm
%{_texmfdistdir}/fonts/afm/public/armenian/artmbs10.afm
%{_texmfdistdir}/fonts/afm/public/armenian/artmi10.afm
%{_texmfdistdir}/fonts/afm/public/armenian/artmr10.afm
%{_texmfdistdir}/fonts/afm/public/armenian/artmsl10.afm
%{_texmfdistdir}/fonts/map/dvips/armenian/arss.map
%{_texmfdistdir}/fonts/map/dvips/armenian/artm.map
%{_texmfdistdir}/fonts/source/public/armenian/arssb10.mf
%{_texmfdistdir}/fonts/source/public/armenian/arssbs10.mf
%{_texmfdistdir}/fonts/source/public/armenian/arssr10.mf
%{_texmfdistdir}/fonts/source/public/armenian/arsssl10.mf
%{_texmfdistdir}/fonts/source/public/armenian/artmb10.mf
%{_texmfdistdir}/fonts/source/public/armenian/artmbi10.mf
%{_texmfdistdir}/fonts/source/public/armenian/artmbs10.mf
%{_texmfdistdir}/fonts/source/public/armenian/artmi10.mf
%{_texmfdistdir}/fonts/source/public/armenian/artmr10.mf
%{_texmfdistdir}/fonts/source/public/armenian/artmsl10.mf
%{_texmfdistdir}/fonts/source/public/armenian/ps2mfbas.mf
%{_texmfdistdir}/fonts/tfm/public/armenian/arssb10.tfm
%{_texmfdistdir}/fonts/tfm/public/armenian/arssbs10.tfm
%{_texmfdistdir}/fonts/tfm/public/armenian/arssr10.tfm
%{_texmfdistdir}/fonts/tfm/public/armenian/arsssl10.tfm
%{_texmfdistdir}/fonts/tfm/public/armenian/artmb10.tfm
%{_texmfdistdir}/fonts/tfm/public/armenian/artmbi10.tfm
%{_texmfdistdir}/fonts/tfm/public/armenian/artmbs10.tfm
%{_texmfdistdir}/fonts/tfm/public/armenian/artmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/armenian/artmr10.tfm
%{_texmfdistdir}/fonts/tfm/public/armenian/artmsl10.tfm
%{_texmfdistdir}/fonts/type1/public/armenian/arssb10.pfb
%{_texmfdistdir}/fonts/type1/public/armenian/arssb10.pfm
%{_texmfdistdir}/fonts/type1/public/armenian/arssbs10.pfb
%{_texmfdistdir}/fonts/type1/public/armenian/arssbs10.pfm
%{_texmfdistdir}/fonts/type1/public/armenian/arssr10.pfb
%{_texmfdistdir}/fonts/type1/public/armenian/arssr10.pfm
%{_texmfdistdir}/fonts/type1/public/armenian/arsssl10.pfb
%{_texmfdistdir}/fonts/type1/public/armenian/arsssl10.pfm
%{_texmfdistdir}/fonts/type1/public/armenian/artmb10.pfb
%{_texmfdistdir}/fonts/type1/public/armenian/artmb10.pfm
%{_texmfdistdir}/fonts/type1/public/armenian/artmbi10.pfb
%{_texmfdistdir}/fonts/type1/public/armenian/artmbi10.pfm
%{_texmfdistdir}/fonts/type1/public/armenian/artmbs10.pfb
%{_texmfdistdir}/fonts/type1/public/armenian/artmbs10.pfm
%{_texmfdistdir}/fonts/type1/public/armenian/artmi10.pfb
%{_texmfdistdir}/fonts/type1/public/armenian/artmi10.pfm
%{_texmfdistdir}/fonts/type1/public/armenian/artmr10.pfb
%{_texmfdistdir}/fonts/type1/public/armenian/artmr10.pfm
%{_texmfdistdir}/fonts/type1/public/armenian/artmsl10.pfb
%{_texmfdistdir}/fonts/type1/public/armenian/artmsl10.pfm
%{_texmfdistdir}/tex/latex/armenian/armscii8.def
%{_texmfdistdir}/tex/latex/armenian/armtex.sty
%{_texmfdistdir}/tex/latex/armenian/ot6cmr.fd
%{_texmfdistdir}/tex/latex/armenian/ot6cmss.fd
%{_texmfdistdir}/tex/latex/armenian/ot6enc.def
%{_texmfdistdir}/tex/latex/armenian/ot6enc.dfu
%{_texmfdistdir}/tex/plain/armenian/arm.tex
%{_texmfdistdir}/tex/plain/armenian/armkb-a8.tex
%{_texmfdistdir}/tex/plain/armenian/armkb-u8.tex
%_texmf_updmap_d/armtex
%doc %{_texmfdistdir}/doc/generic/armenian/examples/latex/alphabet.tex
%doc %{_texmfdistdir}/doc/generic/armenian/examples/latex/manual-e.tex
%doc %{_texmfdistdir}/doc/generic/armenian/examples/latex/manual.tex
%doc %{_texmfdistdir}/doc/generic/armenian/examples/latex/raffi-a8.tex
%doc %{_texmfdistdir}/doc/generic/armenian/examples/latex/raffi-u8.tex
%doc %{_texmfdistdir}/doc/generic/armenian/examples/latex/raffi.tex
%doc %{_texmfdistdir}/doc/generic/armenian/examples/plain/first.tex
%doc %{_texmfdistdir}/doc/generic/armenian/examples/plain/plraf-a8.tex
%doc %{_texmfdistdir}/doc/generic/armenian/examples/plain/plraf-u8.tex
%doc %{_texmfdistdir}/doc/generic/armenian/examples/plain/plraf.tex
%doc %{_texmfdistdir}/doc/generic/armenian/examples/plain/table.tex
%doc %{_texmfdistdir}/doc/generic/armenian/manual-e.pdf
%doc %{_texmfdistdir}/doc/generic/armenian/manual.pdf
%doc %{_texmfdistdir}/doc/generic/armenian/readme.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/armtex <<EOF
MixedMap arss.map
MixedMap artm.map
EOF
