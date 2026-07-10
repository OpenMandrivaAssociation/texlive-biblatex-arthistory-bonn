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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This citation style covers the citation and bibliography guidelines of
the Kunsthistorisches Institut der Universitat Bonn for undergraduates.
It introduces bibliography entry types for catalogs and features a
tabular bibliography, among other things. Various options are available
to change and adjust the outcome according to one's own preferences. The
style is compatible with English and German.

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
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-arthistory-bonn
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-arthistory-bonn
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-arthistory-bonn/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-arthistory-bonn/arthistory-bonn-examples.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-arthistory-bonn/arthistory-bonn.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-arthistory-bonn/arthistory-bonn.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-arthistory-bonn/arthistory-bonn-english.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-arthistory-bonn/arthistory-bonn-german.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-arthistory-bonn/arthistory-bonn.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-arthistory-bonn/arthistory-bonn.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-arthistory-bonn/arthistory-bonn.dbx
