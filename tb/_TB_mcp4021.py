import sys
sys.path.append('../lib')
from mcp4021 import MCP4021

#

pot = [MCP4021(cs) for cs in (27,26,22,21,20)]

TAP = 63
for p in pot:
    p.set(TAP)
