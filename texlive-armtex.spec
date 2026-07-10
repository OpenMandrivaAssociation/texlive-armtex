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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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

