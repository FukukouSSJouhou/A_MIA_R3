import TENSORPYTHONPROCINTERFACE, { TENSORPYTHON_RESULT_PROCINTERFACE } from "./tensorpythonproc_interface";
import pynode from '@fukukoussjouhou/pynode';
const loggerobj=(strkun:string)=>{
    //console.log(strkun);
    let sendmsg:TENSORPYTHON_RESULT_PROCINTERFACE={
        mode:1,
        data:strkun
    }
    if(process.send){
        process.send(sendmsg);
    }
}
console.log( process.cwd());
pynode.startInterpreter();
pynode.appendSysPath('./');
pynode.appendSysPath('./venv/Lib/site-packages');
let pytensor_class=pynode.pyimport("A_MIA_R3_Core.nodewrap.A_MIR_R3_node_tensor")
let pyinstance=pytensor_class.get("A_MIR_R3_node_tensor2").call(loggerobj);
process.on("message",(message:TENSORPYTHONPROCINTERFACE)=>{
    let base64target=message.base64target;
    let filename=message.filename;
    let perframe=message.frameper;
    let msgkun=pyinstance.get("processkun").call(base64target,filename,perframe);
    let sendmsg2:TENSORPYTHON_RESULT_PROCINTERFACE={
        mode:0,
        data:msgkun
    };
    if(process.send){
        process.send(sendmsg2);
    }
});