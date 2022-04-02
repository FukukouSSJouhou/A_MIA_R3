import { processinterface} from "./processinterface";
import pynode from '@fukukoussjouhou/pynode';
import A_MIA_R3_PythonWraps from "./python_wraps";

let current_indexkun:number=0;
pynode.startInterpreter();
pynode.appendSysPath('./');
pynode.appendSysPath('./venv/Lib/site-packages');
let pywraps:A_MIA_R3_PythonWraps=new A_MIA_R3_PythonWraps();
pywraps.Setimagelistsendcallback((datakun:string)=>{
    let sendobj:processinterface={
        command:810,
        data:datakun
    }
    if(process.send){
        //console.log(sendobj)
    process.send(sendobj);
    }

});
process.on("message",(msg:processinterface)=>{
    switch(msg.command){
        case 0:
            pywraps.run();
            break;
        case 1:
            pywraps.setFilename(msg.data);
            break;
        case 2:
            pywraps.setselectimg(msg.data);
            break;
    }
});