%global tl_name biblatex-arthistory-bonn
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	BibLaTeX citation style covers the citation and bibliography guidelines for a...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-arthistory-bonn
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-arthistory-bonn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-arthistory-bonn.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This citation style covers the citation and bibliography guidelines of
the Kunsthistorisches Institut der Universitat Bonn for undergraduates.
It introduces bibliography entry types for catalogs and features a
tabular bibliography, among other things. Various options are available
to change and adjust the outcome according to one's own preferences. The
style is compatible with English and German.

