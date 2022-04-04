import TENSORPYTHONPROCINTERFACE from "./tensorpythonproc_interface";
import pynode from '@fukukoussjouhou/pynode';
const loggerobj = (strkun: string) => {
    console.log(strkun);
}
pynode.startInterpreter();
pynode.appendSysPath('./');
pynode.appendSysPath('./venv/Lib/site-packages');
let pytensor_class = pynode.pyimport("A_MIA_R3_Core.nodewrap.A_MIR_R3_node_tensor")
let pyinstance = pytensor_class.get("A_MIR_R3_node_tensor2").call(loggerobj);
/*if (parentPort) {
    console.log("worker");
    parentPort.on("message", (message: TENSORPYTHONPROCINTERFACE) => {
        let base64target = message.base64target;
        let filename = message.filename;
        let perframe = message.frameper;
    });
}*/
console.log("worker");
let message:TENSORPYTHONPROCINTERFACE=JSON.parse(process.argv[2]);

let base64target = message.base64target;
let filename = message.filename;
let perframe = message.frameper;
console.log(base64target,filename,perframe);
pyinstance.get("processkun").call(base64target,filename,perframe);