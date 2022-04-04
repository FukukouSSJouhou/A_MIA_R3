import path from "path";
import {Worker} from "worker_threads";
export default class TensorPythonMainProc {

    childworker:Worker=new Worker(path.join(__dirname,"tensorpythonchildproc"));
    constructor() {
        
        this.childworker.on("message", (message:string) => {
                console.log("graph base64");
                console.log(message);
        });
    }
    public start(base64target:string,filename:string,frameper:number){
        let senddtobject={
            base64target:base64target,
            filename:filename,
            frameper:frameper
        }
        this.childworker.postMessage(senddtobject);
    }
}