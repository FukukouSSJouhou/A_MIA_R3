import * as childProcess from "child_process";
import path from "path";
import ITensorProcesskun from "./ITensorProcesskun";
import { TENSORPYTHON_RESULT_PROCINTERFACE } from "./tensorpythonproc_interface";

export default class TensorPythonMainProc implements ITensorProcesskun{

    childProckun: childProcess.ChildProcess;
    constructor() {
        this.childProckun=childProcess.fork(path.join(__dirname,"tensorpythonchildproc"))
    }
    public start(base64target:string,filename:string,frameper:number):Promise<string>{
        return new Promise<string>((resolve)=>{

            let senddtobject={
                base64target:base64target,
                filename:filename,
                frameper:frameper
            }
            this.childProckun.on("message", (message:TENSORPYTHON_RESULT_PROCINTERFACE) => {
                if(message.mode==0){
                    console.log("graph base64");
                    //console.log(message.data);
                    resolve(message.data);
                }else{
                    console.log(message.data);
                }
            });
            this.childProckun.send(senddtobject);
        });
    }
}