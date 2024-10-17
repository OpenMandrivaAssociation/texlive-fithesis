Name:		texlive-fithesis
Version:	70531
Release:	1
Summary:	Thesis class and template for Masaryk University (Brno, Czech Republic)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fithesis
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fithesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fithesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fithesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A document class for the typesetting of theses at the Masaryk
University (Brno, Czech Republic). The class has been designed
for easy extensibility by style and locale files of other
academic institutions.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fithesis
%{_texmfdistdir}/tex/latex/fithesis
%doc %{_texmfdistdir}/doc/latex/fithesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
