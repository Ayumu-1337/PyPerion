from requests import post
from .hyperion import Hyperion

def obfuscate(
    code: str,
    obfcontent: bool=True,
    addbuiltins: bool=True,
    camoufle: bool=False,
    safemode: bool=False,
    ultrasafemode: bool=False,
    clean: bool=True,
    renvars: bool=False,
    renlibs: bool=False,
    randlines: bool=False,
    shell: bool=True
):
    
    obf_code = Hyperion(
        addbuiltins=addbuiltins,
        camouflate=camoufle,
        clean=clean,
        content=code,
        obfcontent=obfcontent,
        randlines=randlines,
        renlibs=renlibs,
        renvars=renvars,
        safemode=safemode,
        shell=shell,
        ultrasafemode=ultrasafemode
    ).content

    return obf_code