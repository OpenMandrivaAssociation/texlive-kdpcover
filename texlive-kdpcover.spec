%global tl_name kdpcover
%global tl_revision 79193

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7.0
Release:	%{tl_revision}.1
Summary:	Covers for books published by Kindle Direct Publishing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/kdpcover
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kdpcover.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kdpcover.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kdpcover.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(anyfontsize)
Requires:	texlive(etoolbox)
Requires:	texlive(geometry)
Requires:	texlive(iexec)
Requires:	texlive(microtype)
Requires:	texlive(pgf)
Requires:	texlive(pgfopts)
Requires:	texlive(setspace)
Requires:	texlive(textpos)
Requires:	texlive(xcolor)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The problem this class solves is the necessity to change the size of the
cover PDF according to the number of pages in the book -- the bigger the
book, the larger the spine of the book must be. The provided class makes
the necessary calculations on-the-fly, using the qpdf tool. Obviously,
you need to have it installed. Also, you must run pdflatex with the
--shell-escape option, in order to allow LaTeX to run qpdf.

