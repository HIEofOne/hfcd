from uuid import getnode

gotnode = getnode()

use_default = True

if gotnode == 4404614765057:
    # This is the Digital Ocean Droplet (VPS).
    
    print "SETTINGS: gotnode matched %s" % gotnode
    print "SETTINGS: Using Digital Ocean VPS local_settings.py"
    
    use_default = False
    
    db_name = 'hfcd_digo.sqlite'

#==============================================================================#

elif use_default:
    # This is my MBP 2013.
    
    print "SETTINGS: gotnode did not mach, using default."
    print "SETTINGS: Using Zak MBP 2013 local_settings.py"
    
    use_default = False
    
    db_name = 'hfcd_mbp.sqlite'
