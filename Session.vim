let SessionLoad = 1
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Documents/2020/caiso_connector
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +38 term://~/Documents/2020/caiso_connector//75891:/bin/zsh
badd +1 term://~/Documents/2020/caiso_connector//75943:/bin/zsh
badd +17 sql_app/main.py
badd +7 scratch.py
badd +11 sql_app/database.py
badd +24 src/etl.py
badd +82 app/main.py
badd +22 src/helpers.py
badd +6 sql_app/crud.py
badd +29 src/caiso_connector.py
argglobal
%argdel
$argadd src/etl.py
edit scratch.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd _ | wincmd |
split
1wincmd k
wincmd w
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 101 + 90) / 180)
exe '2resize ' . ((&lines * 19 + 31) / 62)
exe 'vert 2resize ' . ((&columns * 78 + 90) / 180)
exe '3resize ' . ((&lines * 38 + 31) / 62)
exe 'vert 3resize ' . ((&columns * 78 + 90) / 180)
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 7 - ((6 * winheight(0) + 29) / 58)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
7
normal! 0
wincmd w
argglobal
if bufexists("term://~/Documents/2020/caiso_connector//75943:/bin/zsh") | buffer term://~/Documents/2020/caiso_connector//75943:/bin/zsh | else | edit term://~/Documents/2020/caiso_connector//75943:/bin/zsh | endif
if &buftype ==# 'terminal'
  silent file term://~/Documents/2020/caiso_connector//75943:/bin/zsh
endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 19 - ((18 * winheight(0) + 9) / 19)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
19
normal! 0
wincmd w
argglobal
if bufexists("term://~/Documents/2020/caiso_connector//75891:/bin/zsh") | buffer term://~/Documents/2020/caiso_connector//75891:/bin/zsh | else | edit term://~/Documents/2020/caiso_connector//75891:/bin/zsh | endif
if &buftype ==# 'terminal'
  silent file term://~/Documents/2020/caiso_connector//75891:/bin/zsh
endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 2 - ((1 * winheight(0) + 19) / 38)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
2
normal! 054|
wincmd w
exe 'vert 1resize ' . ((&columns * 101 + 90) / 180)
exe '2resize ' . ((&lines * 19 + 31) / 62)
exe 'vert 2resize ' . ((&columns * 78 + 90) / 180)
exe '3resize ' . ((&lines * 38 + 31) / 62)
exe 'vert 3resize ' . ((&columns * 78 + 90) / 180)
tabnext 1
if exists('s:wipebuf') && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 winminheight=1 winminwidth=1 shortmess=filnxtToOFc
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
