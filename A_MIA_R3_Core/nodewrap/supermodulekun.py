import A_MIA_R3_Core.nodewrap.A_MIR_R3_node

mainnodeobject=None
async def recieve_selectimg(indexkun):
    mainnodeobject.recieve_selectimg
    await mainnodeobject.recieve_selectimg(indexkun)
def run_super(filename,loggerobj,callbackkun):
    mainnodeobject=A_MIA_R3_Core.nodewrap.A_MIR_R3_node.A_MIR_R3_node2(loggerobj)
    mainnodeobject.setFilename(filename)
    mainnodeobject.Setimagelistsendcallback(callbackkun)
    return mainnodeobject.run()