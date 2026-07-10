%global tl_name armtex
%global tl_revision 69418

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0~beta5
Release:	%{tl_revision}.1
Summary:	A system for writing in Armenian with TeX and LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/armenian/armtex
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/armtex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/armtex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
ArmTeX is a system for typesetting Armenian text with Plain TeX or
LaTeX(2e). It may be used with input: from a standard Latin keyboard
without any special encoding and/or support for Armenian letters, from
any keyboard which uses an encoding that has Armenian letters in the
second half (characters 128-255) of the extended ASCII table (for
example ArmSCII8 Armenian standard), from an Armenian keyboard using
UTF-8 encoding. Users should note that the manuals still mostly describe
the previous version of the package (ArmTeX 2.0). However, a description
of the new features of ArmTeX 3.0 is provided at the end of the README
file.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/tex/plain
%dir %{_datadir}/texmf-dist/doc/generic/armenian
%dir %{_datadir}/texmf-dist/fonts/afm/public
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/tex/latex/armenian
%dir %{_datadir}/texmf-dist/tex/plain/armenian
%dir %{_datadir}/texmf-dist/doc/generic/armenian/examples
%dir %{_datadir}/texmf-dist/fonts/afm/public/armenian
%dir %{_datadir}/texmf-dist/fonts/map/dvips/armenian
%dir %{_datadir}/texmf-dist/fonts/source/public/armenian
%dir %{_datadir}/texmf-dist/fonts/tfm/public/armenian
%dir %{_datadir}/texmf-dist/fonts/type1/public/armenian
%dir %{_datadir}/texmf-dist/doc/generic/armenian/examples/latex
%dir %{_datadir}/texmf-dist/doc/generic/armenian/examples/plain
%doc %{_datadir}/texmf-dist/doc/generic/armenian/README
%doc %{_datadir}/texmf-dist/doc/generic/armenian/examples/latex/alphabet.tex
%doc %{_datadir}/texmf-dist/doc/generic/armenian/examples/latex/manual-e.tex
%doc %{_datadir}/texmf-dist/doc/generic/armenian/examples/latex/manual.tex
%doc %{_datadir}/texmf-dist/doc/generic/armenian/examples/latex/raffi-a8.tex
%doc %{_datadir}/texmf-dist/doc/generic/armenian/examples/latex/raffi-u8.tex
%doc %{_datadir}/texmf-dist/doc/generic/armenian/examples/latex/raffi.tex
%doc %{_datadir}/texmf-dist/doc/generic/armenian/examples/plain/first.tex
%doc %{_datadir}/texmf-dist/doc/generic/armenian/examples/plain/plraf-a8.tex
%doc %{_datadir}/texmf-dist/doc/generic/armenian/examples/plain/plraf-u8.tex
%doc %{_datadir}/texmf-dist/doc/generic/armenian/examples/plain/plraf.tex
%doc %{_datadir}/texmf-dist/doc/generic/armenian/examples/plain/table.tex
%doc %{_datadir}/texmf-dist/doc/generic/armenian/manual-e.pdf
%doc %{_datadir}/texmf-dist/doc/generic/armenian/manual.pdf
%{_datadir}/texmf-dist/fonts/afm/public/armenian/arssb10.afm
%{_datadir}/texmf-dist/fonts/afm/public/armenian/arssbs10.afm
%{_datadir}/texmf-dist/fonts/afm/public/armenian/arssr10.afm
%{_datadir}/texmf-dist/fonts/afm/public/armenian/arsssl10.afm
%{_datadir}/texmf-dist/fonts/afm/public/armenian/artmb10.afm
%{_datadir}/texmf-dist/fonts/afm/public/armenian/artmbi10.afm
%{_datadir}/texmf-dist/fonts/afm/public/armenian/artmbs10.afm
%{_datadir}/texmf-dist/fonts/afm/public/armenian/artmi10.afm
%{_datadir}/texmf-dist/fonts/afm/public/armenian/artmr10.afm
%{_datadir}/texmf-dist/fonts/afm/public/armenian/artmsl10.afm
%{_datadir}/texmf-dist/fonts/map/dvips/armenian/arss.map
%{_datadir}/texmf-dist/fonts/map/dvips/armenian/artm.map
%doc %{_datadir}/texmf-dist/fonts/source/public/armenian/arssb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/armenian/arssbs10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/armenian/arssr10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/armenian/arsssl10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/armenian/artmb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/armenian/artmbi10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/armenian/artmbs10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/armenian/artmi10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/armenian/artmr10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/armenian/artmsl10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/armenian/ps2mfbas.mf
%{_datadir}/texmf-dist/fonts/tfm/public/armenian/arssb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/armenian/arssbs10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/armenian/arssr10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/armenian/arsssl10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/armenian/artmb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/armenian/artmbi10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/armenian/artmbs10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/armenian/artmi10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/armenian/artmr10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/armenian/artmsl10.tfm
%{_datadir}/texmf-dist/fonts/type1/public/armenian/arssb10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/armenian/arssb10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/armenian/arssbs10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/armenian/arssbs10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/armenian/arssr10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/armenian/arssr10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/armenian/arsssl10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/armenian/arsssl10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/armenian/artmb10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/armenian/artmb10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/armenian/artmbi10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/armenian/artmbi10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/armenian/artmbs10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/armenian/artmbs10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/armenian/artmi10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/armenian/artmi10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/armenian/artmr10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/armenian/artmr10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/armenian/artmsl10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/armenian/artmsl10.pfm
%{_datadir}/texmf-dist/tex/latex/armenian/armscii8.def
%{_datadir}/texmf-dist/tex/latex/armenian/armtex.sty
%{_datadir}/texmf-dist/tex/latex/armenian/ot6cmr.fd
%{_datadir}/texmf-dist/tex/latex/armenian/ot6cmss.fd
%{_datadir}/texmf-dist/tex/latex/armenian/ot6enc.def
%{_datadir}/texmf-dist/tex/latex/armenian/ot6enc.dfu
%{_datadir}/texmf-dist/tex/plain/armenian/arm.tex
%{_datadir}/texmf-dist/tex/plain/armenian/armkb-a8.tex
%{_datadir}/texmf-dist/tex/plain/armenian/armkb-u8.tex
