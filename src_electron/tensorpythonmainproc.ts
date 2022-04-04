import * as childProcess from "child_process";
class TensorPythonMainProc {

    childProckun: childProcess.ChildProcess = childProcess.fork("./tensorpythonchildproc")
    constructor() {
        this.childProckun.on("message", (message) => {
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
        this.childProckun.send(senddtobject);
    }
}