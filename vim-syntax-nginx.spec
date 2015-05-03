%define		syntax	nginx
Summary:	Vim syntax: Highlight code in nginx config file
Summary(pl.UTF-8):	Opis składni dla Vima: podświetlanie kodu wewnątrz plików konfiguracyjnych nginx
Name:		vim-syntax-%{syntax}
Version:	0.3.3
Release:	1
License:	public domain
Group:		Applications/Editors/Vim
Source0:	http://www.vim.org/scripts/download_script.php?src_id=19394&/%{syntax}.vim
# Source0-md5:	10395c7a028cc58030f82ab296f13ff3
URL:		http://www.vim.org/scripts/script.php?script_id=1886
Requires:	vim-rt >= 4:7.2.170
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
This script highlights code in nginx config file.

%description -l pl.UTF-8
Ten skrypt podświetla kod w pliku konfiguracyjnym nginx.

%prep
%setup -qcT
install -d syntax ftdetect
cp -p %{SOURCE0} syntax/%{syntax}.vim
cat > ftdetect/%{syntax}.vim <<EOF
au BufNewFile,BufRead /etc/nginx/*.conf set filetype=%{syntax}
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -a syntax ftdetect $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/nginx.vim
%{_vimdatadir}/ftdetect/nginx.vim
