import IimageCVSelector from "./IimageCVSelector";
import path from "path";
import {client as WebSocketClient} from "websocket";
class imageselector_websocket implements IimageCVSelector{
    constructor(){
        let pythonpath:string;
        let wspath:string;
        if(process.platform === "linux"){
            pythonpath="./venv/bin/python";
            wspath="ws+unix:/" + path.resolve("./ws_selector");
        }else{
            pythonpath="./venv/Scripts/python";
            wspath="ws://localhost:1919/";
        }

    }
    public getNextImageBase64(): string {
        throw new Error("Method not implemented.");
    }
    public create_syoriobj(): Promise<void> {
        throw new Error("Method not implemented.");
    }
    public getselectedimg(indexkun: number): string {
        throw new Error("Method not implemented.");
    }
    public  setFilename(filename: string): Promise<string> {
        throw new Error("Method not implemented.");
    }
    public run(): Promise<number> {
        throw new Error("Method not implemented.");
    }
    public setselectimg(indexkun: number): Promise<void> {
        throw new Error("Method not implemented.");
    }

}
export default imageselector_websocket;