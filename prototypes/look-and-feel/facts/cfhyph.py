import ctypes, ctypes.util
cf = ctypes.CDLL(ctypes.util.find_library("CoreFoundation"))
cf.CFStringCreateWithCString.restype = ctypes.c_void_p
cf.CFStringCreateWithCString.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint32]
cf.CFLocaleCreate.restype = ctypes.c_void_p
cf.CFLocaleCreate.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
cf.CFStringIsHyphenationAvailableForLocale.restype = ctypes.c_bool
cf.CFStringIsHyphenationAvailableForLocale.argtypes = [ctypes.c_void_p]
for loc in ["lt","lt_LT","lv","et","pl","en_US","de","ru","uk","fi","cs","sk","hu"]:
    s = cf.CFStringCreateWithCString(None, loc.encode(), 0x08000100)
    l = cf.CFLocaleCreate(None, s)
    print(loc, cf.CFStringIsHyphenationAvailableForLocale(l))
