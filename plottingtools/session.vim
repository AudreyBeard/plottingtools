let SessionLoad = 1
if &cp | set nocp | endif
map  h
let s:cpo_save=&cpo
set cpo&vim
map <NL> j
map  k
map  l
nmap <silent> ;w;m <Plug>VimwikiMakeTomorrowDiaryNote
nmap <silent> ;w;y <Plug>VimwikiMakeYesterdayDiaryNote
nmap <silent> ;w;t <Plug>VimwikiTabMakeDiaryNote
nmap <silent> ;w;w <Plug>VimwikiMakeDiaryNote
nmap <silent> ;w;i <Plug>VimwikiDiaryGenerateLinks
nmap <silent> ;wi <Plug>VimwikiDiaryIndex
nmap <silent> ;ws <Plug>VimwikiUISelect
nmap <silent> ;wt <Plug>VimwikiTabIndex
nmap <silent> ;ww <Plug>VimwikiIndex
vmap ;8 "mdi**h"mp
vmap ;4 "mdi$$h"mp
nmap ;p :r! cat /tmp/vimtmp
vmap ;y :w! /tmp/vimtmp
vnoremap ;g gq`g
nnoremap ;g mgJvgq`g
nnoremap ;k myO`y
nnoremap ;j myo`y
nnoremap ;s :set hlsearch! hlsearch?
nnoremap ;v :!mupdf %:r.pdf &
nnoremap ;c :w:!rubber --inplace --pdf --warn all %
map ;f :NERDTreeToggle
vmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
vnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(expand((exists("g:netrw_gx")? g:netrw_gx : '<cfile>')),netrw#CheckIfRemote())
imap  α
imap  ∧
imap  ≅
imap  •
imap  β
imap  Δ
imap  δ
imap  ≡
imap  ε
imap  ∃
imap  ∈
imap  ∀
imap  ≥
imap  λ
imap  ≤
imap  Ø
imap  ≠
imap 	 ∩
imap  ∪
imap  ∨
imap  ρ
imap  ⊂
imap  ⊕
inoremap # X#
imap {{{ {{{}}}<<ki    
let &cpo=s:cpo_save
unlet s:cpo_save
set background=dark
set backspace=indent,eol,start
set expandtab
set fileencodings=ucs-bom,utf-8,default,latin1
set helplang=en
set hlsearch
set ignorecase
set incsearch
set laststatus=2
set mouse=a
set printoptions=paper:letter
set ruler
set runtimepath=~/.vim,~/.vim/pack/plugins/start/vimwiki,~/.vim/bundle/nerdtree,~/.vim/bundle/syntastic,~/.vim/bundle/vimwiki,/var/lib/vim/addons,/usr/share/vim/vimfiles,/usr/share/vim/vim80,/usr/share/vim/vimfiles/after,/var/lib/vim/addons/after,~/.vim/after
set shiftwidth=4
set showcmd
set showmatch
set smartcase
set smartindent
set statusline=%F%=%10((%l,\ %c)%)\ --\ %P
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set tabstop=4
set whichwrap=<,>,h,l
set wildignore=*.pyc
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/code/plottingtools/plottingtools
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +0 plot.py
argglobal
silent! argdel *
$argadd plot.py
edit plot.py
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=1 winheight=1 winminwidth=1 winwidth=1
exe '1resize ' . ((&lines * 35 + 36) / 73)
exe '2resize ' . ((&lines * 35 + 36) / 73)
argglobal
setlocal keymap=
setlocal noarabic
setlocal noautoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
set colorcolumn=80
setlocal colorcolumn=80
setlocal comments=b:#,fb:-
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
set foldmethod=indent
setlocal foldmethod=indent
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(v:fname,'\\.','/','g')
setlocal indentexpr=
setlocal indentkeys=0{,0},:,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=pydoc
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=python3complete#Complete
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
set relativenumber
setlocal relativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal signcolumn=auto
setlocal smartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=.py
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=8
setlocal tagcase=
setlocal tags=
setlocal termkey=
setlocal termsize=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
21
normal! zo
42
normal! zo
44
normal! zo
42
normal! zc
65
normal! zo
65
normal! zo
65
normal! zo
90
normal! zo
91
normal! zo
95
normal! zo
97
normal! zo
99
normal! zo
90
normal! zc
106
normal! zo
107
normal! zo
110
normal! zo
110
normal! zo
110
normal! zo
110
normal! zo
114
normal! zo
116
normal! zo
106
normal! zc
118
normal! zo
122
normal! zo
125
normal! zo
137
normal! zo
139
normal! zo
146
normal! zo
147
normal! zo
149
normal! zo
153
normal! zo
155
normal! zo
155
normal! zo
162
normal! zo
165
normal! zo
167
normal! zo
168
normal! zo
171
normal! zo
174
normal! zo
178
normal! zo
188
normal! zo
191
normal! zo
195
normal! zo
202
normal! zo
203
normal! zo
205
normal! zo
208
normal! zo
211
normal! zo
212
normal! zo
212
normal! zo
212
normal! zo
212
normal! zo
232
normal! zo
237
normal! zo
240
normal! zo
241
normal! zo
243
normal! zo
245
normal! zo
251
normal! zo
251
normal! zo
let s:l = 147 - ((14 * winheight(0) + 17) / 35)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
147
normal! 0
wincmd w
argglobal
if bufexists('plot.py') | buffer plot.py | else | edit plot.py | endif
setlocal keymap=
setlocal noarabic
setlocal noautoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
set colorcolumn=80
setlocal colorcolumn=80
setlocal comments=b:#,fb:-
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
set foldmethod=indent
setlocal foldmethod=indent
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(v:fname,'\\.','/','g')
setlocal indentexpr=
setlocal indentkeys=0{,0},:,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=pydoc
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=python3complete#Complete
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
set relativenumber
setlocal relativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal signcolumn=auto
setlocal smartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=.py
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=8
setlocal tagcase=
setlocal tags=
setlocal termkey=
setlocal termsize=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
21
normal! zo
42
normal! zo
44
normal! zo
42
normal! zc
65
normal! zo
65
normal! zo
65
normal! zo
90
normal! zo
95
normal! zo
97
normal! zo
95
normal! zc
99
normal! zo
90
normal! zc
106
normal! zo
107
normal! zo
110
normal! zo
110
normal! zo
110
normal! zo
110
normal! zo
114
normal! zo
116
normal! zo
106
normal! zc
118
normal! zo
125
normal! zo
137
normal! zo
139
normal! zo
137
normal! zc
146
normal! zo
147
normal! zo
149
normal! zo
153
normal! zo
155
normal! zo
155
normal! zo
162
normal! zo
165
normal! zo
167
normal! zo
168
normal! zo
171
normal! zo
174
normal! zo
178
normal! zo
188
normal! zo
191
normal! zo
195
normal! zo
202
normal! zo
203
normal! zo
205
normal! zo
208
normal! zo
21
normal! zc
211
normal! zo
212
normal! zo
212
normal! zo
212
normal! zo
212
normal! zo
232
normal! zo
237
normal! zo
240
normal! zo
241
normal! zo
243
normal! zo
245
normal! zo
251
normal! zo
251
normal! zo
let s:l = 234 - ((25 * winheight(0) + 17) / 35)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
234
normal! 017|
wincmd w
2wincmd w
exe '1resize ' . ((&lines * 35 + 36) / 73)
exe '2resize ' . ((&lines * 35 + 36) / 73)
tabnext 1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
set winminheight=1 winminwidth=1
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
