Name:		texlive-kdpcover
Version:	65150
Release:	2
Summary:	Covers for books published by Kindle Direct Publishing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/kdpcover
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kdpcover.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kdpcover.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kdpcover.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The problem this class solves is the necessity to change the
size of the cover PDF according to the number of pages in the
book -- the bigger the book, the larger the spine of the book
must be. The provided class makes the necessary calculations
on-the-fly, using the qpdf tool. Obviously, you need to have it
installed. Also, you must run pdflatex with the --shell-escape
option, in order to allow LaTeX to run qpdf.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/kdpcover
%{_texmfdistdir}/tex/latex/kdpcover
%doc %{_texmfdistdir}/doc/latex/kdpcover

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
