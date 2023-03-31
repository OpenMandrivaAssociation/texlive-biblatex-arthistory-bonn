Name:		texlive-biblatex-arthistory-bonn
Version:	46637
Release:	2
Summary:	BibLaTeX citation style covers the citation and bibliography guidelines for art historians
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-arthistory-bonn
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-arthistory-bonn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-arthistory-bonn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This citation style covers the citation and bibliography
guidelines of the Kunsthistorisches Institut der Universitat
Bonn for undergraduates. It introduces bibliography entry types
for catalogs and features a tabular bibliography, among other
things. Various options are available to change and adjust the
outcome according to one's own preferences. The style is
compatible with English and German.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-arthistory-bonn
%doc %{_texmfdistdir}/doc/latex/biblatex-arthistory-bonn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
