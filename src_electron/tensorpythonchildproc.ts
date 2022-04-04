import TENSORPYTHONPROCINTERFACE from "./tensorpythonproc_interface";
import pynode from '@fukukoussjouhou/pynode';
import { parentPort } from "worker_threads";
const loggerobj = (strkun: string) => {
    console.log(strkun);
}
let pytensor_class = pynode.pyimport("A_MIA_R3_Core.nodewrap.A_MIR_R3_node_tensor")
let pyinstance = pytensor_class.get("A_MIR_R3_node_tensor2").call(loggerobj);
if (parentPort) {
    console.log("worker");
    parentPort.on("message", (message: TENSORPYTHONPROCINTERFACE) => {
        let base64target = message.base64target;
        let filename = message.filename;
        let perframe = message.frameper;
    });
}