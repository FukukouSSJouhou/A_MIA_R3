import IimageCVSelector from "./IimageCVSelector";

class imageselector_websocket implements IimageCVSelector{
    constructor(){

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
export default imageselector_websocket