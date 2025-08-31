# att (104 vs 65 bytes for gold)
import re
p=lambda a:[[c*3%6for c in re.sub(b'\0(?=\0*(\0+(\0*|+))*\0*$)',b'1',bytes(b))]for b in a]

### joking+mwi (tied, 104 bytes)
import re
p=lambda a:[[c*3%6for c in re.sub(b'\0(?=\0*(\0+(\0*|+))*\0*$)',b'1',bytes(b))]for b in a]
