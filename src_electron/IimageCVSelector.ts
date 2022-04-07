interface IimageCVSelector{
    getNextImageBase64():string;
    create_syoriobj():Promise<void>;
    getselectedimg(indexkun:number):string;
    setFilename(filename:string):Promise<string>;
    run():Promise<number>;
    setselectimg(indexkun:number):Promise<void>;
}
export default IimageCVSelector;