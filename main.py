from config_jumpers import JMP
jmp = JMP()
if jmp.rmt_ctl:
    import main_remote
else:
    import main_manual
